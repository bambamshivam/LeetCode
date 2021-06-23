class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        di={}
        for i in words:
            for j in i:
                if j in di:
                    di[j]+=1
                else:
                    di[j]=1
        print(di)
        for ke in di:
            if di[ke]%len(words)!=0 and len(words)!=1:
                return False
        return True
obj=Solution()

print(obj.makeEqual(["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]))