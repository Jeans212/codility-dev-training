'''
    Task: 
    Count minimal number of jumps from position X to Y.
    
    Approach:
    Subtract position X from position Y to get the distance between them.
    Return the smallest integer greater than or equal to the result obtained from dividing the distance (Y-X) by jump distance D.
'''


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(X, Y, D):
    # write your code in Python 3.6
    return math.ceil((Y-X) / D)
