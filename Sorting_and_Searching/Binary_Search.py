print('Binary Search')


def binary_search(arr, l, r, t):
    """
    basic algorithms

    key point:
        - because of l may larger than 0, so we must plus the l again
        - mid = (r-l) //2 + l
        - e.g.
            - if len(arr) == 6
                - l = 1, r = 6-1 = 5
                - mid = (5 - 1) // 2 + 1 = 2 + 1 = 3

                - l = 2, r = 6-1 = 5
                - mid = (5 - 2) // 2 + 2 = 1 + 2 = 3

    :param arr: the array we finding
    :param l: start position in array of this search
    :param r: end position in array of this search
    :param t: what we try to find, the target value
    :return: the position of target value, if not found return -1
    """
    if l <= r:
        mid = (r-l) // 2 + l
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            # search right side
            return binary_search(arr, mid+1, r, t)
        else:
            return binary_search(arr, l, mid-1, t)
    return -1


def test(tests):
    all_passed = True
    for arr, t, exp in tests:
        # Function call
        result = binary_search(arr, 0, len(arr) - 1, t)
        print('passed.') if result == exp else print(f'failed. arr: {arr}, target: {t}, expected: {exp}')
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
