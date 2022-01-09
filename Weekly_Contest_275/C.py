class Solution:
    def wordCount(self, a: list[str], b: list[str]) -> int:
        d=set();ans=0
        for i in a:
            l=[0]*26
            for j in i:l[ord(j)-97]+=1
            s=''.join(map(str,l))
            d.add(s)
        for i in b:
            l=[0]*26
            for j in i:l[ord(j)-97]+=1
            s=''.join(map(str,l))
            for j in range(len(s)):
                if s[j]=='1':
                    s1=s[:j]+'0'+s[j+1:]
                    if s1 in d:ans+=1;break
        return ans