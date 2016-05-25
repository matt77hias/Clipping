import numpy as np
from mpl_toolkits.mplot3d import Axes3D

###################################################################################################################################################################################
## Plot Utilities 2D
###################################################################################################################################################################################

def set_equal_aspect_ratio_2D(ax, xs, ys, alpha=1.5, delta=0.0):
    ax.set_aspect('equal')
    
    mn = np.array([xs.min(), ys.min()])
    mx = np.array([xs.max(), ys.max()])
    d = 0.5 * (mx - mn)
    c = mn + d
    d = alpha * np.max(d) + delta
    
    ax.set_xlim(c[0] - d, c[0] + d)
    ax.set_ylim(c[1] - d, c[1] + d)
    
def set_equal_aspect_ratio_2D_AABP(ax, AABP, alpha=1.5, delta=0.0):
    set_equal_aspect_ratio_2D(ax, np.array([AABP.pMin[0], AABP.pMax[0]]), np.array([AABP.pMin[1], AABP.pMax[1]]), alpha=alpha, delta=delta)

###################################################################################################################################################################################
## Plot Utilities 3D
###################################################################################################################################################################################

def set_equal_aspect_ratio_3D(ax, xs, ys, zs, alpha=1.5, delta=0.0):
    ax.set_aspect('equal')
    
    mn = np.array([xs.min(), ys.min(), zs.min()])
    mx = np.array([xs.max(), ys.max(), zs.max()])
    d = 0.5 * (mx - mn)
    c = mn + d
    d = alpha * np.max(d) + delta
    
    ax.set_xlim(c[0] - d, c[0] + d)
    ax.set_ylim(c[1] - d, c[1] + d)
    ax.set_zlim(c[2] - d, c[2] + d)
    
def set_equal_aspect_ratio_3D_AABB(ax, AABB, alpha=1.5, delta=0.0):
    set_equal_aspect_ratio_3D(ax, np.array([AABB.pMin[0], AABB.pMax[0]]), np.array([AABB.pMin[1], AABB.pMax[1]]), np.array([AABB.pMin[2], AABB.pMax[2]]), alpha=alpha, delta=delta)