from orientation import get_normal
from plotter import Plotter2D, Plotter3D
from robustsutherlandhodgman import clip_AABB as clip_AABB_robust
from surfacearea import area
from sutherlandhodgman import clip_AABB as clip_AABB_nonrobust

def plot_clip_AABB(p_vs, pMin, pMax, clipf, step=True):
    dim = p_vs[0].shape[0]
    if dim == 2:
        n = None
        plotter = Plotter2D()
    elif dim == 3:
        n = get_normal(p_vs)
        plotter = Plotter3D()
    else:
        return p_vs
    plotter.plot_contour(p_vs, color='r')
    plotter.plot_AABB(pMin, pMax, color='b')
    new_p_vs = clipf(p_vs, pMin, pMax, step=step)
    plotter.plot_contour(new_p_vs, color='g')

    print(area(new_p_vs, n))
    return new_p_vs

def plot_clip_AABB_nonrobust(p_vs, pMin, pMax, step=True):
    return plot_clip_AABB(p_vs=p_vs, pMin=pMin, pMax=pMax, clipf=clip_AABB_nonrobust, step=step)

def plot_clip_AABB_robust(p_vs, pMin, pMax, step=True):
    return plot_clip_AABB(p_vs=p_vs, pMin=pMin, pMax=pMax, clipf=clip_AABB_robust, step=step)

###############################################################################
## Tests
###############################################################################
from numpy import array

def test_triangle_clipping():
    v1 = array([0.0, 0.0, 95.0])
    v2 = array([80.0, 0.0, 32.0])
    v3 = array([100.0, 75.0, -45.0])
    p_vs = [v1, v2, v3]

    pMin = array([-50.0, -50.0, -50.0])
    pMax = array([50.0, 50.0, 50.0])

    plot_clip_AABB_robust(p_vs, pMin, pMax, step=True)
    plot_clip_AABB_nonrobust(p_vs, pMin, pMax, step=True)

def test_polygon_clipping():
    p_vs = [[50.0, 150.0], [200.0, 50.0], [350.0, 150.0], [350.0, 300.0], [250.0, 300.0], [200.0, 250.0], [150.0, 350.0], [100.0, 250.0], [100.0, 200.0]]
    p_vs = [array(v) for v in p_vs]

    pMin = array([100.0, 100.0])
    pMax = array([300.0, 300.0])

    plot_clip_AABB_robust(p_vs, pMin, pMax, step=True)
    plot_clip_AABB_nonrobust(p_vs, pMin, pMax, step=True)

    p_vs = [[50.0, 150.0, 0.0], [200.0, 50.0, 0.0], [350.0, 150.0, 0.0], [350.0, 300.0, 0.0], [250.0, 300.0, 0.0], [200.0, 250.0, 0.0], [150.0, 350.0, 0.0], [100.0, 250.0, 0.0], [100.0, 200.0, 0.0]]
    p_vs = [array(v) for v in p_vs]

    pMin = array([100.0, 100.0, 0.0])
    pMax = array([300.0, 300.0, 0.0])

    plot_clip_AABB_robust(p_vs, pMin, pMax, step=True)
    plot_clip_AABB_nonrobust(p_vs, pMin, pMax, step=True)

def test_polygon_clipping_border():
    p_vs = [[150.0, 100.0], [100.0, 150.0], [150.0, 200.0]]
    p_vs = [array(v) for v in p_vs]

    pMin = array([100.0, 100.0])
    pMax = array([300.0, 300.0])

    plot_clip_AABB_robust(p_vs, pMin, pMax, step=True)
    plot_clip_AABB_nonrobust(p_vs, pMin, pMax, step=True)

    p_vs = [[150.0, 100.0, 0.0], [100.0, 150.0, 0.0], [150.0, 200.0, 0.0]]
    p_vs = [array(v) for v in p_vs]

    pMin = array([100.0, 100.0, 0.0])
    pMax = array([300.0, 300.0, 0.0])

    plot_clip_AABB_robust(p_vs, pMin, pMax, step=True)
    plot_clip_AABB_nonrobust(p_vs, pMin, pMax, step=True)
