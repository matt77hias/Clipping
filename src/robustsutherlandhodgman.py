###############################################################################
## Clipping
## ----------------------------------------------------------------------------
## Convex polygon <> AABB
## Convex polygon <> AABP
###############################################################################
import numpy as np

from math_utils import lerp
from orientation import classify_aligned

def clip_AABB(p_vs, pMin, pMax, step=False):
    for a in range(pMin.shape[0]):
       p_vs = clip_AABP(p_vs, 1.0, a, pMin)
       if step: print(p_vs)
       p_vs = clip_AABP(p_vs, -1.0, a, pMax)
       if step: print(p_vs)
    return p_vs

def clip_AABP(p_vs, s, a, c_v):
    nb_p_vs = len(p_vs)
    if (nb_p_vs <= 1):  return []

    new_p_vs = []
    b = True #polygon is fully located on clipping plane
    for j in range(nb_p_vs):
        p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
        p_v2 = p_vs[j]

        d1 = classify_aligned(s, a, c_v, p_v1)
        d2 = classify_aligned(s, a, c_v, p_v2)
        if d2 < 0:
            b = False
            if d1 > 0:
                alpha  = (p_v2[a] - c_v[a]) / (p_v2[a] - p_v1[a])
                p = lerp(alpha, p_v1, p_v2)
                new_p_vs.append(p)
            elif d1 == 0:
                _safe_append(new_p_vs, p_v1)
        elif d2 > 0:
            b = False
            if d1 < 0:
                alpha  = (p_v2[a] - c_v[a]) / (p_v2[a] - p_v1[a])
                p = lerp(alpha, p_v1, p_v2)
                new_p_vs.append(p)
            elif d1 == 0 :
                _safe_append(new_p_vs, p_v1)
                
            new_p_vs.append(p_v2)
        else:
            if d1 != 0:
                new_p_vs.append(p_v2)

    if b:
        return p_vs
    else:
        return new_p_vs

# (c) Matthias Moulin
def _safe_append(new_p_vs, p_v):
    if (len(new_p_vs) == 0) or (not np.array_equal(new_p_vs[-1], p_v)):
        new_p_vs.append(p_v)
