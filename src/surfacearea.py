import numpy as np

###############################################################################
## Surface Area
## ---------------------------------
## Planar polygon
###############################################################################

#Theorem of Green
#------------------------------------------------------------------------------
#integral_contour(L dx + M dy) = integral_area((dM/dx - dL/dy) dx dy)
#    contour   = oriented, piecewise smooth, simple closed curve in a plane
#    area      = region bounded by perimeter
#    L, M      = functions of (x,y) defined on an open region containing area with continuous partial derivatives
#
#Application: 
#    Planimeter
#    integral_contour(-y dx + x dy) = integral_area((dx/dx - -dy/dy) dx dy) = 2 area

def area(p_vs, n=None):
    if (len(p_vs) < 3):
        return 0.0
       
    dim = p_vs[0].shape[0] 
    if dim == 2:
        return _area2D(p_vs)
    elif dim == 3:
        return _area3D(p_vs, n=n)

def _area2D(p_vs):
    area = 0.0
    nb_p_vs = len(p_vs)
    
    #for j in range(nb_p_vs):
    #    p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
    #    p_v2 = p_vs[j]
    #    area += + p_v1[0]*p_v2[1] - p_v2[0]*p_v1[1]
    
    for j in range(nb_p_vs):
        p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
        p_v2 = p_vs[j]
        p_v3 = p_vs[(j+nb_p_vs+1) % nb_p_vs]
        area += p_v2[0] * (p_v3[1] - p_v1[1])
    
    return 0.5 * abs(area)
    
def _area3D(p_vs, n):
    area = 0.0
    nb_p_vs = len(p_vs)
    
    ax = abs(n[0])
    ay = abs(n[1])
    az = abs(n[2])
    if (ax > ay and ax > az): lca = 0
    elif (ay > az): lca = 1
    else: lca = 2

    an = np.sqrt(ax*ax + ay*ay + az*az)
    if lca == 0:
        for j in range(nb_p_vs):
            p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
            p_v2 = p_vs[j]
            p_v3 = p_vs[(j+nb_p_vs+1) % nb_p_vs]
            area += p_v2[1] * (p_v3[2] - p_v1[2])
        area *= (an / n[0])
    elif lca == 1:
        for j in range(nb_p_vs):
            p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
            p_v2 = p_vs[j]
            p_v3 = p_vs[(j+nb_p_vs+1) % nb_p_vs]
            area += p_v2[2] * (p_v3[0] - p_v1[0])
        area *= (an / n[1])
    else:
        for j in range(nb_p_vs):
            p_v1 = p_vs[(j+nb_p_vs-1) % nb_p_vs]
            p_v2 = p_vs[j]
            p_v3 = p_vs[(j+nb_p_vs+1) % nb_p_vs]
            area += p_v2[0] * (p_v3[1] - p_v1[1])
        area *= (an / n[2])

    return 0.5 * abs(area)
