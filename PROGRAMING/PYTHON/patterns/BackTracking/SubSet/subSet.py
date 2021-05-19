'''
We have a set with integers (for this task all integers are positive and all of
the mare unique). To cycle through all set and check if any of subset meets
requested Sum, if yes print subset, if no, print no
- Appearentlty it should find all subsets,
- AS I understood nodes are calculated sum of all sub sets biggest number and lenght of the set(or smallest number of the set)
'''

def printSubSet(subset):
    print(subset)

def solveSubSet(arr, subset, sumNumb, setsAll):
    if sum(subset) == sumNumb and not (subset in setsAll): return True
    elif sum(subset) > sumNumb or not arr: return False


    for elem in arr:
        if elem in subset: return False
        subset.append(elem)
        # print(subset)
        if solveSubSet(arr[1:], subset, sumNumb, setsAll): return True
        subset.remove(elem)

    return False

if __name__=='__main__':
    set1 = [x for x in range(1,10)]
    # set1 = [15, 22, 14, 26, 32, 9, 16, 8]
    sumN = 5
    subSetAll = []
    nodes = 0

    for x in range(len(set1)):
        subSet1 = []
        if solveSubSet(set1,subSet1, sumN,subSetAll):
            subSetAll.append(subSet1)
            printSubSet(subSet1)

    for xnodes in subSetAll:
        nodes += sorted(xnodes)[-1]
    else:
        print('Nodes Generated:', nodes + len(set1))

    if not subSetAll: print(f'Sum: {sumN}, can not be found in provided set: {set1}')
