class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.recently_used = []
        
    def get(self, key):
        if key not in self.cache:
            return -1
        
        self.recently_used.remove(key)
        self.recently_used.append(key)
        return self.cache[key]
        
    def put(self, key, value):
        if key in self.cache:
            self.recently_used.remove(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                oldest_key = self.recently_used.pop(0)
                del self.cache[oldest_key]
            self.cache[key] = value

        self.recently_used.append(key)