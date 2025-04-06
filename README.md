Best Buy Retail Point Of Sale System

Python


Description

This is a simple Point of Sale (POS) system that was created to allow the user to do the following functions: 

1. Add items to the cart
2. View all products
3. Remove items from the cart
4. View the cart
5. Checkout
6. Exit the system


Features

This python program was created for Best Buy Retail's point of sale system, and it contains the following features:

1. Product Management – It stores the product's name, and its respective price and quantity.  
2. Shopping Cart Operations– It allows the user to add, remove, and view items in the cart.  
3. Checkout & Payment Processing – Calculates subtotal, tax (10%), and validates payment.  
4. Discount System– 5% discount for any purchase over five thousand dollars ($5000).  
5. Low-Stock Alerts – Alerts are given to the user when the stock is below five (5).  
6. Receipt Generation – Formats a receipt for the customer after the transaction is completed.  
7. Multiple Transactions – Allows multiple purchases within a single session until the user opts to exit the program.
8. Input Validation – Prevents incorrect inputs and ensures smooth operation.


Requirements To Use Program

1. Python 
2. Google Colab


Usage

Firstly, run the script using Python or Google Colab. The user will then receive an on screen prompt which allows the user to input data based on the criteria(prompt). The user will be presented a menu with a list of options. Based on the function that the user may want to carry out, they should select the choice given accordingly. The user is urged to follow the instructions on the screen in order to maximise the program's efficiency and to avoid any possible errors.


Program Functionalities

1. Product Management:  The program maintains a product catalog with ten (10) predefined products. It checks stock availability before adding the items to the cart.


2. Shopping Cart Operations:  

- Add Item: Allows the user to enter the product name and quantity.  
- Remove Item:  Allows the user to remove a specific quantity or the entire product from the cart.  
- View Cart: See all selected items with their price and quantity.


3. Checkout & Payment Validation:

- Subtotal Calculation: Adds up all item costs.  
- Sales Tax (10%): Applied to the subtotal.  
- Discounts (5%): Applied if the total cost of items is over $5000 
- Payment Validation: Ensures customers cannot pay less than the total amount stipulated.  
- Change Calculation: Returns the correct amount of change after payment.


4. Receipt Generation: Displays formatted receipt including the store's name, list of purchased items, subtotal, tax, discount(if qualified), total amount due, payment received and change returned.


Possible Modification

- The user can modify the product catalog by adding or changing it from within the products seen in the dictionary.
- The sales tax and discount values can be adjusted in the checkout function.

Issues & Debugging

- The program is menu-driven and text-based. Which means it can only accept valid input based on the instructions prompted in the program. The user must enter valid inputs in order to proceed to the next step in the program.  
- If the product's name is not spelled correctly, the program will not recognize it as an available product. Displaying a message saying this product was not found.
- The program does not store any user information or transaction history.

Possible Future Improvements

- Implement a graphical user interface (GUI) - This would allow the user to interact with the screen using icons, eg. Menu icon.
- Add a database that would be able to store the transaction history
- Implement user authentication, that way only authorized users can access the program.
