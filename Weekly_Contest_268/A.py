class Solution:
    def maxDistance(self, c) -> int:
        m=0
        for i in range(len(c)):
            for j in range(i+1,len(c)):
                if c[i]!=c[j]:
                    m=max(m,j-i)
        return m