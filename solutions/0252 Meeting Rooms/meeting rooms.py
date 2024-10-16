class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def overlap(i1, i2):
    return i1.start < i2.end and i2.start < i1.end


def can_attend_meetings(intervals):
    intervals.sort(key=lambda x: x.start)
    n = len(intervals)

    for i in range(n - 1):
        i1, i2 = intervals[i], intervals[i + 1]

        if overlap(i1, i2):
            return False
    return True
