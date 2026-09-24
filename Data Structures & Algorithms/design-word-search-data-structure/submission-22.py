class WordDictionary:

    class Node:

        def __init__(self):
            self.children = {}
            self.word = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word):

        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = self.Node()
            cur = cur.children[c]

        cur.word = True

    def search(self, word):

        def dfs(root, j):
            cur = root
            #print(word)
            for i in range(j, len(word)):
                
                char = word[i]
                if char != ".":
                    if char not in cur.children:
                        return False
                    #print(cur)
                    cur = cur.children[char]
                else:
                    for child in cur.children:
                        if dfs(cur.children[child], i+1):
                            return True
                    return False
            return cur.word
        
        return dfs(self.root, 0)
                    
    