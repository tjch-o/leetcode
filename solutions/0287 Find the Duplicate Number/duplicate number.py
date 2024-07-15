def find_duplicate(nums):
    # implement Tortoise and Hare algorithm
    slow = 0
    fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        # cycle detected
        if slow == fast:
            break

    other_slow = 0

    while slow != other_slow:
        slow = nums[slow]
        other_slow = nums[other_slow]
    return slow
