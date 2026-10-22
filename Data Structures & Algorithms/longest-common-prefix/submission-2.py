class Solution:
    class Node:
        def __init__(self):
            self.times = 1
            self.children = {}

    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = self.Node()
        end = len(strs[0])
        for word in strs:
            end = min(len(word), end)
            cur = root
            for i in range(len(word)):
                char = word[i]
                if cur.children and char not in cur.children:
                    end = min(end, i)
                    break
                elif cur.children:
                    cur.children[char].times+=1
                else:
                    cur.children[char] = self.Node()

                cur = cur.children[char]
        return strs[0][:end]

