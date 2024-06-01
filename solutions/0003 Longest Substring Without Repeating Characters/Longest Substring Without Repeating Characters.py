def length_of_longest_substring(s):
    longest = 0
    curr_substr = ""

    for i in range(len(s)):
        if s[i] in curr_substr:
            start = curr_substr.index(s[i])
            curr_substr = curr_substr[start + 1 :]

        curr_substr += s[i]
        longest = max(longest, len(curr_substr))
    return longest
