class Solution:
    def maxMatrixSum(self, matrix) -> int:
        c=s=0
        m=math.inf
        for i in matrix:
            for j in i:
                if j<0:
                    c+=1
                m=min(m,abs(j))
                s+=abs(j)
        if c%2==0:
            return s
        return s-2*m
        