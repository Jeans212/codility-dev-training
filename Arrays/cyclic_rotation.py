# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

'''
    Rotate an array A to the right by a given number of steps K.
    
    Covert the array to a deque
    Apply the rotate() method the rotate the deque in positive K steps
    Convert the deque to array
    
'''

from collections import deque

def solution(A, K):
    # write your code in Python 3.6
    deq_A = deque(A)
    deq_A.rotate(K)
    return list(deq_A)
