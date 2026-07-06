#airthmetic operators
t=int(input("enter telugu marks"));
h=int(input("enter hindi marks"));
e=int(input("enter english  marks"));
m=int(input("enter maths marks"));
sc=int(input("enter science marks"));
so=int(input("enter social marks"));
total=t+h+e+m+sc+so;
percentage=(total/600)*100;
print("total marks is", total);
print("percentage is", percentage);

#assignment operators
a=10;
a+=5;
b=4;
b-=2;
b*=2;
print(a,b);


#comparision operators
x=10;
y=20;
print(x<y);

age=18;
if (age>=18):
    print("eligible for vote");
else:
    print("not eligible");
