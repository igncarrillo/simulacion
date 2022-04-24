import config


def get_static_params():
    return config.STATIC_ANG_XY, config.STATIC_ANG_XZ, config.STATIC_VEL, config.STATIC_ALT


def get_variable_params():
    ang_xy = get_ang_xy_value()
    ang_xz = get_ang_xz_value()
    vel = get_vel_value()
    alt = get_alt_value()
    return ang_xy, ang_xz, vel, alt


def get(static_params):
    if static_params:
        return get_static_params()
    else:
        return get_variable_params()


def get_float_value(msg):
    while True:
        value = input(msg)
        try:
            float_val = float(value)
            break
        except ValueError:
            print(f"{value} no es un float valido, intente nuevamente")
    return float_val


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
