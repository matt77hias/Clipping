import numpy as np

def intersect2D(c_v1, c_v2, p_v1, p_v2):
    A1 = c_v2[1] - c_v1[1]
    B1 = c_v1[0] - c_v2[0]
    C1 = c_v1[0] * A1 + c_v1[1] * B1
    
    A2 = p_v2[1] - p_v1[1]
    B2 = p_v1[0] - p_v2[0]
    C2 = p_v1[0] * A2 + p_v1[1] * B2
    
    det = A1 * B2 - B1 * A2
    X1 = (C1 * B2 - B1 * C2) / det;
    X2 = (A1 * C2 - C1 * A2) / det;
    return [X1, X2]
    
def intersect3D(c_v1, c_v2, p_v1, p_v2, a0, a1):
    A1 = c_v2[a1] - c_v1[a1]
    B1 = c_v1[a0] - c_v2[a0]
    C1 = c_v1[a0] * A1 + c_v1[a1] * B1
    
    A2 = p_v2[a1] - p_v1[a1]
    B2 = p_v1[a0] - p_v2[a0]
    C2 = p_v1[a0] * A2 + p_v1[a1] * B2
    
    det = A1 * B2 - B1 * A2
    X1 = (C1 * B2 - B1 * C2) / det;
    X2 = (A1 * C2 - C1 * A2) / det;
    
    alpha = -1.0
    if B2 != 0:
        alpha = (X1 - p_v2[a0]) / np.double(B2)
    else:
        alpha = (p_v2[a1] - X2) / np.double(A2)
    
    a2 = 3 - (a1 + a0)
    X3 = alpha * p_v1[a2] + (1.0 - alpha) * p_v2[a2]

    X = [0.0, 0.0, 0.0]
    X[a0] = X1
    X[a1] = X2
    X[a2] = X3
    return X
    
def interpolate(alpha, p_v1, p_v2):
    p_v1 = np.array(p_v1, np.float64)
    p_v2 = np.array(p_v2, np.float64)
    p = alpha * p_v1 + (1.0 - alpha) * p_v2 #clamping? 
    return p.tolist()