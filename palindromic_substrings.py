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