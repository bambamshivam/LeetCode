class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        s={};l=[]
        for i in nums:s[i]=s.get(i,0)+1
        for i in nums:
            if i+1 not in s and i-1 not in s and s[i]==1:l.append(i)
        return l