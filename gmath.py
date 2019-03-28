import math
from display import *



#vector functions

#return magnitude of vector
def magnitude(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2) 

#normalize vetcor, should modify the parameter
def normalize(vector):
    m = magnitude(vector)
    return [vector[0]/m, vector[1]/m, vector[2]/m]

#Return the dot product of a . b
def dot_product(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] 

#find angle of a and b
def ret_angle(a, b):
    am = magnitude(a)
    bm = magnitude(b)
    tm = am*bm
    return math.acos(dot_product(a, b)/tm)
    
#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    a = polygons[i]
    return None
