class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_the_end = False

    def set_end(self):
        self.is_the_end = True

    def is_end_of_word(self):
        return self.is_the_end

    def set_child(self, c):
        if c not in self.children:
            self.children[c] = TrieNode()

    def get_child(self, c):
        return self.children.get(c)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for c in word:
            curr.set_child(c)
            curr = curr.get_child(c)
        curr.set_end()

    def search(self, word):
        curr = self.root

        for c in word:
            curr = curr.get_child(c)

            if not curr:
                return False
        return curr.is_end_of_word()

    def starts_with(self, word):
        curr = self.root

        for c in word:
            curr = curr.get_child(c)

            if not curr:
                return False
        return True
