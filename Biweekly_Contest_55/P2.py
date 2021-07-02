class Solution(object):

    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        def solve(s,part):
            if s.find(part)==-1:
                return s
            else:
                i=s.find(part)
                s=s[:i]+s[i+len(part):]
                return solve(s,part)
        return solve(s,part)

obj=Solution()
print(obj.removeOccurrences("daabcbaabcbc","abc"))