g=int(input())
flag=0
for i in range (2,g-1):
	if g%i==0:
	 flag=1
	 break
if flag==0:
	  print("yes")
else:
	 print("no")
