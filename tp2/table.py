import csv

import config
import graphic
import physics

header = ['x[m]', 'y[m]', 't[s]']


def generate(ang, vel, alt):
    x, y = graphic.get_data()
    with open("table.csv", "w") as tabla:
        writer = csv.writer(tabla)
        writer.writerow(header)
        for i in range(len(x) - 1):
            writer.writerow([f"{x[i]:2f}", f"{y[i]:2f}", f"{config.TIME_TICK * i:2f}"])
        writer.writerow(
            [f"{x[len(x) - 1]:2f}", f"{y[len(y) - 1]:2f}", f"{physics.calculate_flight_time(ang, vel, alt):2f}"])
        tabla.close()

    print(f"Altura Maxima: {physics.calculate_maximum_height(ang, vel, alt):2f}m")
    print(f"Rango maximo: {physics.calculate_maximum_range(ang, vel, alt):2f}m")
    print(f"Tiempo de vuelo: {physics.calculate_flight_time(ang, vel, alt):2f}s")

