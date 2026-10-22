#BILLING SOFTWERE

products={

    101:{"name":"leptop","price":60000},
    102:{"name":"phone","price":30000},
    103:{"name":"Headphone","price":4500},
    104:{"name":"usb cable","price":300}
}
cart=[]

def show_item():
    for pid,data in products.items():
        print(f"ID:{pid}|name:{data["name"]}|Price:{data["price"]}")

def add_to_card():
    show_item()
    try:

        pid=int(input("\n Enter product id:"))

        if pid not in products:
            print("products not found!!!")
        
        qty=int(input("\nEnter Product Quantity:"))

        if qty<=0:
            print("Quantity must be greater than 0 !!!")
        
        total_tiem=products[pid]["price"]*qty

        cart.append({
            "ID":pid,
            "name":products[pid]["name"],
            "price":products[pid]["price"],
            "qty":qty,
            "total":total_tiem
        })
        print("Item Add Successfuly!!!")
    
    except ValueError:
        print("Ivalid Input!!!!")

def view_cart():
    if len(cart)==0:
        print("\nCart is Empty")
        return
    grand_total=0
    print("\n======== CART ========")

    for item in cart:
        print(f"{item["name"]}|{item["price"]} x {item["qty"]}={item["total"]}")

    grand_total+=item["total"]

    print("----------------------------------")

    print("GRAND TOTAL=",grand_total)
def generate_bill():
    if len(cart) == 0:
        print("\n❌ No Items In Cart")
        return
    print("\n")
    print("="*45)
    print("     FINAL BILL")
    print("="*45)

    grand_total=0
    


    
     
while True:
    print("\n<----mainu----->\n")
    print("1. Show Products")
    print("2. Add To Cart")
    print("3. View Cart")
    print("4. Generate Bill")
    print("5. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
       show_item()
    elif choice==2:
        add_to_card()
    elif choice==3:
        view_cart()
        

        
       

                
            

