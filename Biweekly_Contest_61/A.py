class Solution:
    def countKDifference(self, nums, k: int) -> int:
        di={}
        n=len(nums)
        for i in range(n):
            di[nums[i]]=di.get(nums[i],0)+1
        l=[]
        for ke in di:
            l.append([ke,di[ke]])
        l.sort()
        c=0
        for i in range(len(l)):
            if di.get(l[i][0]+k,0)!=0:
                c+=di[l[i][0]]*di[l[i][0]+k]
        return c
        