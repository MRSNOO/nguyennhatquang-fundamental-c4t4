import getpass
username=input("Username:")
if username !="c4e":
    print("You are not a superuser")
else:
    password=getpass.getpass("Password:")
    
    if password=="123":
        print("Welcome,c4e")
    else :
        print("Password is incorrect")



