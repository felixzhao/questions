class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Recursion

        Complex Labor Question

        loigc:
            - two pointer figure p, s position
            - check current position is match or not
            - recursive 3 cases:
                - current position match, check next
                - pattern following '*', skip current pattern position
                - pattern following '*', current match check next


        My Bugs:
            - matched check
                - p[0] in {s[0], '.'},
                - NOT s[0] in {p[0], '.'}
            - check p len,
                - if len(p) >=2 and p[1] == '*':,
                - NOT if len(s) >=2 and p[1] == '*':
            - must check matched,
                - return matched and self.isMatch(s[1:], p[1:]),
                - NOT return self.isMatch(s[1:], p[1:])

        time  O((t+P)*2^(T+p/2))
        space O(T^2 + P^2)
        """
        if not p:
            return not s
        matched = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            isSkip = self.isMatch(s, p[2:])
            hasNextMatch = matched and self.isMatch(s[1:], p)
            return isSkip or hasNextMatch
        else:
            return matched and self.isMatch(s[1:], p[1:])