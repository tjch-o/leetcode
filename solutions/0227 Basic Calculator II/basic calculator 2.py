def evaluate_op(op, x, y):
    func = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y),
    }
    return func[op](x, y)


def get_precedence(op):
    if op == "*" or op == "/":
        return 2
    elif op == "+" or op == "-":
        return 1
    return 0


def apply_ops(nums, op):
    n2 = nums.pop()
    n1 = nums.pop()
    res = evaluate_op(op, n1, n2)
    nums.append(res)


def calculate(s):
    nums = []
    ops = []
    prev = ""

    for c in s:
        if c.isnumeric():
            if nums and prev.isnumeric():
                nums[-1] = nums[-1] * 10 + int(c)
            else:
                nums.append(int(c))
        elif c != " ":
            if c in "+-*/":
                while ops and get_precedence(ops[-1]) >= get_precedence(c):
                    apply_ops(nums, ops.pop())
                ops.append(c)
        prev = c

    while ops:
        op = ops.pop()
        apply_ops(nums, op)
    return int(nums[0])
