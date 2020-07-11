class Solution:
    def __init__(self):
        self.result = []
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}

    def getLetterCombinations(self, combinations: List[str], next_digits: str) -> List[str]:
        """
        Recursion

        logic:
            - each digit as a level in the recursion
            - recursive call each letter in level as branch in the tree
            - recursive stop condition no digit in digits

        time  O(3^M * 4^N)
        space O(3^M * 4^N)
        """
        # print(self.phone)
        if len(next_digits) == 0:
            return self.result.append(combinations)
        if next_digits[0] in self.phone:
            for l in self.phone[next_digits[0]]:
                self.getLetterCombinations(combinations + l, next_digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        if digits:
            self.getLetterCombinations("", digits)
        return self.result
