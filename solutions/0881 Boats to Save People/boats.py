def num_rescue_boats(people, limit):
    people.sort()
    count = 0
    start = 0
    end = len(people) - 1

    while start <= end:
        curr = people[start] + people[end]

        if curr <= limit:
            count += 1
            start += 1
            end -= 1
        else:
            count += 1
            end -= 1
    return count
