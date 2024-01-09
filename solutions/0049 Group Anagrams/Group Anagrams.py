def groupAnagrams(strs):
    def get_anagram(s):
        result = list(s)
        result.sort()
        return "".join(result)

    anagram_dict = {}

    for word in strs:
        anagram = get_anagram(word)
        if anagram not in anagram_dict:
            anagram_dict[anagram] = [word]
        else:
            anagram_dict[anagram].append(word)

    return list(anagram_dict.values())
