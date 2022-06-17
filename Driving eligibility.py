print("Driving eligibility criteria")
print("Enter your age")
L1=range(7,100,1)
L1=list(L1)
a= 18
b= int(input())
if b not in L1:
    print("Not valid")
elif b>a:
    print("You are eligible, go for a test:)")
elif b==a:
    print("You have to go through some physical checkup and then\ndriving test")
else :
    print("You are not eligible kid, Wait for some years:)")