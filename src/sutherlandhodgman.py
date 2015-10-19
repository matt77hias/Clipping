import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

###################################################################################################################################################################################
## TEST VALUES
###################################################################################################################################################################################
polygon2D = [[50.0, 150.0], [200.0, 50.0], [350.0, 150.0], [350.0, 300.0], [250.0, 300.0], [200.0, 250.0], [150.0, 350.0], [100.0, 250.0], [100.0, 200.0]]
clipper2D = [[100.0, 100.0], [300.0, 100.0], [300.0, 300.0], [100.0, 300.0]]

polygon3D = [[50.0, 150.0, 0.0], [200.0, 50.0, 0.0], [350.0, 150.0, 0.0], [350.0, 300.0, 0.0], [250.0, 300.0, 0.0], [200.0, 250.0, 0.0], [150.0, 350.0, 0.0], [100.0, 250.0, 0.0], [100.0, 200.0, 0.0]]
clipper3D = [[100.0, 100.0, 0.0], [300.0, 100.0, 0.0], [300.0, 300.0, 0.0], [100.0, 300.0, 0.0]]

t1 = [[0.0,0.0],[10.0,0.0],[0.0,10.0]]
t2 = [[0.0,0.0],[10.0,0.0],[0.0,-10.0]]
t3 = [[0.0,0.0],[10.0,0.0],[10.0,10.0]]
t4 = [[0.0,0.0],[10.0,0.0],[-10.0,10.0]]
t5 = [[10.0,0.0],[10.0,0.0],[10.0,0.0]]
t6 = [[1.0,0.0],[2.0,0.0],[3.0,0.0]]
t7 = [[1.0,0.0],[3.0,0.0],[2.0,0.0]]
t8 = [[1.0,0.0],[2.0,0.0],[3.0,3.0]]
t9 = [[1.0,2.0],[3.0,5.0],[7.0,9.0]]

c1 = [[-50.0, -50.0, 0.0], [50.0, -50.0, 0.0], [50.0, 50.0, 0.0], [-50.0, 50.0, 0.0]]
c2 = c1[1:]+[c1[0]]
c3 = c2[1:]+[c2[0]]
c4 = c3[1:]+[c3[0]]
c5 = [[-50.0, -50.0, 0.0], [-50.0, 50.0, 0.0], [50.0, 50.0, 0.0], [50.0, -50.0, 0.0]]
c6 = c5[1:]+[c5[0]]
c7 = c6[1:]+[c6[0]]
c8 = c7[1:]+[c7[0]]

###################################################################################################################################################################################
## 2D clipping
## ---------------------------------
## Convex polygon <> Convex polygon
###################################################################################################################################################################################

def plot_clip2D(p_vs, c_vs):
    plot_line2D(p_vs, color='r')
    plot_line2D(c_vs, color='b')
    plot_line2D(clip2D(p_vs, c_vs), color='g')

def plot_line2D(p_vs, color):
    nb_p_vs = len(p_vs)
    for j in range(nb_p_vs):
        p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
        p_v2 = p_vs[j]
        plt.plot([p_v1[0], p_v2[0]], [p_v1[1], p_v2[1]], color=color, linestyle='-', linewidth=2)

def clip2D(p_vs, c_vs):
    new_p_vs = p_vs
    
    nb_c_vs = len(c_vs)
    for i in range(nb_c_vs):
        c_v1 = c_vs[(i+nb_c_vs-1) % nb_c_vs]
        c_v2 = c_vs[i]
        
        old_p_vs = new_p_vs
        new_p_vs = []

        nb_p_vs = len(old_p_vs)
        for j in range(nb_p_vs):
            p_v1 = old_p_vs[(j+nb_p_vs-1) % nb_p_vs]
            p_v2 = old_p_vs[j]
            
            #Line segment clipping
            if inside2D(c_v1, c_v2, p_v2):
                if not inside2D(c_v1, c_v2, p_v1): 
                    new_p_vs.append(intersect2D(c_v1, c_v2, p_v1, p_v2))
                new_p_vs.append(p_v2)
            elif inside2D(c_v1, c_v2, p_v1):
                new_p_vs.append(intersect2D(c_v1, c_v2, p_v1, p_v2))
    return new_p_vs
        
def inside2D(c_v1, c_v2, p_v):
    return (c_v1[0] - p_v[0]) * (c_v2[1] - p_v[1]) >= (c_v1[1] - p_v[1]) * (c_v2[0] - p_v[0]);
    
def intersect2D(c_v1, c_v2, p_v1, p_v2):
    A1 = c_v2[1] - c_v1[1]
    B1 = c_v1[0] - c_v2[0]
    C1 = c_v1[0] * A1 + c_v1[1] * B1
    
    A2 = p_v2[1] - p_v1[1]
    B2 = p_v1[0] - p_v2[0]
    C2 = p_v1[0] * A2 + p_v1[1] * B2
    
    det = A1 * B2 - B1 * A2
    X1 = (C1 * B2 - B1 * C2) / det;
    X2 = (A1 * C2 - C1 * A2) / det;
    return [X1, X2]   

###################################################################################################################################################################################
## 3D clipping
## ---------------------------------
## Convex polygon <> Plane
## Convex Polygon << AABB
###################################################################################################################################################################################

def plot_AABB(pmin, pmax):
    plot_line3D([[pmin[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmin[2]], [pmax[0], pmax[1], pmin[2]], [pmin[0], pmax[1], pmin[2]]], color='b')
    plot_line3D([[pmin[0], pmin[1], pmax[2]], [pmax[0], pmin[1], pmax[2]], [pmax[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmax[2]]], color='b')
    plot_line3D([[pmin[0], pmin[1], pmin[2]], [pmin[0], pmin[1], pmax[2]], [pmin[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmin[2]]], color='b')
    plot_line3D([[pmax[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmax[2]], [pmax[0], pmax[1], pmax[2]], [pmax[0], pmax[1], pmin[2]]], color='b')
    plot_line3D([[pmin[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmin[2]], [pmax[0], pmin[1], pmax[2]], [pmin[0], pmin[1], pmax[2]]], color='b')
    plot_line3D([[pmin[0], pmax[1], pmin[2]], [pmax[0], pmax[1], pmin[2]], [pmax[0], pmax[1], pmax[2]], [pmin[0], pmax[1], pmax[2]]], color='b')

def plot_clip3D_AABB(p_vs, pmin, pmax):
    plot_line3D(p_vs, color='r')
    plot_AABB(pmin, pmax)
    plot_line3D(clip3D_AABB(p_vs, pmin, pmax), color='g')

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

def clip3D_AABB(p_vs, pmin, pmax):
    print(p_vs)
    print('------------------------------------------------------------------------------------------------------------------------------')
    sort_vertices(p_vs, a0=1, a1=2)
    c_vs = [[0.0, pmax[1],pmax[2]], [0.0, pmin[1],pmax[2]], [0.0, pmin[1], pmin[2]], [0.0, pmax[1], pmin[2]]]
    p_vs = clip3D_plane(p_vs, c_vs, a0=1, a1=2)
    print(p_vs)
    print('------------------------------------------------------------------------------------------------------------------------------')
    sort_vertices(p_vs, a0=2, a1=0)
    c_vs = [[pmin[0], 0.0, pmax[2]],[pmax[0], 0.0, pmax[2]],[pmax[0], 0.0, pmin[2]],[pmin[0], 0.0, pmin[2]]]
    p_vs = clip3D_plane(p_vs, c_vs, a0=2, a1=0)
    print(p_vs)
    print('------------------------------------------------------------------------------------------------------------------------------')
    sort_vertices(p_vs, a0=0, a1=1)
    c_vs = [[pmax[0], pmin[1], 0.0],[pmax[0], pmax[1], 0.0],[pmin[0], pmax[1], 0.0],[pmin[0], pmin[1], 0.0]]
    p_vs = clip3D_plane(p_vs, c_vs, a0=0, a1=1)
    print(p_vs)
    print('------------------------------------------------------------------------------------------------------------------------------')
    return p_vs
    
def clip3D_plane(p_vs, c_vs, a0=0, a1=1):
    new_p_vs = p_vs
    
    nb_c_vs = len(c_vs)
    for i in range(nb_c_vs):
        c_v1 = c_vs[(i+nb_c_vs-1) % nb_c_vs]
        c_v2 = c_vs[i]
        
        old_p_vs = new_p_vs
        new_p_vs = []

        nb_p_vs = len(old_p_vs)
        for j in range(nb_p_vs):
            p_v1 = old_p_vs[(j+nb_p_vs-1) % nb_p_vs]
            p_v2 = old_p_vs[j]
            
            if inside3D(c_v1, c_v2, p_v2, a0, a1):
                if not inside3D(c_v1, c_v2, p_v1, a0, a1): 
                    new_p_vs.append(intersect3D(c_v1, c_v2, p_v1, p_v2, a0, a1))
                new_p_vs.append(p_v2)
            elif inside3D(c_v1, c_v2, p_v1, a0, a1):
                new_p_vs.append(intersect3D(c_v1, c_v2, p_v1, p_v2, a0, a1))
    return new_p_vs

def inside3D(c_v1, c_v2, p_v2, a0, a1):
    return (c_v1[a0] - p_v2[a0]) * (c_v2[a1] - p_v2[a1]) >= (c_v1[a1] - p_v2[a1]) * (c_v2[a0] - p_v2[a0]);   
            
def intersect3D(c_v1, c_v2, p_v1, p_v2, a0, a1):
    A1 = c_v2[a1] - c_v1[a1]
    B1 = c_v1[a0] - c_v2[a0]
    C1 = c_v1[a0] * A1 + c_v1[a1] * B1
    
    A2 = p_v2[a1] - p_v1[a1]
    B2 = p_v1[a0] - p_v2[a0]
    C2 = p_v1[a0] * A2 + p_v1[a1] * B2
    
    det = A1 * B2 - B1 * A2
    X1 = (C1 * B2 - B1 * C2) / det;
    X2 = (A1 * C2 - C1 * A2) / det;
    
    alpha = -1.0
    if B2 != 0:
        alpha = (X1 - p_v2[a0]) / np.double(B2)
    else:
        alpha = (p_v2[a1] - X2) / np.double(A2)
    
    a2 = 3 - (a1 + a0)
    X3 = alpha * p_v1[a2] + (1.0 - alpha) * p_v2[a2]

    X = [0.0, 0.0, 0.0]
    X[a0] = X1
    X[a1] = X2
    X[a2] = X3
    return X
   
###################################################################################################################################################################################
## Vertex sorting tools
################################################################################################################################################################################### 

def sort_vertices(p_vs, a0=0, a1=1):
    index0 = -1
    index1 = -1
    
    nb_p_vs = len(p_vs)
    for j in range(nb_p_vs):
        p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
        p_v2 = p_vs[j]
        d0 = p_v2[a0] - p_v1[a0]
        d1 = p_v2[a1] - p_v1[a1]
        
        b0 = (d0 != 0.0) #TODO: precision
	b1 = (d1 != 0.0)
        if b0 and b1:
            if d1 / d0  < 0:
                return p_vs
            else:
                p_vs.reverse()
                return p_vs
        elif not b0 and b1:
            if index1 != -1:
                p_v = p_vs[index1]
                if inside3D(p_v, p_v1, p_v2, a0, a1): #or not inside3D(p_v, p_v2, p_v1, a0, a1):
                    return p_vs
                else:
                    p_vs.reverse()
                    return p_vs
            index0 = (j+nb_p_vs-1) % nb_p_vs
        elif b0 and not b1:
            if index0 != -1:
                p_v = p_vs[index0]
                if inside3D(p_v, p_v1, p_v2, a0, a1): #or not inside3D(p_v, p_v2, p_v1, a0, a1):
                    return p_vs
                else:
                    p_vs.reverse()
                    return p_vs
            index1 = (j+nb_p_vs-1) % nb_p_vs
    return p_vs