def no_overlap(i1, i2):
    return i1[1] < i2[0] or i2[1] < i1[0]


def merge_interval(i1, i2):
    return [min(i1[0], i2[0]), max(i1[1], i2[1])]


def merge(intervals):
    intervals.sort(key=lambda x: (x[0], x[1]))
    stack = []

    for interval in intervals:
        if not stack or no_overlap(stack[-1], interval):
            stack.append(interval)
        else:
            curr = interval
            while stack and not no_overlap(stack[-1], curr):
                merged_interval = merge_interval(stack.pop(), curr)
                curr = merged_interval
            stack.append(curr)
    return stack
