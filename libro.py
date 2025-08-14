class Libro:
    def __init__(self, titulo, autor, anno_publicacion, estado="disponible"):
        self.titulo = titulo
        self.autor = autor
        self.anno_publicacion = anno_publicacion
        self.estado = estado.lower()

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anno_publicacion}, Estado: {self.estado.capitalize()}"

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_anno(self):
        return self.anno_publicacion

    def get_estado(self):
        return self.estado

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado.lower()
