class MinStack:

    def __init__(self):
        self.stack = []
        self.minState = []        

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = min(self.minState[-1], val) if self.minState else val
        self.minState.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minState.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minState[-1]
        