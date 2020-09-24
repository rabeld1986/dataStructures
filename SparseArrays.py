'''
Created on Sep 23, 2020

@author: rabel
'''
# Complete the matchingStrings function below.
# solution to HackerRank problem
def matchingStrings(strings, queries):
    results = []
    inst = 0
    for q in range(len(queries)):
        for s in range(len(strings)):
            if queries[q] == strings[s]:
                inst +=1
        results.append(inst)
        inst = 0   
    return results

if __name__ == '__main__':


    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))