
from datetime import timedelta
from haversine import haversine, Unit

from opm_manager.settings import SHIPPING_AVE_MPH, FREQUENCY_WEIGHTS


class BinLocation:

    REFRIGERATION = "REFRIGERATION"
    HAZMAT = "HAZMAT"
    STANDARD = "STANDARD"


class Location(object):

    def __init__(self, latitude, longitude, buffer):
        """
        Represents a location and additional functionality
        :param latitude: float
        :param longitude: float
        :param buffer: timeDelta
        """
        self.coords = (latitude, longitude)
        self.buffer = buffer

    def lead_time(self, location):
        """
        Return the time between two locations + buffer time
        :param location: Location
        :return: timedelta
        """
        miles = self.distance(location)
        hours = timedelta(hours=miles * SHIPPING_AVE_MPH)
        total = self.buffer + hours
        return total

    def distance(self, location):
        """
        Return the distance in miles between locations
        :param location:
        :return:
        """
        return haversine(self.coords, location.coords, unit=Unit.MILES)


def init_network_volume(network, materials, forecast, p):
    """
    Populate the network with initial amounts
    :return:
    """
    week_forecast = forecast.get_week()

    for sku in week_forecast:
        mid = sku[:5]
        dcid = sku[5:]
        forecast = round(week_forecast[sku] * p)

        material = materials[mid]
        dc = network.nodes[dcid].location
        supplier = network.nodes[material.sid].location

        excess = supplier.ship_to(dc, material, forecast)


def get_availability(network, fulfillment):
    """
    Get the availability of a week
    :param network:
    :param fulfillment:
    :return:
    """
    avail_by_freq = {f: [] for f in FREQUENCY_WEIGHTS}
    avail_by_dc = {sku[5:]: avail_by_freq for sku in fulfillment}

    for sku in fulfillment:
        mid = sku[:5]
        dcid = sku[5:]
        demand = fulfillment[sku][0]
        unfulfilled = fulfillment[sku][1]
        frequency = fulfillment[sku][2]
        availability = (demand + unfulfilled) / demand  # unfulfilled is negative
        avail_by_dc[dcid][frequency].append(availability)

    individual_availabilities = []
    for dcid in avail_by_dc:
        vals = {f: sum(avail_by_dc[dcid][f]) / len(avail_by_dc[dcid][f]) for f in avail_by_dc[dcid]}
        dc_availability = 0
        for f in vals:
            dc_availability += FREQUENCY_WEIGHTS[f] * vals[f]
        network.nodes[dcid].individual_score = dc_availability
        individual_availabilities.append(dc_availability)

    total_availability = sum(individual_availabilities) / len(individual_availabilities)
    network_availability = network.get_network_score()

    return total_availability, network_availability





