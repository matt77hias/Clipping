import plot_utils as plt
import orientation

import numpy as np

from intersection import interpolate 
from surfacearea import area3D

###################################################################################################################################################################################
## 3D clipping
## ---------------------------------
## Convex Polygon <> AABB
###################################################################################################################################################################################
  
def plot_clip3D_AABB(p_vs, pmin, pmax):
    n = orientation.get_normal(p_vs)
    plt.plot_line3D(p_vs, color='r')
    plt.plot_AABB(pmin, pmax)
    result = clip3D_AABB(p_vs, pmin, pmax, step=True)
    print(result)
    print(area3D(result, n))
    plt.plot_line3D(result, color='g')

def clip3D_AABB(p_vs, pmin, pmax, step=False):
    for a in range(3):
       p_vs = clip3D_plane(p_vs, 1.0, a, pmin)
       if step: print(p_vs)
       p_vs = clip3D_plane(p_vs, -1.0, a, pmax)
       if step: print(p_vs)
    return p_vs
    
def clip3D_plane(p_vs, s, a, c_v):
    new_p_vs = []

    nb_p_vs = len(p_vs)
    if (nb_p_vs <= 1):  return []
    for j in range(nb_p_vs):
        p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
        p_v2 = p_vs[j]
     
        d1 = orientation.classify_aligned(s, a, c_v, p_v1)
        d2 = orientation.classify_aligned(s, a, c_v, p_v2)
        
        if d2 < 0 and d1 > 0:
             alpha  = (np.double(p_v2[a]) - np.double(c_v[a])) / (np.double(p_v2[a]) - np.double(p_v1[a]))
             p = interpolate(alpha, p_v1, p_v2)
             new_p_vs.append(p)     
        elif d2 > 0:
            if d1 < 0:
                alpha  = (np.double(p_v2[a]) - np.double(c_v[a])) / (np.double(p_v2[a]) - np.double(p_v1[a]))
                p = interpolate(alpha, p_v1, p_v2)
                new_p_vs.append(p)
            elif d1 == 0:
                new_p_vs.append(p_v1)
            new_p_vs.append(p_v2) 
        elif d2 == 0 and d1 < 0:
            new_p_vs.append(p_v2)
    return new_p_vs