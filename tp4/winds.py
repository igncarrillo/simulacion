import random
import math
import csv

# CONSTANTS
RHO = 1.205  # CNPT kg/m3
KNOTS_TO_MS = 0.514444


def generate(r, alt_disk):
    winds = [(0, 0, 0, 0)]
    file = open('wind_input.csv')
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    area = calculate_area(r, alt_disk)
    for row in csv_reader:
        hr = int(row[0])
        ang = float(row[1])
        v = float(row[2]) * KNOTS_TO_MS
        t = random.uniform(0, 3)  # secs of actuation between 0 and 3
        p = (1 / 2) * math.pow(v, 2) * RHO  # Pa = N/m2
        f = p * area  # N
        winds.append((ang, f, t, hr))
    return winds


def calculate_area(r, altura):
    # area_bases = 2 * math.pi * math.pow(r, 2) creo q no actua porq el viento es lateral
    area_bases = 0
    area_lateral = 2 * math.pi * r * altura
    return area_lateral + area_bases
