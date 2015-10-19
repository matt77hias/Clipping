import numpy as np

def get_normal(triangle):
    p1 = np.array(triangle[0])
    return normalize(np.cross(np.array(triangle[1])-p1, np.array(triangle[2])-p1))
    
def normalize(v):
    norm=np.linalg.norm(v)
    if norm==0: 
       return v
    return v/norm