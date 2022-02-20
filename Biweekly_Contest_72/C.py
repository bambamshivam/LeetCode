class Solution:
    def maximumEvenSplit(self, s: int) -> list[int]:
        if s%2==1:return []
        n=int(((1+4*s)**0.5 -1)/2)
        if n%2==1:n-=1
        d=s-(n*(n+1))
        if 1<=d<=2*n and d%2==0:
            l=list(range(2,2*n,2))+[2*n+d]
        else:
            l=list(range(2,2*n+1,2))+[d]
        return l