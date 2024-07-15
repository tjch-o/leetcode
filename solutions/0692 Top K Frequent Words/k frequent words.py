from collections import Counter


def top_k_frequent(words, k):
    counts = Counter(words)
    result = list(counts.items())

    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], result[:k]))
