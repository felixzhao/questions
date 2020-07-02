class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        time  O(N)
        space O(1)
        
        logic
        - two pointers, from left and right
        - skip not char or number, compare
        - if not match return False
        
        key point
        - "alphanumeric" means alpha or number
        - .isalnum() is the way check alphanumeric in python
        - .lower() is trans char to lowercase 
        
        """
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j and s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
