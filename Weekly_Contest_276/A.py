class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        j=0;ans=[]
        while j<len(s):
            ans.append(s[j:min(len(s),j+k)]);j+=k
        ans[-1]=ans[-1]+fill*(k-len(ans[-1]))
        return ans