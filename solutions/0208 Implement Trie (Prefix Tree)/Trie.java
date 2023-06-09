class Trie {
    private final int n = 26;
    TrieNode root;

    class TrieNode {
        TrieNode[] chars;
        boolean isTheEnd;
    
        TrieNode() {
            this.chars = new TrieNode[n];
            this.isTheEnd = false;
        }

        void setEnd() { 
            this.isTheEnd = true;
        }

        boolean isEnd() {
            return this.isTheEnd;
        }

        TrieNode get(char c) {
            return this.chars[c - 'a'];
        }

        boolean contains(char c) {
            return this.get(c) != null;
        }

        void put(TrieNode node, char c) {
            this.chars[c - 'a'] = node;
        }
    }
    
    public Trie() {
        this.root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode currentNode = root;
        for (int i = 0; i < word.length(); i += 1) {
            char c = word.charAt(i);
            if (!currentNode.contains(c)) {
                currentNode.put(new TrieNode(), c);
            }
            currentNode = currentNode.get(c);
        }
        currentNode.setEnd();
    }

    public boolean search(String word) {
        TrieNode currentNode = root;
        for (int i = 0; i < word.length(); i += 1) {
            char c = word.charAt(i);
            if (currentNode.contains(c)) {
                currentNode = currentNode.get(c);
            } else {
                return false;
            }
        }
        return currentNode.isEnd();
    }

    /* search and startsWith have same logic just that search needs to check if 
    it is the exact match by checking isTheEnd while startsWith doesn't */ 
    public boolean startsWith(String prefix) {
        TrieNode currentNode = root;
        for (int i = 0; i < prefix.length(); i += 1) {
            char c = prefix.charAt(i);
            if (currentNode.contains(c)) {
                currentNode = currentNode.get(c);
            } else {
                return false;
            }
        }
        return true;
    }
}