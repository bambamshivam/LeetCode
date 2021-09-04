class Solution:
    def findMiddleIndex(self, nums) -> int:
        a=nums
        n=len(a)
        if 0==sum(a[1:]):
            return 0
        for i in range(1,n-1):
            if sum(a[:i])==sum(a[i+1:]):
                return i
        if sum(a[:n-1])==0:
            return n-1
        return -1