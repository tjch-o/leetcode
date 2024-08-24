from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root, target_sum):
    paths = []

    if not root:
        return paths

    queue = deque()
    queue.append((root, root.val, [root.val]))

    while queue:
        curr, ps, accumulated_path = queue.popleft()

        # take root-to-leaf paths only
        if ps == target_sum and not curr.left and not curr.right:
            paths.append(accumulated_path)

        if curr.left:
            queue.append(
                (curr.left, ps + curr.left.val, accumulated_path + [curr.left.val])
            )

        if curr.right:
            queue.append(
                (curr.right, ps + curr.right.val, accumulated_path + [curr.right.val])
            )
    return paths
