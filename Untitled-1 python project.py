print("Welcome To SK Cafe")
print("Here is our menu card. What would you like to have?")

menu = {
    "Espresso": 60,
    "Cappuccino": 100,
    "Latte": 120,
    "Black Coffee": 50,
    "Green Tea": 40,
    "Cold Coffee": 130,
    "Hot Chocolate": 140,
    "Masala Chai": 30,
    "Veg Sandwich": 80,
    "Cheese Sandwich": 100,
    "Paneer Wrap": 120,
    "Veg Puff": 40,
    "French Fries": 70,
    "Brownie": 70,
    "Cheesecake Slice": 100,
    "Ice Cream (1 SCOOP)": 60
}

# Show menu
for item, price in menu.items():
    print(f"{item}: ₹{price}")

order = {}
while True:
    item = input("\nEnter item name (or type 'done' to finish): ").strip()
    if item.lower() == 'done':
        break
    if item in menu:
        try:
            qty = int(input(f"How many {item}? "))
            if item in order:
                order[item] += qty
            else:
                order[item] = qty
        except ValueError:
            print("Please enter a valid quantity.")
    else:
        print("Sorry, we don't have that item.")

# Billing
total = 0
print("\n--- BILL ---")
for item, qty in order.items():
    price = menu[item] * qty
    total += price
    print(f"{item} x {qty} = ₹{price}")
print(f"Total Amount: ₹{total}")
