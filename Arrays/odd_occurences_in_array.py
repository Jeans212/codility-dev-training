'''

    Odd occurences in array
    Find value that occurs in odd number of elements.
  
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # If all the items in the list are integers, you can use counts = defaultdict(int)
    counts = dict()

    # Get the distinct counts of items in A
    for i in A:
        counts[i] = counts.get(i, 0) + 1

    # Check which count value or occurence is odd and break if found
    for key, value in counts.items():
        if value % 2 == 1:
            return key
            break
