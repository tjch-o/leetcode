def within_grid(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])


def dfs(board, i, j, word, visited):
    if not word:
        return True
    elif not within_grid(board, i, j) or visited[i][j] or board[i][j] != word[0]:
        return False

    visited[i][j] = True
    next_word = word[1:]

    left = dfs(board, i, j - 1, next_word, visited)
    if left:
        return left

    right = dfs(board, i, j + 1, next_word, visited)
    if right:
        return right

    up = dfs(board, i - 1, j, next_word, visited)
    if up:
        return up

    down = dfs(board, i + 1, j, next_word, visited)
    # backtracking for future searches since the same cell can be visited in different paths
    visited[i][j] = False
    return left or right or up or down


def exist(board, word):
    m, n = len(board), len(board[0])
    start_pos = []

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                start_pos.append((i, j))

    for i, j in start_pos:
        visited = [[False for _ in range(n)] for _ in range(m)]
        result = dfs(board, i, j, word, visited)
        if result:
            return True
    return False
