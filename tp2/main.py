import config
import graphic
import params
import table

# Modelos y simulacion

# TP2

# -Lanzamiento atlético de disco 3D (TIRO PARABOLICO)
# -Lenguaje: Python
# -Tick de tiempo: medio segundo
# -Modelo deterministico (A- tabla , B- grafico)


if __name__ == '__main__':
    ang, vel, alt = params.get(config.STATIC_PARAMS)
    animation = graphic.Animation(ang, vel, alt)
    animation.draw()
    table.generate(ang, vel, alt)
