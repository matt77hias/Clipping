# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

###################################################################################################################################################################################
## Plotter
###################################################################################################################################################################################
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
    def plot_line(self, v1, v2, **kwargs):
        return
   
    def plot_contour(self, vs, **kwargs):
        nb_vs = len(vs)
        for j in range(nb_vs):
            self.plot_line(vs[(j+nb_vs-1) % nb_vs], vs[j], **kwargs)
            
    @abstractmethod
    def plot_AABB(self, pmin, pmax, **kwargs):
        return
         
    def save(self, fname, **kwargs):
        self.fig.savefig(fname, **kwargs)
        plt.close(self.fig)

###################################################################################################################################################################################
## Plotter2D
###################################################################################################################################################################################  
from plot_utils import set_equal_aspect_ratio_2D_AABP

class Plotter2D(Plotter):
    
    def __init__(self, window_title=None, title=None):
        super(Plotter2D, self).__init__(window_title=window_title, title=title)
    
    def get_default_axes(self):
        return self.fig.gca()

    def set_labels(self):
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        
    def set_equal_aspect_ratio(self, AABP, alpha=1.5, delta=0.0):
        set_equal_aspect_ratio_2D_AABP(self.ax, AABP, alpha=alpha, delta=delta)
   
    def plot_line(self, v1, v2, **kwargs):
        self.ax.plot([v1[0], v2[0]], [v1[1], v2[1]], **kwargs)
    
    def plot_AABB(self, pmin, pmax, **kwargs):
        self.plot_contour([[pmin[0], pmin[1]], [pmax[0], pmin[1]], [pmax[0], pmax[1]], [pmin[0], pmax[1]]], **kwargs)

###################################################################################################################################################################################
## Plotter3D
################################################################################################################################################################################### 
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
        
    def set_equal_aspect_ratio(self, AABB, alpha=1.5, delta=0.0):
        set_equal_aspect_ratio_3D_AABB(self.ax, AABB, alpha=alpha, delta=delta)
   
    def plot_line(self, v1, v2, **kwargs):
        self.ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], **kwargs)
   
    def plot_AABB(self, pmin, pmax, **kwargs):
        self.plot_contour([[pmin[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmin[2]], [pmax[0], pmax[1], pmin[2]], [pmin[0], pmax[1], pmin[2]]], **kwargs)
        self.plot_contour([[pmin[0], pmin[1], pmax[2]], [pmax[0], pmin[1], pmax[2]], [pmax[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmax[2]]], **kwargs)
        self.plot_contour([[pmin[0], pmin[1], pmin[2]], [pmin[0], pmin[1], pmax[2]], [pmin[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmin[2]]], **kwargs)
        self.plot_contour([[pmax[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmax[2]], [pmax[0], pmax[1], pmax[2]], [pmax[0], pmax[1], pmin[2]]], **kwargs)
        self.plot_contour([[pmin[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmax[2]], [pmin[0], pmin[1], pmax[2]]], **kwargs)
        self.plot_contour([[pmin[0], pmax[1], pmin[2]], [pmax[0], pmax[1], pmin[2]], [pmax[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmax[2]]], **kwargs)