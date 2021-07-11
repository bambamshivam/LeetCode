class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n=len(s)
        s1=s[::-1]
        l=[[0 for i in range(27)] for j in range(n+1)]
        c=0
        for i in range(1,n+1):
            for j in range(1,27):
                if ord(s[i-1])-96==j:
                    l[i][j]=l[i-1][j]+1
                else:
                    l[i][j]=l[i-1][j]
        d={}
        for i in range(n):
            p=d.get(s[i],[])
            p.append(i)
            d[s[i]]=p
        k=0
        for ke in d:
            if len(d[ke])>1:
                t1=d[ke][0]
                t2=d[ke][-1]
                for i in range(1,27):
                    if l[t2][i]!=l[t1+1][i]:
                        k+=1
        return k
        
obj=Solution()
print(obj.countPalindromicSubsequence("abca"))