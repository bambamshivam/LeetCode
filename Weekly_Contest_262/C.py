class StockPrice:

    def __init__(self):
        self.d={}
        self.ma=[]
        self.mi=[]
        self.cur=0
        self.elma={}
        self.elmi={}

    def update(self, timestamp: int, price: int) -> None:
        if self.d.get(timestamp,0)!=0:
            self.elma[self.d[timestamp]]=self.elma.get(self.d[timestamp],0)+1
        if self.d.get(timestamp,0)!=0:
            self.elmi[self.d[timestamp]]=self.elmi.get(self.d[timestamp],0)+1
        heapq.heappush(self.ma,-price)
        heapq.heappush(self.mi,price)
        self.d[timestamp]=price
        self.cur=max(self.cur,timestamp)

    def current(self) -> int:
        return self.d[self.cur]

    def maximum(self) -> int:
        while True:
            t=heapq.heappop(self.ma)
            if self.elma.get(-t,0)!=0:
                self.elma[-t]-=1
                continue
            else:
                heapq.heappush(self.ma,t)
                return -t

    def minimum(self) -> int:
        while True:
            t=heapq.heappop(self.mi)
            if self.elmi.get(t,0)!=0:
                self.elmi[t]-=1
                continue
            else:
                heapq.heappush(self.mi,t)
                return t


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()