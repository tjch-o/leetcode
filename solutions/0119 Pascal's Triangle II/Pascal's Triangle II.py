def get_row(row_index):
    if row_index == 0:
        return [1]
    elif row_index == 1:
        return [1, 1]
    else:
        previous_row = get_row(row_index - 1)
        result = [1]

        for i in range(1, len(previous_row)):
            result.append(previous_row[i - 1] + previous_row[i])

        result.append(1)
        return result
