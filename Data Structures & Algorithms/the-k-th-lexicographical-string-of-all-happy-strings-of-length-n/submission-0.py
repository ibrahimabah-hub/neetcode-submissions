class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        bucket = set()

        def dfs(word):
            if len(word)==n:
                if word not in bucket:
                    bucket.add(word)
                return
            if len(bucket)>=k:
                return

            for i in range(3):
                if len(word)>0 and ord(word[-1])==ord('a')+i:
                    continue
                dfs(word+chr(ord('a')+i))

        dfs("")
        if len(bucket)<k:
            return ""
        else:
            return sorted(list(bucket))[k-1]


