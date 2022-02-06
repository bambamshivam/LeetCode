class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n=len(corridor);ans=1;j=0;t=corridor.count('S')
        if t==0 or t%2!=0:return 0
        for i in range(1,t//2):
            c=p=0
            while j<n and c<2:
                c+=(corridor[j]=='S');j+=1
            k=j
            while j<n and c<3:
                c+=(corridor[j]=='S');p+=(corridor[j]=='P');j+=1
            j=k
            ans=(ans*(p+1))%1000000007
        return ans