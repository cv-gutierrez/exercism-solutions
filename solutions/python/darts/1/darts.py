""" Dart Game
"""
import math

def score(x, y):
    """Dummy comment.
    """
    center=(0,0)
    point_on_circle=(x,y)
    radius = math.dist(center,point_on_circle)
    
    if radius<=1:
        return 10
    if radius<=5:
        return 5
    if radius <=10:
        return 1
    return 0

    
    
