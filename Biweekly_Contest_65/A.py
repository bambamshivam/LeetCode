class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d1,d2={},{}
        for i in word1:
            d1[i]=d1.get(i,0)+1
        for i in word2:
            d2[i]=d2.get(i,0)+1
        for i in range(97,123):
            if abs(d1.get(chr(i),0)-d2.get(chr(i),0))>3:
                return False
        return True