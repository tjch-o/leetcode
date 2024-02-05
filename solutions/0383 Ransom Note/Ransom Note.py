def canConstruct(ransom_note, magazine):
    remainder = list(magazine)

    for char in ransom_note:
        if char in remainder:
            i = remainder.index(char)
            remainder.pop(i)
        else:
            return False
    return True
