import random
from variablefile import food_app
class foodOperation:
    food_item_list =[]
    def add_item(self):
        print("add operation")
        foodId =random.randint(10000,20000)
        name =input("Enter the name: ")
        quantity =float(input("Enter the quatity: "))
        price =float(input("Enter the price: "))
        discount=float(input("Enyter the discount: "))
        stock =int(input("Enter the stck: "))
        obj_item =food_app(foodId,name,quantity,price,discount,stock,)
        foodOperation.food_item_list.append(obj_item)

        
    def edit_item(self):
        foodid =int(input("Enter the FooDId to be edited: "))
        for obj_item in foodOperation.food_item_list:
            if obj_item.get_foodId() == foodid:
                name =input("Enter the name: ")
                quantity =float(input("Enter the quatity: "))
                price =float(input("Enter the price: "))
                discount=float(input("Enyter the discount: "))
                stock =int(input("Enter the stck: "))
                
                obj_item.set_name(name)
                obj_item.set_quantity(quantity)
                obj_item.set_price(price)
                obj_item.set_stock(stock)
                obj_item.set_discount(discount)
        else:
            print("This foodid is not found")        

    def view_item(self):
         for i in foodOperation.food_item_list:
             print(i)
    def remove_item(self):
        foodid =int(input("Enter the FoodId to be removed: "))
        for obj_item in foodOperation.food_item_list:
            if obj_item.get_foodId() == foodid:
                foodOperation.food_item_list.remove(obj_item) 
            else:
                print("removed")    
        else:
            print("This FoodId is found and  removed")    


     






     