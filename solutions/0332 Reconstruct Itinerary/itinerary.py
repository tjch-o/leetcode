from collections import defaultdict


def dfs(airports, airport, res):
    while airports[airport]:
        next_airport = airports[airport].pop()
        dfs(airports, next_airport, res)
    res.append(airport)


def find_itinerary(tickets):
    airports = defaultdict(list)

    for start, end in tickets:
        airports[start].append(end)

    for airport in airports:
        airports[airport].sort(reverse=True)

    res = []
    dfs(airports, "JFK", res)
    return res[::-1]
