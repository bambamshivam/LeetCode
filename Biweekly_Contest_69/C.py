class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        d={};ans=0
        for i in words:
            d[i]=d.get(i,0)+1
        for i in d:
            if i[0]!=i[1] and i[::-1] in d:
                ans+=2*min(d[i],d[i[::-1]])
                d[i]=0;d[i[::-1]]=0
            if i[0]==i[1]:
                if d[i]%2==0:
                    ans+=d[i]
                else:
                    ans+=(d[i]-1)
                    d[i]=1
        for i in d:
            if d[i]==1 and i[0]==i[1]:
                ans+=1;break
        return 2*ans