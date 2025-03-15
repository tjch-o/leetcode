from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res = []
        q = deque([root])

        while q:
            curr = q.popleft()

            if curr:
                res.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                res.append("null")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        values = data.split(",")
        root = TreeNode(values[0])
        q = deque([root])
        i = 1

        while q:
            curr = q.popleft()

            if values[i] != "null":
                curr.left = TreeNode(values[i])
                q.append(curr.left)
            i += 1

            if values[i] != "null":
                curr.right = TreeNode(values[i])
                q.append(curr.right)
            i += 1
        return root
