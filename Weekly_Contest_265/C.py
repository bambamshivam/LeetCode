class Solution:
    def minimumOperations(self, nums, start: int, goal: int) -> int:
        d={start};a=0
        q=deque([start])
        while q:
            for _ in range(len(q)):
                t=q.popleft()
                if t==goal: return a
                if 0<=t<=1000:
                    for i in nums:
                        if t+i not in d:
                            d.add(t+i)
                            q.append(t+i)
                        if t-i not in d:
                            d.add(t-i)
                            q.append(t-i)
                        if t^i not in d:
                            d.add(t^i)
                            q.append(t^i)
            a+=1
        return -1
        