from alternativa import Alternativa # Importamos la clase Alternativa

class Pregunta:
    def __init__(self, enunciado: str, ayuda: str, requerida: bool, alternativas: list) -> None:
        """
        Crea una nueva pregunta con el enunciado, ayuda, requerimiento y alternativas especificados.

        Args:
            enunciado (str): El enunciado o texto de la pregunta.
            ayuda (str): Una descripción adicional o ayuda relacionada con la pregunta.
            requerida (bool): Indica si la pregunta es obligatoria.
            alternativas (list): Una lista de diccionarios con las alternativas disponibles.
                Cada diccionario debe contener las claves 'contenido' y 'ayuda'.
        """
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.__alternativas = [Alternativa(a['contenido'], a['ayuda']) for a in alternativas]

    @property
    def alternativas(self) -> list:
        """
        Obtiene la lista de alternativas disponibles para esta pregunta.

        Returns:
            list: Lista de objetos Alternativa.
        """
        return self.__alternativas

    @alternativas.setter
    def alternativas(self, alternativas: list) -> None:
        """
        Establece las alternativas disponibles para esta pregunta.

        Args:
            alternativas (list): Lista de objetos Alternativa.
        """
        self.__alternativas = alternativas

    def mostrar_pregunta(self) -> None:
        """
        Muestra el enunciado de la pregunta, la ayuda (si está disponible) y las alternativas.
        """
        print(f"Enunciado: {self.enunciado}")

        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")

        for a in self.__alternativas:
            a.mostrar_alternativa()
