class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l=nums
        i=c=s=0
        while i<n:
            j=i
            if c==0:
                while j<n-1 and l[j]<=l[j+1]:
                    j+=1
                s+=l[j]
                i=j+1
                c=1
            else:
                while j<n-1 and l[j]>=l[j+1]:
                    j+=1
                if j<n-1:
                    s-=l[j]
                i=j+1
                c=0
        return s


obj=Solution()
print(obj.maxAlternatingSum([6,2,1,2,4,5]))



