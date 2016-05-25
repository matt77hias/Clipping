# Clipping

Use
--------

![example](https://github.com/matt77hias/Clipping/blob/master/res/Example.png)

~~~~{.python}
from numpy import array
from test import plot_clip_AABB_robust

# The vertices of the polygon to clip
p_vs = [array([0.0, 0.0, 95.0]), array([80.0, 0.0, 32.0]), array([100.0, 75.0, -45.0])]

# The min and max bounds of the Axis Aligned Bounding Box used for clipping
pMin = array([-50.0, -50.0, -50.0])
pMax = array([50.0, 50.0, 50.0])

# Robust Sutherland-Hodgman as described in C. Ericson's Real-Time Collision Detection with my own addition of ensuring no duplicate vertices
plot_clip_AABB_robust(p_vs, pMin, pMax)
~~~~

Note that optimizations, method reuse and Python specific shorthands are still possible. The code however is currently easy portable to C, C++, C# and Java.
