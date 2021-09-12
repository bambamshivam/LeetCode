class Solution:
    def countQuadruplets(self, nums) -> int:
        n=len(nums)
        di={}
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    di[(i,j,k)]=nums[i]+nums[j]+nums[k]
        c=0
        for ke in di:
            for i in range(ke[-1]+1,n):
                if di[ke]==nums[i]:
                    c+=1
        return c
        
        