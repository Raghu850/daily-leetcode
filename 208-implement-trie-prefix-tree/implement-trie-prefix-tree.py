class Trie:

    def __init__(self):
        self.words = set()
        self.pref = set()
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word), 0, -1):
            prefix = word[:i]
            if prefix in self.pref:
                break
            self.pref.add(prefix)
        

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.pref
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)