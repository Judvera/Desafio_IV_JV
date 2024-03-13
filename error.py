class DimensionError(Exception):
    def __init__(self, mensaje="", dimension=None, maximo=None):
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is None or self.maximo is None:
            return super().__str__()
        else:
            return f"Error: {self.dimension} fuera de rango. Máximo permitido: {self.maximo}"
