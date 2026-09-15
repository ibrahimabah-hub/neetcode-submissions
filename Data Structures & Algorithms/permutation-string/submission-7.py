class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = {}
        for s in s1:
            counts[s] = 1 + counts.get(s, 0)
        print(counts)
        window = {}
        l = 0
        r = len(s1)
        n_done = len(counts)
        h_done = 0
        for s in s2[l:r]:
            window[s] = 1 + window.get(s, 0)
            if s in counts and counts[s] == window[s]:
                h_done+=1
                #print(f"{s} now done. {h_done} so far")
        #print(window)
        while r<len(s2):
            if h_done == n_done:
                #print(window)
                return True
            window[s2[l]] -=1
            if s2[l] in counts and window[s2[l]] == counts[s2[l]]-1:
                h_done -=1
            l+=1
            window[s2[r]] = 1 + window.get(s2[r], 0)
            #print(window)
            if s2[r] in counts and window[s2[r]]==counts[s2[r]]:
                print(f"{s2[r]} now done. {h_done} so far")
                h_done +=1
            r+=1
        if h_done == n_done:
            return True
        return False

