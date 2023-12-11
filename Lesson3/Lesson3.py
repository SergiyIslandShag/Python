
#a,b,c=1,2,3
#print(a,b,c)

#a=b=c=22
#print(a,b,c)

#d=111
#d=5

#login
#print(login)



#from pickle import FALSE


#print("1==1", 1==1) #True
#print("1==2", 1==2) #False
#print("1!=1", 1!=1) #False
#print("1!=2", 1!=1) #True
#print("1>1", 1>1)   #False
#print("1>2", 1>2)   #False
#print("1>2", 1>2)   #True
#print("1<1", 1<1)   #False
#print("1<2", 1<2)   #True
#print("1>=1", 1>=1) #False
#print("1>=2", 1>=2) #False
#print("1<=1", 1<=1) #True
#print(bool(""))
#print(bool(0.0))
#print(bool(0))
#print(bool(None))
#print(bool("Hello"))
#print(bool(2))

##and

#competent= True
#responsible=False
#print(competent and responsible)

##or
#print(competent or responsible)


##not
#print(not competent)


#age=int(input("Enter age:"))
#if age>=18 and age<=120:
#    print("Age is Ok")
#else:
#    print("Age is not valid")

#if 18<= age <=120:
#    print("Age is Ok")

#if age <=18:
#    print("Aqe is too small")

day = int(input("Enter number day of week [1-7]"))

if day ==1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("It is not a day of week")

login = input("Enter login:")
if login == "admin":
    password=input("Enter password")
    if password=="step":
        print("Welcome to the program")
    else :
        print("Password is invalid")
elif login =="exit":
    print("Goodbye")
else :
    print("Error login")
