class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3) :
        d1={};d2={};d3={}
        nums=nums1+nums2+nums3
        for i in range(len(nums1)):
            d1[nums1[i]]=1
        for i in range(len(nums2)):
            d2[nums2[i]]=1
        for i in range(len(nums3)):
            d3[nums3[i]]=1
        l=[];d={}
        for ke in nums1+nums2+nums3:
            if d1.get(ke,0)+d2.get(ke,0)+d3.get(ke,0)>=2:
                d[ke]=1
        for ke in d:
            l.append(ke)
        return l