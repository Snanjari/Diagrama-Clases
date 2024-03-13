class Alternativa:
    def __init__(self, contenido: str, ayuda: str):
        """
        Crea una nueva alternativa con el contenido y la ayuda especificados.

        Args:
            contenido (str): El contenido principal de la alternativa.
            ayuda (str): Una descripción adicional o ayuda relacionada con la alternativa.
        """
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self) -> None:
        """
        Muestra el contenido de la alternativa y, si está disponible, la ayuda asociada.
        """
        print(f"Contenido: {self.contenido}")

        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")
