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