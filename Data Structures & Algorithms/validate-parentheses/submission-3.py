class Solution:
    def isValid(self, s: str) -> bool:
        ops = ['(', ')', '{', '}', '[',']']
        opening = ['(', '[', '{']
        pairs = [('(', ')'), ('{', '}'), ('[',']')]
        stack = []
        for char in s:
            if char in ops:
                if char in opening:
                    stack.append(char)
                    continue
                if len(stack)>0:
                    if (stack[-1], char) in pairs:
                        stack.pop()
                        continue
                return False
        return True if len(stack)==0 else False

