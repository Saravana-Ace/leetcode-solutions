class Trie:

    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        temp = self
        for c in word:
            if c not in temp.children:
                new_t = Trie()
                temp.children[c] = new_t
                temp = new_t
            else:
                temp = temp.children[c]
        
        temp.end = True
        

    def search(self, word: str) -> bool:
        temp = self
        for c in word:
            if c not in temp.children: return False
            temp = temp.children[c]
        
        return temp.end
        

    def startsWith(self, prefix: str) -> bool:
        temp = self
        for c in prefix:
            if c not in temp.children: return False
            temp = temp.children[c]
        
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)