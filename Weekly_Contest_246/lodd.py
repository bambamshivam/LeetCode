num=input()
c,i=1,len(num)-1
while i>=0:
	if int(num[i])%2!=0:
		c=0
		break
	i-=1
if c==0:
	print(num[:i+1])
