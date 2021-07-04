class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        n-len(chalk)
        s,i=k%sum(chalk),0
        while i<n and chalk[i]<=s:
            s-=chalk[i]
            i+=1

        return i