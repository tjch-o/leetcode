class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        history = self.arr[index]

        if history[-1][0] == self.snap_id:
            history[-1] = (self.snap_id, val)
        else:
            history.append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.arr[index]
        left, right = 0, len(history) - 1
        res = 0

        while left <= right:
            mid = (left + right) // 2

            if history[mid][0] <= snap_id:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return history[res][1]
