class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        s1=set(spaces)
        l=list(s)
        for i in range(1,len(s)):
            if i in s1:
                l[i-1]=l[i-1]+' '
        if 0 in s1:
            l[0]=' '+l[0]
        return ''.join(l)