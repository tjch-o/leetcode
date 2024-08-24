from functools import cmp_to_key


def compare_strings(x: str, y: str):
    if x + y < y + x:
        return -1
    elif x + y > y + x:
        return 1
    return 0


def largest_number(nums):
    s = [str(num) for num in nums]
    s.sort(key=cmp_to_key(compare_strings), reverse=True)

    if s[0] == "0":
        return "0"
    return "".join(s)
