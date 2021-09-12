class Solution:
    def numberOfWeakCharacters(self, p) -> int:
        n=len(p)
        p.sort(key=lambda x:(-x[0],x[1]))
        m=c=0
        for i in range(n):
            if p[i][1]<m:
                c+=1
            else:
                m=p[i][1]
        return c
        