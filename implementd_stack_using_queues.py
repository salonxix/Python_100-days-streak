from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Push to q2
        self.q2.append(x)
        # Move all from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Example test
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())    # Output: 2
print(myStack.pop())    # Output: 2
print(myStack.empty())  # Output: False
