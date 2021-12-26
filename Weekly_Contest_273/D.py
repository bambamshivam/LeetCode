class Solution:
    def recoverArray(self, nums: list[int]) -> list[int]:
        nums.sort();a=[];n=len(nums)//2
        for i in range(1,len(nums)):
            p=nums[i]-nums[0]
            if p!=0 and p%2==0:a.append(p)
        for k in a:
            d=defaultdict(deque)
            for i in range(2*n):d[nums[i]].append(i)
            ans=[];j=0;v=[0]*(2*n);f=0
            for i in range(n):
                while j<2*n and v[j]==1:j+=1
                if j>=2*n or len(d[nums[j]+k])==0:f=1;break
                t=d[nums[j]+k].pop();v[t]=1;v[j]=1
                ans.append(nums[j]+k//2);d[nums[j]].popleft()
            if f==0:return ans