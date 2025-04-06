# Point of Sale (POS) System created for Best Buy Retail Store

# Predefined product list; the product's price is on the right and the stock is on the left
products = {
    "Rice": [100, 20], "White Bread": [350, 10], "Flour": [100, 20],
    "Cornflakes": [450, 15], "Sugar": [200, 20], "Brown Rice": [150,10],
    "Lasco": [650, 15], "Milk": [250, 15], "Cornbeef": [650, 10],
    "Mackerel": [350, 20],
}

#This represents the shopping cart
cart = {}

# This function will allow the items to be displayed
def view_products():
    print("Available products: ")
    for item, details in products.items():
      print(f"{item}: ${details[0]} JMD (Stock: {details[1]})")


# This function allows the user to add items to the cart
def add_item():
    item = input("Please enter the product's name: ").title()
# The .title string method changes the initial letter to uppercase and the the following characters to lowercase

    if item in products:
        quantity = input("Please enter the amount: ")
        if quantity.isdigit():
# The .isdigit method ensures that the input received is solely numbers, otherwise it would return a False

            quantity = int(quantity)
            if quantity <= products[item][1]:
                cart[item] = cart.get(item, 0) + quantity
                products[item][1] -= quantity
                print(f"You just added {quantity} {item}(s) to the cart.")
                print(f"There are {products[item][1]} {item}(s) left in stock.")

                #Low stock prompt
                if products[item][1] <= 5:
                    print("Low stock alert!")
                    print(f"Only {products[item][1]} {item}(s) left in stock.")

            else:
                print(f"Not enough {item} available in stock.")
                print(f"Only {products[item][1]} {item}(s) available.")
                print("Please select a smaller quantity")


        else:
            print("Invalid input. Please select a valid option from the menu. ")

    else:
        print("This product was not found.")
        print("Please try again. ")

# This function will allow the user to remove items from the cart
def remove_item():
    if not cart:
        print("Your cart is currently empty.")
        return

    print("Current Cart:", cart)
    item = input("Please enter the product's name that you wish to remove from the cart: ").title()

    if item in cart:
        quantity = int(input("Please enter the amount that you wish to remove from the cart: "))
        if quantity >= cart[item]:
            products[item][1] += cart[item]
            del cart[item]
        else:
            cart[item] -= quantity
            products[item][1] += quantity
        print(f"You just removed {quantity} {item}(s) from your cart.")
    else:
        print("This item was not found in your cart.")

# This allows the user to view the items in the cart
def view_cart():
    if not cart:
        print("Your cart is currently empty.")
        return
    print("Your Cart: ")
    total = 0
    for item, quantity in cart.items():
        price = products[item][0]
        print(f"{item}: {quantity} x ${price} = ${quantity * price}")
        total += quantity * price
    print(f"Subtotal: ${total} JMD")

# This function facilitates the checkout process
def checkout():
    if not cart:
        print("Your cart is currently empty.")
        return

    subtotal = sum(products[item][0] * quantity for item, quantity in cart.items())
    tax = subtotal * 0.10
    discount = 0

    if subtotal > 5000:
        discount = subtotal * 0.05
        print(f" 5% Discount Applied: -${discount:.2f}")
#The .2f method returns the value with two decimal places(eg. $100.50), unlike the float method alone

    total = subtotal + tax - discount
    print(f"Total: ${total:.2f} JMD (Tax Included)")

    while True:
        payment = input("Please enter the payment amount: ")
        if payment.replace(".", "").isdigit() and float(payment) >= total:
            change = float(payment) - total
            print(f" Your payment was successful! Your change is: ${change:.2f} JMD")
            print_receipt(subtotal, tax, discount, total, payment, change)
            cart.clear()
            break

        else:
            print(" Insufficeint funds.")
            print(f"${total} needed in order to complete your order ")


# Function that allows the user to print the receipt
def print_receipt(subtotal, tax, discount, total, payment, change):
    print(" Best Buy Retail Store ")
    print("_______________________")

    print("         RECEIPT       ")
    print("_______________________")
    for item, quantity in cart.items():
        print(f"{item}: {quantity} x ${products[item][0]} = ${products[item][0] * quantity}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Paid: ${payment}")
    print(f"Change: ${change:.2f}")

    print("  Thank you for shopping!  ")
    print("    Have a great day!  ")
    print("__________________________")

# This function will be the main menu displayed to the user
def main():
    while True:
        print(" Best Buy Retail Point of Sale System ")
        print("______________________________________")
        print("1. Add Item  2. View Products  3. Remove Item  4. View Cart  5. Checkout  6. Exit")
        print("___________________________________________________________________________________")
        choice = input("Please enter choice: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            view_products()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Exiting Best Buy Point Of Sale Program....")
            print("Have a great day!")
            break
        else:
            print(" Invalid input. Please select a valid choice from the menu.")

# Based on te function, this will check te script and allow the menu to be displayed
if __name__ == "__main__":
    main()

#I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT
