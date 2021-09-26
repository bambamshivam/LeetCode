class Solution:
    def placeWordInCrossword(self, l, s) -> bool:
        n=len(l)
        m=len(l[0])
        p=len(s)
        for i in range(n):
            j=0
            while j<m:
                t=0
                while j<m and t<p and l[i][j]!='#' and (s[t]==l[i][j] or l[i][j]==" "):
                    t+=1
                    j+=1
                if t==len(s) and ((j<m and l[i][j]=='#') or j>=m) and ((j-t>0 and l[i][j-t-1]=='#') or j-t<=0):
                    return True
                j+=1
        for i in range(m):
            j=0
            while j<n:
                t=0
                while j<n and t<p and l[j][i]!='#' and (s[t]==l[j][i] or l[j][i]==' '):
                    t+=1
                    j+=1
                if t==len(s) and ((j<n and l[j][i]=='#') or j>=n) and ((j-t>0 and l[j-t-1][i]=='#') or j-t<=0):
                    return True
                j+=1
        t=[];d=[]
        for i in l:
            k=i[::-1]
            t.append(k)
        for i in range(m):
            k=[]
            for j in range(n):
                k.append(t[j][i])
            k=k[::-1]
            for j in range(n):
                t[j][i]=k[j]
        l=t
        for i in range(n):
            j=0
            while j<m:
                t=0
                while j<m and t<p and l[i][j]!='#' and (s[t]==l[i][j] or l[i][j]==" "):
                    t+=1
                    j+=1
                if t==len(s) and ((j<m and l[i][j]=='#') or j>=m) and ((j-t>0 and l[i][j-t-1]=='#') or j-t<=0):
                    return True
                j+=1
        for i in range(m):
            j=0
            while j<n:
                t=0
                while j<n and t<p and l[j][i]!='#' and (s[t]==l[j][i] or l[j][i]==' '):
                    t+=1
                    j+=1
                if t==len(s) and ((j<n and l[j][i]=='#') or j>=n) and ((j-t>0 and l[j-t-1][i]=='#') or j-t<=0):
                    return True
                j+=1
        return False