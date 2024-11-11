class Trie:

    def __init__(self):
        self.trie ={}

    def insert(self, word: str) -> None:
        dic = self.trie

        for w in word:
            if w not in dic:
                dic[w] = {}
            dic = dic[w]

        dic['\U0001f600'] = '\U0001f600'
        
    def search(self, word: str) -> bool:
        dic = self.trie

        for w in word:
            if w not in dic:
                return False
            dic = dic[w]

        return '\U0001f600' in dic
        
    def startsWith(self, prefix: str) -> bool:
        dic = self.trie

        for w in prefix:
            if w not in dic:
                return False
            dic = dic[w]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
