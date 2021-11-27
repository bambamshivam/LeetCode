import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
class Solution:
    def countWords(self, words1, words2) -> int:
        c=0
        for i in words1:
            if i in words2 and words2.count(i)==1 and words1.count(i)==1:
                c+=1
        return c