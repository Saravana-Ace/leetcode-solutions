class Solution:
    def countSubstrings(self, s: str) -> int:
        mapper = {}
        res = len(s)
        hold = 2
        i, j = 0, hold

        while j <= len(s):
            while j <= len(s):
                string = s[i:j]
                if string in mapper and mapper[string]:
                    res += 1
                else:
                    a = 0
                    b = len(string)-1

                    mapper[string] = True
                    while a <= b:
                        if string[a] != string[b]:
                            mapper[string] = False
                        a += 1
                        b -= 1
                    
                    if mapper[string]: 
                        res += 1
                i += 1
                j += 1

            i = 0
            hold += 1
            j = hold
        
        return res

#solution 2 - finding palindromes from inward out to reduce redundancy
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.counter(i, i, s)
            res += self.counter(i, i+1, s)

        return res
        
    def counter(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res