import matplotlib.pyplot as plt
from scipy import constants as scipy
from matplotlib import animation
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import math
import config
import physics


class Animation:
    def __init__(self, ang_xy, ang_xz, vel, alt, winds, mass):
        # First set up the figure, the axis, and the plot element we want to animate
        self.fig = plt.figure()
        ax = Axes3D(self.fig)
        ax.set_xlabel('X[m]')
        ax.set_ylabel('Z[m]')
        ax.set_zlabel('Y[m]')
        ax.set_xlim3d(0, 60)
        ax.set_ylim3d(0, 100)
        ax.set_zlim3d(0, 30)
        ax.set_title('Desplazamiento del disco [m]', fontdict={'fontsize': 12}, loc='center')

        self.ang_xy = ang_xy
        self.ang_xz = ang_xz
        self.alt = alt
        self.vel = vel
        self.winds = winds
        self.mass = mass
        self.max_height = physics.calculate_maximum_height(ang_xy, vel, alt)
        self.flight_time = physics.calculate_flight_time(ang_xy, vel, alt)

        # create axes draw
        self.lines = []
        for i in range(len(self.winds)):
            if i == 0:
                line, = ax.plot([], [], [], lw=2, label='Posicion ideal disco [m]', color='blue')
                self.lines.append(line)
                continue
            line, = ax.plot([], [], [], lw=1, label='Posicion disco [m], curve {0}'.format(i))
            self.lines.append(line)

        # create movement quantity data
        self.movement_quantity = [[[physics.calculate_initial_x_movement_quantity(ang_xz, ang_xy, vel, mass)],
                                   [physics.calculate_initial_y_movement_quantity(ang_xy, vel, mass)],
                                   [physics.calculate_initial_z_movement_quantity(ang_xz, ang_xy, vel, mass)]]
                                  for i in range(len(self.lines))]

        # create position data
        self.position = [[[0], [alt], [0]] for i in range(len(self.lines))]

        # wind time vector
        self.wind_time = [0 for i in range(len(self.winds))]

    def init(self):
        for line in self.lines:
            line.set_data([], [])
            line.set_3d_properties([])

    def draw(self):
        # noinspection PyTypeChecker
        self.anim = animation.FuncAnimation(self.fig, self.grapher, init_func=self.init,
                                            frames=np.arange(0, self.flight_time + config.TIME_TICK, config.TIME_TICK),
                                            interval=config.GRAPH_DELAY_MS, repeat=False)

        plt.grid(True)
        plt.legend(loc='upper right')
        plt.show()
        self.fig.savefig('figure.png')
        plt.close()

    def grapher(self, i):
        for idx, wind in enumerate(self.winds):
            mx = self.movement_quantity[idx][0][-1]
            my = self.movement_quantity[idx][1][-1] - self.mass * config.TIME_TICK * scipy.g
            mz = self.movement_quantity[idx][2][-1]

            yi = physics.calculate_displacement(self.position[idx][1][-1], my, self.mass)

            # add wind effect
            if self.should_wind(yi, wind[2], idx):
                mx += self.winds[idx][1] * math.cos(self.winds[idx][0]) * config.TIME_TICK

                mz += self.winds[idx][1] * math.sin(self.winds[idx][0]) * config.TIME_TICK
                self.wind_time[idx] += config.TIME_TICK

            xi = physics.calculate_displacement(self.position[idx][0][-1], mx, self.mass)
            zi = physics.calculate_displacement(self.position[idx][2][-1], mz, self.mass)

            # contact point
            if yi < 0:
                yi = 0
                self.anim.event_source.stop()

            else:
                # append new movement quantity
                self.movement_quantity[idx][0].append(mx)
                self.movement_quantity[idx][1].append(my)
                self.movement_quantity[idx][2].append(mz)

            # append new positions
            self.position[idx][0].append(xi)
            self.position[idx][1].append(yi)
            self.position[idx][2].append(zi)

            # add to graphic
            self.lines[idx].set_data(self.position[idx][0], self.position[idx][2])
            self.lines[idx].set_3d_properties(self.position[idx][1])

    def get_data(self):
        return self.position, self.flight_time

    def get_wind(self):
        return self.winds

    def should_wind(self, yi, max_time, idx):
        return (yi >= ((2 / 3) * self.max_height)) and max_time >= self.wind_time[idx]
