def cupos_genero(peliculas, cartelera, genero):
    total = 0
    genero_buscado = genero.lower()
    for codigo, datos in peliculas.items():
        if datos[1].lower() == genero_buscado:
            if codigo in cartelera:
                total += cartelera[codigo][1]
    print("El total de cupos disponibles es: ", total)
    
def busqueda_precio(peliculas, cartelera, p_min, p_max):
    encontradas = []
    for codigo, datos_cartelera in cartelera.items():
        precio = datos_cartelera[0]
        cupos = datos_cartelera[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            if codigo in peliculas:
                titulo = peliculas[codigo][0]
                encontradas.append(titulo)
                encontradas.append(codigo)
    if encontradas:
        encontradas.sort()
        print("Las películas encontradas son: ", encontradas)
    else:
        print("No hay películas en ese rango de precios.")
        
def buscar_codigo(diccionario, codigo):
    for k in diccionario.keys():
        if k.upper() == codigo.upper():
            return True
    return False
def obtener_codigo_real(diccionario, codigo):
    for k in diccionario.keys():
        if k.upper() == codigo.upper():
            return k
    return codigo

def actualizar_precio(peliculas, cartelera, codigo, nuevo_precio):
    if buscar_codigo(cartelera, codigo):
        codigo_real = obtener_codigo_real(cartelera, codigo)
        cartelera[codigo_real][0] = nuevo_precio
        return True
    return False
def agregar_pelicula(peliculas, cartelera, codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    if buscar_codigo(peliculas, codigo):
        return False
    
    codigo_formateado = codigo.upper()
    es_3d_bool = True if es_3d.lower() == 's' else False
    
    peliculas[codigo_formateado] = [titulo, genero, duracion, clasificacion, idioma, es_3d_bool]
    cartelera[codigo_formateado] = [precio, cupos]
    return True

def eliminar_pelicula(peliculas, cartelera, codigo):
    if buscar_codigo(peliculas, codigo):
        codigo_real = obtener_codigo_real(peliculas, codigo)
        del peliculas[codigo_real]
        if codigo_real in cartelera:
            del cartelera[codigo_real]
        return True
    return False

def menu():
    peliculas = {
        'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
        'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
        'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
        'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
    }

    cartelera = {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3]
    }

    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")
        
        opcion = int(input("Ingrese una opcion valida: "))
        
        if opcion == 1:
            genero = input("Ingrese el genero a buscar: ")
            cupos_genero(peliculas, cartelera, genero)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    if p_min >= 0 and p_max >= p_min:
                        busqueda_precio(peliculas, cartelera, p_min, p_max)
                        break
                    else:
                        print("El precio minimo debe ser mayor o igual a 0, y menor o igual al maximo.")
                except ValueError:
                    print("Debe ingresar valores enteros")
        
        elif opcion == 3:
            while True:
                codigo = input("Ingrese código de película: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio <= 0:
                        print("El precio debe ser mayor que cero.")
                        continue
                except ValueError:
                    print("Debe ingresar un valor entero válido.")
                    continue
                
                exito = actualizar_precio(peliculas, cartelera, codigo, nuevo_precio)
                if exito:
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                
                resp = input("¿Desea actualizar otro precio (s/n)?: ")
                if resp.lower() != "s":
                    break
        
        elif opcion == 4:
        
            codigo = input("Ingrese código de película: ")
                
            titulo = input("Ingrese título: ")
                        
            genero = input("Ingrese género: ")
            
            duracion_str = input("Ingrese duración (minutos): ")
            
            duracion = int(duracion_str)
            
            clasificacion = input("Ingrese clasificación: ")
                       
            idioma = input("Ingrese idioma: ")
                    
            es_3d = input("¿Es 3D? (s/n): ")
            
            precio_str = input("Ingrese precio: ")
            
            precio = int(precio_str)
            
            cupos_str = input("Ingrese cupos: ")
            
            cupos = int(cupos_str)
            
            exito = agregar_pelicula(peliculas, cartelera, codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos)
            if exito:
                print("Película agregada")
            else:
                print("El código ya existe")

        elif opcion == 5:
            codigo = input("Ingrese código de película a eliminar: ")
            exito = eliminar_pelicula(peliculas, cartelera, codigo)
            if exito:
                print("Película eliminada")
            else:
                print("El código no existe")
        
        elif opcion == 6:
            print("Programa finalizado.")
            break
        
        
if __name__ == "__main__":
    menu()


