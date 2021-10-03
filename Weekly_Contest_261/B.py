class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s=sum(rolls)
        m=len(rolls)
        s1=mean*(m+n) - s
        l=[0]*n
        while s1>0:
            for i in range(n):
                if s1<=0:
                    break
                l[i]+=1
                s1-=1
            if s1<=0:
                break
        if max(l)>6 or min(l)<1:
            return []
        return l