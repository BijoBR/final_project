from xoperation import user_operation
class choice:
    def execute(self,choice,operation):
        if choice ==1:
            operation.registering()
        elif choice ==2:
            operation.login_user()
        elif choice==3:
            operation.login_admin()
        elif choice ==4:
            operation.place_order()
        elif choice==5:
            operation.order_history()
        elif choice==6:
            operation.update_profile()
        else:
            exit(1) 
obj =choice()
operation =user_operation()



while True:
    choice =int(input("Enter \n1 for registering \n2 forlogin \n3 for login_admin \n4 place order \n5 order history \n6 update profile \n7 Exit "))
    obj.execute(choice,operation)

# Admin login
# Email == "don123@gmail.com" and password =="abcd@"