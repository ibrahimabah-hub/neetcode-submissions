class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={}
        for num in range(5):
            start = ord('a')+(num*3)
            letters[num+2] = [chr(start), chr(start+1), chr(start+2)]
        
        

        letters[7] = ["p","q","r","s"]
        letters[8] = ["t","u","v"]
        letters[9] = ["w","x","y","z"]
        res = []

        def dfs(i, word):
            if i>= len(digits):
                if word:
                    res.append(str(word))
                return
            arr = letters[int(digits[i])]
            for l in arr:
                dfs(i+1, word+l)

        dfs(0, "")

        return res

