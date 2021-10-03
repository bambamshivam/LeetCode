class Solution:
    def stoneGameIX(self, l) -> bool:
        n=len(l)
        a=[0]*3
        for i in range(n):
            a[l[i]%3]+=1
        p=a[:]
        def solve(a,t):
            s=i=-1
            if a[t]>0:
                i=0
                while i<n:
                    if s==-1:
                        s=0
                    elif (s%3==2 or s%3==1) and a[0]>0:
                        t=0
                    elif s%3==1 and a[1]>0:
                        t=1
                    elif s%3==2 and a[2]>0:
                        t=2
                    else:
                        break
                    i+=1
                    a[t]-=1
                    s=(s+t)%3
            return i
        i,j=solve(a,1),solve(p,2)
        if (i%2==1 and i!=n and i!=-1) or (j%2==1 and j!=n and j!=-1):
            return True
        return False