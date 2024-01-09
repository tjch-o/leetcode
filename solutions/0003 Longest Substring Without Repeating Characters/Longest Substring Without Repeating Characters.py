def lengthOfLongestSubstring(s):
    substr = ""
    max_length = 0

    for char in s:
        if char not in substr:
            max_length = max(len(substr) + 1, max_length)
            substr += char
        else:
            i = substr.index(char)
            substr = substr[i + 1 :] + char
    return max_length
