print('Binary Search')


def binary_search(arr, l, r, t):
    if l <= r:
        mid = (r-l)// 2 + l
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
