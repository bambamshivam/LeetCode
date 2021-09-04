class LockingTree:

    def __init__(self, parent):
        self.p=parent
        n=len(parent)
        self.a=[-1]*n
        self.d=[{} for i in range(n)]
        for i in range(n):
            cur=i
            while parent[cur]!=-1:
                if self.d[parent[cur]].get(i,-1)==-1:
                    self.d[parent[cur]][i]=1
                cur=parent[cur]

    def lock(self, num: int, user: int) -> bool:
        print(self.a)
        if self.a[num]==-1:
            self.a[num]=user
            print(self.a)
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        print(self.a)
        if self.a[num]!=user:
            return False
        self.a[num]=-1
        return True

    def upgrade(self, num: int, user: int) -> bool:
        f1=0;f2=1
        if self.a[num]!=-1:
            return False
        for ke in self.d[num]:
            if self.a[ke]!=-1:
                self.a[ke]=-1
                f1=1
        cur=self.p[num]
        while cur!=-1:
            if self.a[cur]!=-1:
                f2=0
                break
            cur=self.p[cur]
        if f1==0 or f2==0:
            return False
        self.a[num]=user
        return True
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)


