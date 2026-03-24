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

def error_duplicate_data(user_input, available_categories, list_product_category):
    print(available_categories[user_input-1])
    print(list_product_category)

    if available_categories[user_input-1] in list_product_category:
        return("\n\033[1;31m" + "-"*60 + f"\nError: This data is already duplicated." + "\n" + "-"*60 + "\033[0m")
    
    return None

def confirm_exit(message="Press (n) to finish and any key to continue: "):
    """
    Function: confirm_exit

    Parameters:

    - message:
    Text message displayed to the user to decide whether to continue
    or exit a loop. By default, it prompts the user to press (n) to finish
    or any other key to continue.

    Description:
    This function displays a confirmation message that allows the user
    to either continue or terminate a loop (e.g., a while loop) based
    on their input.
    """

    user_option = input(f"\n\033[31m >> \033[0m{message}").strip().lower()
        
    if user_option == "n":
        return True     






def add_product(inventory, available_categories, title):

    product_history = {}

    act_add_product = True
    while act_add_product:
        title(f"Add Product N°{len(product_history)+1} - ID{len(inventory)+1}")

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
                if list_product_category:
                    print(f"\n{len(list_product_category)+1} categories added successfully.")
                    print(", ".join(list_product_category))
                    break

                print("\n\033[1;31m" + "-"*60 + f"\nError: You must select a category to classify the product." + "\n" + "-"*60 + "\033[0m")
                continue

            error = error_category_out_of_range(product_category, available_categories)
            if error:
                print(error)
                continue 

            error = error_duplicate_data(product_category, available_categories, list_product_category)
            if error:
                print(error)
                continue 

            list_product_category.append(available_categories[product_category-1]) 

        add_product_inventory(product_name,product_price,product_stock,list_product_category, inventory, product_history)

        # Ask user if they want to continue
        exit = confirm_exit()
        if exit == True:
            act_add_product = False
        else:
            continue

        print(inventory)

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
