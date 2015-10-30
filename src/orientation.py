import numpy as np
from vector_utils import normalize

def get_normal(triangle):
    p1 = np.array(triangle[0])
    return normalize(np.cross(np.array(triangle[1])-p1, np.array(triangle[2])-p1))

###################################################################################################################################################################################
## Vertex classification tools
###################################################################################################################################################################################  

def inside2D(c_v1, c_v2, p_v):
    return (c_v1[0] - p_v[0]) * (c_v2[1] - p_v[1]) >= (c_v1[1] - p_v[1]) * (c_v2[0] - p_v[0]);  
   
def inside3D(c_v1, c_v2, p_v2, a0, a1):
    #print((np.float32(c_v1[a0]) - np.float32(p_v2[a0])) * (np.float32(c_v2[a1]) - np.float32(p_v2[a1])))
    #print((np.float32(c_v1[a1]) - np.float32(p_v2[a1])) * (np.float32(c_v2[a0]) - np.float32(p_v2[a0])))
    #print((np.float64(c_v1[a0]) - np.float64(p_v2[a0])) * (np.float64(c_v2[a1]) - np.float64(p_v2[a1])))
    #print((np.float64(c_v1[a1]) - np.float64(p_v2[a1])) * (np.float64(c_v2[a0]) - np.float64(p_v2[a0])))
    
    #return (c_v1[a0] - p_v2[a0]) * (c_v2[a1] - p_v2[a1]) >= (c_v1[a1] - p_v2[a1]) * (c_v2[a0] - p_v2[a0]);   
    #return (np.float32(c_v1[a0]) - np.float32(p_v2[a0])) * (np.float32(c_v2[a1]) - np.float32(p_v2[a1])) >= (np.float32(c_v1[a1]) - np.float32(p_v2[a1])) * (np.float32(c_v2[a0]) - np.float32(p_v2[a0]))
    return (np.float64(c_v1[a0]) - np.float64(p_v2[a0])) * (np.float64(c_v2[a1]) - np.float64(p_v2[a1])) >= (np.float64(c_v1[a1]) - np.float64(p_v2[a1])) * (np.float64(c_v2[a0]) - np.float64(p_v2[a0]))
   
PLANE_THICKNESS_EPSILON = 0.00001; 

def classify_distance(d):
    if (d > PLANE_THICKNESS_EPSILON):
        return 1
    elif (d < -PLANE_THICKNESS_EPSILON):
        return -1
    else:
        return 0

def classify(n, c_v, p_v):
    d = signed_distance(np.array(n, dtype=np.float64), np.array(c_v, dtype=np.float64), np.array(p_v, dtype=np.float64))
    return classify_distance(d)
        
def classify_aligned(s, a, c_v, p_v):
    d = signed_distance_aligned(s, a, np.array(c_v, dtype=np.float64), np.array(p_v, dtype=np.float64))
    return classify_distance(d)
          
def signed_distance(n, c_v, p_v):
    return np.dot(n, p_v - c_v)
    
def signed_distance_aligned(s, a, c_v, p_v):
    return s * (p_v[a] - c_v[a])
     
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