def error_empty_field(user_input):

    if str(user_input).strip() == "":
        return ("\n\033[1;31m" + "-"*60 + f"\nError: This field cannot be empty." + "\n" + "-"*60 + "\033[0m")
    
    return None

def error_negative_value(user_input):

    if user_input <= 0:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: Negative numbers or zero are not allowed." + "\n" + "-"*60 + "\033[0m")
    
    return None

def error_category_out_of_range(user_input, inventory_list):

    if user_input < 1 and user_input > len(inventory_list):
        return ("\n\033[1;31m" + "-"*60 + f"\nError: The option must be between 1 and {len(inventory_list)}." + "\n" + "-"*60 + "\033[0m")
    
    return None

def display_inventory_list(inventory_list):

    for enumeration , record  in enumerate(inventory_list):
        print(f"{enumeration+1}. {record}")












def add_product(inventory, available_categories, title):
    product_history = {}

    while True:

        product_name = input("\n\033[34m >> \033[0mPlease enter the product name: ")

        error = error_empty_field(product_name)
        if error:
            print(error)
            continue 

        break

    while True:

        try:
            product_price = float(input("\n\033[34m >> \033[0mPlease enter the product price: "))
            
        except ValueError:
            print("\n\033[1;31m" + "-"*60 + f"\nError: Please enter numbers only in this field." + "\n" + "-"*60 + "\033[0m")
            continue

        error = error_empty_field(product_price)
        if error:
            print(error)
            continue 

        error = error_negative_value(product_price)
        if error:
            print(error)
            continue 

        break
        
    while True:

        try:
            product_stock = int(input("\n\033[34m >> \033[0mPlease enter the product stock quantity: "))
            
        except ValueError:
            print("\n\033[1;31m" + "-"*60 + f"\nError: Please enter numbers only in this field." + "\n" + "-"*60 + "\033[0m")
            continue

        error = error_empty_field(product_stock)
        if error:
            print(error)
            continue

        error = error_negative_value(product_stock)
        if error:
            print(error)
            continue 

        break   


    list_product_category = []
    title("List Category")

    display_inventory_list(available_categories)
    print("\033[34m-"*60)
    print("\n\033[31mEnter '0' to finish.\033[0m")
        
    while True:

        try:
            product_category = int(input(f"\n\033[34m >> \033[0mPlease select a category option for the product N°{len(list_product_category)+1}: "))
        except ValueError:
            print("\n\033[1;31m" + "-"*60 + f"\nError: Please enter numbers only in this field." + "\n" + "-"*60 + "\033[0m")
            continue

        error = error_empty_field(product_category)
        if error:
            print(error)
            continue 

        if product_category == 0:
            if not list_product_category == False:
                print("q")
                break

        error = error_category_out_of_range(product_category, available_categories)
        if error:
            print(error)
            continue 

        list_product_category.append(available_categories[product_category-1]) 

    add_product_inventory(product_name,product_price,product_stock,list_product_category, inventory, product_history)

    print(product_history)

def add_product_inventory(product_name, product_price, product_stock, product_category, inventory, history):

    auto_id = len(inventory) + 1

    inventory[auto_id] = {
        "name" : product_name,
        "price" : product_stock,
        "stock" : product_price,
        "category" : product_category,
        "status" : True
    }

    history[auto_id] = {
        "name" : product_name,
        "price" : product_stock,
        "stock" : product_price,
        "category" : product_category,
        "status" : True
    }

    print(inventory)

def edit_product(inventory):
    # EN: Edits an existing product in the inventory
    # ES: Edita un producto existente en el inventario
    pass


def delete_product(inventory):
    # EN: Removes a product from the inventory
    # ES: Elimina un producto del inventario
    pass


def search_product(inventory):
    # EN: Searches for a product in the inventory
    # ES: Busca un producto en el inventario
    pass
