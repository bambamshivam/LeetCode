
import itertools

class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = [1, 22, 122, 333, 1333, 4444, 44441, 55555, 22333, 122333, 155555, 224444, 666666]
        tmp = [str(t) for t in tmp]
        candidates = []
        for t in tmp:
        
            candidates += list( set("".join(p) for p in itertools.permutations(list(t)) ) )
        
        candidates = [int(c) for c in candidates]
        candidates.append(1224444)
        candidates.sort()
        # print(candidates)
        ind = bisect.bisect_right(candidates, n)
        return candidates[ind]