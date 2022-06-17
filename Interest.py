x=int(input("Enter first number : "))
opr=int(input("1)Addition \n2)Substraction \n3)Multiplication \n4)Division\nSelect the operator :"))
y=int(input("Enter the second number :"))
if x==45 and opr==3 and y==3:
	print("555")
elif x==56 and opr==1 and y==9:
	print("77")
elif x==56 and opr==4 and y==6:
	print("4")
else:
	if opr==1:
		print(x+y)
	elif opr==2:
		print(x-y)
	elif opr==3:
		print(x*y)
	else :
		print(x/y)