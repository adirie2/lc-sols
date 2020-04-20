#Implement Trie (Prefix Trie)
#

class Node:
    """
       Every Node has a char, a set of children, and a flag to determine if that char is a word 
    """
    def __init__(self, char, children, isWord):
        self.char = char
        self.children = children
        self.isWord = isWord

class Trie:

    def __init__(self):
        """
        The trie data structure is essentially just a dummy node holding the each first char of every word that is added
        in an initial children list
        """
        self.children = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        O(n) where n is the length of the word to be inserted
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
        O(n) where n is the length of the word to be searched for
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
        O(N) where n is the length of the prefix.
        basically checks to see if their are any children in that last node if that char exists in the Trie.
        if it does not we simply return false, and if it keeps hitting the else statement at the end of the loop
        we know that their are words in that sub tree
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