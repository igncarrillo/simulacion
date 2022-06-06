import config


def get(static_params):
    if static_params:
        return get_static_params()
    else:
        return get_variable_params()


def get_static_params():
    return config.STATIC_ANG_XY, config.STATIC_ANG_XZ, config.STATIC_VEL, \
           config.STATIC_ALT, config.SHOTS_NUMBER


def get_variable_params():
    ang_xy = get_ang_xy_value()
    ang_xz = get_ang_xz_value()
    vel = get_vel_value()
    alt = get_alt_value()
    q = get_shots_value()
    m = get_mass_value()
    return ang_xy, ang_xz, vel, alt, q


# region values
def get_shots_value():
    while True:
        value = get_int_value("Ingrese una cantidad de tiros: ")
        if value > 0:
            break
        print(f"{value} no es un valor de tiros valido, intente nuevamente")
    return value


def get_ang_xy_value():
    while True:
        value = get_float_value("Ingrese un angulo de tiro menor a 90 grados: ")
        if 90 > value > 0:
            break
        print(f"{value} no es un valor de angulo valido, intente nuevamente")
    return value


def get_ang_xz_value():
    while True:
        value = get_float_value("Ingrese un angulo de giro entre 0 y 180 grados: ")
        if 180 > value > 0:
            break
        print(f"{value} no es un valor de angulo valido, intente nuevamente")
    return value


def get_vel_value():
    while True:
        value = get_float_value("Ingrese una velocidad inicial superior a 0: ")
        if value > 0:
            break
        print(f"{value} no es un valor de velocidad inicial valida, intente nuevamente")
    return value


def get_alt_value():
    while True:
        value = get_float_value("Ingrese una altura superior o igual a 0: ")
        if value >= 0:
            break
        print(f"{value} no es un valor de altura valida, intente nuevamente")
    return value


def get_mass_value():
    while True:
        value = get_float_value("Ingrese una masa superior o igual a 0 en kg: ")
        if value >= 0:
            break
        print(f"{value} no es un valor de masa valido, intente nuevamente")
    return value


# endregion

# region type values
def get_int_value(msg):
    while True:
        value = input(msg)
        try:
            int_val = int(value)
            break
        except ValueError:
            print(f"{value} no es un entero valido, intente nuevamente")
    return int_val


def get_float_value(msg):
    while True:
        value = input(msg)
        try:
            float_val = float(value)
            break
        except ValueError:
            print(f"{value} no es un float valido, intente nuevamente")
    return float_val


# endregion

# CARACTERISTICAS DISCO COMPETICION FEMENINA
MASS = 1.0  # kg
ALTURA_DISCO = 0.037  # m
RADIO_DISCO = 0.09  # m


def get_disk_params():
    return MASS, ALTURA_DISCO, RADIO_DISCO
