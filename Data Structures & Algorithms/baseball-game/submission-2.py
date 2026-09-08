class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores=[]
        for i in range(len(operations)):
            if operations[i]=="+":
                scores.append(scores[-1] + scores[-2])
                continue
            if operations[i]=="D":
                scores.append(scores[-1]*2)
                continue
            if operations[i]=="C":
                scores.pop()
                continue
            scores.append(int(operations[i]))

        total = 0
        for score in scores:
            total+=score
        print(scores)
        return total