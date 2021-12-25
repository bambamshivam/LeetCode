class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(locked);a=['']*n
        for i in range(n):
            if locked[i]=='1':a[i]=s[i]
        if a[0]==')' or a[-1]=='(' or n%2==1 or a.count('(')>n//2 or a.count(')')>n//2:return False
        a[0]=='(';a[-1]==')';o=c=0
        for i in range(n):
            if a[i]==')':c+=1
            else:o+=1
            if c>o:return False
        o=c=0
        for i in range(n-1,-1,-1):
            if a[i]=='(':o+=1
            else:c+=1
            if o>c:return False
        return True