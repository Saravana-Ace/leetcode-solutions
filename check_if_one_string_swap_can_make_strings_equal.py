# solution 1 - using two pointers and no hashmap
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
                return False #accounts for the case where they are not anagrams
            
            if count == 2:
                return False
            
            i, j = i+1, j-1

        return True

# solution 2 - using a hashmap to keep a count of characters in s1 and s2
from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        h1 = Counter(s1)
        h2 = Counter(s2)
        count = 0

        for i in range(len(s1)):
            if h1[s1[i]] != h2[s1[i]]:
                return False

            if s1[i] != s2[i]:
                count += 1
            
            if count > 2: return False
        
        return True