class Bitset:

    def __init__(self, size: int):
        self.a=[0]*size;self.s=size;self.c=0;self.f=0

    def fix(self, idx: int) -> None:
        if self.f%2==0:
            if self.a[idx]==0:
                self.a[idx]=1;self.c+=1
        else:
            if self.a[idx]==1:
                self.a[idx]=0;self.c+=1

    def unfix(self, idx: int) -> None:
        if self.f%2==0:
            if self.a[idx]==1:
                self.a[idx]=0;self.c-=1
        else:
            if self.a[idx]==0:
                self.a[idx]=1;self.c-=1

    def flip(self) -> None:
        self.f+=1;self.c=self.s-self.c

    def all(self) -> bool:
        return self.c==self.s

    def one(self) -> bool:
        return self.c>0

    def count(self) -> int:
        return self.c

    def toString(self) -> str:
        if self.f%2==0:
            return ''.join(map(str,self.a))
        else:
            b=[]
            for i in range(len(self.a)):b.append(1-self.a[i])
            return ''.join(map(str,b))

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()