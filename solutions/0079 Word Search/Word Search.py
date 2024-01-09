def exist(board, word):
    def isWithinBoard(i, j):
        return 0 <= i < len(board) and 0 <= j < len(board[0])

    def dfs(i, j, index, visited):
        if index == len(word):
            return True

        if isWithinBoard(i, j) and board[i][j] == word[index] and not visited[i][j]:
            visited[i][j] = True

            left = dfs(i, j - 1, index + 1, visited)
            if left:
                return left

            right = dfs(i, j + 1, index + 1, visited)
            if right:
                return right

            up = dfs(i - 1, j, index + 1, visited)
            if up:
                return up

            down = dfs(i + 1, j, index + 1, visited)
            if down:
                return down

            # need to backtrack for other explorations through the grid
            visited[i][j] = False
            return left or right or up or down

        return False

    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    # search the whole grid for the word
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0, visited):
                return True
    return False
