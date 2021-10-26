class Solution:
    def countValidWords(self, s: str) -> int:
        l=list(s.split());c=0
        for i in l:
            if i[0]=='-' or i[-1]=='-' or i.count('-')>1 or i[-1].isdigit(): continue
            t=i.find('-')
            if t!=-1 and (not i[t-1].isalpha() or not i[t+1].isalpha()): continue
            f=0
            for t in range(len(i)-1):
                j=i[t]
                if j!='-' and not j.isalpha():
                    f=1
                    break
            if f==0:c+=1
        return c