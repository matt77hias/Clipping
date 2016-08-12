import numpy as np

from orientation import get_normal
from robustsutherlandhodgman import clip_AABB as clip_AABB_robust
from surfacearea import area
from test import plot_clip_AABB_robust

fstat="C:/Users/Matthias/Documents/Courses/Masterproef/pbrt/pbrt-v2/pbrt-v2/src/pbrt.vs2012/clipping.txt"

def check(fstat):
    with open(fstat, 'r') as infile:
        for line in infile:
            if eval(line) != 0:
                print(line)
                print(eval(line))
            
def f(p_vs, pMin, pMax):
    new_p_vs = clip_AABB_robust(np.array(p_vs), np.array(pMin), np.array(pMax))
    return area(new_p_vs, n=get_normal(np.array(p_vs)))
    
def g(p_vs, pMin, pMax):
    plot_clip_AABB_robust(np.array(p_vs), np.array(pMin), np.array(pMax), step=True)
    
def e(p_vs, pMin, pMax):
    return np.array(pMax) - np.array(pMin)