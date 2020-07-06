class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sorting

        time  O(NlogN)
        space O(N), if result space not include then O(1)

        logic:
            - two loop
                - sort itervals by first item
                - merge sorted itervals
                    - if fisrt item in node is less than last item inlast node in result, then merge

        key point:
            - if merge must check max(node[1], result last node[1])
                - e.g. [[1,4],[2,3]]
                - first smaller, but second larger
            - python sort + lambda is power

        """
        # sorted by first item
        intervals.sort(key=lambda x: x[0])

        # merge
        result = []
        for i in intervals:
            if not result or i[0] > result[-1][1]:
                result.append(i)
            else:
                result[-1][1] = max(i[1], result[-1][1])
        return result
