class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_the_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode()
            ptr = ptr.children[char]

        ptr.is_the_end = True

    def searchHelper(self, word, node, index):
        while index < len(word):
            if word[index] == ".":
                # . is a substitute for any character so loop through the children
                for key in node.children.keys():
                    child_node = node.children[key]
                    if self.searchHelper(word, child_node, index + 1):
                        return True
                return False

            elif word[index] not in node.children:
                return False

            node = node.children[word[index]]
            index += 1

        return node.is_the_end

    def search(self, word):
        return self.searchHelper(word, self.root, 0)
