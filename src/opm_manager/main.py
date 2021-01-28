
from opm_manager import settings
from opm_manager.tools import get_availability, init_network_volume
from opm_manager.models.file_loader import load_distribution_centers, load_materials, load_suppliers, load_simulation
from opm_manager.models.network import Network


def main():
    """
    Run a simulated supply chain
    :return:
    """
    materials = {m.id: m for m in load_materials(settings.MATERIAL_PATH)}
    dcs = load_distribution_centers(settings.DC_PATH)
    suppliers = load_suppliers(settings.SUPPLIER_PATH)
    network = Network(dcs, suppliers, settings.NEIGHBOR_DISTANCE_THRESHOLD)

    season = load_simulation(settings.SEASON_PATH)
    season_length = len(season.weeks)

    forecast_good = load_simulation(settings.GOOD_FORECAST_PATH)
    forecast_moderate = load_simulation(settings.MODERATE_FORECAST_PATH)
    forecast_bad = load_simulation(settings.BAD_FORECAST_PATH)

    forecast = forecast_moderate

    init_network_volume(network, materials, forecast, .30)
    for w in range(season_length):
        availability = execute_week(network, materials, season, forecast)
        a = round(availability*100, 3)
        print(f"<b>Week {w+1}</b> {a}%  ")


def execute_week(network, materials, season, forecast):
    """
    Execute a week
    :param network:
    :param materials:
    :param season:
    :param forecast:
    :return:
    """
    week_actual = season.get_week()
    week_forecast = forecast.get_week()
    if week_actual is None:
        return None

    fulfillment = {mid: [0, 0, materials[mid].frequency] for mid in materials}

    for sku in week_actual:
        mid = sku[:5]
        dcid = sku[5:]
        actual = week_actual[sku]
        forecast = week_forecast[sku]

        material = materials[mid]
        dc = network.nodes[dcid].location
        supplier = network.nodes[material.sid].location

        excess = supplier.ship_to(dc, material, forecast)  # not enough dc space --> excess
        unfulfilled = dc.sell_inventory(material, actual)

        fulfillment[mid][0] += actual
        fulfillment[mid][1] += unfulfilled

    return get_availability(fulfillment)


if __name__ == "__main__":
    main()

