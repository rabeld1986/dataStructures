'''
Created on Sep 21, 2020

@author: rabel
'''

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    
    seq = []    
    for i in range(len(queries)):
        s_num = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]
        
        if s_num == 1:
            ind = ((x ^ lastAnswer)%n)
            seqList[ind].append(y)
        if s_num == 2:
            ind = ((x ^ lastAnswer)%n)
            val = y%len(seqList[ind])
            lastAnswer = seqList[ind][val]
            seq.append(lastAnswer)
    return seq

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    for i in range(len(result)):
        print(result[i])