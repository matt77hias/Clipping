from robustsutherlandhodgman import clip3D_AABB
from surfacearea import area3D
from orientation import get_normal

fstat="C:/Users/Matthias/Documents/Courses/Masterproef/pbrt/pbrt-v2/pbrt-v2/src/pbrt.vs2012/Stats.txt"
fstat1 = "C:/Users/Matthias/Documents/Courses/Masterproef/pbrt/Scenes/OBJReader/Assets/Icosahedron/Stats.txt"

def check(fstat):
    with open(fstat, 'r') as infile:
        for line in infile:
            if eval(line) != 0.0:
                print(line)
            
def f(p_vs, pmin, pmax):
    n = get_normal(p_vs)
    result = clip3D_AABB(p_vs, pmin, pmax, step=False)
    return area3D(result, n)