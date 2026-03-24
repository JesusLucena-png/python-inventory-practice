import gestion_productos


inventory = {
    1 : {   
    "nombre" : "pan",
    "stock" : 50,
    "categorias" : ["panaderia", "alimento"],
    "precio" : 1.0,
    "estado" : True
    },
    2 : {   
    "nombre" : "pan",
    "stock" : 50,
    "categorias" : ["panaderia", "alimento"],
    "precio" : 1.0,
    "estado" : True
    }
}

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

def title(title_text):

    # Centers the title with dashes on the sides
    if len(title_text) % 2 == 0:
        dash_count = (58 - len(title_text)) // 2
        print("\033[34m" + "-"*dash_count + " " + title_text + " " + "-"*dash_count + "\033[0m")
    else:
        dash_count = ((58 - 1) - len(title_text) + 1) // 2
        print("\n\033[34m" + "-"*dash_count + " " + title_text + " -" + "-"*dash_count + "\033[0m")

def menu():

    title("Menu De Opciones Del Sistema")

    print("""
1. Agregar Producto
2. Mostrar Inventario
3. realizar pedido
4. Editar Produto
5. Eliminar Producto
6. Buscar Producto
7. Ordenar Inventario
8. Alertas De Stock
    """)


ws = True
cont_product = 0
while ws:

    option = "1"

    if option == "1":
        gestion_productos.add_product(inventory, available_categories, title)


    print(inventory)
    break








