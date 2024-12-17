def is_balanced(num: str):
    odd_sum = 0
    even_sum = 0

    for i in range(len(num)):
        if i % 2 == 0:
            even_sum += int(num[i])
        else:
            odd_sum += int(num[i])
    return odd_sum == even_sum
