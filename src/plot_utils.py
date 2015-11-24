import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

###################################################################################################################################################################################
## 2D plotting
###################################################################################################################################################################################
def plot_clip2D(p_vs, c_vs, clipf):
    plot_line2D(p_vs, color='r')
    plot_line2D(c_vs, color='b')
    plot_line2D(clipf(p_vs, c_vs), color='g')
    
def plot_line2D(p_vs, color):
    nb_p_vs = len(p_vs)
    for j in range(nb_p_vs):
        p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
        p_v2 = p_vs[j]
        plt.plot([p_v1[0], p_v2[0]], [p_v1[1], p_v2[1]], color=color, linestyle='-', linewidth=2)

###################################################################################################################################################################################
## 3D plotting
###################################################################################################################################################################################  
def plot_clip3D(p_vs, c_vs, clipf, a0=0, a1=1):
    plot_line3D(p_vs, color='r')
    plot_line3D(c_vs, color='b')
    plot_line3D(clipf(p_vs, c_vs, a0, a1), color='g')

def plot_line3D(p_vs, color):
    ax = plt.gca(projection='3d')
    nb_p_vs = len(p_vs)
    for j in range(nb_p_vs):
        p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
        p_v2 = p_vs[j]
        ax.plot([p_v1[0], p_v2[0]], [p_v1[1], p_v2[1]], [p_v1[2], p_v2[2]], color=color, linestyle='-', linewidth=2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    
def plot_AABB(pmin, pmax):
    plot_line3D([[pmin[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmin[2]], [pmax[0], pmax[1], pmin[2]], [pmin[0], pmax[1], pmin[2]]], color='b')
    plot_line3D([[pmin[0], pmin[1], pmax[2]], [pmax[0], pmin[1], pmax[2]], [pmax[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmax[2]]], color='b')
    plot_line3D([[pmin[0], pmin[1], pmin[2]], [pmin[0], pmin[1], pmax[2]], [pmin[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmin[2]]], color='b')
    plot_line3D([[pmax[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmax[2]], [pmax[0], pmax[1], pmax[2]], [pmax[0], pmax[1], pmin[2]]], color='b')
    plot_line3D([[pmin[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmax[2]], [pmin[0], pmin[1], pmax[2]]], color='b')
    plot_line3D([[pmin[0], pmax[1], pmin[2]], [pmax[0], pmax[1], pmin[2]], [pmax[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmax[2]]], color='b')