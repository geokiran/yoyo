f=int(input())
t=f
temp=0
while t!=0:
	temp=temp*10+t%10
	t=t//10
if f==temp:
	print("yes")
else:
    print("no")
