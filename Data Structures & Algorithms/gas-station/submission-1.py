class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = 0
        have = 0
        spent = 0
        start = 0
        for i in range(len(gas)):
            have+=gas[i]
            spent+=cost[i]

        if have<spent:
            return -1

        for i in range(len(gas)):
            surplus += gas[i]-cost[i]
            if surplus<0:
                start = i+1
                surplus = 0

        return start



