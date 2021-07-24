# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    # converting the input N to binary number
    binary = format(N, 'b')
    temp = []
    
    # case 1: there are no '0's in the binary number e.g. '11111111111'
    if '0' not in binary:
        return 0
    
    # case 2a: there are less than two '1's in the binary number e.g. '10000000'
    if binary.count('1') < 2:
        return 0
    else:   # case 2b: if there are 2 or more '1's in the binary number e.g. '1100010000000'
        if binary[-1] == '1':
            for each_zeros in binary.split('1'):
                temp.append(len(each_zeros))
            return max(temp)
        elif binary[0] != '1':
            for each_zeros in binary.split('1'):
                temp.append(len(each_zeros))
            temp.remove(temp[0])
            return max(temp)
        else:
            for each_zeros in binary.split('1'):
                temp.append(len(each_zeros))
            temp.remove(temp[-1])
            return max(temp)
