class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        def nex(i,j,c):
            if c=='L':return [i,j-1]
            if c=='R':return [i,j+1]
            if c=='U':return [i-1,j]
            if c=='D':return [i+1,j]
        ans=[];m=len(s)
        for k in range(m):
            c=0;i,j=startPos
            for l in range(k,m):
                i,j=nex(i,j,s[l])
                if i<0 or i>=n or j<0 or j>=n:break
                c+=1
            ans.append(c)
        return ans