typeofpizza=[]
typeoftopping=[]
size=[]
crust=[]
sauce=[]
side=[]
desert=[]
drink=[]

typeofpizza.append("Meat Overload")
typeofpizza.append("Cheese Lava (Veg)")
typeofpizza.append("Cheese Lava (Non-Veg)")
typeofpizza.append("Non-Veg Supreme")
typeofpizza.append("Farm House")
typeofpizza.append("Chicken Keema")
typeofpizza.append("Cheese Volcano (Veg)")
typeofpizza.append("Cheese Volcano (Non-Veg)")
typeofpizza.append("Paneer Tikka")
typeofpizza.append("Fiery Chicken")
typeofpizza.append("Spicy Vegies")

typeoftopping.append("Peperoni")
typeoftopping.append("Jalapenos")
typeoftopping.append("Chicken")
typeoftopping.append("Bacon")
typeoftopping.append("Sausage")
typeoftopping.append("Capscicum")
typeoftopping.append("Extra Cheese")
typeoftopping.append("Paneer")
typeoftopping.append("Mushroom")
typeoftopping.append("Spam")
typeoftopping.append("Caramalized Onion")
typeoftopping.append("Olives")
typeoftopping.append("Pineapple")
typeoftopping.append("Basil")
typeoftopping.append("Mozzarella")

size.append("Small")
size.append("Medium")
size.append("Large")
size.append("Family")
size.append("Party")

crust.append("Thin")
crust.append("Extra Thin")
crust.append("Medium Crust")
crust.append("Pan")

sauce.append("Tomato Sauce")
sauce.append("Mayonese")
sauce.append("Olive Oil")
sauce.append("Shezwan Sauce")
sauce.append("Mint Chutney")
sauce.append("Tamarind Chutney")

side.append("Garlic Bread")
side.append("Meat Balls")
side.append("Chicken Wings")
side.append("Mac & Cheese")
side.append("Nachos & Cheese")
side.append("Chicken Party Box")
side.append("Chicken Popcorn")
side.append("Pizza Burger")

desert.append("Cheese Cake")
desert.append("Tiramisu")
desert.append("Blueberry Cheese Cake")
desert.append("Cup Cakes")

drink.append("Coke")
drink.append("Pepsi")
drink.append("Orange Juice")
drink.append("Water")
drink.append("Thumbs Up")
drink.append("Sparkling Water")
drink.append("Beer")

price_list={
    "Meat Overload":160,
    "Cheese Lava (Veg)":90,
    "Cheese Lava (Non-Veg)":130,
    "Non-Veg Supreme":200,
    "Farm House":170,
    "Chicken Keema":120,
    "Cheese Volcano (Veg)":100,
    "Cheese Volcano (Non-Veg)":150,
    "Paneer Tikka":90,
    "Fiery Chicken":99,
    "Spicy Vegies":60,
    "Peperoni":20,
    "Jalapenos":10,
    "Chicken":30,
    "Bacon":40,
    "Sausage":20,
    "Capscicum":10,
    "Extra Cheese":15,
    "Paneer":35,
    "Spam":30,
    "Caramalized Onion":15,
    "Olives":20,
    "Pineapple":10,
    "Basil":5,
    "Mozzarella":20,
    "Small":250,
    "Medium":400,
    "Large":650,
    "Family":1000,
    "Party":1700,
    "Thin":30,
    "Extra Thin":25,
    "Medium Crust":0,
    "Pan":40,
    "Tomato Sauce":3,
    "Mayonese":5,
    "Olive Oil":6,
    "Shezwan Sauce":8,
    "Mint Chutney":5,
    "Tamarind Chutney":5,
    "Garlic Bread":175,
    "Meat Balls":230,
    "Chicken Wings":99,
    "Mac & Cheese":199,
    "Nachos & Cheese":120,
    "Chicken Party Box":450,
    "Chicken Popcorn":70,
    "Pizza Burger":250,
    "Cheese Cake":100,
    "Tiramisu":105,
    "Blueberry Cheese Cake":115,
    "Cup Cakes":99,
    "Coke":20,
    "Pepsi":20,
    "Orange Juice":40,
    "Water":10,
    "Thumbs Up":20,
    "Sparkling Water":80,
    "Beer":199
}
while(True):
    
    print(f"Hello There!!\nWelcome To Our Restraunt\n\nPlease Feel Free To Order Anything From Our Restraunt\n\nOur Available Pizzas:{typeofpizza}")
    order_pizza=input("Enter Which Type Of Pizza You Want:")
    while order_pizza not in typeofpizza:
                
        print(f"\n\nSorry But We Don't Have Your Preferred Pizza Availble!!\n\nWould You Like To Have One Of Our Available Pizzas?:{typeofpizza}")
        order_pizza=input("Which Pizza You Will Prefer?:")
        
    print(f"\nWhat Toppings Would You Like?:{typeoftopping}")
    order_topping=input("My Preference:")
    while order_topping not in typeoftopping:
                print(f"\n\nSorry But We Don't Have Your Preferred Topping Availble!!\n\nWould You Like To Have One Of Our Available Toppings?:{typeoftopping}")
                order_topping=input("Which Topping You Would Like To Add?:")
                
    print(f"\nWhat Size You Want Your Pizza To Be?:{size}")
    order_size=input("My Preference:")
    while order_size not in size:
                
        print(f"\n\nSorry But We Don't Have Your Preferred Size Availble!!\n\nWould You Like To Have One Of Our Available Sizes?:{size}")
        order_size=input("What Size You Will Prefer?:")
    
    print(f"\nWhat Crust You Will Prefer?:{crust}")
    order_crust=input("My Preference:")
    while order_crust not in crust:
                
        print(f"\n\nSorry But We Don't Have Your Preferred Crust Availble!!\n\nWould You Like To Have One Of Our Available Crusts?:{crust}")
        order_crust=input("Which Crust You Will Prefer?:")
    
    print(f"\nWhat Additional Sauce You Want To Add?:{sauce}")
    order_sauce=input("My Preference:")
    while order_sauce not in sauce:
                
        print(f"\n\nSorry But We Don't Have Your Preferred Sauce Availble!!\n\nWould You Like To Have One Of Our Available Sauces?:{sauce}")
        order_sauce=input("Which Sauce You Will Prefer?:")
    
    print(f"\nWhat You Want For Your Sides?:{side}")
    order_side=input("My Preference:")
    while order_side not in side:
                
        print(f"\n\nSorry But We Don't Have Your Preferred Side Availble!!\n\nWould You Like To Have One Of Our Available Sides?:{side}")
        order_side=input("Which Side You Will Prefer?:")
    
    print(f"\nWhat Desert You Would Like?:{desert}")
    order_desert=input("My Preference:")
    while order_desert not in desert:
                
        print(f"\n\nSorry But We Don't Have Your Preferred Desert Availble!!\n\nWould You Like To Have One Of Our Available Deserts?:{desert}")
        order_desert=input("Which Desert You Will Prefer?:")
    
    print(f"\nWhat Drink You Would Prefer?:{drink}")
    order_drink=input("My Preference:")
    while order_drink not in drink:
                
        print(f"\n\nSorry But We Don't Have Your Preferred Drink Availble!!\n\nWould You Like To Have One Of Our Available Drinks?:{drink}")
        order_drink=input("Which Drink You Will Prefer?:")
    
            
    print(f"\n\n1x {order_size} {order_crust} Crust {order_pizza} Pizza with {order_topping} with Extra {order_sauce}  --  ₹{price_list[order_size]+price_list[order_crust]+price_list[order_pizza]+price_list[order_topping]+price_list[order_sauce]}\n1x {order_side}  --  ₹{price_list[order_side]}\n1x {order_desert}  --  ₹{price_list[order_desert]}\n1x Chilled {order_drink}  --  ₹{price_list[order_drink]}")
        
    total=price_list[order_size]+price_list[order_crust]+price_list[order_pizza]+price_list[order_topping]+price_list[order_sauce]+price_list[order_side]+price_list[order_desert]+price_list[order_drink]
        
    print(f"\nYour TotalBill Is: ₹{total}")
    ans=input("\n\nWould You Like to Have Anything Else?:")
    a=ans.lower()
    if a=="no":
        break
    print("\n\n\n") 