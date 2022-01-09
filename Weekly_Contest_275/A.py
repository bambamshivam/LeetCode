class Solution:
    def checkValid(self, l: list[list[int]]) -> bool:
        n=len(l);m=len(l[0]);s=set(list(range(1,n+1)))
        for i in range(n):
            if set(l[i])!=s:return False
        for i in range(m):
            s1=set()
            for j in range(n):
                s1.add(l[j][i])
            if s1!=s:return False
        return True