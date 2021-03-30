import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch


def generate(width, figsize, color, max_val, increment, rotate_func, radius_func, circle_radius_func, circle_angle_factor, debug=False):
    points = generate_points(max_val, increment, rotate_func, radius_func, circle_radius_func, circle_angle_factor, debug)
    fig, ax = plot(points, width, figsize, color, debug)

    return fig, ax


def generate_points(max_val, increment, offset, rotate_func, radius_func, circle_radius_func, circle_angle_factor, debug):
    """

    :param max_val:
    :param increment:
    :param rotate_func:
    :param radius_func:
    :param circle_radius_func:
    :param circle_angle_factor:
    "param debug:
    :return:
    """

    t = np.arange(0, max_val, increment)
    base_angle = rotate_func(t) + offset
    radius = radius_func(t)
    circle_angle = np.arange(0, len(t)) * circle_angle_factor
    circle_radius = circle_radius_func(t)

    if debug:
        ax1 = plt.subplot(411)
        plt.plot(t, base_angle)
        plt.title('Base Angle Rotation')
        ax2 = plt.subplot(412, sharex=ax1)
        plt.plot(t, radius)
        plt.title('Base Radius')
        ax3 = plt.subplot(413, sharex=ax1)
        plt.plot(t, circle_angle)
        plt.title('Circle Angle')
        ax4 = plt.subplot(414, sharex=ax1)
        plt.plot(t, circle_radius)
        plt.title('Circle Radius')
        plt.show()

    centers = np.column_stack((radius * np.cos(base_angle), radius * np.sin(base_angle)))
    points = centers + np.column_stack((circle_radius * np.cos(circle_angle), circle_radius * np.sin(circle_angle)))

    return points


# Need to add in line width
def plot(points, width, figsize, color, debug=False):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_aspect('equal')

    if not debug:
        plt.grid(False)
        plt.axis('off')

    ax.set_xlim(-width, width)
    ax.set_ylim(-width, width)

    ax.plot(points[:, 0], points[:, 1], color=color, )
    return fig, ax
