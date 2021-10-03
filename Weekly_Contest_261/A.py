class Solution:
    def minimumMoves(self, s: str) -> int:
        n=len(s)
        i=c=0
        while i<n:
            if s[i]=='X':
                i+=3
                c+=1
            else:
                i+=1
        return c
        
        