

from opm_manager.tools import Location


class Supplier(Location):

    def __init__(self, sid, latitude, longitude,  buffer):
        """
        Class to represent a supplier in the supply chain network
        :param sid: str
        :param latitude: float
        :param longitude: float
        :param buffer: timedelta
        """
        Location.__init__(self, latitude, longitude, buffer)
        self.id = sid

    def ship_to(self, dc, material, cube):
        """
        Place an order to a distribution center and adjust both DC's inventory
        :param dc: DistributionCenter
        :param material: Material
        :param cube: int
        :return: int (unfulfilled shipment quantity returned)
        """
        tgt_storage = dc.storage_dict[material.bin_loc]
        unfulfilled = tgt_storage.update_inventory(material, cube)  # ship as much of the cube as possible
        return unfulfilled  # non-shipped cube

    def __deepcopy__(self, memodict={}):
        """
        Deep clone of a Supplier
        :param memodict:
        :return:
        """
        new_mids = [mid for mid in self.mids]
        return Supplier(self.id, self.coords[0], self.coords[1], self.buffer)



