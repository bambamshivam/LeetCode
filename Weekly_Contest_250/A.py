class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        n=len(text)
        i=c=0
        di={}
        for i in range(len(brokenLetters)):
            di[brokenLetters[i]]=1
        i=0
        while i<n:
            if text[i]==" ":
                i+=1
                continue
            j=i
            f=0
            while j<n and text[j]!=" ":
                if di.get(text[j],0)!=0:
                    f=1
                j+=1
            if f==0:
                c+=1
            i=j
            i+=1
        return c
            
            
obj=Solution()
print(obj.canBeTypedWords("leet code","e"))