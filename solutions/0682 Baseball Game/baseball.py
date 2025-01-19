def calculate_points(ops):
    nums = []

    for op in ops:
        if op.isdigit():
            nums.append(int(op))
        elif "-" in op:
            nums.append(-int(op[1:]))
        elif op == "D":
            nums.append(int(nums[-1]) * 2)
        elif op == "C":
            nums.pop()
        else:
            n2 = nums.pop()
            n1 = nums.pop()
            nums.extend([n1, n2])
            nums.append(n1 + n2)
    return sum(nums)
