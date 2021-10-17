class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=list(s.split());a=[];f=0
        for i in l:
            if i.isdigit():
                a.append(int(i))
        for i in range(len(a)-1):
            if a[i]>=a[i+1]:
                f=1
                break
        if f==1:
            return False
        return True
        