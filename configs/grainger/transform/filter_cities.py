import csv

output = "major_cities.csv"

CITY_COUNT = 350
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
    sortable.sort(reverse=True)
    top_cities = sortable[:CITY_COUNT]


states = dict()
for row in top_cities:
    if row[1] in states:
        states[row[1]].append(row)
    else:
        states[row[1]] = [row]

final_list = []
for state in states:
    states[state].sort(reverse=True)
    if len(states[state]) > MAX_PER_STATE:
        final_list.extend(states[state][:MAX_PER_STATE])


with open(output, "w") as f:
    writer = csv.writer(f)
    header = ["State", "City", "Population", "latitude", "longitude"]
    writer.writerow(header)
    for row in final_list:
        writer.writerow(output_sortable_row(row))



