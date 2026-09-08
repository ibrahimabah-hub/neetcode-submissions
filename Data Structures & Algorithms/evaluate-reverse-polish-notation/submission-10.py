import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = []
        operators = ["+", "-", '*', "/"]
        for token in tokens:
            if token not in operators:
                operand.append(int(token))
                continue
            else:
                r = operand.pop()
                l = operand.pop()
                if token == "+":
                    operand.append(l + r)
                elif token == "-":
                    operand.append(l - r)
                elif token == "*":
                    operand.append(l * r)
                else:
                    if r == 0:
                        operand.append(0)
                    else:
                        operand.append(int(l / r))

        return operand[-1]
        
