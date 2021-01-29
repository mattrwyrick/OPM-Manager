import csv
import random


random.seed(2021)


INPUT = "./season.csv"

GOOD = "./forecast_good.csv"
G_RATE = 10

MODERATE = "./forecast_moderate.csv"
M_RATE = 30

BAD = "./forecast_bad.csv"
B_RATE = 70


def forecast(n, rate):
    r = (random.randint(-1*rate, rate) / 100.0) + 1
    v = round(n * r)
    return v


with open(INPUT, "r") as f:
    sku_actual = csv.reader(f)
    h = next(sku_actual)
    WEEKS = [f"Week {i+1}" for i in range(len(h)-2)]
    HEADER = ["MID", "DCID"]
    HEADER.extend(WEEKS)
    skus_weeks = list(sku_actual)


with open(GOOD, "w") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for actual in skus_weeks:
        mid = actual[0]
        dcid = actual[1]
        row = [mid, dcid]
        weeks = [forecast(int(value), G_RATE) for value in actual[2:]]
        row.extend(weeks)
        writer.writerow(row)


with open(MODERATE, "w") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for actual in skus_weeks:
        mid = actual[0]
        dcid = actual[1]
        row = [mid, dcid]
        weeks = [forecast(int(value), M_RATE) for value in actual[2:]]
        row.extend(weeks)
        writer.writerow(row)


with open(BAD, "w") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for actual in skus_weeks:
        mid = actual[0]
        dcid = actual[1]
        row = [mid, dcid]
        weeks = [forecast(int(value), B_RATE) for value in actual[2:]]
        row.extend(weeks)
        writer.writerow(row)







