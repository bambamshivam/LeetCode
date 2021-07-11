class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        H=1000000007
        if m==1:
            return (3*pow(2,n-1,H))%H
        if m==2:
            return (6*pow(3,N-1,H))%H
        if m==3:
            s=d=6
            for i in range(n-1):
                s1=(3*s)%H + (2*d)%H
                d1=(2*s)%H + (2*d)%H
                s=s1
                d=d1
            return (s+d)%H
        #not completed for m=4 and m=5
