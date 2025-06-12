class Queue:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())
        return self.q2.pop()

    def peek(self):
        if not self.q2:
            return self.q1[0]
        return self.q2[-1]

    def empty(self):
        return not self.q1 and not self.q2
