class Solution:
    def earliestFullBloom(self, p: list[int], g: list[int]) -> int:
        l=[];n=len(p)
        for i in range(n):l.append([p[i],g[i]])
        l.sort(key=lambda x:-x[1])
        cur=ans=0
        for i in range(n):
            cur+=l[i][0]
            ans=max(ans,cur+l[i][1])
        return ans