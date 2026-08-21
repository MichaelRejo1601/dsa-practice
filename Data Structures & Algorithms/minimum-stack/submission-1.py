class MinStack:

    def __init__(self):
        self.min = float('-inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(val, self.min)

    def pop(self) -> None:
        top = self.stack.pop()
        if top < 0: 
            self.min = self.min - top

    def top(self) -> int:
        top = self.stack[-1]
        if top < 0: 
            return self.min
        else: 
            return top+self.min

    def getMin(self) -> int:
        return self.min
