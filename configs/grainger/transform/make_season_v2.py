import csv
import random


random.seed(2021)


MATERIALS_FILE = "./materials.csv"
DCS_FILE = "./distribution_centers.csv"
SEASON_FILE = "./season.csv"

WEEKS = 10
FORECAST_INTERVAL = (-35, 15)  # 30% below allowable space to 15% above


class DCHelper:

    def __init__(self, dcid, ss, hs, rs, inv_range):
        self.id = dcid
        self.ss = int(ss)
        self.hs = int(hs)
        self.rs = int(rs)
        self.materials = {"STANDARD": [], "HAZMAT": [], "REFRIGERATION": []}
        self.inv_range = inv_range
        self.header = ["MID", "DCID"]
        weeks = [f"Week {i+1}" for i in range(WEEKS)]
        self.header.extend(weeks)

    def get_material_bin_loc_dict(self):
        bld = {"STANDARD": [], "HAZMAT": [], "REFRIGERATION": []}
        for m in self.materials:
            bld[material[2]].append(m)
        return bld

    def get_max_space(self, binloc):
        if binloc == "STANDARD":
            return self.ss
        elif binloc == "HAZMAT":
            return self.hs
        else:
            return self.rs

    def make_dc_forecast(self):
        forecasts = []
        for binloc in self.materials:
            mats = self.materials[binloc]
            n = len(mats)
            max_space = self.get_max_space(binloc)
            portion = max_space / n
            for material in mats:
                mid = material[0]
                dcid = self.id
                mat_forecasts = []
                for week in range(WEEKS):
                    r = (random.randint(*self.inv_range) / 100.0) + 1
                    forecast = round(portion * r)
                    mat_forecasts.append(forecast)
                row = [mid, dcid]
                row.extend(mat_forecasts)
                forecasts.append(row)
        return forecasts


with open(DCS_FILE, "r") as f:
    dcs = csv.reader(f)
    dc_header = next(dcs)
    dcs = list(dcs)

with open(MATERIALS_FILE, "r") as f:
    materials = csv.reader(f)
    mat_header = next(materials)
    materials = list(materials)

helpers = []
for dc in dcs:
    helper = DCHelper(dc[0], dc[3], dc[4], dc[5], FORECAST_INTERVAL)
    for material in materials:
        helper.materials[material[2]].append(material)
    helpers.append(helper)

rows = [helper.header]
for h in helpers:
    rows.extend(h.make_dc_forecast())

with open(SEASON_FILE, "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

check = 1

