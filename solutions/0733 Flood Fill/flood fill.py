def within_grid(image, i, j):
    m, n = len(image), len(image[0])
    return i >= 0 and i <= m - 1 and j >= 0 and j <= n - 1


def dfs(image, i, j, original, new):
    if not within_grid(image, i, j) or image[i][j] != original:
        return

    image[i][j] = new
    dfs(image, i - 1, j, original, new)
    dfs(image, i + 1, j, original, new)
    dfs(image, i, j - 1, original, new)
    dfs(image, i, j + 1, original, new)


def flood_fill(image, sr, sc, color):
    curr = image[sr][sc]

    if curr != color:
        dfs(image, sr, sc, curr, color)
    return image
