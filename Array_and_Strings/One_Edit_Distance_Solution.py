class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        This is a simple version of Edit Distance
        One Edit Distance only happen when two string with same length or 1 diff
        Thus we only need to do is compare each chr if diff more than once or no diff means not,
        otherwise is One Edit Distance

        Logic:
            - keep two pointer
            - loop compare
            - use a flag to figure out diff found status
            - if found diff, short string pointer move back one step

        key points:
            - pre-check if two string same return False
            - move back for "SHORT" string! when diff found

        """
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        i, j = 0, 0
        found_diff = False
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if found_diff: return False
                found_diff = True
                # found diff short string pointer move back-ward
                if len(s) > len(t):
                    j -= 1
                elif len(t) > len(s):
                    i -= 1
            i += 1
            j += 1
        return True
