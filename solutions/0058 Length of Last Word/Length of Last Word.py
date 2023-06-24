def lengthOfLastWord(s):
    start = 0
    end = 0
    current_word = ""
    words = []
    
    for i in range(len(s)):
        if s[i] == " ":
            words.append(current_word)
            current_word = ""
        else:
            if current_word == "":
                start = i
            current_word += s[i]
            end = i
            
    words.append(current_word)
    
    words = list(filter(lambda x: x != "", words))
    return len(words[-1])