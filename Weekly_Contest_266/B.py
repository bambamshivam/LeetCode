class Solution:
    def countVowels(self, s: str) -> int:
        l=[];n=len(s);c=0
        for i in range(n):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                l.append(i+1)
            else:
                l.append(0)
        for i in range(1,n):
            l[i]+=l[i-1]
        for i in range(n):
            c+=l[i]
        return c