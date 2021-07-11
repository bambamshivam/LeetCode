import math
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=-1*pow(2,31)
        r=pow(2,31)-1
        n=len(s)
        if n==0:
            return 0
        for i in range(n):
            if s[i]!=" ":
                break
        s=s[i:]
        n=len(s)
        if n==0:
            return 0
        k=0
        if s[0].isalpha():
            return 0
        else:
            c=0
            if s[0]=='+' or s[0]=='-':
                i=1
                while i<n and (s[i].isdigit() or s[i]=='.') and c<=1:
                    if s[i]=='.':
                        c+=1
                    i+=1
                s=s[:i]
                if len(s)==1:
                    return 0
                else:
                    k=float(s)
            elif s[0].isdigit():
                i=0
                while i<n and (s[i].isdigit() or s[i]=='.') and c<=1:
                    if s[i]=='.':
                        c+=1
                    i+=1
                s=s[:i]
                k=float(s)
            else:
                return 0
        if k>r:
            return r
        if k<l:
            return l
        return int(round(k))



obj=Solution()
print(obj.myAtoi(""))
                    
                
            
        