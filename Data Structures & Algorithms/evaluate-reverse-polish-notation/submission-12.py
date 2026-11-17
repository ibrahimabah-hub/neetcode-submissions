import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        
        operands = []

        cur = 0

        while(cur<len(tokens)):
            if tokens[cur] in operators:
                r = int(operands.pop())
                l = int(operands.pop())
                if tokens[cur] == "+":
                    operands.append(l+r)
                if tokens[cur] == "-":
                    operands.append(l-r)
                if tokens[cur] == "*":
                    operands.append(l*r)
                if tokens[cur] == "/":
                    operands.append(l/r)
            else:
                operands.append(tokens[cur])
            cur+=1

        return int(operands[0])
