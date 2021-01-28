
import random

random.seed(321654)

SW_REFRIGERATION_MIN = 100
SW_REFRIGERATION_MAX = 250

SW_HAZMAT_MIN = 200
SW_HAZMAT_MAX = 350

SW_STANDARD_MIN = 900
SW_STANDARD_MAX = 1300


def get_space_available(weight):
    r = random.randint(SW_REFRIGERATION_MIN, SW_HAZMAT_MAX) * weight
    h = random.randint(SW_HAZMAT_MIN, SW_HAZMAT_MAX) * weight
    s = random.randint(SW_STANDARD_MIN, SW_STANDARD_MAX) * weight
    print(f"{s},{h},{r}")


dc_weights = [5, 3, 4, 5, 3, 3, 4, 4, 3, 5]


for weight in dc_weights:
    get_space_available(weight)


