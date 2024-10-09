import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1_freq = {c: 0 for c in string.ascii_lowercase}
        s2_freq = {c: 0 for c in string.ascii_lowercase}

        for i in range(len(s1)):
            s1_freq[s1[i]] += 1
            s2_freq[s2[i]] += 1

        print(s1_freq)
        
        #now you have the counts of s1 and the first window of length s1 in s2
        matches = 0
        for i in range(26):
            matches += (1 if s1_freq[chr(i+97)] == s2_freq[chr(i+97)] else 0)
        print(matches)
        i = 0
        for j in range(len(s1), len(s2)):
            if matches == 26: return True

            s2_freq[s2[j]] += 1
            if s2_freq[s2[j]] == s1_freq[s2[j]]: 
                matches += 1
            elif s2_freq[s2[j]]-1 == s1_freq[s2[j]]: #if the count is greater than then only reduce
                matches -= 1
            #the matches should only decrease if the freq of c in s2 is greater than the freq of c in s1 by only 1
            #suppose you already have 2 b's in the s2 freq and you add another b which makes it 3
            #but the b freq in s1 is only 1, by adding another b doesn't make the number of matches go down
            s2_freq[s2[i]] -= 1
            if s2_freq[s2[i]] == s1_freq[s2[i]]: 
                matches += 1
            elif s2_freq[s2[i]]+1 == s1_freq[s2[i]]:
                matches -= 1
            #suppose there is one less in the s2 freq than the s1 freq, then decrease matches by 1
        
            i += 1
        
        return matches == 26