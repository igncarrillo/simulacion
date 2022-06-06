import math

from scipy import constants as scipy

import config

# CONSTANTS
DEGREES_to_RADIANS = (math.pi / 180)


# Ecuaciones fisicas del movimiento
# hmax = h + V² * sin(α)² / (2 * g)                                             (maximum height)


def calculate_flight_time(ang, vel, alt):
    return (vel * math.sin(ang * DEGREES_to_RADIANS) + math.sqrt(
        math.pow(vel * math.sin(ang * DEGREES_to_RADIANS), 2) + 2 * scipy.g * alt)) / scipy.g


def calculate_maximum_height(ang, vel, alt):
    return alt + math.pow(vel * math.sin(ang * DEGREES_to_RADIANS), 2) / (2 * scipy.g)


def calculate_displacement(pos_ant, movement_quantity, mass):
    return pos_ant + (movement_quantity / mass) * config.TIME_TICK


def calculate_initial_x_movement_quantity(ang_xz, ang_xy, vel, mass):
    return mass * vel * math.cos(ang_xy * DEGREES_to_RADIANS) * math.sin(ang_xz * DEGREES_to_RADIANS)


def calculate_initial_z_movement_quantity(ang_xz, ang_xy, vel, mass):
    return mass * vel * math.cos(ang_xy * DEGREES_to_RADIANS) * math.cos(ang_xz * DEGREES_to_RADIANS)


def calculate_initial_y_movement_quantity(ang_xy, vel, mass):
    return mass * vel * math.sin(ang_xy * DEGREES_to_RADIANS)


def calculate_total_displacement(initial_mov_quantity, wind_force, wind_time, mass, total_time):
    return ((initial_mov_quantity + wind_force * wind_time) / mass) * total_time
