import csv

from opm_manager.settings import SUPPLIER_BUFFER, DC_BUFFER
from opm_manager.tools import BinLocation
from opm_manager.models.sku import Material, DistributionCenter, Storage
from opm_manager.models.supplier import Supplier
from opm_manager.models.simulation import Simulation


def load_materials(path):
    """
    Load materials from the given csv file
    :param path: str
    :return: list of Materials
    """
    def get_material_from_row(row):
        """
        Create a material from the row
        :param row:
        :return:
        """
        mid = row[0]
        sid = row[1]
        bin_loc = row[2]
        ipc = int(row[3])
        cpi = float(row[4])
        ibq = int(row[5])
        safety = int(row[6])
        min_ord_qty = int(row[7])
        frequency = int(row[8])
        return Material(mid, sid, bin_loc, ipc, cpi, ibq, safety, min_ord_qty, frequency)

    with open(path, "r") as f:
        rows = csv.reader(f)
        header = next(rows)
        return [get_material_from_row(row) for row in rows]


def load_distribution_centers(path):
    """
    Load distribution centers from the given csv file
    :param path: str
    :return: list of Distribution Centers
    """

    def get_dc_from_row(row):
        """
        Create a distribution center from the row
        :param row:
        :return:
        """
        dcid = row[0]
        lat = float(row[1])
        lng = float(row[2])
        standard = int(row[3])
        hazmat = int(row[4])
        refrig = int(row[5])

        s_storage = Storage(BinLocation.STANDARD, standard)
        h_storage = Storage(BinLocation.HAZMAT, hazmat)
        r_storage = Storage(BinLocation.REFRIGERATION, refrig)

        storage = {BinLocation.STANDARD: s_storage, BinLocation.HAZMAT: h_storage, BinLocation.REFRIGERATION: r_storage}

        return DistributionCenter(dcid, lat, lng, DC_BUFFER, storage)

    with open(path, "r") as f:
        rows = csv.reader(f)
        header = next(rows)
        return [get_dc_from_row(row) for row in rows]


def load_suppliers(path):
    """
    Load suppliers from the given csv file
    :param path: str
    :return: list of Distribution Centers
    """

    def get_supplier_from_row(row):
        """
        Create a supplier from the row
        :param row:
        :return:
        """
        dcid = row[0]
        lat = float(row[1])
        lng = float(row[2])
        return Supplier(dcid, lat, lng, SUPPLIER_BUFFER)

    with open(path, "r") as f:
        rows = csv.reader(f)
        header = next(rows)
        return [get_supplier_from_row(row) for row in rows]


def load_simulation(path):
    """
    Load demand/forecast weeks from the given csv file
    :param path: str
    :return: list of Materials
    """
    with open(path, "r") as f:
        rows = [row for row in csv.reader(f)]
        return Simulation(rows)







