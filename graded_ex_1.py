# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == 'asc':
        products_list.sort(key=lambda x: x[1])
    if sort_order == 'desc':
        products_list.sort(key=lambda x: x[1], reverse=True)
    display_products(products_list)
    return products_list


def display_products(products_list):
    print("The products available for selection are as follows:")
    index = 1
    for name, price in products_list:
        print(f"{index}. {name}: ${price}")
        index += 1


def display_categories():
    print("Please fill in the categories of product (select a number):")
    index = 0
    products_list = list(products.keys())
    for key in products_list:
        print(f"{index + 1}. {key}")
        index += 1
    categories = input()
    if categories.isdigit():
        num = int(categories)
        if 1 <= num <= len(products_list):
            return num - 1
    print("Invalid input")
    return None

def add_to_cart(cart, product, quantity):
     cart.append((product[0], product[1], quantity))
    

def display_cart(cart):
    total_cost = 0
    print("Your cart contains:")
    for item in cart:
        name, price, quantity = item
        cost = price * quantity
        total_cost += cost
        print(f"{name} - ${price} x {quantity} = ${cost}")
    print(f"Total cost: ${total_cost}")
    return total_cost


def generate_receipt(name, email, cart, total_cost, address):
    print("Receipt")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print("Items purchased:")
    for item in cart:
        name, price, quantity = item
        print(f"{name} - ${price} x {quantity}")
    print(f"Total Cost: ${total_cost}")


def validate_name(name):
    name_check = name.split()
    if len(name_check) == 2:
        if name_check[0].isalpha() and name_check[1].isalpha():
            if name_check[0].istitle() and name_check[1].istitle():
                return True
            else:
                print("Invalue input")
                print("Place try again!")
                return False
        else:
            print("Invalue input")
            print("Place try again!")
            return False
    else:
        print("Invalue input")
        print("Place try again!")
        return False

def validate_email(email):
    for x in email:
        if x == '@':
            return True
        if x == len(email):
            print("Invalue input")
            print("Place try again!")
            return False


def main():
    print("Place enter your name:")
    name = input()
    validate_name(name)
    print("Place enter your email:")
    email = input()
    validate_email(email)
    cart = []
    flag = True
    while flag:
        num = display_categories()
        products_list = list(products.keys())
        products_list = products[products_list[num]]
        display_products(products_list)
        print("Please choose your next action:")
        print("1.Add to cart")
        print("2.Sort by price")
        print("3.Return to last selection")
        print("4.Complete shopping")
        choice_number = int(input())
        if choice_number == 1:
            print("Please fill in the desired product:(select a number)")
            product_index = int(input())
            product = products_list[product_index - 1]
            print("Please fill in the quantity of products needed:")
            quantity = int(input())
            add_to_cart(cart,product,quantity)
        if choice_number == 2:
            print("1.Ascending order")
            print("2.Descending order")
            sort_order_num = int(input())
            if sort_order_num == 1:
                sort_order = 'asc'
            if sort_order_num == 2:
                sort_order = 'desc'
            display_sorted_products(products_list,sort_order)
        if choice_number == 3:
            print()
        if choice_number == 4:
            if len(cart) > 0:
                total_cost = display_cart(cart)
                print("Place enter your address")
                address = input()
                generate_receipt(name, email, cart, total_cost, address)
                flag = False
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day")
                flag = False

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()