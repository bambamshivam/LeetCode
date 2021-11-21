class RangeFreqQuery:

    def __init__(self, arr):
        self.d={}
        for i in range(len(arr)):
            p=self.d.get(arr[i],[])
            p.append(i)
            self.d[arr[i]]=p
            

    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.d.get(value,[]),right)-bisect_left(self.d.get(value,[]),left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)