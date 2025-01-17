class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}

        for word in strs:
            val = "".join(sorted(word))
            if val not in mapper:
                mapper[val] = []
            mapper[val].append(word)
        
        return list(mapper.values())