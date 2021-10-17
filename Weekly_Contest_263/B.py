class Bank:

    def __init__(self, balance):
        self.b=balance[:]

    def transfer(self, a1,a2,m) -> bool:
        n=len(self.b)
        if 1<=a1<=n and 1<=a2<=n and self.b[a1-1]>=m:
            self.b[a1-1]-=m
            self.b[a2-1]+=m
            return True
        return False
            

    def deposit(self,a,m) -> bool:
        if 1<=a<=len(self.b):
            self.b[a-1]+=m
            return True
        return False

    def withdraw(self, a,m) -> bool:
        if 1<=a<=len(self.b) and self.b[a-1]>=m:
            self.b[a-1]-=m
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)