s,f=input().split()
a1=list(map(int,s.split(":")))
ms=a1[0]*60 + a1[1]
a2=list(map(int,f.split(":")))
mf=a2[0]*60 + a2[1]
mf1=mf
ms1=ms
if mf%15!=0:
	mf=(mf//15)*15
if ms%15!=0:
	ms=(ms//15 + 1)*15
if mf1>=ms1 and ms>=mf:
	print(0)
elif mf1>ms1 and mf>=ms:
	print((mf-ms)//15)
else:
	print((mf+(24*60 - ms))//15)


