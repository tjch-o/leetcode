def generate_adjacency_list(numCourses, prerequisites):
    adjacency_list = [[] for _ in range(numCourses)]

    for course, prerequisite in prerequisites:
        adjacency_list[course].append(prerequisite)
    return adjacency_list


def dfs(node, visited, adjacency_list):
    # encounter a cycle
    if node in visited:
        return False

    visited.add(node)
    neighbours = adjacency_list[node]

    for neighbour in neighbours:
        if dfs(neighbour, visited, adjacency_list) == False:
            return False

    # for backtracking to prevent other paths from incorrectly marking as a cycle
    visited.remove(node)
    # if a new path does dfs on this node again and this node has not been visited before 
    adjacency_list[node] = []
    return True


def can_finish(numCourses, prerequisites):
    adjacency_list = generate_adjacency_list(numCourses, prerequisites)
    visited = set()

    for i in range(numCourses):
        if not dfs(i, visited, adjacency_list):
            return False
    return True
