def mergeAlternatively(word1, word2):
    if word1 and not word2:
        return word1
    elif word2 and not word1:
        return word2
    else:
        length_shorter_word = len(word1) if len(word1) <= len(word2) else len(word2)
        result = ""

        for i in range(length_shorter_word):
            result += word1[i]
            result += word2[i]

        result += word1[length_shorter_word:]
        result += word2[length_shorter_word:]
        return result
