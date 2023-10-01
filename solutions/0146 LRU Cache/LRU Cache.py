class LRUCache:
    def __init__(self, capacity: int):
        self.n = 0
        self.capacity = capacity
        self.dict = {}
        # stack stores the keys where left is the least used key
        self.stack = []
        
    def set(self, key, value):
        self.stack.append(key)
        self.dict[key] = value
        
    def updateStack(self, key):
        self.stack.remove(key)
        self.stack.append(key)

    def get(self, key):
        if key in self.dict:
            self.updateStack(key)
            return self.dict[key]
        return -1

    def put(self, key, value):
        if key in self.dict:
            self.dict[key] = value
            self.updateStack(key)
        elif self.n == self.capacity:
            least_used_key = self.stack.pop(0)
            self.dict.pop(least_used_key)
            self.set(key, value)
        else:
            self.set(key, value)
            self.n += 1