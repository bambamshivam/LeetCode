class Solution:
    def countPoints(self, rings: str) -> int:
        n=len(rings);c=0
        d=defaultdict(set)
        for i in range(0,n,2):
            d[rings[i+1]].add(rings[i])
        for i in d:
            if len(d[i])==3:c+=1
        return c