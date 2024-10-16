import random


class RandomizedSet:
    def __init__(self):
        self.values = []
        self.indices = {}

    def insert(self, val):
        if val in self.indices:
            return False

        n = len(self.values)
        self.indices[val] = n
        self.values.append(val)
        return True

    def remove(self, val):
        if val not in self.indices:
            return False

        last_elem = self.values[-1]
        i = self.indices[val]

        self.indices[last_elem] = i
        self.values[i] = last_elem
        self.values[-1] = val

        self.values.pop()
        del self.indices[val]
        return True

    def get_random(self):
        n = len(self.values)
        i = random.randint(0, n - 1)
        return self.values[i]
