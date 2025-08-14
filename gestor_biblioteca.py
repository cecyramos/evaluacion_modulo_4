from libro import Libro
from libro_digital import LibroDigital
from biblioteca import Biblioteca

def menu():
    print("\n--- Gestor de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Ver todos los libros")
    print("4. Buscar libro")
    print("5. Marcar libro como prestado")
    print("6. Devolver libro")
    print("7. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tipo = input("¿Es un libro digital? (s/n): ").lower()
            titulo = input("Título: ")
            autor = input("Autor: ")
            anno = input("Año de publicación: ")
            estado = "disponible"

            if tipo == "s":
                formato = input("Formato (PDF, ePub, etc.): ")
                libro = LibroDigital(titulo, autor, anno, estado, formato)
            else:
                libro = Libro(titulo, autor, anno, estado)

            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            titulo = input("Ingresa el título del libro a eliminar: ")
            biblioteca.eliminar_libro(titulo)

        elif opcion == "3":
            biblioteca.ver_libros()

        elif opcion == "4":
            titulo = input("Ingresa el título del libro a buscar: ")
            biblioteca.buscar_libro(titulo)

        elif opcion == "5":
            titulo = input("Ingresa el título del libro a marcar como prestado: ")
            biblioteca.prestar(titulo)

        elif opcion == "6":
            titulo = input("Ingresa el título del libro a devolver: ")
            biblioteca.devolver(titulo)

        elif opcion == "7":
            print("¡Nos vemos a la próxima!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
