class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a = []
        for i in range(len(triplets)):
            b = triplets[i]
            if not a or a[0]>target[0] or a[1]>target[1] or a[2]>target[2]:
                a = b
            
            if b[0]>target[0] or b[1]>target[1] or b[2]>target[2]:
                continue

            check = [max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2])]
            #print(f"check: {check}")
            #print(b)
            if check == target:
                return True
            if check[0]==target[0] or check[1]==target[1] or check[1]==target[2]:
                a = check


        if a == target:
            return True
        return False