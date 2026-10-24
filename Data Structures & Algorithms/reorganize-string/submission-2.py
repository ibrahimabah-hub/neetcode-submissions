class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = {}
        for char in s:
            letters[char] = 1 + letters.get(char, 0)

        heap = []
        for l,c in letters.items():
            heapq.heappush_max(heap, (c,l))

        q = collections.deque()
        res = ""
        while heap or q:
            if q and res and res[-1]!=q[0][1]:
                print(f"pushing saved {q[0][1]} to res")
                res = res + q[0][1]
                cur = q.popleft()
                if cur[0]>1:
                    heapq.heappush_max(heap, (cur[0]-1, cur[1]))
            if heap:
                cur = heapq.heappop_max(heap)
                if res and res[-1]==cur[1]:
                    print(f"saving {cur[1]} to q")
                    q.append(cur)
                else:
                    res = res + cur[1]
                    print(f"adding {cur[1]} to res")
                    if cur[0]>1:
                        print(f"running {cur[1]} back with {cur[0]-1} vals")
                        heapq.heappush_max(heap, (cur[0]-1, cur[1]))
            if not heap and res and q and res[-1]==q[0][1]:
                return ""
        
        return res

