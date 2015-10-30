import plot_utils as plt
import orientation

from intersection import intersect2D, intersect3D 
from surfacearea import area3D

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
            if orientation.inside2D(c_v1, c_v2, p_v2):
                if not orientation.inside2D(c_v1, c_v2, p_v1): 
                    new_p_vs.append(intersect2D(c_v1, c_v2, p_v1, p_v2))
                new_p_vs.append(p_v2)
            elif orientation.inside2D(c_v1, c_v2, p_v1):
                new_p_vs.append(intersect2D(c_v1, c_v2, p_v1, p_v2))
    return new_p_vs

###################################################################################################################################################################################
## 3D clipping
## ---------------------------------
## Convex polygon <> Plane
## Convex Polygon <> AABB
###################################################################################################################################################################################

def plot_clip3D_plane(p_vs, c_vs, a0=0, a1=1):
    plt.plot_clip3D(p_vs, c_vs, clip3D_plane, a0=a0, a1=a1)
    
def plot_clip3D_AABB(p_vs, pmin, pmax):
    n = orientation.get_normal(p_vs)
    plt.plot_line3D(p_vs, color='r')
    plt.plot_AABB(pmin, pmax)
    result = clip3D_AABB(p_vs, pmin, pmax, step=True)
    print (area3D(result, n))
    plt.plot_line3D(result, color='g')

def clip3D_AABB(p_vs, pmin, pmax, step=False):
    orientation.sort_vertices(p_vs, a0=1, a1=2)
    c_vs = [[0.0, pmax[1],pmax[2]], [0.0, pmin[1],pmax[2]], [0.0, pmin[1], pmin[2]], [0.0, pmax[1], pmin[2]]]
    if (step):
        print(p_vs)
        print(c_vs)
        print('------------------------------------------------------------------------------------------------------------------------------')
    p_vs = clip3D_plane(p_vs, c_vs, a0=1, a1=2)
    orientation.sort_vertices(p_vs, a0=2, a1=0)
    c_vs = [[pmin[0], 0.0, pmax[2]],[pmax[0], 0.0, pmax[2]],[pmax[0], 0.0, pmin[2]],[pmin[0], 0.0, pmin[2]]]
    if (step):
        print(p_vs)
        print(c_vs)
        print('------------------------------------------------------------------------------------------------------------------------------')
    p_vs = clip3D_plane(p_vs, c_vs, a0=2, a1=0)
    orientation.sort_vertices(p_vs, a0=0, a1=1)
    c_vs = [[pmax[0], pmin[1], 0.0],[pmax[0], pmax[1], 0.0],[pmin[0], pmax[1], 0.0],[pmin[0], pmin[1], 0.0]]
    if (step):
        print(p_vs) 
        print(c_vs)
        print('------------------------------------------------------------------------------------------------------------------------------')
    p_vs = clip3D_plane(p_vs, c_vs, a0=0, a1=1)
    if (step):
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
            
            if orientation.inside3D(c_v1, c_v2, p_v2, a0, a1):
                if not orientation.inside3D(c_v1, c_v2, p_v1, a0, a1):
                    new_p_vs.append(intersect3D(c_v1, c_v2, p_v1, p_v2, a0, a1))
                new_p_vs.append(p_v2)
            elif orientation.inside3D(c_v1, c_v2, p_v1, a0, a1):
                new_p_vs.append(intersect3D(c_v1, c_v2, p_v1, p_v2, a0, a1))
    return new_p_vs