import csv
import random


random.seed(2021)

INPUT = "major_cities.csv"
OUTPUT = "store_fronts.csv"

COORD_FUNCTION = (-300, 300)
POP_THRESHOLD = 1500000


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
    return s, h, r


def get_coordinate_flunction(lat, lng):
    r1 = random.randint(*COORD_FUNCTION) / 100.0
    r2 = random.randint(*COORD_FUNCTION) / 100.0
    return lat+r1, lng+r2


def get_weight(pop):
    if int(pop) > POP_THRESHOLD:
        return 2
    return 1


def make_address(city, state):
    n = random.randint(100, 999)
    return f"{n} simulated way, {city}, {state}"


with open(INPUT, "r") as f1:
    data = csv.reader(f1)
    next(data)
    with open(OUTPUT, "w") as f2:
        writer = csv.writer(f2)
        header = ["ID", "LATITUDE", "LONGITUDE", "STANDARD SPACE", "HAZMAT SPACE", "REFRIGERATION SPACE"]
        writer.writerow(header)
        for i, row in enumerate(data):
            weight = get_weight(row[2])
            ss, hs, rs = get_space_available(weight)
            out_row = [f"SF{i+1:03d}", row[3], row[4], ss, hs, rs]
            writer.writerow(out_row)



