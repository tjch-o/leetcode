class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_the_end = False

    def add_child(self, c):
        if c not in self.children:
            self.children[c] = TrieNode()
    
    def get_child(self, c):
        return self.children.get(c)
        
    def is_end(self):
        return self.is_the_end
    
    def set_end(self):
        self.is_the_end = True


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for c in word:
            curr.add_child(c)
            curr = curr.get_child(c)
        
        curr.set_end()

    def search(self, word):
        # dfs is specifically required to handle the wildcard
        def dfs(word, node, index):
            if index == len(word):
                return node.is_end()
            
            curr = word[index]
            if curr == ".":
                for child in node.children.values():
                    result = dfs(word, child, index + 1)
                    if result == True:
                        return True
                return False

            next = node.get_child(curr)
            if next == None:
                return False
            return dfs(word, next, index + 1)
        return dfs(word, self.root, 0)
            

            


