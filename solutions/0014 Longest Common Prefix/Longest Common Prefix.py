def longestCommonPrefix(strs):
    # prefix is the beginning of the word
    longest_prefix = ""
    first_str = strs[0]
    should_exit = False

    for i in range(len(first_str)):
        for j in range(1, len(strs)):
            if i >= len(strs[j]):
                should_exit = True
                break

            if first_str[i] != strs[j][i]:
                should_exit = True
                break

        if should_exit:
            break

        longest_prefix += first_str[i]
    return longest_prefix
