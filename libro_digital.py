from libro import Libro

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anno_publicacion, estado="disponible", formato="PDF"):
        super().__init__(titulo, autor, anno_publicacion, estado)
        self.formato = formato

    def __str__(self):
        return f"{super().__str__()}, Formato: {self.formato}"
