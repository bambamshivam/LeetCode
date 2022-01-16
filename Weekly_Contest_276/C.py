class Solution(object):
    def mostPoints(self, a):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        a=a+[[0,0]];n=len(a);dp=[0]*n
        for i in range(n-2,-1,-1):
            c=a[i][0];j=i+a[i][1]+1
            if j<n:c+=dp[j]
            dp[i]=max(c,dp[i+1])
        return max(dp)