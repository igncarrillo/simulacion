import csv

import config
import graphic
import physics

header = ['x[m]', 'y[m]', 'z[m]', 't[s]']


def generate(ang_xy, ang_xz, vel, alt):
    x, y, z = graphic.get_data()
    with open("table.csv", "w") as tabla:
        writer = csv.writer(tabla)
        writer.writerow(header)
        for i in range(len(x) - 1):
            writer.writerow([f"{x[i]:2f}", f"{y[i]:2f}", f"{z[i]:2f}", f"{config.TIME_TICK * i:2f}"])
        writer.writerow(
            [f"{x[len(x) - 1]:2f}", f"{y[len(y) - 1]:2f}", f"{z[len(z) - 1]:2f}",
             f"{physics.calculate_flight_time(ang_xy, vel, alt):2f}"])
        tabla.close()

    print(f"Altura Maxima: {physics.calculate_maximum_height(ang_xy, vel, alt):2f}m")
    ti = physics.calculate_flight_time(ang_xy, vel, alt)
    print(f"Tiempo de vuelo: {ti:2f}s")
    print(f"Rango maximo: {physics.calculate_x_displacement(ang_xy, ang_xz, vel, ti):2f}m")
