print('Binary Search')

"""
overflow bug
https://en.wikipedia.org/wiki/Binary_search_algorithm#Implementation_issues

may not happen in python, but need to known this.
"""


def binary_search_recursive(arr, l, r, t):
    """
    basic algorithms

    key point:
        - because of l may larger than 0, so we must plus the l again
        - mid = (l + r) // 2
        - e.g.
            - if len(arr) == 6
                - l = 1, r = 6-1 = 5
                - mid = (5 + 1) // 2 = 3

                - l = 2, r = 6-1 = 5
                - mid = (5 + 2) // 2 = 7 // 2 = 3

    :param arr: the array we finding
    :param l: start position in array of this search
    :param r: end position in array of this search
    :param t: what we try to find, the target value
    :return: the position of target value, if not found return -1
    """
    if l <= r:
        #mid = (l+r) // 2
        mid = (r - l) // 2 + l
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            # search right side
            return binary_search_recursive(arr, mid+1, r, t)
        else:
            return binary_search_recursive(arr, l, mid-1, t)
    return -1


def binary_search_iterative(arr, t):
    l, r = 0, len(arr) - 1
    while l <= r:
        # mid = (l+r) // 2
        mid = (r - l) // 2 + l
        if arr[mid] == t:
            return mid
        elif arr[mid] > t:
            # search left branch
            r = mid - 1
        else:
            # search right branch
            l = mid + 1
    return -1


def test(tests):
    all_passed = True
    for arr, t, exp in tests:
        # call recursive
        result = binary_search_recursive(arr, 0, len(arr) - 1, t)
        print('recursive passed.') if result == exp else print(f'failed. arr: {arr}, target: {t}, expected: {exp}')
        # call iterative
        result = binary_search_iterative(arr, t)
        print('iterative passed.') if result == exp else print(f'failed. arr: {arr}, target: {t}, expected: {exp}')
    if all_passed:
        print('all passed.')


tests = [
    (
        [],
        2,
        -1
    ),
    (
        [2],
        2,
        0
    ),
    (
        [3, 5],
        3,
        0
    ),
    (
        [3, 5],
        5,
        1
    ),
    (
        [1, 3, 5],
        3,
        1
    ),
    (
        [1, 3, 4, 5],
        3,
        1
    ),
    (
        [1, 3, 4, 5],
        4,
        2
    ),
    (
        [1, 3, 4, 5, 7],
        4,
        2
    ),
]

test(tests)
