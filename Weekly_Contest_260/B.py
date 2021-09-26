class Solution:
    def gridGame(self, l) -> int:
        n=len(l[0])
        a=[[0],[0]]
        s1=s2=0
        for i in range(n):
            s1+=l[0][i]
            s2+=l[1][i]
            a[0].append(s1)
            a[1].append(s2)
        a[0].append(s1)
        a[1].append(s2)
        i=0
        while i<n and a[1][i]<a[0][-1]-a[0][i+1]:
            i+=1
        print(i)
        if i<n:
            return min(a[0][-1]-a[0][i],a[1][i])
        