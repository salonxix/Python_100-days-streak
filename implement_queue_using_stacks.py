class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._shift_stacks()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._shift_stacks()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def _shift_stacks(self):
        if not self.stack_out:  # Only move when stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


# Example usage
myQueue = MyQueue()
myQueue.push(1)         # queue: [1]
myQueue.push(2)         # queue: [1, 2]
print(myQueue.peek())   # Output: 1
print(myQueue.pop())    # Output: 1
print(myQueue.empty())  # Output: False
