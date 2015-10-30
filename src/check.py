from sutherlandhodgman import clip3D_AABB

fstat="C:/Users/Matthias/Documents/Courses/Masterproef/pbrt/pbrt-v2/pbrt-v2/src/pbrt.vs2012/Stats.txt"
fstat1 = "C:/Users/Matthias/Documents/Courses/Masterproef/pbrt/Scenes/OBJReader/Assets/Icosahedron/Stats.txt"

def check(fstat):
    with open(fstat, 'r') as infile:
        for line in infile:
            if len(eval(line)) != 0:
                print(line)
            
            
        