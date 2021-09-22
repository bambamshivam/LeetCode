class Solution:
    def sumOfBeauties(self, ar) -> int:
        l,r=[],[]
        n=len(ar)
        m=ar[0]
        t=0
        for i in range(n):
            if ar[i]>m:
                m=ar[i]
                t=i
            l.append((m,t))
        m=ar[-1]
        t=n-1
        for i in range(n-1,-1,-1):
            if ar[i]<m:
                m=ar[i]
                t=i
            r.append((m,t))
        r=r[::-1]
        c=0
        for i in range(1,n-1):
            if l[i][1]==i and r[i][1]==i:
                c+=2
            elif ar[i-1]<ar[i]<ar[i+1]:
                c+=1
        return c