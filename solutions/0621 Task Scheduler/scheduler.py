from collections import Counter

def least_interval(tasks, n):
    task_counts = Counter(tasks)

    task_slots = list(task_counts.values())
    task_slots.sort(reverse=True)
    highest_freq = task_slots[0]

    # if n = 2 and there are 3 (highest) As it should look like A __ A __ A
    num_intervals = highest_freq - 1
    idle_slots = num_intervals * n

    for slots in task_slots[1:]:
        # can only put one of each character in each interval
        idle_slots -= min(slots, num_intervals)

    idle_slots = max(idle_slots, 0)
    return len(tasks) + idle_slots
