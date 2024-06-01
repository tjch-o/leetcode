class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)

        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self):
        val = self.stack.pop()

        if val == self.min[-1]:
            self.min.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min[-1]
