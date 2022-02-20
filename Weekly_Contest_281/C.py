class Solution:
    def repeatLimitedString(self, s: str, r: int) -> str:
        d=[0]*26;ans="";f=0
        for i in s:d[ord(i)-97]+=1
        i=0;j=1;d.reverse()
        while 1:
            while i<26 and d[i]==0:i+=1
            while j<26 and (j<=i or d[j]==0):j+=1
            if not (i<26 and j<26):break
            m=min(r-f,d[i]);f=0
            ans+=chr(122-i)*m+chr(122-j)
            d[i]-=m;d[j]-=1
            if d[i]==0 and d[j]>0:f=1
        if i<26:ans+=chr(122-i)*min(r-f,d[i]);f=0
        if j<26:ans+=chr(122-j)*min(r-f,d[j]);f=0
        return ans