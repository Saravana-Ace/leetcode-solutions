class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            elif not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True

# solution 2 - converting string to alphabets/numbers only
class Solution:
    def isPalindrome(self, s:str) -> bool:
        res = ""
        for c in s:
            if c.isalnum():
                res += c.lower()
            res += c.lower() if c.isalnum() else ''
        return res == res[::-1]
    
# solution 3 - using filter function, returns an iterable
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
    
# solution 4 - similar to solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i <= j:
            while i < j and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1
            # if s[i].isalpha() and s[j].isalpha():
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True