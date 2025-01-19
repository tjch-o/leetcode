def car_pooling(trips, capacity):
    events = []

    for num_passengers, start, end in trips:
        events.append((start, num_passengers))
        events.append((end, -num_passengers))

    events.sort(key=lambda x: (x[0], x[1]))
    curr = 0

    for _, x in events:
        curr += x

        if curr > capacity:
            return False
    return True
