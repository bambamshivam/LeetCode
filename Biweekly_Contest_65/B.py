class Robot:

    def __init__(self, width: int, height: int):
        self.x=width
        self.y=height
        self.pos=[0,0]
        self.dir=0
        self.r=[[1,0],[0,1],[-1,0],[0,-1]]

    def move(self, num: int) -> None:
        k=num
        num=num%(2*self.x + 2*self.y -4)
        if num!=k:
            if self.pos[0]==0 and self.pos[1]==0:
                self.dir=3
            if self.pos[0]==self.x-1 and self.pos[1]==0:
                self.dir=0
            if self.pos[0]==0 and self.pos[1]==self.y-1:
                self.dir=2
            if self.pos[0]==self.x-1 and self.pos[1]==self.y-1:
                self.dir=1
        while num>0:
            if self.dir==0:
                k=self.x-self.pos[0]-1
                if num>=k:
                    self.pos[0]=self.x-1
                    if num>k:
                        self.dir=(self.dir+1)%4
                    num-=k
                else:
                    self.pos[0]+=num
                    num=0
            if self.dir==1:
                k=self.y-self.pos[1]-1
                if num>=k:
                    self.pos[1]=self.y-1
                    if num>k:
                        self.dir=(self.dir+1)%4
                    num-=k
                else:
                    self.pos[1]+=num
                    num=0
            if self.dir==2:
                k=self.pos[0]
                if num>=k:
                    self.pos[0]=0
                    if num>k:
                        self.dir=(self.dir+1)%4
                    num-=k
                else:
                    self.pos[0]-=num
                    num=0
            if self.dir==3:
                k=self.pos[1]
                if num>=k:
                    self.pos[1]=0
                    if num>k:
                        self.dir=(self.dir+1)%4
                    num-=k
                else:
                    self.pos[1]-=num
                    num=0
            
    def getPos(self):
        return self.pos

    def getDir(self) -> str:
        d={};d[0]="East";d[1]="North";d[2]="West";d[3]="South"
        return d[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()