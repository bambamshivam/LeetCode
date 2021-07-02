class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        for i in range(n-1):
            if nums[i]>=nums[i+1]:
                break
        if i>=n-2:
            return True
        l=nums[:]
        l.pop(i)
        nums.pop(i+1)
        a,b=0,0
        for i in range(n-2):
            if nums[i]>=nums[i+1]:
                a=1
            if l[i]>=l[i+1]:
                b=1
        if a==1 and b==1:
            return False
        return True


obj=Solution()
print(obj.canBeIncreasing([105,924,32,968]))