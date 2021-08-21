class Solution:
    def minTimeToType(self, word: str) -> int:
        s=0
        word='a'+word
        for i in range(1,len(word)):
            t=abs(ord(word[i-1])-ord(word[i]))
            s+=min(t,26-t)+1
        return s
        