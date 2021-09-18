class Solution:
    def minOperations(self, ar) -> int:
        di={}
        for i in ar:
            di[i]=1
        l=[]
        for ke in di:
            l.append(ke)
        l.sort()
        n=len(ar)
        n1=len(l)
        j=0
        i=c=m=1
        while i<n1:
            if l[i]-l[j]<=n-1:
                c+=1
                i+=1
                m=max(m,c)
            else:
                c-=1
                j+=1
        return n-m