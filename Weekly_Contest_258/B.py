class Solution:
    def interchangeableRectangles(self, r) -> int:
        n=len(r)
        di={}
        s=0
        for i in range(n):
            di[r[i][0]/r[i][1]]=di.get(r[i][0]/r[i][1],0)+1
        for ke in di:
            s+=math.comb(di[ke],2)
        return s
        