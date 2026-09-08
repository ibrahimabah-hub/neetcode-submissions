class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            tmp = 0
            j=i+1
            while j<len(arr):
                if arr[j]>tmp:
                    tmp=arr[j]
                j+=1
            arr[i]=tmp
        arr[-1]=-1
        return arr
