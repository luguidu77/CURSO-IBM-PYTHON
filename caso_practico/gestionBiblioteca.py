
import sys

# ------------ definiciones --------------------------------------------------------
# clase libro
class libro:
    titulo = ''
    autor = ''
    isbn = ''
    disponible = True



# stock libreria 
stockLibreria: list[libro] = []

# ------------ agregar libro --------------------------------------------------------
def agregar():
    _libro =  libro()
    _libro.titulo = str(input('Título: '))
    _libro.autor = str(input('Autor: '))
    _libro.isbn = str(input('ISBN: '))
    _libro.disponible = True
    
    if(len(stockLibreria)== 0):
        stockLibreria.append(_libro)
        print("Libro agregado con éxito.")
    else:

        for lib in stockLibreria:
            if lib.isbn == _libro.isbn :
          
             print("No se pudo agregar, ya exite ISBN.")
             break
            else:
             stockLibreria.append(_libro)
             print("Libro agregado con éxito.")
             break
    
   

# ------------ prestar libro --------------------------------------------------------
def prestar():
    
    _isbn = input('Ingresa el ISBN: ')
   
    for lib in stockLibreria:
        if lib.isbn == _isbn:
            if  lib.disponible:
                lib.disponible = False
                print("Libro prestado con éxito.")
            else:
                print("El libro ya está prestado.")
            break
    else:
        print("Libro no encontrado.")

# ------------ devolver libro --------------------------------------------------------
def devolver():
    
    _isbn = input('Ingresa el ISBN: ')
   
    for lib in stockLibreria:
        if lib.isbn == _isbn:
            if not lib.disponible:
                lib.disponible = True
                print("Libro devuelto con éxito.")
            else:
                print("El libro ya se encuentra en la librería.")
            break
    else:
        print("Libro no encontrado.")

# ------------ buscar libro --------------------------------------------------------
def buscar():
    
    _isbn = input('Ingresa el ISBN: ')
   
    for lib in stockLibreria:
        if lib.isbn == _isbn:
           
             
            print(f"{lib.titulo} ({lib.autor}) - IBSN: {lib.isbn} - Disponible: {'Si' if lib.disponible else 'No'}")
            break
       
    else:
        print("Libro no encontrado.")

# ------------ mostrar todos los libros -----------------------------------------------------
def mostrar():
    for idx, lib in enumerate(stockLibreria, start=1):
        print(f"{idx}. {lib.titulo} ({lib.autor}) - IBSN: {lib.isbn} - Disponible: {'Si' if lib.disponible else 'No'}")


# ------------ menu opciones -------------------------------------------------------
def mostrar_menu():
 
 
    print('\nBienvenido al Sistema de Gestión de Biblioteca\n')
    print(' 1. Agregar libro')
    print(' 2. Prestar libro')
    print(' 3. Devolver libro')
    print(' 4. Mostrar libros')
    print(' 5. Buscar')
    print(' 6. Salir')



# ------------ eleccion de opciones en pantalla         ----------------------------

def main():
    while True:
        # muestra el menu de opciones en pantalla 
        mostrar_menu()
        try:
            # pide la opcion a elegir asegurando que el dato introducido 
            # sea un entero sino envía exepción evitando se rompa el programa
            opcion = int(input('\nElige una opción: '))
        except ValueError:
            print("Por favor ingresa un número válido.")
            input("Presiona Enter para continuar...")
            continue

        match opcion:
            case 1:
                print("\nAgregar libro:")
                agregar()
            case 2:
                print("\nPrestar libro")
                prestar()
            case 3:
                print("\nDevolver libro")
                devolver()
            case 4:
                print("\nMostrar libros:")
                mostrar()
            case 5:
                print("\nBuscar libro")
                buscar()
            case 6:
                print("Saliendo...")
                sys.exit()
            case _:
                print("Opción no válida.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == '__main__':
    main()