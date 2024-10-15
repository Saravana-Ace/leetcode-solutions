class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])

        for val in tokens:
            a, b = None, None
            if val in ops:
                b=int(stack.pop())
                a=int(stack.pop())
                if val == '+':
                    stack.append(a+b)
                elif val == '-':
                    stack.append(a-b)
                elif val == '*':
                    stack.append(a*b)
                else:
                    stack.append(a/b)
            else:
                stack.append(val)
        
        return int(stack[0])