def get_frequency_list(s):
    result = {}
    for c in s:
        result[c] = result.get(c, 0) + 1
    return result


def longest_palindrome(s):
    freq_list = get_frequency_list(s)
    count = 0
    is_odd = False

    for key in freq_list:
        if freq_list[key] % 2 == 0:
            count += freq_list[key]
        else:
            is_odd = True
            count += freq_list[key] - 1

    if is_odd:
        return count + 1
    return count
