
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


def get_availability(fulfillment):
    """
    Get the availability of a week
    :param fulfillment: dict {mid: (demand, unfulfilled, frequency}
    :return:
    """
    availability_by_freq = {f: [] for f in FREQUENCY_WEIGHTS}

    for mid in fulfillment:
        demand = fulfillment[mid][0]
        unfulfilled = fulfillment[mid][1]
        frequency = fulfillment[mid][2]

        availability = (demand + unfulfilled) / demand  # unfulfilled is negative
        availability_by_freq[frequency].append(availability)

    aves_by_freq = {f: sum([a for a in availability_by_freq[f]]) / len(availability_by_freq[f]) for f in availability_by_freq}

    final = 0
    for f in aves_by_freq:
        final += FREQUENCY_WEIGHTS[f] * aves_by_freq[f]

    return final






