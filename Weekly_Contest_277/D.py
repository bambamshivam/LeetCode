class Solution:
    def maximumGood(self, l: list[list[int]]) -> int:
        n=len(l);c=(1<<n)-1;ans=0
        for i in range(c+1):
            s=bin(i)[2:];s='0'*(n-len(s))+s;a=[];f=1
            for i in range(n):
                if s[i]=='1':a.append(i)
            for j in a:
                for k in range(n):
                    if l[j][k]!=2 and l[j][k]!=int(s[k]):f=0;break
                if not f:break
            if f:ans=max(ans,s.count('1'))
        return ans