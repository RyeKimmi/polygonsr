import math
from display import *



#vector functions

#return magnitude of vector
def magnitude(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2) 

#normalize vetcor, should modify the parameter
def normalize(vector):
    m = magnitude(vector)
    vector[0] = vector[0]/m
    vector[1] = vector[1]/m
    vector[2] = vector[2]/m
    pass

#Return the dot product of a . b
def dot_product(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] 

#Return the cross product of a x b
def cross_product(a,b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

#find angle of a and b
def ret_angle(a, b):
    am = magnitude(a)
    bm = magnitude(b)
    tm = am*bm
    return math.acos(dot_product(a, b)/tm)
    
#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    a = [ polygons[i+1][0] - polygons[i][0],
          polygons[i+1][1] - polygons[i][1],
          polygons[i+1][2] - polygons[i][2] ]
    b = [ polygons[i+2][0] - polygons[i][0],
          polygons[i+2][1] - polygons[i][1],
          polygons[i+2][2] - polygons[i][2] ]
    return cross_product(a,b)
