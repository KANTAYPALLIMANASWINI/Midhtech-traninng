print("validation form");
name=input("enter your username:");
password=input("enter your password:");
special_characters=True;
if(len(password)<=8):
    if special_characters:
        print("password  is valid");
    else:
        print("password  need at least one special character");
     
else:
        print("invalid password");
