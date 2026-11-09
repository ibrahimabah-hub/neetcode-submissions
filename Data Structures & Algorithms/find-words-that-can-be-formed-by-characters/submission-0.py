class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        letters = {}

        for char in chars:
            letters[char] = 1 + letters.get(char, 0)
        tot = 0
        for word in words:
            cur = {}
            good = True
            for char in word:
                cur[char] = 1 + cur.get(char, 0)
                if char not in letters or letters[char]<cur[char]:
                    good = False
                    break
            if good:
                tot+=len(word)

        return tot
                