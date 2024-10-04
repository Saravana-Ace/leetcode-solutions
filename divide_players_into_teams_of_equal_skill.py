class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0, len(skill)-1
        res = 0
        check = skill[0] + skill[-1]
        
        while i < j:
            if skill[i] + skill[j] != check:
                return -1
            res += skill[i] * skill[j]
            i += 1
            j -= 1
        
        return res