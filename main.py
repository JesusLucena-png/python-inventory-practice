import gestion_productos
import operaciones_inventario
import os


inventory = gestion_productos.cargar_csv("inventario.csv")

# List of available categories for products
available_categories = [
    "Food & Grocery",
    "Bakery",
    "Dairy Products",
    "Meat & Poultry",
    "Seafood",
    "Fruits",
    "Vegetables",
    "Frozen Foods",
    "Snacks & Confectionery",
    "Beverages",
    "Alcoholic Beverages",
    "Household Cleaning",
    "Personal Care",
    "Health & Pharmacy",
    "Baby Products",
    "Pet Supplies",
    "Electronics",
    "Office Supplies",
    "Clothing & Apparel",
    "Home & Living",
    "Kitchenware",
    "Hardware & Tools",
    "Toys & Games",
    "Sports & Fitness"
]

# Function to display a formatted title
def title(title_text):

    # Check if the title length is even
    if len(title_text) % 2 == 0:
        dash_count = (98 - len(title_text)) // 2
        print("\033[1;34m" + "-" * dash_count + " " + title_text + " " + "-" * dash_count + "\033[0m")
    else:
        # Adjust formatting if the title length is odd
        dash_count = ((98 - 1) - len(title_text) + 1) // 2
        print("\n\033[1;34m" + "-" * dash_count + " " + title_text + " -" + "-" * dash_count + "\033[0m")


# Control variable for the main loop
is_running = True
# Main program loop
while is_running:

    title("Menu De Opciones - Gestion De Invenario")

    # Display menu options
    print("""
\033[1;34m 1. \033[0mAgregar Producto
\033[1;34m 2. \033[0mMostrar Inventario
\033[1;34m 3. \033[0mEditar Produto
\033[1;34m 4. \033[0mEliminar Producto
\033[1;34m 5. \033[0mBuscar Producto
\033[1;34m 6. \033[0mAlertas De Stock
\033[1;34m 7. \033[0mCalcular Estadisticas(Inventario)

\033[1;31m 8. \033[0mExit
    """)

    # Print separator line
    print("\033[1;34m" + "-" * 100 + "\033[0m")

    # Get user input
    option = input("\n\033[34m >> \033[0mPlease select a option: ")

    print("\n\033[1;34m" + "-" * 100 + "\033[0m")

    # Clear console depending on OS (Windows/Linux/Mac)
    os.system("cls" if os.name == "nt" else "clear")

    # Menu options handling
    if option == "1":
        gestion_productos.add_product(inventory, available_categories, title)
    elif option == "2":
        operaciones_inventario.show_inventory(inventory, title)
    elif option == "3":
        gestion_productos.edit_product(inventory, available_categories, title)
    elif option == "4":
        gestion_productos.delete_product(inventory, title)
    elif option == "5":
        operaciones_inventario.search_product(inventory, title)
    elif option == "6":
        operaciones_inventario.stock_alerts(inventory, title)
    elif option == "7":
        operaciones_inventario.calculate_statistics(inventory, title)
    elif option == "8":
        is_running = False
    else:
        # Error message for invalid option
        print("\n\033[1;31m" + "-" * 100 + f"\n{'INVALID OPTION!':^100}\n" + "-" * 100 + "\033[0m")
