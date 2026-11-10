class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        out = []

        for i in range(len(searchWord)):
            cur = []
            for prod in products:
                if len(prod)<i+1 or prod[:i+1]!=searchWord[:i+1] or len(cur)>=3:
                    continue
                cur.append(prod)
            out.append(cur)

        return out
