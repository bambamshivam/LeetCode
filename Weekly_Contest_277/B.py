class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        a=[];b=[];l=[]
        for i in nums:
            if i>0:a.append(i)
            else:b.append(i)
        for i in range(len(nums)//2):
            l.append(a[i]);l.append(b[i])
        return l