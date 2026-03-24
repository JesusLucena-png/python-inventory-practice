    
    elif opcion == "2":
        for key, date in productos.items():
            print(f"{key:>10}{date['nombre']:>10}{date['stock']:>10}{date['precio']:>10}")
    elif opcion == "3":

        edit = input("ingresa id o nombre del produvto a edita").upper()

        for key, date in productos.items():

            id_producto = date["nombre"].upper()
           
            if id_producto == edit:
                       
                print(f"{key:>10}{date['nombre']:>10}{date['stock']:>10}{date['precio']:>10}")
                cont_product += 1
      
            
            if  edit == str(key):
                print("encontrado")
                break
            else:
                print("898")
