# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

###############################################################################
## Plotter
###############################################################################
from abc import ABCMeta, abstractmethod

class Plotter(object):

    __metaclass__ = ABCMeta

    def __init__(self, window_title=None, title=None):
        self.fig = plt.figure()
        self.ax  = self.get_default_axes()
        self.set_labels()
        if window_title is not None:
            self.set_window_title(window_title)
        if title is not None:
            self.set_title(title)

    def show(self):
        plt.show()

    def close(self):
        plt.close(self.fig)

    def clear(self):
        self.fig.clf()

    @abstractmethod
    def get_default_axes(self):
        return

    def set_window_title(self, title):
        self.fig.canvas.set_window_title(title)

    def set_title(self, title):
        self.fig.suptitle(title)

    @abstractmethod
    def set_labels(self):
        return

    @abstractmethod
    def set_equal_aspect_ratio(self, nAABB, alpha, delta):
        return

    @abstractmethod
    def plot_text(self, text, p, ha='center', va='center', **kwargs):
        return

    @abstractmethod
    def plot_point(self, p, **kwargs):
        return

    @abstractmethod
    def plot_line(self, v1, v2, **kwargs):
        return

    def plot_contour(self, vs, **kwargs):
        nb_vs = len(vs)
        for j in range(nb_vs):
            self.plot_line(vs[(j+nb_vs-1) % nb_vs], vs[j], **kwargs)

    @abstractmethod
    def plot_vector(self, rmin, rmax, **kwargs):
        return

    def plot_triangle(self, v1, v2, v3, **kwargs) :
        self.plot_contour([v1, v2, v3], **kwargs)

    @abstractmethod
    def plot_sphere(self, center, radius, **kwargs):
        return

    @abstractmethod
    def plot_AABB(self, pmin, pmax, **kwargs):
        return

    def save(self, fname, **kwargs):
        self.fig.savefig(fname, **kwargs)
        plt.close(self.fig)

###############################################################################
## Plotter2D
###############################################################################
from plot_utils import set_equal_aspect_ratio_2D_AABP

class Plotter2D(Plotter):

    def __init__(self, window_title=None, title=None):
        super(Plotter2D, self).__init__(window_title=window_title, title=title)

    def get_default_axes(self):
        return self.fig.gca()

    def set_labels(self):
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")

    def set_equal_aspect_ratio(self, nAABB, alpha=1.5, delta=0.0):
        set_equal_aspect_ratio_2D_AABP(self.ax, nAABB, alpha=alpha, delta=delta)

    def plot_text(self, text, p, ha='center', va='center', **kwargs):
        self.ax.text(p[0], p[1], text, ha=ha, va=va, **kwargs)

    def plot_point(self, p, **kwargs):
        self.ax.scatter([p[0]], [p[1]], **kwargs)

    def plot_line(self, v1, v2, **kwargs):
        self.ax.plot([v1[0], v2[0]], [v1[1], v2[1]], **kwargs)

    def plot_vector(self, rmin, rmax, **kwargs):
        a = Arrow2D([rmin[0], rmax[0]], [rmin[1], rmax[1]], **kwargs)
        self.ax.add_artist(a)

    def plot_sphere(self, center, radius, **kwargs):
        c = plt.Circle(center, radius=radius, fill=False, **kwargs)
        self.ax.add_artist(c)

    def plot_AABB(self, pmin, pmax, **kwargs):
        self.plot_contour([[pmin[0], pmin[1]], [pmax[0], pmin[1]], [pmax[0], pmax[1]], [pmin[0], pmax[1]]], **kwargs)

###############################################################################
## Plotter3D
###############################################################################
from plot_utils import set_equal_aspect_ratio_3D_AABB

class Plotter3D(Plotter):

    def __init__(self, window_title=None, title=None):
        super(Plotter3D, self).__init__(window_title=window_title, title=title)

    def get_default_axes(self):
        return plt.gca(projection='3d')

    def set_labels(self):
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_zlabel("z")

    def set_equal_aspect_ratio(self, nAABB, alpha=1.5, delta=0.0):
        set_equal_aspect_ratio_3D_AABB(self.ax, nAABB, alpha=alpha, delta=delta)

    def plot_text(self, text, p, ha='center', va='center', **kwargs):
        self.ax.text(p[0], p[1], p[2], text, ha=ha, va=va, **kwargs)

    def plot_point(self, p, **kwargs):
        self.ax.scatter([p[0]], [p[1]], [p[2]], **kwargs)

    def plot_line(self, v1, v2, **kwargs):
        self.ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], **kwargs)

    def plot_vector(self, rmin, rmax, **kwargs):
        a = Arrow3D([rmin[0], rmax[0]], [rmin[1], rmax[1]], [rmin[2], rmax[2]], **kwargs)
        self.ax.add_artist(a)

    def plot_sphere(self, center, radius, **kwargs):
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x = center[0] + radius * np.cos(u) * np.sin(v)
        y = center[1] + radius * np.sin(u) * np.sin(v)
        z = center[2] + radius * np.cos(v)
        self.ax.plot_wireframe(x, y, z, **kwargs)

    def plot_AABB(self, pmin, pmax, **kwargs):
        self.plot_contour([[pmin[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmin[2]], [pmax[0], pmax[1], pmin[2]], [pmin[0], pmax[1], pmin[2]]], **kwargs)
        self.plot_contour([[pmin[0], pmin[1], pmax[2]], [pmax[0], pmin[1], pmax[2]], [pmax[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmax[2]]], **kwargs)
        self.plot_contour([[pmin[0], pmin[1], pmin[2]], [pmin[0], pmin[1], pmax[2]], [pmin[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmin[2]]], **kwargs)
        self.plot_contour([[pmax[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmax[2]], [pmax[0], pmax[1], pmax[2]], [pmax[0], pmax[1], pmin[2]]], **kwargs)
        self.plot_contour([[pmin[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmax[2]], [pmin[0], pmin[1], pmax[2]]], **kwargs)
        self.plot_contour([[pmin[0], pmax[1], pmin[2]], [pmax[0], pmax[1], pmin[2]], [pmax[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmax[2]]], **kwargs)

###############################################################################
## Plot Utilities
###############################################################################
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow2D(FancyArrowPatch):
    def __init__(self, xs, ys, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts2d = xs, ys

    def draw(self, renderer):
        xs2d, ys2d = self._verts2d
        xs, ys = xs2d, ys2d
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)
