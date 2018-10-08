from numpy import array

###############################################################################
## Clipping
###############################################################################

def clip_AABB(p_vs, pMin, pMax, step=False):
    dim = p_vs[0].shape[0]
    if dim == 2:
        return clip2D_AABB(p_vs, pMin, pMax, step=step)
    elif dim == 3:
        return clip3D_AABB(p_vs, pMin, pMax, step=step)
    else:
        return p_vs

###############################################################################
## 2D clipping
## ----------------------------------------------------------------------------
## Convex polygon <> Convex polygon
###############################################################################
from intersection import intersect2D
from orientation import inside2D

def clip2D_AABB(p_vs, pMin, pMax, step=False):
    c_vs = [[pMax[0], pMin[1]],[pMax[0], pMax[1]],[pMin[0], pMax[1]],[pMin[0], pMin[1]]]
    c_vs = [array(v) for v in c_vs]
    new_p_vs = clip2D(p_vs, c_vs)
    if (step): print(new_p_vs)
    return new_p_vs

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

###############################################################################
## 3D clipping
## ----------------------------------------------------------------------------
## Convex polygon <> AABB
## Convex polygon <> AABP
###############################################################################

from intersection import intersect3D
from orientation import inside3D, sort_vertices

def clip3D_AABB(p_vs, pMin, pMax, step=False):
    sort_vertices(p_vs, a0=1, a1=2)
    c_vs = [[0.0, pMax[1],pMax[2]], [0.0, pMin[1],pMax[2]], [0.0, pMin[1], pMin[2]], [0.0, pMax[1], pMin[2]]]
    c_vs = [array(v) for v in c_vs]
    if (step): print(p_vs)
    p_vs = clip3D_AABP(p_vs, c_vs, a0=1, a1=2)

    sort_vertices(p_vs, a0=2, a1=0)
    c_vs = [[pMin[0], 0.0, pMax[2]],[pMax[0], 0.0, pMax[2]],[pMax[0], 0.0, pMin[2]],[pMin[0], 0.0, pMin[2]]]
    c_vs = [array(v) for v in c_vs]
    if (step): print(p_vs)
    p_vs = clip3D_AABP(p_vs, c_vs, a0=2, a1=0)

    sort_vertices(p_vs, a0=0, a1=1)
    c_vs = [[pMax[0], pMin[1], 0.0],[pMax[0], pMax[1], 0.0],[pMin[0], pMax[1], 0.0],[pMin[0], pMin[1], 0.0]]
    c_vs = [array(v) for v in c_vs]
    if (step): print(p_vs)
    p_vs = clip3D_AABP(p_vs, c_vs, a0=0, a1=1)

    if (step): print(p_vs)
    return p_vs

def clip3D_AABP(p_vs, c_vs, a0=0, a1=1):
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
