class Solution:

    def __init__(self):
        self.breaks = []
    
    def encode(self, strs: List[str]) -> str:
        for word in strs:
            self.breaks.append(len(word))
        
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        out = []

        for b in self.breaks:
            out.append(s[:b])
            s = s[b:]
        
        if not self.breaks:
            return []
        return out