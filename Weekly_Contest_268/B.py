class Solution:
    def wateringPlants(self, p: list[int], c: int) -> int:
        s=c;ans=1;i=0
        while i<len(p):
            if p[i]>c:
                ans+=(2*i)
                c=s
            else:
                ans+=1
                c-=p[i]
                i+=1
        return ans-1