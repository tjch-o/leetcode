from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point):
        self.points[tuple(point)] += 1

    def count(self, point):
        x, y = point
        count = 0

        for (px, py), val in self.points.items():
            if (x, y) == (px, py):
                continue

            dx = abs(x - px)
            dy = abs(y - py)

            if dx != dy:
                continue

            p1 = (x, py)
            p2 = (px, y)

            count += val * self.points.get(p1, 0) * self.points.get(p2, 0)
        return count
