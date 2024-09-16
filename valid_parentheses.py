class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for c in s:
            peek = 'l'
            if res:
                peek = res[len(res)-1]
            if peek == '(' and c == ')' or peek == '[' and c == ']' or peek == '{' and c == '}':
                res.pop()
            else:
                res.append(c)
                
        return not res