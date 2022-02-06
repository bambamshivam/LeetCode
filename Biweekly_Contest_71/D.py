from heapq import heapify,heappop,heappush
class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n=len(nums)//3
        def solve(nums):
            h=[]
            for i in range(n):h.append(-nums[i])
            heapify(h);s=sum(h);l=[s]
            for i in range(n,2*n):
                heappush(h,-nums[i])
                t=heappop(h)
                if t==-nums[i]:
                    l.append(s)
                else:
                    s=s-t-nums[i]
                    l.append(s)
            return l
        def solve1(nums):
            h=[]
            for i in range(n):h.append(nums[i])
            heapify(h);s=sum(h);l=[s];print(h)
            for i in range(n,2*n):
                heappush(h,nums[i])
                t=heappop(h);print(t)
                if t==nums[i]:
                    l.append(s)
                else:
                    s=s-t+nums[i]
                    l.append(s)
            return l
        l1=solve(nums)
        l2=solve1(nums[::-1])[::-1];print(l1,l2)
        ans=math.inf
        for i in range(len(l1)):
            ans=min(-l1[i]-l2[i],ans)
        return ans