from collections import deque


class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)

        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return not self.q1 and not self.q2
