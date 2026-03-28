import csv
import gestion_productos

def show_inventory(inventory, title):
    # EN: Displays all available products in the inventory
    ws = True

    while ws:
        title("Show Inventory")

        # Header section
        print("\n" + "\033[1;34m" + "-" * 100)
        print("PRODUCTS")
        print("-" * 100)
        print(f"{'ID':^5}| {'NAME':<20}| {'CATEGORY':<50}|{'STOCK':^10}|{'PRICE':^10}")
        print("-" * 100 + "\033[0m")

        # Loop through inventory and display products
        for product_id, product_data in inventory.items():

            # Only show active products with stock
            if product_data['status'] and product_data['stock'] != 0:

                # Join categories into a single string
                categories = ", ".join(product_data['category'])

                print(f"\033[1;0m{product_id:^5}| {product_data['name']:<20}| {categories:<50}|{product_data['stock']:^10}|{product_data['price']:^10}\033[0m")
                print("\033[1;34m" + "-" * 100 + "\033[0m")

        ws = False

def calculate_statistics(inventory, title):
    report_data = {}

    # Show section title
    title("Calculate Statistics")

    # Initialize counters
    inventory_value = 0
    total_products = 0
    total_stock = 0

    # Header for report
    row_id = len(report_data) + 1
    report_data[row_id] = ('ID', 'NAME', 'CATEGORY', 'STOCK', 'PRICE', 'TOTAL')

    # First pass: products with stock > 50
    for product_id, product_data in inventory.items():

        if product_data['status'] and product_data['stock'] > 50:

            categories = ", ".join(product_data['category'])

            row_id = len(report_data) + 1
            report_data[row_id] = (
                product_id,
                product_data['name'],
                categories,
                product_data['stock'],
                product_data['price'],
                product_data["price"] * product_data['stock']
            )

            inventory_value += (product_data["price"] * product_data['stock'])
            total_products += 1
            total_stock += product_data['stock']

    # Second pass: products with stock <= 50 and > 0
    for product_id, product_data in inventory.items():

        if product_data['status'] and product_data['stock'] <= 50 and product_data['stock'] != 0:

            categories = ", ".join(product_data['category'])

            row_id = len(report_data) + 1
            report_data[row_id] = (
                product_id,
                product_data['name'],
                categories,
                product_data['stock'],
                product_data['price'],
                product_data["price"] * product_data['stock']
            )

            inventory_value += (product_data["price"] * product_data['stock'])
            total_products += 1
            total_stock += product_data['stock']

    # Third pass: products with zero stock
    for product_id, product_data in inventory.items():

        if True == product_data['status'] and product_data['stock'] == 0:

            categories = ", ".join(product_data['category'])

            row_id = len(report_data) + 1
            report_data[row_id] = (
                product_id,
                product_data['name'],
                categories,
                product_data['stock'],
                product_data['price'],
                product_data["price"] * product_data['stock']
            )

            total_products += 1

    # Final summary row
    report_data[row_id] = (
        f"Total Inventory Value :{inventory_value}",
        f"Total Number Of Products :{total_products}",
        f"Total Stock Of Products :{total_stock}"
    )

    # Generate CSV report
    generate_final_report(report_data)

    # Print statistics
    print(f"Total Number Of Products : {total_products}")
    print(f"Total Stock Of Products : {total_stock}")
    print(f"Total Inventory Value : {inventory_value}")


def generate_final_report(report_data, filename="final_report.csv"):

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for row in report_data.values():
            writer.writerow(row)

    print(f"\n\033[1;32mFinal report generated successfully as '{filename}'.\033[0m")


def stock_alerts(inventory, title):
    # EN: Displays alerts for products with zero or low stock

    title("stock alerts")

    # ZERO STOCK ALERT
    ws = True
    while ws:
        print("\n" + "\033[1;31m" + "-" * 100)
        print("ZERO STOCK ALERT")
        print("-" * 100)
        print(f"{'ID':^5}| {'NAME':<20}| {'CATEGORY':<50}|{'STOCK':^10}|{'PRICE':^10}")
        print("-" * 100 + "\033[0m")

        for product_id, product_data in inventory.items():

            if product_data['status'] and product_data['stock'] == 0:

                categories = ", ".join(product_data['category'])

                print(f"\033[1;0m{product_id:^5}| {product_data['name']:<20}| {categories:<50}|{product_data['stock']:^10}|{product_data['price']:^10}\033[0m")
                print("\033[1;31m" + "-" * 100 + "\033[0m")

        ws = False

    # VERY LOW STOCK ALERT
    ws = True
    while ws:

        print("\n" + "\033[1;33m" + "-" * 100)
        print("VERY LOW STOCK ALERT")
        print("-" * 100)
        print(f"{'ID':^5}| {'NAME':<20}| {'CATEGORY':<50}|{'STOCK':^10}|{'PRICE':^10}")
        print("-" * 100 + "\033[0m")

        for product_id, product_data in inventory.items():

            if product_data['status'] and product_data['stock'] <= 50 and product_data['stock'] != 0:

                categories = ", ".join(product_data['category'])

                print(f"\033[1;0m{product_id:^5}| {product_data['name']:<20}| {categories:<50}|{product_data['stock']:^10}|{product_data['price']:^10}\033[0m")
                print("\033[1;33m" + "-" * 100 + "\033[0m")

        ws = False

def search_product(inventory, title):
    # EN: Searches for a product in the inventory

    title("Search Product")

    # ===== INPUT SEARCH VALUE =====
    while True:
        print("\033[1;33m" + "-" * 100 + f"\n{'search by name, category, price, and stock.':^100}" + "\n" + "-" * 100 + "\033[0m")

        search_value = input("\n\033[33m >> \033[0mPlease enter the product to search: ").lower()
    
        # Validate empty input
        error = gestion_productos.error_empty_field(search_value)
        if error:
            print(error)
            continue

        break

    # Flag to check if any product was found
    product_not_found = True

    # ===== DISPLAY HEADER =====
    print("\n" + "\033[1;34m" + "-" * 100)
    print("PRODUCT")
    print("-" * 100)
    print(f"{'ID':^5}| {'NAME':<20}| {'CATEGORY':<50}|{'STOCK':^10}|{'PRICE':^10}")
    print("-" * 100 + "\033[0m")

    # ===== SEARCH LOOP =====
    for product_id, product_data in inventory.items():

        # Join categories for search/display
        categories = ", ".join(product_data['category'])

        # Search conditions
        if (search_value in [
            product_data['name'].lower(),
            str(product_data['stock']),
            str(product_data["price"]),
            str(product_id)
        ] or search_value in categories.lower()) and product_data["status"] == True:

            product_not_found = False

            # Display matching product
            print(f"\033[1;0m{product_id:^5}| {product_data['name']:<20}| {categories:<50}|{product_data['stock']:^10}|{product_data['price']:^10}\033[0m")
            print("\033[1;34m" + "-" * 100 + "\033[0m")
    
    # If no product matched
    if product_not_found:
        print("\n\033[1;31m" + "-" * 100 + f"\nError: Product not found." + "\n" + "-" * 100 + "\033[0m")