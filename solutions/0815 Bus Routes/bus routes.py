from collections import defaultdict, deque


def num_buses_to_destination(routes, src, dest):
    adj_list = defaultdict(set)

    for i, route_num in enumerate(routes):
        for stop in route_num:
            adj_list[stop].add(i)

    visited_routes = set()
    visited_stops = set()
    queue = deque()
    queue.append((src, 0))

    while queue:
        stop, n = queue.popleft()

        if stop == dest:
            return n

        if stop in visited_stops:
            continue

        visited_stops.add(stop)

        for route_num in adj_list[stop]:
            if route_num in visited_routes:
                continue

            visited_routes.add(route_num)

            for s in routes[route_num]:
                queue.append((s, n + 1))
    return -1
