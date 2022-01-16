class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        c=0
        while target>1:
            while maxDoubles>0 and target%2==0:
                target//=2;c+=1;maxDoubles-=1
            if target!=1:
                if maxDoubles>0:target-=1;c+=1
                else:c+=target-1;break
        return c