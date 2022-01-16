from sortedcontainers import SortedList
class Solution(object):
    def maxRunTime(self, n, b):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        b.sort();b=b[::-1];c=sum(b[n:])
        def f(m):s=sum(max(0,m-b[i]) for i in range(n));return s<=c
        l=0;r=sum(b)//n;ans=0
        while l<=r:
            m=(l+r)//2
            if f(m):ans=m;l=m+1
            else:r=m-1
        return ans