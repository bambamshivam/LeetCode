class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d={};ans=0
        for i in s:d[i]=d.get(i,0)+1
        for i in t:d[i]=d.get(i,0)-1
        for i in d:ans+=abs(d[i])
        return ans