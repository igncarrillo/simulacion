import csv

import config
import physics

header = ['x[m]', 'y[m]', 'z[m]', 't[s]']
wind_header = ['hr', 'ang[d]', 'force[N]', 't[s]']


def generate(position, flight_time):
    count = -3
    for idx, curve in enumerate(position):
        name = "wind_hr_{0}.csv".format(count)
        if idx == 0:
            name = "ideal.csv"
        with open(name, "w") as tabla:
            writer = csv.writer(tabla)
            writer.writerow(header)
            for i in range(len(curve[0]) - 1):
                writer.writerow(
                    [f"{curve[0][i]:2f}", f"{curve[1][i]:2f}", f"{curve[2][i]:2f}", f"{config.TIME_TICK * i:2f}"])
            writer.writerow(
                [f"{curve[0][-1]:2f}", f"{curve[1][-1]:2f}", f"{curve[2][-1]:2f}", f"{flight_time:2f}"])
            tabla.close()
        count += 3


def generate_wind(winds):
    with open("winds.csv", "w") as tabla:
        writer = csv.writer(tabla)
        writer.writerow(wind_header)
        for i in range(len(winds)):
            if i == 0:
                continue
            writer.writerow(
                [f"{winds[i][3]}", f"{winds[i][0]:2f}", f"{winds[i][1]:2f}", f"{winds[i][2]:2f}"])
        tabla.close()
