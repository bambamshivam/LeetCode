class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        c=0
        for i in range(left,right+1):
            for j in range(len(ranges)):
                if ranges[j][0]<=i<=ranges[j][1]:
                    c+=1
                    break
        if c!=right-left+1:
            return False
        return True