class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(prefix_sum_counts, curr, curr_sum, target_sum):
    if not curr:
        return 0

    curr_sum += curr.val
    complement = curr_sum - target_sum
    paths = prefix_sum_counts.get(complement, 0)

    prefix_sum_counts[curr_sum] = prefix_sum_counts.get(curr_sum, 0) + 1
    paths += dfs(prefix_sum_counts, curr.left, curr_sum, target_sum)
    paths += dfs(prefix_sum_counts, curr.right, curr_sum, target_sum)

    # backtrack
    prefix_sum_counts[curr_sum] -= 1
    return paths


def path_sum(root, target_sum):
    # key is sum, value is number of paths leading up to the sum
    prefix_sum_counts = {0: 1}
    return dfs(prefix_sum_counts, root, 0, target_sum)
