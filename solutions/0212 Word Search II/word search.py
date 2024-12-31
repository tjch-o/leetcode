class TrieNode:
    def __init__(self):
        self.chars = [None for _ in range(26)]
        self.word = None


def build_trie(words):
    root = TrieNode()

    for word in words:
        node = root
        for c in word:
            i = ord(c) - 97

            if not node.chars[i]:
                node.chars[i] = TrieNode()

            node = node.chars[i]
        node.word = word
    return root


def within_board(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])


def dfs(board, i, j, node, res):
    if not within_board(board, i, j) or board[i][j] == "#":
        return

    c = board[i][j]
    index = ord(c) - 97

    if not node.chars[index]:
        return

    node = node.chars[index]
    board[i][j] = "#"

    if node.word:
        res.add(node.word)

    dfs(board, i - 1, j, node, res)
    dfs(board, i + 1, j, node, res)
    dfs(board, i, j - 1, node, res)
    dfs(board, i, j + 1, node, res)
    board[i][j] = c


def find_words(board, words):
    m, n = len(board), len(board[0])
    node = build_trie(words)
    res = set()

    for i in range(m):
        for j in range(n):
            dfs(board, i, j, node, res)
    return list(res)
