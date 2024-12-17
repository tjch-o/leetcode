def check_if_exist(arr):
    arr.sort(reverse=True)
    seen = set()

    for num in arr:
        if num * 2 in seen or num * 0.5 in seen:
            return True
        seen.add(num)
    return False
