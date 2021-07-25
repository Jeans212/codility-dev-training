'''

    Task:
      Find the missing element in a given permutation.
      
    Approach:
      Note that the length of your array should initially be len(A) + 1
      
      1. If the given array, A is empty, then the missing number is 1
      2. If A is not empty, e.g. [2,3,1,6,4]
          - Sort the array e.g. [1,2,3,4,6]
          - Generate a array with range of values for the same length e.g [1,2,3,4,5]
          - Check if both array are same.
            - If True, that means the last number is missing. e.g if [1,2,3] == [1,2,3] that means 4 is the missing number
            - If False, compare their elements and see which is missing.
              - If found, return the missing number and stop running.
              
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if A == []:
        return 1
    else:
        A = sorted(A)
        B = list(range(1, len(A) + 1))
        if A == B:
            return (len(A) + 1)
        else:
            for i, j in zip(B, A):
                if i != j:
                    return i
                    break
