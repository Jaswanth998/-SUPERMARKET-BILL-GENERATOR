# ------------------- SUPERMARKET BILL GENERATOR -------------------
from datetime import datetime

# Predefined items with price per unit
ITEMS = {
    'rice': 10,
    'sugar': 8,
    'oil': 30,
    'salt': 25,
    'paneer': 40,
    'maggie': 12,
    'boost': 200,
}

# Display available items
def show_items():
    print("\nAvailable Items:")
    print("-" * 40)
    print("Item".ljust(15), "Price")
    print("-" * 40)
    for item, price in ITEMS.items():
        unit = "kg" if item not in ['oil', 'maggie', 'boost'] else ("liter" if item == "oil" else "pack/bottle")
        print(f"{item.capitalize():<15} Rs {price}/{unit}")
    print("-" * 40)


# Generate final bill
def generate_bill(name, cart):
    if not cart:
        print("\nNo items purchased. Thank you for visiting!")
        return

    total = sum(qty * ITEMS[item] for item, qty in cart.items())
    tax = round(total * 0.12, 2)  # 12% tax
    final_amount = total + tax

    print("\n" + "=" * 25, "PYTHONLIFE SUPERMARKET", "=" * 25)
    print(" " * 28, "Hyderabad")
    print("Name:", name)
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 75)
    print(f"{'S.No':<6}{'Item':<15}{'Qty':<10}{'Price':<10}{'Total':<10}")
    print("-" * 75)

    for idx, (item, qty) in enumerate(cart.items(), start=1):
        price = ITEMS[item]
        total_price = price * qty
        print(f"{idx:<6}{item.capitalize():<15}{qty:<10}{price:<10}{total_price:<10}")

    print("-" * 75)
    print(f"{'Subtotal':<50} Rs {total}")
    print(f"{'Tax (12%)':<50} Rs {tax}")
    print("-" * 75)
    print(f"{'Final Amount':<50} Rs {final_amount}")
    print("-" * 75)
    print(" " * 25, "Thank You & Visit Again!")
    print("=" * 75)


# Main program
def supermarket():
    name = input("Enter your Name: ")
    cart = {}

    while True:
        print("\nOptions:")
        print("1. Show Items")
        print("2. Buy Items")
        print("3. Generate Bill & Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            show_items()

        elif choice == '2':
            show_items()
            item = input("Enter the item you want to buy: ").lower()
            if item in ITEMS:
                while True:
                    qty_input = input(f"Enter quantity for {item}: ")
                    if qty_input.isdigit() and int(qty_input) > 0:
                        qty = int(qty_input)
                        cart[item] = cart.get(item, 0) + qty
                        print(f"✔ Added {qty} {item}(s) to cart")
                        break
                    else:
                        print("Invalid quantity. Please enter a positive number.")
            else:
                print("❌ Item not available. Please select from the list.")

        elif choice == '3':
            generate_bill(name, cart)
            break

        else:
            print("❌ Invalid option. Please choose 1, 2, or 3.")



# Run the program
if __name__ == "__main__":
    supermarket()
