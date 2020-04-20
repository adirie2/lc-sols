class Node:
    def __init__(self, char, children, isWord):
        self.char = char
        self.children = children
        self.isWord = isWord

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = None
        children = self.children
        for char in word:
            if char not in children:
                node = Node(char, {}, False)
                children[char] = node
            else:
                node = children[char]
            children = node.children
        node.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        children = self.children
        node = None
        for char in word:
            if char in children:
                node = children[char]
                children = node.children
            else:
                return False
        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        children = self.children
        for char in prefix:
            if char not in children:
                return False
            else:
                children = children[char].children
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)