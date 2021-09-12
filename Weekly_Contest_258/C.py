class Solution:
    def maxProduct(self, s: str) -> int:
        n=len(s)
        l,a=[],[]
        def pal(s):
            t=len(s)
            for i in range(t//2):
                if s[i]!=s[t-i-1]:
                    return False
            return True
        def maxp(s1):
            n=len(s1)
            s2=s1[::-1]
            m=n
            dp=[[0 for i in range(m+1)] for j in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if s1[i-1]==s2[j-1]:
                        dp[i][j]=1+dp[i-1][j-1]
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            return (dp[n][m])
        def solve(i,s1,di):
            if i>=n:
                l.append([s1,di])
                return
            solve(i+1,s1,di)
            di1=di[:]
            di1.append(i)
            solve(i+1,s1+s[i],di1)
        solve(0,'',[])
        l.pop(0)
        m=0
        for i in l:
            if pal(i[0]):
                a.append([i[0],i[1]])
        for i in range(len(a)):
            s1=""
            for j in range(n):
                if j not in a[i][1]:
                    s1+=s[j]
            p=maxp(s1)
            m=max(m,len(a[i][0])*p)
        return m
            
            
            
            
            
            
            
            
            
        