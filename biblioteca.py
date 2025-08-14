from libro import Libro
from libro_digital import LibroDigital

class Biblioteca:
    def __init__(self, archivo="biblioteca.txt"):
        self.archivo = archivo
        self.libros = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                for linea in file:
                    datos = linea.strip().split("|")
                    if len(datos) == 4:
                        titulo, autor, anno_publicacion, estado = datos
                        self.libros.append(Libro(titulo, autor, anno_publicacion, estado))
                    elif len(datos) == 5:
                        titulo, autor, anno_publicacion, estado, formato = datos
                        self.libros.append(LibroDigital(titulo, autor, anno_publicacion, estado, formato))
        except FileNotFoundError:
            pass  # Si el archivo no existe, empezamos con lista vacía

    def guardar_en_archivo(self):
        with open(self.archivo, "w", encoding="utf-8") as file:
            for libro in self.libros:
                if isinstance(libro, LibroDigital):
                    file.write(f"{libro.titulo}|{libro.autor}|{libro.anno_publicacion}|{libro.estado}|{libro.formato}\n")
                else:
                    file.write(f"{libro.titulo}|{libro.autor}|{libro.anno_publicacion}|{libro.estado}\n")

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
        self.guardar_en_archivo()
        print("Libro agregado exitosamente.")

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                self.libros.remove(libro)
                self.guardar_en_archivo()
                print("Libro eliminado.")
                return
        print("Libro no encontrado.")

    def ver_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros:
                print(libro)

    def buscar_libro(self, titulo):
        encontrados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontró ningún libro con ese título.")

    def prestar(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                if libro.estado == "prestado":
                    print("Este libro ya está prestado.")
                else:
                    libro.set_estado("prestado")
                    self.guardar_en_archivo()
                    print("Libro marcado como prestado.")
                return
        print("Libro no encontrado.")

    def devolver(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                if libro.estado == "disponible":
                    print("Este libro ya está disponible.")
                else:
                    libro.set_estado("disponible")
                    self.guardar_en_archivo()
                    print("Libro devuelto.")
                return
        print("Libro no encontrado.")
