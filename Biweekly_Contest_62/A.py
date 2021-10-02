class Solution:
    def construct2DArray(self, l, m: int, n: int):
        k=0
        a=[]
        if len(l)!=m*n:
            return []
        for i in range(m):
            a.append([])
            for j in range(n):
                a[-1].append(l[k])
                k+=1
        return a