import math

from scipy import constants as scipy

# CONSTANTS
DEGREES_to_RADIANS = (math.pi / 180)


# Ecuaciones fisicas del movimiento
## Trayectoria
# Horizontal ->  x = v0 * cos(θo) * t + Xo                          (MRU)
# Vertical   ->  y = v0 * sen(θo) * t - 1/2 g * (t*t) + Yo          (MRUV)
# t = [V * sin(α) + √((V * sin(α))² + 2 * g * h)] / g               (flight time)
# R = V * cos(α) * [V * sin(α) + √(V * sin(α))² + 2 * g * h)] / g   (maximum range)
# hmax = h + V² * sin(α)² / (2 * g)                                 (maximum height)


def calculate_x_displacement(ang, vel, time):
    return vel * math.cos(ang * DEGREES_to_RADIANS) * time


def calculate_y_displacement(ang, vel, alt, time):
    return vel * math.sin(ang * DEGREES_to_RADIANS) * time + alt - 1 / 2 * math.pow(time, 2) * scipy.g


def calculate_flight_time(ang, vel, alt):
    return (vel * math.sin(ang * DEGREES_to_RADIANS) + math.sqrt(
        math.pow(vel * math.sin(ang * DEGREES_to_RADIANS), 2) + 2 * scipy.g * alt)) / scipy.g


def calculate_maximum_range(ang, vel, alt):
    return vel * math.cos(ang * DEGREES_to_RADIANS) * (vel * math.sin(ang * DEGREES_to_RADIANS) + math.sqrt(
        math.pow(vel * math.sin(ang * DEGREES_to_RADIANS), 2) + 2 * scipy.g * alt)) / scipy.g


def calculate_maximum_height(ang, vel, alt):
    return alt + math.pow(vel * math.sin(ang * DEGREES_to_RADIANS), 2) / (2 * scipy.g)
