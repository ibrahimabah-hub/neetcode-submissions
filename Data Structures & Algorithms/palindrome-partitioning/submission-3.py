class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        sub = []

        def isPalindrome(arr):
            if not arr:
                return False
            for i in range(len(arr)//2):
                if arr[i] != arr[len(arr)-i-1]:
                    return False

            return True

        def dfs(i, j):
            if i>=len(s) or j>len(s):
                if sub not in res and sub:
                    res.append(sub.copy())
                return
            if i>=j:
                return

            cur = s[i:j]
            if cur and isPalindrome(cur):
                sub.append(cur)
                dfs(j, len(s))
                sub.pop()
            dfs(i, j-1)

        dfs(0, len(s))

        return res