class Solution:
    def finalValueAfterOperations(self, l) -> int:
        c=0
        for i in range(len(l)):
            if l[i][0]=='-' or l[i][-1]=='-':
                c-=1
            else:
                c+=1
        return c