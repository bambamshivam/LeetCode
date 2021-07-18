class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        l=rungs
        n=len(l)
        c=0
        if l[0]>dist:
            c+=(l[0]-1)//dist
        for i in range(n-1):
            if l[i+1]-l[i]>dist:
                c+=(l[i+1]-l[i]-1)//dist
        return c
        
obj=Solution()
print(obj.addRungs([4,6],1))