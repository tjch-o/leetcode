def compressed_string(word):
    prev = ""
    curr = ""
    result = ""
    curr_prefix = 1
    n = len(word)

    if n == 1:
        return "1" + word

    for i in range(1, n):
        prev, curr = word[i - 1], word[i]

        if prev == curr:
            if curr_prefix == 9:
                result += str(curr_prefix) + prev
                curr_prefix = 1
            else:
                curr_prefix += 1
        else:
            result += str(curr_prefix) + prev
            curr_prefix = 1

    prev = curr
    result += str(curr_prefix) + prev
    return result
