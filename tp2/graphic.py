import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

import config
import physics

# initializing empty values
# for x and y co-ordinates
xdata, ydata, zdata = [], [], []


class Animation:
    def __init__(self, ang_xy, ang_xz, vel, alt):
        # First set up the figure, the axis, and the plot element we want to animate
        self.fig = plt.figure()
        ax = Axes3D(self.fig)
        ax.set_xlabel('X[m]')
        ax.set_ylabel('Z[m]')
        ax.set_zlabel('Y[m]')
        ax.set_xlim3d(config.X_START_GRAPHIC, physics.calculate_x_displacement(ang_xy, ang_xz, vel,
                                                                               physics.calculate_flight_time(ang_xy,
                                                                                                             vel,
                                                                                                             alt)) + config.DRAWING_MARGIN)
        ax.set_ylim3d(-100, 100)
        ax.set_zlim3d(config.Y_START_GRAPHIC,
                      physics.calculate_maximum_height(ang_xy, vel, alt) + config.DRAWING_MARGIN)
        ax.set_title('Desplazamiento del disco [m]', fontdict={'fontsize': 12}, loc='center')
        self.line, = ax.plot([], [], [], lw=3, label='Posicion disco [m]')

        self.ang_xy = ang_xy
        self.ang_xz = ang_xz
        self.alt = alt
        self.vel = vel

    def draw(self):
        # noinspection PyTypeChecker
        anim = animation.FuncAnimation(self.fig, self.grapher, init_func=self.init,
                                       frames=np.arange(config.X_START_GRAPHIC,
                                                        physics.calculate_flight_time(self.ang_xy,
                                                                                      self.vel,
                                                                                      self.alt) + config.TIME_TICK,
                                                        config.TIME_TICK),
                                       fargs=(self.ang_xy, self.ang_xz, self.vel, self.alt),
                                       interval=config.GRAPH_DELAY_MS, repeat=False)

        plt.grid(True)
        plt.legend(loc='upper right')
        plt.show()
        self.fig.savefig('figure.png')
        plt.close()

    def init(self):
        self.line.set_data([], [])
        self.line.set_3d_properties([])

    def grapher(self, i, ang_xy, ang_xz, vel, alt):
        yi = physics.calculate_y_displacement(ang_xy, vel, alt, i)
        xi = physics.calculate_x_displacement(ang_xy, ang_xz, vel, i)
        zi = physics.calculate_z_displacement(ang_xy, ang_xz, vel, i)
        if yi < 0:
            ti = physics.calculate_flight_time(ang_xy, vel, alt)
            xi = physics.calculate_x_displacement(ang_xy, ang_xz, vel, ti)
            zi = physics.calculate_z_displacement(ang_xy, ang_xz, vel, ti)
            yi = 0
        xdata.append(xi)
        ydata.append(yi)
        zdata.append(zi)
        self.line.set_data(xdata, zdata)
        self.line.set_3d_properties(ydata)


def get_data():
    return xdata, ydata, zdata
