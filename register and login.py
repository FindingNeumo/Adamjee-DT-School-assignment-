insert_user=input("Please Choose Your Username: ")
print("Hello!", insert_user)
insert_pass=input("Please Enter Your Password: ")
print("Thank You")
print("Successfully Created Account")
u_login_q=input("Would you like to login?(Y/N): ")
if u_login_q =='Y' or 'y':
    username=input("Please Enter Your Username: ")
    user_checker=(insert_user in username)
    if user_checker ==True:
        password=input("Please Enter Your Password: ")
        pass_checker=(insert_pass in password)
        if pass_checker==True:
            print("Login Successful")
            print("Welcome", insert_user,"!")
            news=input("Would You Like To Check The News?(Y/N) ")
            if news == 'Y' or 'y':
                print("NEWS!!!!!!!!!!!!!!!!")
                print("MRBEAST WILL RESPOND SOON")
                print("A Fellow Creator Named Ludwig Who Is A Friend of Mrbeast")
                print("Called Him And Asked when he will Be respond. Mrbeast")
                print("Replied Said He Is Waiting For All The Accusations To be")
                print("Said Before he Makes a Statement Of ALL OF THEM in one ")
                print("Video. Thats The News Please Come Back SOON FOR MORE NEWWWWWWWWS")
                print("Logged Out!")
            else:
                print("Okay man")
                print("LOGGED OUT")
            
            
        else:
            print("Password Not Correct! u hax!")
    else:
        print("That User Doesn't Exist!")
        
else:
    print("okay then")
    