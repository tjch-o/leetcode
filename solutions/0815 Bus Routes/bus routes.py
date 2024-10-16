from collections import defaultdict, deque


def num_buses_to_destination(routes, src, target):
    adj_list = defaultdict(set)

    for i, route in enumerate(routes):
        for stop in route:
            adj_list[stop].add(i)

    visited_routes = set()
    visited_stops = set()
    pq = deque([(src, 0)])

    while pq:
        curr, n = pq.popleft()

        if curr == target:
            return n

        if curr in visited_stops:
            continue

        visited_stops.add(curr)

        for route in adj_list[curr]:
            if route in visited_routes:
                continue

            visited_routes.add(route)

            for stop in routes[route]:
                pq.append((stop, n + 1))
    return -1
