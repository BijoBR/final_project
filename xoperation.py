from xuservariable import*
class user_operation:
    login_lst=[]
    ordered_lst =[]
    def registering(self):
        print("Login completed")
        name =input("Enter the name: ")
        phone_number =int(input("Enter the mobile number: "))
        email =input("Enter the Email Id: ")
        address =input("Enter the address: ")
        password=input("Enter the password: ")
        user_obj =user(name,phone_number,email,address,password)
        user_operation.login_lst.append(user_obj)
    def login_user (self):
        print("Login details")
        email=input("Enter the user name (email Id)")
        EnterPassword =input("Enter the password: ")
        for user_obj in user_operation.login_lst:
            if user_obj.get_email() == email and user_obj.get_password() == EnterPassword:
                print("User found and successfully loged in")
            else:
                print("User not found logedin failed")
                break
    def login_admin(self):
        print("Login through admin")
        Email =input("Enter the email Id: ").lower()
        password =input("Enter the passsword: ").lower()
        if Email == "don123@gmail.com" and password =="abcd@":
            print("Login sucessfully and details found")
        else:
            print("Login failed enter the correct login details: ")    
    def place_order(self):
        number_of_item=int(input("Enter the number of item to be ordered: "))
        for i in range(number_of_item):
            order =int(input("Enter \n1 for Tandoori Chicken (4 pieces) [INR 240] \n2 for Vegan Burger (1 Piece) [INR 320] \n3 for Truffle Cake (500gm) [INR 900] "))
            if order ==1:
                print("Tandoori Chicken (4 pieces) [INR 240]")
                user_operation.ordered_lst.append("Tandoori Chicken (4 pieces) [INR 240]")
            elif order==2:
                print("Vegan Burger (1 Piece) [INR 320]")
                user_operation.ordered_lst.append("Vegan Burger (1 Piece) [INR 320]")
            elif order ==3:
                print("Truffle Cake (500gm) [INR 900]")
                user_operation.ordered_lst.append("ruffle Cake (500gm) [INR 900] ")     
            else:
               print("Item is not available")
            for i in user_operation.ordered_lst:
               print("Your orders are :",i)
    
    def order_history(self):
        print("order history")
        for i in user_operation.ordered_lst:
            print("Your order history is: ",i)

    def update_profile(self):
        print("profile is updated")
        Enter_mobilnumber =int(input("Enter the applicant mobile to update the profile: "))
        for user_obj in user_operation.login_lst:
            if user_obj.get_phone_number() == Enter_mobilnumber:
                name =input("Enter the new name: ")
                email =input("Enter the new Email Id: ")
                address =input("Enter the new address: ")
                password=input("Enter the new password: ")

                user_obj.set_name(name)
                user_obj.set_email(email)
                user_obj.set_address(address)
                user_obj.set_password(password)
        else:
            print("Mobile number not found")        

