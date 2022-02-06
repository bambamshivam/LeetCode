class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        l1=[];l2=[];a=[]
        for i in range(len(nums)):
            if i%2==0:l1.append(nums[i])
            else:l2.append(nums[i])
        l1.sort();l2.sort(reverse=True)
        for i in range(len(nums)):
            if i%2==0:a.append(l1[i//2])
            else:a.append(l2[i//2])
        return a