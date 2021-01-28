import os
import random

from pathlib import Path


random.seed(2021)

APP_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
SRC_DIRECTORY = Path(APP_DIRECTORY).parent
ROOT_DIRECTORY = Path(SRC_DIRECTORY).parent
DATA_DIRECTORY = os.path.join(ROOT_DIRECTORY, "data")

MATERIAL_PATH = os.path.join(DATA_DIRECTORY, "materials.csv")
DC_PATH = os.path.join(DATA_DIRECTORY, "distribution_centers.csv")
SUPPLIER_PATH = os.path.join(DATA_DIRECTORY, "suppliers.csv")

SEASON_PATH = os.path.join(DATA_DIRECTORY, "season.csv")
GOOD_FORECAST_PATH = os.path.join(DATA_DIRECTORY, "forecast_good.csv")
MODERATE_FORECAST_PATH = os.path.join(DATA_DIRECTORY, "forecast_moderate.csv")
BAD_FORECAST_PATH = os.path.join(DATA_DIRECTORY, "forecast_bad.csv")


SHIPPING_AVE_MPH = 60
NEIGHBOR_DISTANCE_THRESHOLD = SHIPPING_AVE_MPH * 8 * 1.5  # 8 Hour day 1.5 days to ship

# buffer in weeks
SUPPLIER_BUFFER = 2
DC_BUFFER = 0

FREQUENCY_WEIGHTS = {
    1: .05,
    2: .1,
    3: .20,
    4: .27,
    5: .38
}

AVAILABILITY_GOAL = .9
SPACE_GOAL = .10

AVAILABILITY_WEIGHT = .8
SPACE_WEIGHT = 1.0 - AVAILABILITY_WEIGHT


