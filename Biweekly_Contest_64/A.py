class Solution:
    def kthDistinct(self, arr, k: int) -> str:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        for i in arr:
            if d[i]==1:
                if k==1:
                    return i
                k-=1
        return ""