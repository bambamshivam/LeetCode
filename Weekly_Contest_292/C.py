class Solution:
    def countTexts(self, s: str) -> int:
        n=100000;dp1=[0]*(n+1);dp2=[0]*(n+1);mod1=1000000007;ans=1
        dp1[0]=0;dp1[1]=1;dp1[2]=2;dp1[3]=4
        for i in range(4,n+1):dp1[i]=(dp1[i-1]+dp1[i-2]+dp1[i-3])%mod1
        dp2[0]=0;dp2[1]=1;dp2[2]=2;dp2[3]=4;dp2[4]=8
        for i in range(5,n+1):dp2[i]=(dp2[i-1]+dp2[i-2]+dp2[i-3]+dp2[i-4])%mod1
        i=0;n=len(s)
        while i<n:
            j=i+1
            while j<n and s[j]==s[i]:j+=1
            if s[i] in ['7','9']:ans=(ans*dp2[j-i])%mod1
            else:ans=(ans*dp1[j-i])%mod1
            i=j
        return ans