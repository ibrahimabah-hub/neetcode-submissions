class PrefixTree:

    def __init__(self):
        self.words = set()
        self.pres = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word)):
            self.pres.add(word[0:i+1])

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        if prefix in self.pres:
            return True
        return False        
        