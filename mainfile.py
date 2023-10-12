from operation import*
class choice:
    def execute (self,choice,opr):
        if choice==1:
            opr.add_item()
        elif choice ==2:
           opr.edit_item() 
        elif choice ==3:
            opr.view_item()
        elif choice==4:
            opr.remove_item()  
        else:
            exit(1)  
obj =choice()             
opr = foodOperation() 
while True:
    choice =int(input("Enter \n1.add_item \n2 edit_item \n3 view_item \n4 remove_item \n5 Exit "))
    obj.execute(choice,opr)
                   
