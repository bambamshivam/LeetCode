class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums);a,b=nums.index(max(nums)),nums.index(min(nums))
        t=min(max(a+1,b+1),max(n-a,n-b))
        if a<b:
            t=min(a+1+n-b,t)
        elif a>b:
            t=min(b+1+n-a,t)
        else:
            t=n
        return t