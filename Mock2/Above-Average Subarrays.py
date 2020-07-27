"""
Question
Above-Average Subarrays
find Sub arrays which avg above rest of others in this arrays.
e.g.
input    [3, 4, 2]
expected [[3, 4, 2], [4], [4, 2]]
"""
def avgSubset(arr, i, j):
    print(f'{i}, {j} : {arr}')
    m = []
    n = arr[:]
    if i == j:
        m.append(arr[i])
        n.remove(arr[i])
    else:
        while i < j:
            m.append(arr[i])
            n.remove(arr[i])
            i += 1
    inner = 0
    outer = 0
    if len(m) > 0:
        inner = sum(m) // len(m)
    if len(n) > 0:
        outer = sum(n) // len(n)

    print(f'in: {inner}, out: {outer}')
    return [inner, outer]


def find(a):
    """
    Brute

    logic:
    - each every substring vs rest string
    - compare by copy out the substring

    time  O(M^2)
    space O(M^2)

    """
    res = []
    i = 0
    while i < len(a):
        j = 0
        while j < len(a):
            innerAvg, outerAvg = avgSubset(a, i, j)
            if innerAvg > outerAvg:
                if i == j:
                    res.append([a[i]])
                else:
                    res.append(a[i:(j+1)])
            j += 1
        i += 1
    return res


res = find([3, 4, 2])
print(res)
