import math
import random

# CONSTANTS
RHO = 1.205  # CNPT kg/m3


def generate(quantity, r, alt_disk):
    winds = []
    area = calculate_area(r, alt_disk)
    for i in range(quantity):
        if i == 0:
            winds.append((0, 0, 0))
            continue
        ang = random.randint(0, 360)  # degrees
        v = random.uniform(0, 10)  # vientos hasta 36km/h en m/s
        t = random.uniform(0, 3)  # secs of actuation between 0 and 3
        p = (1 / 2) * math.pow(v, 2) * RHO  # Pa = N/m2
        f = p * area  # N
        winds.append((ang, f, t))
    return winds


def calculate_area(r, altura):
    # area_bases = 2 * math.pi * math.pow(r, 2) creo q no actua porq el viento es lateral
    area_bases = 0
    area_lateral = 2 * math.pi * r * altura
    return area_lateral + area_bases
