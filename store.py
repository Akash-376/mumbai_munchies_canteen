
def add_new_item(inventory,id, item, quantity, pricePeritem):
    if item in inventory:
        print("This item is already in inventory, you can update it")
    else:
        item_class = {"item_name": item, "quantity":quantity, "price":pricePeritem}
        availability = ""
        if int(quantity)==0:
            availability = "currently unavailable"
        elif int(quantity)<3:
            availability = "only "+ quantity+" left"
        else:
            availability = "available"
        
        item_class["availability"] = availability
        inventory[id] = item_class
        print("\nItem added successfully\n")




# print(inventory)

def remove_item_by_id(id):
    if id in inventory:
        inventory.__delitem__(id)
        print("\nitem deleted successfully\n")
    else:
        print("Invalid id")

def update_item_by_id(id):
    if id in inventory:
        inventory[id]["item_name"] = input("enter new name ")
        inventory[id]["quantity"] = int(input("enter new quantity "))
        inventory[id]["price"] = int(input("enter updated price "))

        print("\nitem updated successfully\n")
    else:
        print("Invalid id")


def purchase_item_by_id(id):
    if id in inventory:
        qtyToPurchase = int(input("Enter quantity to purchase "))
        if qtyToPurchase<= int(inventory[id]["quantity"]):
            inventory[id]["quantity"] = int(inventory[id]["quantity"])- qtyToPurchase

            # updating availability
            if int(inventory[id]["quantity"])==0:
                inventory[id]["availability"] = "currently unavailable"
            elif int(inventory[id]["quantity"]) < 3:
                inventory[id]["availability"] = "only "+ inventory[id]["quantity"]+ " quantity available"
            else:
                inventory[id]["availability"] = "Available"

            print("\npurchased successfully\n")
            sale = {
                    "item_name": inventory[id]["item_name"],
                    "quantity":qtyToPurchase,
                    "price":inventory[id]["price"]
                    }
            if id in salesRecord:
                salesRecord[id]["quantity"] = int(salesRecord[id]["quantity"]) + qtyToPurchase
            else:
                salesRecord[id] = sale
        elif inventory[id]["quantity"]==0:
            print("This item is temporaryly unavailable")
        else:
            print("only ", inventory[id]["quantity"], "items are available")
    else:
        print("Invalid id")


def view_item_list():
    if len(inventory)==0:
        print("\nNo any item in inventory\n")
    else:
        for key in inventory:
            print("item_id:", key,"item:", inventory[key]["item_name"],"price:",inventory[key]["price"], "Availability:",inventory[key]["availability"])


def view_sales():
    if len(salesRecord)==0:
        print("\nNo any item in inventory\n")
    else:
        for key in salesRecord:
            print("item_id:", key,"item:", salesRecord[key]["item_name"],"price:",salesRecord[key]["price"])

def view_item_list_withQuantity():
    if len(inventory)==0:
        print("No any item in inventory")
    else:
        for key in inventory:
            print("item_id:", key,"item:", inventory[key]["item_name"],"price:",inventory[key]["price"], "Quantity:",inventory[key]["quantity"])

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

inventory = {}
salesRecord = {}


while True:
    print(GREEN + "\nwelcome to Mumbai Munchies\n"+RESET)
    print("press 1 to admin login")
    print("press 2 to customer login")
    print(RED+"press 0 to exit\n"+RESET)

    choice = int(input())
    # for admin module
    if choice==1:
        user_name = input("Enter username : ")
        password = input("Enter password : ")

        if user_name== "admin" and password == "admin":
            print("\nwelcome admin\n")
            while True:
                print("Press 1 to add item")
                print("Press 2 to view all items")
                print("Press 3 to update item")
                print("Press 4 to remove item")
                print("Press 5 to view sales")
                print("Press 0 to exit\n")

                admin_choice = int(input())
                if admin_choice==1:
                    item = input("Enter item name ")
                    item_id = input("Enter item Id ")
                    quantity = input("Enter quantity ")
                    price = input("Enter price per item ")

                    add_new_item(inventory,item_id, item, quantity, price)
                elif admin_choice==2:
                    
                    view_item_list_withQuantity()
                    
                elif admin_choice==3:
                    id = int(input("enter item id : "))
                    update_item_by_id(id)
                elif admin_choice==4:
                    id = int(input("enter item id : "))
                    remove_item_by_id(id)
                elif admin_choice==5:
                    view_sales()
                elif admin_choice==0:
                    print("exiting from admin module")
                    break
                else:
                    print("Invalid choice. please try again...")
        else:
            print("Wrong credencials. please try again...")
    elif choice==2: # for customer module
        
        while True:

            print("\nWelcome to Mumbai Munchies")
            print("press 1 to view item list")
            print("press 2 to purchase item")
            print("press 0 to exit")

            customerChoice = int(input())

            if customerChoice==1:
                view_item_list()
                # break
            elif customerChoice==2:
                item_id = int(input("please enter item id to purchase : "))
                purchase_item_by_id(item_id)
                # break
            elif customerChoice==0:
                print("Exiting...")
                break
            else:
                print("Invalid choice. please try again... ")
    
    elif choice == 0:
        print("bye bye")
        break
    else:
        print("Invalid choice. please try again...")


