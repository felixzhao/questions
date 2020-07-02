class Solution:
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        """
        Good Question
        "Greedy"

        logic
            - two pointer, from start and end
            - if found char not same
                - check either i+1 ~ j is palindrome
                - either i ~ j-1 is palindrome
            - if all char same, until i == j
                - then check hole string is palindrome

        python
            - s[::-1], reverse string
            - s[~i] get item from end with 0 base index

        time  O(N), 2 substring check still O(N)
        space O(1)
        """
        i, j = 0, len(s) - 1
        while (i < j):
            if s[i] != s[j]:
                return self.isPalindrome(s, i, j - 1) or self.isPalindrome(s, i + 1, j)
            i += 1
            j -= 1
        return s == s[::-1]
