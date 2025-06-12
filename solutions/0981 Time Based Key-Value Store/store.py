class TimeMap:
    def __init__(self):
        self.cache = {}

    def set(self, key, value, timestamp):
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append((value, timestamp))

    def get(self, key, timestamp):
        if key not in self.cache:
            return ""

        timestamps = self.cache[key]
        highest = -1
        left, right = 0, len(timestamps)

        while left < right:
            mid = left + (right - left) // 2

            if timestamps[mid][1] <= timestamp:
                highest = timestamps[mid][0]
                left = mid + 1
            else:
                right = mid

        if highest == -1:
            return ""
        return highest
