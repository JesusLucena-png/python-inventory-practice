import csv
import os

def cargar_csv(file_path="inventario.csv"): 
    # EN: Loads inventory data from a CSV file and converts it into a dictionary
    inventory = {}

    try:
        # EN: Open the CSV file in read mode
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # EN: Iterate through each row in the CSV
            for row in reader:
                product_id = int(row["id"])  # EN: Convert ID to integer

                # EN: Store each product in the inventory dictionary
                inventory[product_id] = {
                    "name": row["name"],
                    "price": float(row["price"]),  # EN: Convert price to float
                    "stock": int(row["stock"]),    # EN: Convert stock to integer
                    "category": row["category"].split("|"),  # EN: Convert string to list
                    "status": row["status"] == "True"  # EN: Convert string to boolean
                }

    except FileNotFoundError:
        # EN: If file does not exist, notify user
        print("\n\033[1;33mCSV file not found. A new one will be created.\033[0m")

    except Exception as e:
        # EN: Catch any unexpected error
        print(f"\n\033[1;31mError loading CSV: {e}\033[0m")

    return inventory


def guardar_producto_csv(product_data, file_path="inventario.csv"):
    """
    EN: Saves a single product to the CSV file without deleting existing data.
    """

    # EN: Check if the file already exists
    file_exists = os.path.isfile(file_path)

    try:
        # EN: Open file in append mode
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # EN: Write header only if file does not exist
            if not file_exists:
                writer.writerow(["id", "nombre", "precio", "stock", "categoria"])

            # EN: Convert category list to string
            categorias = ", ".join(product_data["category"])

            # EN: Write product data row
            writer.writerow([
                product_data["id"],
                product_data["name"],
                product_data["price"],
                product_data["stock"],
                categorias
            ])

    except Exception as e:
        # EN: Handle any writing error
        print(f"\n\033[1;31mError saving CSV: {e}\033[0m")


def actualizar_csv(inventory, file_path):
    # EN: Rewrites the entire CSV file with the current inventory data

    try:
        # EN: Open file in write mode (overwrite)
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # EN: Write header
            writer.writerow(["id", "name", "price", "stock", "category", "status"])

            # EN: Iterate through inventory and write each product
            for product_id, data in inventory.items():

                writer.writerow([
                    product_id,
                    data["name"],
                    data["price"],
                    data["stock"],
                    "|".join(data["category"]),  # EN: Convert list to string
                    data["status"]
                ])

        print(f"\n\033[1;32mCSV successfully updated.\033[0m")

    except Exception as e:
        # EN: Handle any writing error
        print(f"\n\033[1;31mError updating CSV: {e}\033[0m")

def error_empty_field(user_input):

    if str(user_input).strip() == "":
        return ("\n\033[1;31m" + "-"*100 + f"\nError: This field cannot be empty." + "\n" + "-"*100 + "\033[0m")
    
    return None

def error_negative_value(user_input,num):

    if user_input < num:
        return ("\n\033[1;31m" + "-"*100 + f"\nError: Negative numbers or zero are not allowed." + "\n" + "-"*100 + "\033[0m")
    
    return None

def error_category_out_of_range(user_input, inventory_list):

    if user_input < 1 or user_input > len(inventory_list):
        return ("\n\033[1;31m" + "-"*100 + f"\nError: The option must be between 1 and {len(inventory_list)}." + "\n" + "-"*100 + "\033[0m")
    
    return None

def display_inventory_list(inventory_list):

    for enumeration , record  in enumerate(inventory_list):
        print(f"{enumeration+1}. {record}")

def error_duplicate_data(user_input, available_categories, list_product_category):

    if available_categories[user_input-1] in list_product_category:
        return("\n\033[1;31m" + "-"*100 + f"\nError: This data is already duplicated." + "\n" + "-"*100 + "\033[0m")
    
    return None

def confirm_exit(message="Press (n) to finish and any key to continue: "):

    user_option = input(f"\n\033[1;31m >> \033[0m{message}").strip().lower()
        
    if user_option == "n":
        return True     

def menu():

    print("""
\033[1;34m 1. \033[0mEdit Name
\033[1;34m 2. \033[0mEdit Price
\033[1;34m 3. \033[0mEdit Category
\033[1;34m 4. \033[0mEdit Stock
          
\033[1;31m 5. \033[0mExit""")

def add_product(inventory, available_categories, title):

    # Dictionary to store created products history
    product_history = {}

    # Control variable for main loop
    is_adding_product = True
    while is_adding_product:

        # Show dynamic title with product number and ID
        title(f"Add Product N°{len(product_history)+1} - ID {len(inventory)+1}")

        # ===== PRODUCT NAME =====
        while True:
            product_name = input("\n\033[34m >> \033[0mPlease enter the product name: ").capitalize()

            # Validate empty input
            error = error_empty_field(product_name)
            if error:
                print(error)
                continue 

            break

        print("\n" + "\033[1;34m-\033[0m" * 100)

        # ===== PRODUCT PRICE =====
        while True:
            try:
                product_price = float(input("\n\033[34m >> \033[0mPlease enter the product price: "))
            except ValueError:
                # Handle non-numeric input
                print("\n\033[1;31m" + "-" * 100 + f"\nError: Please enter numbers only in this field." + "\n" + "-" * 100 + "\033[0m")
                continue

            # Validate empty input
            error = error_empty_field(product_price)
            if error:
                print(error)
                continue 

            # Validate minimum value
            error = error_negative_value(product_price, 0.01)
            if error:
                print(error)
                continue 

            break

        print("\n" + "\033[1;34m-\033[0m" * 100)
            
        # ===== PRODUCT STOCK =====
        while True:
            try:
                product_stock = int(input("\n\033[34m >> \033[0mPlease enter the product stock quantity: "))
            except ValueError:
                # Handle non-numeric input
                print("\n\033[1;31m" + "-" * 100 + f"\nError: Please enter numbers only in this field." + "\n" + "-" * 100 + "\033[0m")
                continue

            # Validate empty input
            error = error_empty_field(product_stock)
            if error:
                print(error)
                continue

            # Validate minimum value
            error = error_negative_value(product_stock, 0)
            if error:
                print(error)
                continue 

            break   

        # ===== PRODUCT CATEGORY =====
        selected_categories = []

        title("List Category")

        # Display available categories
        display_inventory_list(available_categories)

        print("\n" + "\033[1;34m-\033[0m" * 100)

        print("\033[1;31m" + "-" * 100 + f"\n{'Enter [ 0 ] to finish.':^100}" + "\n" + "-" * 100 + "\033[0m")
            
        while True:
            try:
                category_option = int(input(f"\n\033[34m >> \033[0mPlease select a category option for the product N°{len(selected_categories)+1}: "))
            except ValueError:
                # Handle non-numeric input
                print("\n\033[1;31m" + "-" * 100 + f"\nError: Please enter numbers only in this field." + "\n" + "-" * 100 + "\033[0m")
                continue

            # Validate empty input
            error = error_empty_field(category_option)
            if error:
                print(error)
                continue 

            print("\n" + "\033[1;34m-\033[0m" * 100)

            # Finish category selection
            if category_option == 0:
                if selected_categories:
                    print(f"\n\033[34m >> \033[0m{len(selected_categories)} categories added successfully.")
                    print(" - ".join(selected_categories))
                    break
                else:
                    print("\n\033[1;31m" + "-" * 100 + f"\nError: You must select a category to classify the product." + "\n" + "-" * 100 + "\033[0m")
                    continue

            # Validate range
            error = error_category_out_of_range(category_option, available_categories)
            if error:
                print(error)
                continue 

            # Validate duplicates
            error = error_duplicate_data(category_option, available_categories, selected_categories)
            if error:
                print(error)
                continue 

            # Add selected category
            selected_categories.append(available_categories[category_option - 1]) 

        # Add product to inventory and history
        add_product_inventory(product_name, product_price, product_stock, selected_categories, inventory, product_history)

        print("\n" + "\033[1;34m-\033[0m" * 100)

        # Ask user if they want to continue adding products
        exit_flag = confirm_exit()
        if exit_flag == True:
            is_adding_product = False
        else:
            continue

        # ===== PRODUCTS CREATION HISTORY =====

        print("\n" + "\033[1;34m" + "-" * 100)
        print("PRODUCTS CREATION HISTORY")
        print("-" * 100)
        print(f"{'ID':^5}| {'NAME':<20}| {'CATEGORY':<50}|{'STOCK':^10}|{'PRICE':^10}")
        print("-" * 100 + "\033[0m")

        # Display created products
        for product_id, product_data in product_history.items():
            categories = ", ".join(product_data['category'])
            print(
                f"\033[1;0m{product_id:^5}| {product_data['name']:<20}| {categories:<50}|{product_data['stock']:^10}|{product_data['price']:^10}\033[0m"
            )
            print("\033[1;34m" + "-" * 100 + "\033[0m")



def add_product_inventory(product_name, product_price, product_stock, product_category, inventory, history):

    # Generate automatic ID based on inventory size
    product_id = len(inventory) + 1

    # Add product to main inventory
    product_data = {
        "id": product_id,
        "name": product_name,
        "price": product_price,
        "stock": product_stock,
        "category": product_category,
        "status": True
    }

    # Save product in creation history
    history[product_id] = product_data
    inventory[product_id] = product_data

    guardar_producto_csv(product_data)


def edit_product(inventory, available_categories, title):
    # EN: Edits an existing product in the inventory

    is_editing_product = True
    while is_editing_product:

        # Check if inventory is empty
        if not inventory:
            print("\n\033[1;31m" + "-" * 100 + f"\nError: Please Enter A Product Into The System, There Are No Products Created" + "\n" + "-" * 100 + "\033[0m")
            is_editing_product = False
        
        else:
            title("Edit Product")

            # ===== INPUT PRODUCT ID =====
            try:
                product_id = int(input("\n\033[34m >> \033[0mPlease enter the product ID: "))
            except ValueError:
                print("\n\033[1;31m" + "-" * 100 + f"\nError: Please enter numbers only in this field." + "\n" + "-" * 100 + "\033[0m")
                continue

            # Validate empty input
            error = error_empty_field(product_id)
            if error:
                print(error)
                continue

            # Validate product existence
            if product_id not in inventory:
                print("\n\033[1;31m" + "-" * 100 + f"\nError: Please enter a valid id, that id was not found." + "\n" + "-" * 100 + "\033[0m")
                continue

            print("\n" + "\033[1;34m-\033[0m" * 100)
                
            while is_editing_product:

                # ===== DISPLAY SELECTED PRODUCT =====
                print("\n" + "\033[1;34m" + "-" * 100)
                print("PRODUCT")
                print("-" * 100)
                print(f"{'ID':^5}| {'NAME':<20}| {'CATEGIRIE':<50}|{'STOCK':^10}|{'PRICE':^10}")
                print("-" * 100 + "\033[0m")

                for current_id, product_data in inventory.items():

                    if product_id == current_id:

                        categories = ", ".join(product_data['category'])

                        print(f"\033[1;0m{current_id:^5}| {product_data['name']:<20}| {categories:<50}|{product_data['stock']:^10}|{product_data['price']:^10}\033[0m")
                        print("\033[1;34m" + "-" * 100 + "\033[0m")
                
                        title(f"Product Edition ID {current_id} - {product_data['name']}")

                        # Show edit menu
                        menu()
                        print("\n" + "\033[1;34m-\033[0m" * 100)

                        option = input("\n\033[34m >> \033[0mPlease select a option: ")

                        print("\n" + "\033[1;34m-\033[0m" * 100)

                        # ===== OPTION 1: EDIT NAME =====
                        if option == "1":
                            while True:
                                new_name = input("\n\033[34m >> \033[0mPlease enter the product name: ").capitalize()

                                error = error_empty_field(new_name)
                                if error:
                                    print(error)
                                    continue 

                                product_data['name'] = new_name
                                actualizar_csv(inventory, "inventario.csv")
                                break

                        # ===== OPTION 2: EDIT PRICE =====
                        elif option == "2":
                            while True:
                                try:
                                    new_price = float(input("\n\033[34m >> \033[0mPlease enter the product price: "))
                                except ValueError:
                                    print("\n\033[1;31m" + "-" * 100 + f"\nError: Please enter numbers only in this field." + "\n" + "-" * 100 + "\033[0m")
                                    continue

                                error = error_empty_field(new_price)
                                if error:
                                    print(error)
                                    continue 

                                error = error_negative_value(new_price, 0.01)
                                if error:
                                    print(error)
                                    continue

                                product_data['price'] = new_price
                                actualizar_csv(inventory, "inventario.csv")
                                break
                                
                        # ===== OPTION 3: EDIT CATEGORY =====
                        elif option == "3":

                            selected_categories = []

                            title("List Category")
                            display_inventory_list(available_categories)

                            print("\n" + "\033[1;34m-\033[0m" * 100)
                            print("\033[1;31m" + "-" * 100 + f"\n{'Enter [ 0 ] to finish.':^100}" + "\n" + "-" * 100 + "\033[0m")
                                    
                            while True:
                                try:
                                    category_option = int(input(f"\n\033[34m >> \033[0mPlease select a category option for the product N°{len(selected_categories)+1}: "))
                                except ValueError:
                                    print("\n\033[1;31m" + "-" * 100 + f"\nError: Please enter numbers only in this field." + "\n" + "-" * 100 + "\033[0m")
                                    continue

                                error = error_empty_field(category_option)
                                if error:
                                    print(error)
                                    continue 

                                if category_option == 0:
                                    if selected_categories:
                                        print(f"\n{len(selected_categories)} categories added successfully.")
                                        print(", ".join(selected_categories))
                                        break
                                    else:
                                        print("\n\033[1;31m" + "-" * 100 + f"\nError: You must select a category to classify the product." + "\n" + "-" * 100 + "\033[0m")
                                        continue

                                error = error_category_out_of_range(category_option, available_categories)
                                if error:
                                    print(error)
                                    continue 

                                error = error_duplicate_data(category_option, available_categories, selected_categories)
                                if error:
                                    print(error)
                                    continue 

                                selected_categories.append(available_categories[category_option - 1]) 

                                # Ask if user wants to continue selecting categories
                                exit_flag = confirm_exit()
                                if exit_flag:
                                    product_data['category'] = selected_categories
                                    actualizar_csv(inventory, "inventario.csv")
                                    break
                                else:
                                    continue

                        # ===== OPTION 4: EDIT STOCK =====
                        elif option == "4":
                            while True:
                                try:
                                    new_stock = int(input("\n\033[34m >> \033[0mPlease enter the product stock quantity: "))
                                except ValueError:
                                    print("\n\033[1;31m" + "-" * 100 + f"\nError: Please enter numbers only in this field." + "\n" + "-" * 100 + "\033[0m")
                                    continue

                                error = error_empty_field(new_stock)
                                if error:
                                    print(error)
                                    continue

                                error = error_negative_value(new_stock, 0)
                                if error:
                                    print(error)
                                    continue 

                                product_data['stock'] = new_stock
                                actualizar_csv(inventory, "inventario.csv")
                                break   

                        # ===== OPTION 5: EXIT =====
                        elif option == "5":
                            is_editing_product = False

                        # ===== INVALID OPTION =====
                        else:
                            print("\n\033[1;31m" + "-" * 100)
                            print("Error: Invalid Value Entered. Enter an option between 1 and 5")
                            print("-" * 100 + "\033[0m")




def delete_product(inventory, title):
    # EN: Deletes (logically) a product from the inventory by changing its status

    is_deleting_product = True
    while is_deleting_product:

        # Check if inventory is empty
        if not inventory:
            print("\n\033[1;31m" + "-" * 100 + f"\nError: Please Enter A Product Into The System, There Are No Products Created" + "\n" + "-" * 100 + "\033[0m")
            is_deleting_product = False
        
        else:
            # ===== INPUT PRODUCT ID =====
            while True:
                title("Delete Product")

                try:
                    product_id = int(input("\n\033[34m >> \033[0mPlease enter the product ID: "))
                except ValueError:
                    # Handle non-numeric input
                    print("\n\033[1;31m" + "-" * 100 + f"\nError: Please enter numbers only in this field." + "\n" + "-" * 100 + "\033[0m")
                    continue

                # Validate empty input
                error = error_empty_field(product_id)
                if error:
                    print(error)
                    continue

                # Validate product existence
                if product_id not in inventory:
                    print("\n\033[1;31m" + "-" * 100 + f"\nError: Please enter a valid id, that id was not found." + "\n" + "-" * 100 + "\033[0m")
                    continue

                break

            # ===== DELETE (LOGICAL) PRODUCT =====
            while is_deleting_product:

                # Display product header
                print("\n" + "\033[1;34m" + "-" * 100)
                print("PRODUCT")
                print("-" * 100)
                print(f"{'ID':^5}| {'NAME':<20}| {'CATEGORY':<40}|{'STOCK':^10}|{'PRICE':^10}|{'STATUS':^10}")
                print("-" * 100 + "\033[0m")

                # Find and update the selected product
                for current_id, product_data in inventory.items():

                    if product_id == current_id:

                        # Logical deletion (change status to False)
                        product_data["status"] = False
                        actualizar_csv(inventory, "inventario.csv")

                        # Format categories for display
                        categories = ", ".join(product_data['category'])

                        # Display updated product
                        print(f"\033[1;0m{current_id:^5}| {product_data['name']:<20}| {categories:<40}|{product_data['stock']:^10}|{product_data['price']:^10}|{str(product_data['status']):^10}\033[0m")
                        print("\033[1;34m" + "-" * 100 + "\033[0m")
                    
                is_deleting_product = False
