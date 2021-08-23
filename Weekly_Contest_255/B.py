class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        di={}
        n=len(nums[0])
        for i in range(len(nums)):
            nums[i]=int(nums[i],2)
            di[nums[i]]=1
        for i in range(0,2**n):
            if di.get(i,-1)==-1:
                return '0'*(n-len(bin(i)[2:]))+bin(i)[2:]
        