def rand10():
    while True:
        row = rand7() - 1
        col = rand7() - 1
        val = row * 7 + col

        if val < 40:
            return val % 10 + 1
