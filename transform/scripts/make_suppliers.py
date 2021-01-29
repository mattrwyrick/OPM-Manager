import csv
import random


random.seed(1234)

N_SUPPLIERS = 5

INPUT = "./uscities.csv"
OUTPUT = "suppliers.csv"

COORD_FUNCTION = (-300, 300)
POP_THRESHOLD = 1500000

MAX_PER_STATE = 2

CITY = 0
STATE = 3
LAT = 6
LNG = 7
POP = 8


def make_sortable_row(row):
    return [int(row[POP]), row[STATE], row[CITY], float(row[LAT]), float(row[LNG])]


def output_sortable_row(row):
    return [row[1], row[2], row[0], row[3], row[4]]


with open("./uscities.csv", "r") as f:
    data = csv.reader(f)
    sortable = [make_sortable_row(row) for i, row in enumerate(data) if i != 0]

indexes = [random.randint(0, len(sortable)-1) for i in range(N_SUPPLIERS)]


def make_address(city, state):
    n = random.randint(100, 999)
    return f"{n} simulated way, {city}, {state}"


with open(OUTPUT, "w") as f2:
    writer = csv.writer(f2)
    header = ["ID", "ADDRESS", "LATITUDE", "LONGITUDE", "WEIGHT"]
    writer.writerow(header)
    for i, index in enumerate(indexes):
        row = sortable[index]
        out_row = [f"SP{i+1:03d}", make_address(row[2], row[1]), row[3], row[4]]
        writer.writerow(out_row)