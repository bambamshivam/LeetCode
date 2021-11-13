class Solution:
    def maximumBeauty(self, items, queries):
        items.sort();a=[items[0][1]];ans=[]
        for i in range(1,len(items)):
            a.append(max(items[i][1],a[-1]))
        for i in range(len(items)):
            items[i]=items[i][0]
        for i in queries:
            t=bisect_right(items,i)
            if t==0:
                ans.append(0)
            else:
                ans.append(a[t-1])
        return ans