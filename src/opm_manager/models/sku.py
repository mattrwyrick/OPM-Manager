
from copy import deepcopy

from opm_manager.tools import Location


class Material(object):

    def __init__(self, mid, sid, bin_loc, items_per_cube, cost_per_item, economic_order_qty, safety_stock,
                 min_order_qty, frequency):
        """
        Represents a material in a Sku
        :param mid: str
        :param sid: str
        :param bin_loc: BinLocation
        :param items_per_cube: int
        :param cost_per_item: float
        :param safety_stock: int (units)
        :param economic_order_qty: int (units)
        :param min_order_qty: int
        :param frequency: int [1, 5]
        """
        self.id = mid
        self.sid = sid
        self.bin_loc = bin_loc
        self.items_per_cube = items_per_cube
        self.cost_per_item = cost_per_item
        self.eoq = economic_order_qty  # back up to this
        self.safety_stock = safety_stock  # auto order when here
        self.min_order_qty = min_order_qty  # from supplier
        self.frequency = frequency

    def __deepcopy__(self, memodict={}):
        """
        Deep clone of the Material
        :param memodict:
        :return:
        """
        return Material(self.id, self.bin_loc, self.items_per_cube, self.cost_per_item, self.safety_stock,
                        self.eoq, self.min_order_qty, self.frequency)


class DistributionCenter(Location):

    def __init__(self, dcid, latitude, longitude, buffer, storage_dict):
        """
        Represents a Distribution Center in a Sku
        :param dcid: str
        :param latitude: float
        :param longitude: float
        :param buffer: timedelta (time to load/unload a truck)
        :param storage_dict: dict  {BinLocation str: Storage}
        """
        Location.__init__(self, latitude, longitude, buffer)
        self.id = dcid
        self.storage_dict = storage_dict
        self.max_cube = sum([self.storage_dict[key].max_cube for key in self.storage_dict])

    def ship_to(self, dc, material, cube):
        """
        Place an order to a distribution center and adjust both DC's inventory
        :param dc: DistributionCenter
        :param material: Material
        :param cube: int
        :return: int (unfulfilled shipment quantity returned)
        """
        tgt_storage = dc.storage_dict[material.bin_loc]
        src_storage = self.storage_dict[material.bin_loc]

        unfulfilled = tgt_storage.update_inventory(material, cube)  # ship as much of the cube as possible
        actual = cube - unfulfilled
        zero = src_storage.update_inventory(material, -1 * actual)  # remove shipped inventory

        return unfulfilled  # non-shipped cube

    def sell_inventory(self, material, cube):
        """
        Remove inventory from storage
        :param material:
        :param cube:
        :return:
        """
        r = self.storage_dict[material.bin_loc].update_inventory(material, -1*cube)
        if r != 0:
            check = 1
        return r

    def __deepcopy__(self, memodict={}):
        """
        Deep clone of the DistributionCenter
        :param memodict:
        :return:
        """
        sdict = {key: deepcopy(self.storage_dict[key]) for key in self.storage_dict}
        return DistributionCenter(self.id, self.coords[0], self.coords[1], self.buffer, sdict)


class Storage(object):

    def __init__(self, bin_loc, max_cube):
        """
        Represents a storage space in a Distribution Center
        :param bin_loc: BinLocation
        :param max_cube: int
        """
        self.bin_loc = bin_loc
        self.max_cube = max_cube
        self.available_cube = max_cube
        self.materials = dict()   # {material_id: cube}

    def update_inventory(self, material, cube):
        """
        Attempt to place an order in the storage space
        :param material: Material
        :param cube: int
        :return: unfulfilled cube (0 if completely successful)
        """
        if material.id not in self.materials:
            self.materials[material.id] = 0

        change = cube
        unfulfilled = 0

        if material.bin_loc != self.bin_loc:
            return cube

        if self.available_cube < 0:
            return cube

        check = self.available_cube - cube
        if check < 0:
            change = self.available_cube
            unfulfilled = cube - change

        if (-1*change) > self.materials[material.id]:
            unfulfilled = change + self.materials[material.id]
            self.materials[material.id] = 0
            return unfulfilled

        self.materials[material.id] += change
        self.available_cube -= change

        return unfulfilled

    def __deepcopy__(self, memodict={}):
        """
        Deep clone of a DC's storage
        :param memodict:
        :return:
        """
        new_mat = {key: self.materials[key] for key in self.materials}
        storage = Storage(self.bin_loc, self.max_cube)
        storage.materials = new_mat
        storage.available_cube = self.available_cube
        return storage






