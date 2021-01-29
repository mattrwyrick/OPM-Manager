import csv
import random

from prob_value import ProbValue


random.seed(2021)


INPUT = "./materials.csv"
DC = "./distribution_centers.csv"
OUTPUT = "./season.csv"

WEEKS = 10


def get_init_value(v1, v2):
    diff = v1 - v2
    r = random.randint(-150, 150) / 100
    return v1 + (diff*r)


def random_rate():
    return random.randint(-30, 30) / 100


# TRENDS
linear_trend = lambda rate, init: lambda new: round((new + (init*rate)) * (1 + (random.randint(-10, 10)/100.0)))
random_trend = lambda rate, init: lambda new: round(new + (random_rate()*init))


with open(DC, "r") as f:
    dcs = csv.reader(f)
    header = next(dcs)
    sids = [row[0] for row in dcs]

with open(INPUT, "r") as f1:
    materials = csv.reader(f1)
    header = next(materials)
    materials = list(materials)
    season = []
    for sid in sids:
        for row in materials:
            mid = row[0]
            ibq = int(row[5])
            safety = int(row[6])
            value = get_init_value(ibq, safety)
            if value < 0:
                value = ibq - (safety * .75)
            if random.randint(0, 100) < 30:
                generate = linear_trend(random_rate(), value)
            else:
                generate = random_trend(random_rate(), value)

            week_actuals = [mid, sid]
            for i in range(WEEKS):
                week_actuals.append(round(value))
                new_value = generate(value)
                if new_value < 0:
                    value = value * (1 + abs(random_rate()))
                else:
                    value = new_value

            season.append(week_actuals)

with open(OUTPUT, "w") as f2:
    writer = csv.writer(f2)
    week_headers = [f"Week {i+1}" for i in range(WEEKS)]
    header = ["MID", "DCID"]
    header.extend(week_headers)
    writer.writerow(header)
    for row in season:
        writer.writerow(row)


check = 1






