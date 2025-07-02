from collections import Counter


def can_be_formed(word, counts):
    word_count = Counter(word)

    for c in word_count:
        if word_count.get(c, 0) > counts.get(c, 0):
            return False
    return True


def count_characters(words, chars):
    counts = Counter(chars)
    total = 0

    for word in words:
        if can_be_formed(word, counts):
            total += len(word)
    return total
