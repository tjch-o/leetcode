from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.freq_map = defaultdict(int)
        self.group = defaultdict(list)
        self.max = 0

    def push(self, val):
        self.freq_map[val] += 1
        self.group[self.freq_map[val]].append(val)
        self.max = max(self.max, self.freq_map[val])

    def pop(self):
        group = self.group[self.max]
        elem = group.pop()
        self.freq_map[elem] -= 1

        if not self.group[self.max]:
            self.max -= 1
        return elem
