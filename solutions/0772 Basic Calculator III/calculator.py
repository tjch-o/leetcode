def apply_op(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return a // b if a * b >= 0 else -(abs(a) // abs(b))


def precedence(op):
    if op in "+-":
        return 1
    elif op in "*/":
        return 2
    return 0


def calculate(s):
    n = len(s)
    i = 0
    nums = []
    ops = []

    while i < n:
        c = s[i]

        if c == " ":
            i += 1
            continue
        elif c == "(":
            ops.append(c)
            i += 1
        elif c.isdigit():
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            nums.append(num)
        elif c == ")":
            while i < n and ops[-1] != "(":
                b = nums.pop()
                a = nums.pop()
                op = ops.pop()
                nums.append(apply_op(a, b, op))
            ops.pop()
            i += 1
        else:
            while i < n and ops and (precedence(ops[-1]) >= precedence(c)):
                b = nums.pop()
                a = nums.pop()
                op = ops.pop()
                nums.append(apply_op(a, b, op))
            ops.append(c)
            i += 1

    while ops:
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        nums.append(apply_op(a, b, op))
    return nums[0] if nums else 0
