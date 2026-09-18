class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        if len(b)<len(a):
            a, b = b, a
    
        half = (len(b) + len(a))//2

        if half == 0:
            return b[0]
        if len(a)<1:
            if len(b) % 2 == 1:
                return(b[half])
            else:
                return((b[half-1]+b[half])/2)

        la = 0
        ra = len(a)-1
        
        while True:
            ai = (la + ra)//2
            a1 = a[ai] if ai>=0 else float("-infinity")
            a2 = a[ai+1] if (ai +1 )<len(a) else float("infinity")
            bi = half - ai - 2
            b1 = b[bi] if bi>=0 else float("-infinity")
            b2 = b[bi+1] if (bi +1)<len(b) else float("infinity")
            #print(f"a1: {a1} a2: {a2} b1: {b1} b2: {b2}")
            if a1<=b2 and b1<= a2:
                left = max(a1, b1)
                right = min(a2, b2)
                break

            elif a1>b2:
                ra = ai - 1
                continue
            else:
                la = ai + 1
                continue
        #print(f"{left} , {right}")
        if (len(a) + len(b)) % 2 == 1:
            return(right)
        else:
            return((left+right)/2)


                    
            
             


        