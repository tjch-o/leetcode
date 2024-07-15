def permute(curr, mapping):
    result = []

    if not curr:
        return mapping

    for elem in curr:
        for c in mapping:
            result.append(elem + c)
    return result


def letter_combinations(digits):
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    result = []

    for digit in digits:
        result = permute(result, mapping[digit])
    return result
