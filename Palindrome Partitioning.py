class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, one_possibility = [], []
        def check_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        def backtrack(i):
            if i >= len(s):
                res.append(one_possibility.copy())
                return
            
            for j in range(i, len(s)):
                if check_palindrome(i, j):
                    one_possibility.append(s[i:j+1])
                    backtrack(j+1)
                    one_possibility.pop()
            return res
            

        return backtrack(0)