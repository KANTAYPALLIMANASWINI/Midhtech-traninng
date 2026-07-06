#instead of if else finding max value
# a=10;
# b=7;
# c=89;
# result=max(a,b,c);
# print("max value is",result);



# a=9;
# b=7;
# c=8;
# if(a>b and a>c):
#     print(" a is max");
# elif(b>a and b>c):
#     print("b is max");
# else:
#     print("c is max");


# marks=int(input("enter your marks"));
# if(marks>=90):
#     print("grade is A");
# elif(marks>=70):
#     print("grade is B"); 
# elif(marks>=60):
#     print("grade is c");
# else:
#     print("need to improve") ;  
 
 


####nested if 
# age=int(input("enter your age"));
# citizen=False;
# if(age>=18):
#     if citizen:
#         print("eligible for vote")
#     else:
#         print("citizenship required");
# else:
#     print(" he must be 18 yrs old and a citizen");

   #simple calculator
a=float(input("enter  first number"));
b=float(input("enter  second number"));
operators=(input("choose operators(+,-,*,/)"));
if operators=="+":
    print(a+b);
elif operators=="-":
    print(a-b);
elif operators=="*":
    print(a*b);
elif operators=="/":
    if b!=0:
        print(a/b);
    else:
        print("Division by zero is not possible!");
else:
    print("Invalid Choice!");
