#first code
print("Hello, Python World")
a= "Yash here"
print(a)
x = 3  #int
y= 3.4 #float
z= 1j  #complex
print(type(x))
print(type(y))
print(type(z))
L = int(y)  
#you can't convert complex
M = float(x)
print(L)
print(M)
print("\n")
" " "next line tag ⊙﹏⊙ Sorry! I use it too much" " "
A= 20
B= 10
#remove every space even a single gap can create Identation error
N = (A + B)
print(N)
l=[1,2,3,0,5]
print(l[3]) #position wise 0,1,2,3,4
print('\n')
#the fourth position, if missing Index error
name = input('What is your name?\n')
print('Hello,%s!'% name)
H = input('How is life going?\n' )
print('Well n good:) Stay happy, %s!' %H)
print('\n') #input name..for including %name
 #input format need to be understood properly
#CALCULATOR COMPLETE 
# ^ MAKE IT SHORT AND SIMPLE
print("CALCULATOR" ,"\n\nSpecial case:- p stand for percentage In which first num. depict   TOTAL VALUE & second num. depict VALUE ")
a = float (input("first num. :"))
b = float(input("second num. :"))
c= input("what to do such as + - * /  // % ** p :")
if "+" in c:
     print(a+b)
elif "-" in c:
    print(a-b)
elif "*" in c:
     print(a*b)
elif "/" in c:
     print(a/b)
elif "//" in c:
     print(a//b)
elif "p" in c:
      print((b/a)*100, "%")
else :
        print(a**b)
#ADVANCE CALCULATOR
print("CALCULATOR" ,"\n\nSpecial case:- p stand for percentage In which first num. depict   TOTAL VALUE & second num. depict VALUE ")
a = input("first num. :")
b = input ("second num. :")
c= input ("what to do such as + - * /  // % ** p :")
if "+" in c:
     print(int(a) + int(b))
elif "-" in c:
    print(int(a) - int(b))  
elif "*" in c:
     print(int(a) * int(b))
elif "/" in c:
     print(int(a) / int(b))
elif "//" in c:
     print(int(a) // int(b))
elif "p" in c:
      print((int(b)/int(a))*100, "%")
else :
        print(int(a) ** int(b))
#COMPLETE        
#next level typing > ** <
abc = 5 
abc2 = '45' #mainly a string at this pt.
abc3 = 55.95
xyz = 5.0
abc4=int(abc2)
print(abc+abc4) # Output : 50 
print(abc+int(abc2)) # Output : 50 
print(float(abc)+xyz) 
# It will add 5.0 + 5.0 and will return 10.0
print(str(abc)+abc2)
print("\n")
" " " TWO STRINGS CAN ONLY ATTACHED BUT NEVER GET ADDED " " "
l1=[ ] #list
t1=( ) #tuple
d1={ } #dict
print(type(l1))
print(type(t1))
print(type(d1))
" " " LIFE ISN'T FAIR IF YOU ARE NOT MAKING YOUR HIGHEST EFFORT TO LIVE IT " " "
print("\n")
#DICTIONARY PROJECT
print("WELCOME TO THE DICTIONARY")
d1 = {"Abandon" :"to leave everything behind" , "Dogmatism" : "prespective treated as fact" ,"Stark" : "strong" ,"Yelling"
: "crying"}
d1["Conquer"]="to win"
d1["Pretending"]="to act fake"
del d1["Conquer"]
print("ENTER YOUR WORD")
L1=input()
print("HERE IS YOUR MEANING:)")
print(d1[L1])
print("\nTHANK YOU FOR USING DICTIONARY,Have you good day:)")
#COMPLETE DICTIONARY
print("\n")
#simple dictionary
abc = input("enter your word :")
print(d1[abc])
#you did a long code bro...that's easy
print("\n")
#DRIVING ELIGIBILITY CHECK
print("Driving eligibility criteria")
print("Enter your age")
L1=range(7,100,1) 
" " "1st no. belong to starting point, 2nd no. ending point and 3rd belong to the different between the range of 7 to 100.....means no gap" " "
L1=list(L1)
a= 18
b= int(input())
" " "if valid check, else for non valid which importantly not include any condition, elif...means if python reads the starting code and it's valid then it will automatically skip the others " " "
if b not in L1:
    print("Not valid")
elif b>a:
    print("You are eligible, go for a test:)")
elif b==a:
    print("You have to go through some physical checkup and then driving test")
else :
    print("You are not eligible kid, Wait for some years:)")

#COMPLETE CHECK
# String Functions:

demo = "Aakash is a good boy" 
print(demo.endswith("boy"))
print(demo.count('o'))
print(demo.capitalize())
print(demo.upper())
print(demo.lower())
print(demo.find("is"))
print(demo.replace("is","are"))
print ("\n")

# List Methods :
l1=[1,8,4,3,15,20,25,89,65]       #l1 is a list
print(l1)

l1.sort()
print(l1)    
" " " l1 after sorting(ascending order)" " "
l1.reverse()
print(l1)      #l1 after reversing all elements

#seq = list1[start_index:stop_index]
