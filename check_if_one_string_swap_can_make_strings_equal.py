class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1)-1
        count = 0

        while i <= j:
            while s1[i] == s2[i]:
                i += 1
                if i == len(s1): return True
            while s1[j] == s2[j]:
                j -= 1
            
            if i > j: break


            if s1[i] == s2[j] and s1[j] == s2[i]:
                count += 1
            else:
                return False
            
            if count == 2:
                return False
            
            i, j = i+1, j-1

        return True