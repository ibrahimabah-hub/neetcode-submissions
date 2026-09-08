class MinStack:

    def __init__(self):
        self.stack = []
        self.minitop = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minitop)==0:
            self.minitop.append((val,val))
            return
        mini = self.minitop[-1][0]
        if val<mini:
            mini = val
        top = self.minitop[-1][1]
        if val>top:
            top = val
        self.minitop.append((mini,top))
        #print((mini,top))

    def pop(self) -> None:
        self.stack.pop()
        self.minitop.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minitop[-1][0]
