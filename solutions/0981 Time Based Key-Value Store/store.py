class TimeMap:
    def __init__(self):
        self.dict = {}

    def set(self, key, value, timestamp):
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.dict or not self.dict[key]:
            return ""

        timestamps = self.dict[key]
        highest = None
        start = 0
        end = len(timestamps) - 1

        while start <= end:
            middle = start + (end - start) // 2

            if timestamps[middle][0] == timestamp:
                return timestamps[middle][1]
            elif timestamps[middle][0] < timestamp:
                highest = timestamps[middle][1]
                start = middle + 1
            else:
                end = middle - 1

        if not highest:
            return ""
        return highest
