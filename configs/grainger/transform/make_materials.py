import csv
import random

from prob_value import ProbValue


random.seed(2021)

SUPPLIER_FILE = "./suppliers.csv"
MATERIALS_FILE = "./materials.csv"

def n_items():
    return random.randint(2,10)


BINLOC_PVS = ProbValue.get_probability_list([ProbValue(2, "REFRIGERATION"), ProbValue(1, "HAZMAT"), ProbValue(7, "STANDARD")])
FREQUENCY_PVS = ProbValue.get_probability_list([ProbValue(1, 1), ProbValue(3, 2), ProbValue(5, 3), ProbValue(3, 4), ProbValue(1, 5)])


with open(SUPPLIER_FILE, "r") as f1:
    reader = csv.reader(f1)
    next(reader)
    supplier_ids = [row[0] for row in reader]
    with open(MATERIALS_FILE, "w") as f2:
        writer = csv.writer(f2)
        count = 1
        header = ["ID", "SID", "BIN LOC", "ITEMS PER CUBE", "COST PER ITEM", "IBQ", "SAFETY STOCK", "MIN ORD QTY", "FREQ"]
        writer.writerow(header)
        for sid in supplier_ids:
            for i in range(n_items()):
                mid = f"MT{count:03d}"
                binloc = ProbValue.get_value_from_probability_list(BINLOC_PVS, len(BINLOC_PVS))
                ipc = random.randint(1, 30)
                cpi = round(random.randint(450, 99999) / 100, 2)
                economic_order_qty = random.randint(20, 130)
                safety_stock = round(economic_order_qty*.25)
                min_order_qty = round(economic_order_qty * .08)
                frequency = ProbValue.get_value_from_probability_list(FREQUENCY_PVS, len(FREQUENCY_PVS))
                row = [mid, sid, binloc, ipc, cpi, economic_order_qty, safety_stock, min_order_qty, frequency]
                writer.writerow(row)
                count += 1

