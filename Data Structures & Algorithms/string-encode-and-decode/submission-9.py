class Solution:

    def __init__(self):
        self.delimiters = []
    
    def encode(self, strs: List[str]) -> str:
        if len(strs)<1:
            return 'empty'
        if len(strs)<2:
            return strs[0]
        string = ""
        for i in range(len(strs)):
            word = strs[i]
            string = string+word
            self.delimiters.append(len(word))
            print(word)
        return string


    def decode(self, s: str) -> List[str]:
        words = []
        if s == 'empty':
            return []
        if len(self.delimiters)<1:
            return [s]

        print(s)
        for delimiter in self.delimiters:
            
            words.append(s[:delimiter])
            s = s[delimiter:]
        return words