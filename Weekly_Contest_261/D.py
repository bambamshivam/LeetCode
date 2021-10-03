class Solution:
    def smallestSubsequence(self, s: str, k: int, l: str, r: int) -> str:
        n1=len(s)
        n2=list(s).count(l)
        d=[]
        for i,j in enumerate(s):
            while d and d[-1]>j and (len(d)+n1-i>k) and (d[-1]!=l or n2>r):
                p=d.pop()
                if p==l:
                    r+=1
            if len(d)<k:
                if j==l:
                    d.append(j)
                    r-=1
                elif k-len(d)>r:
                    d.append(j)
            if j==l:
                n2-=1
        return "".join(d)