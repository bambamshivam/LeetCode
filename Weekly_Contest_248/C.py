class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=int(1e9+7)
        if n%2==0:
            x=n//2
        else:
            x=n//2 +1
        t=n-x
        c=1
        c*=pow(5,x,m)
        c*=pow(4,t,m)


        return (c%m)
        