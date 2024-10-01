class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        mapper = {}

        for c in ransomNote:
            if c in mapper:
                mapper[c] += 1
            else:
                mapper[c] = 1
        
        for c in magazine:
            if c in mapper:
                mapper[c] -= 1
        
        for vals in mapper.values():
            if vals > 0:
                return False
        return True