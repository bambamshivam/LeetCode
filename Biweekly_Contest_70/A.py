class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True);i=ans=0
        while i<len(cost):
            ans+=cost[i]
            if i+1<len(cost):ans+=cost[i+1]
            i+=3
        return ans