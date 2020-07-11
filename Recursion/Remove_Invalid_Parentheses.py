class Solution:
    def __init__(self):
        self.res = {0: ['']}

    def backtracking(self, path: str, dif: int, s: str) -> None:
        """
        My Solution:

        Back Tracking

        Can Handle cases:
        ""
        "()())()"
        "(a)())()"
        ")("
        ")(f"
        ")o(v("
        "))(()("

        Can NOT handle cases:
        "()((((()"

        logic:
            - each char in the string as a leaf
            - each level jump to next to char as leaves in next level
            - a count 'dif' figure out how many count diff between '(' and ')'
                - if dif > 0 means '(' count larger than ')' count
                - otherwise opposite
            - a dictionary save all possible result, key is length, value is the string
            - after all process done. return the value in dict if max length of the key in dict
            - in this algorithm if diff < 0, we think it NOT potential result.
                - that's why it can not handle  "()((((()"
                - this may need to be improve.
        """
        if dif < 0:
            k = ''
            for c in s:
                if c != '(' and c != ')':
                    k += c
            self.res[len(k)] = [k]
            return
        if path and dif == 0:
            k = self.res.get(len(path), [])
            k.append(path)
            self.res[len(path)] = k
        if len(s) >= 2:
            t = dif
            if s[1] == '(':
                t += 1
            elif s[1] == ')':
                t -= 1
            self.backtracking(path + s[1], t, s[2:])
        if len(s) == 0:
            return

        t = dif
        if s[0] == '(':
            t += 1
        elif s[0] == ')':
            t -= 1
        self.backtracking(path + s[0], t, s[1:])

    def removeInvalidParentheses(self, s: str) -> List[str]:
        if str:
            i = 0
            while i < len(s) and s[i] == ')':
                print(i)
                i += 1
            self.backtracking('', 0, s[i:])

        if max(self.res.keys()) == 0:
            return ['']

        return list(set(self.res[max(self.res.keys())]))
