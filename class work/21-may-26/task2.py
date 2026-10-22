# =============================
# BILLING SOFTWARE IN PYTHON
# Mid-Level Console Project
# =============================

products = {
    101: {"name": "Laptop", "price": 55000},
    102: {"name": "Mouse", "price": 500},
    103: {"name": "Keyboard", "price": 1200},
    104: {"name": "Headphone", "price": 1500},
    105: {"name": "USB Cable", "price": 250}
}

cart = []


# -----------------------------
# Display Products
# -----------------------------
def show_products():
    print("\n========== PRODUCT LIST ==========")

    for pid, data in products.items():
        print(f"ID: {pid} | Name: {data['name']} | Price: ₹{data['price']}")


# -----------------------------
# Add Product To Cart
# -----------------------------
def add_to_cart():
    show_products()

    try:
        pid = int(input("\nEnter Product ID: "))

        if pid not in products:
            print("❌ Product Not Found")
            return

        qty = int(input("Enter Quantity: "))

        if qty <= 0:
            print("❌ Quantity must be greater than 0")
            return

        item_total = products[pid]["price"] * qty

        cart.append({
            "id": pid,
            "name": products[pid]["name"],
            "price": products[pid]["price"],
            "qty": qty,
            "total": item_total
        })

        print("✅ Item Added Successfully")

    except ValueError:
        print("❌ Invalid Input")


# -----------------------------
# View Cart
# -----------------------------
def view_cart():
    if len(cart) == 0:
        print("\n🛒 Cart is Empty")
        return

    print("\n========== CART ==========")

    grand_total = 0

    for item in cart:
        print(
            f"{item['name']} | ₹{item['price']} x {item['qty']} = ₹{item['total']}"
        )

        grand_total += item["total"]

    print("--------------------------------")
    print(f"Grand Total = ₹{grand_total}")


# -----------------------------
# Generate Bill
# -----------------------------
def generate_bill():
    if len(cart) == 0:
        print("\n❌ No Items In Cart")
        return

    print("\n")
    print("=" * 45)
    print("           FINAL BILL")
    print("=" * 45)

    grand_total = 0

    for item in cart:
        print(
            f"{item['name']:15} "
            f"{item['qty']} x ₹{item['price']} = ₹{item['total']}"
        )

        grand_total += item["total"]

    # GST Calculation
    gst = grand_total * 0.18
    final_amount = grand_total + gst

    print("-" * 45)
    print(f"Sub Total : ₹{grand_total}")
    print(f"GST (18%) : ₹{gst}")
    print(f"Final Bill: ₹{final_amount}")
    print("=" * 45)

    # Save Bill In File
    with open("billng.txt", "w") as file:
        file.write("========== FINAL BILL ==========\n")

        for item in cart:
            file.write(
                f"{item['name']} | "
                f"{item['qty']} x ₹{item['price']} = ₹{item['total']}\n"
            )

        file.write(f"\nSub Total : ₹{grand_total}")
        file.write(f"\nGST (18%) : ₹{gst}")
        file.write(f"\nFinal Bill: ₹{final_amount}")

    print("✅ Bill Saved In bill.txt")


# -----------------------------
# Main Program
# -----------------------------
while True:

    print("\n")
    print("========== BILLING SOFTWARE ==========")
    print("1. Show Products")
    print("2. Add To Cart")
    print("3. View Cart")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        generate_bill()

    elif choice == "5":
        print("✅ Thank You")
        break

    else:
        print("❌ Invalid Choice")
        