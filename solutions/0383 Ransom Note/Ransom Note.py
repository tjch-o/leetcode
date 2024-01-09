def canConstruct(ransomNote, magazine):
    remainder = list(magazine)

    for char in ransomNote:
        if char in remainder:
            i = remainder.index(char)
            remainder.pop(i)
        else:
            return False
    return True
