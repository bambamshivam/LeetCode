class DetectSquares:

    def __init__(self):
        self.di={}

    def add(self, point) -> None:
        self.di[(point[0],point[1])]=self.di.get((point[0],point[1]),0)+1

    def count(self, point) -> int:
        c=0
        for ke in self.di:
            i=ke[0]
            x=abs(point[0]-i)
            if x!=0 and ke[1]==point[1]:
                a1=self.di.get((i,point[1]),0)
                a2=self.di.get((i,point[1]+x),0)
                a3=self.di.get((point[0],point[1]+x),0)
                c+=a1*a2*a3
                b1=self.di.get((i,point[1]),0)
                b2=self.di.get((i,point[1]-x),0)
                b3=self.di.get((point[0],point[1]-x),0)
                c+=b1*b2*b3
                
        return c

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)