def is_valid(t, target):
    return t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]


def merge_triplets(triplets, target):
    n = len(triplets)
    matches = set()

    for i in range(n):
        if is_valid(triplets[i], target):
            for j in range(3):
                if triplets[i][j] == target[j]:
                    matches.add(j)
    return len(matches) == 3
