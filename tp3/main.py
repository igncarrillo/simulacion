import config
import graphic
import params
import table

# Modelos y simulacion

# TP3

# -Lanzamiento atlético de disco 3D (TIRO PARABOLICO) con fuerza aleatoria a partir de 2/3 hmax
# -Lenguaje: Python
# -Tick de tiempo: medio segundo
# -Modelo deterministico (A- tabla , B- grafico)
import wind

if __name__ == '__main__':
    ang_xy, ang_xz, vel, alt, quantity = params.get(config.STATIC_PARAMS)
    mass, alt_disk, r_disk = params.get_disk_params()
    winds = wind.generate(quantity, r_disk, alt_disk)
    animation = graphic.Animation(ang_xy, ang_xz, vel, alt, winds, mass)
    animation.draw()
    wind_data = animation.get_wind()
    pos, time = animation.get_data()
    table.generate(pos, time)
    table.generate_wind(wind_data)
