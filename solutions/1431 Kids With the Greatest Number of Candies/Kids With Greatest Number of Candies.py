def kidsWithCandies(candies, extraCandies):
    current_max = max(candies)
    result = []
    for i in range(len(candies)):
        if candies[i] + extraCandies >= current_max:
            result.append(True)
        else:
            result.append(False)
    return result
