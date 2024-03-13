from encuesta import Encuesta  # Importamos la clase Encuesta

class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        """
        Crea un nuevo usuario con los atributos especificados.

        Args:
            correo (str): El correo electrónico del usuario.
            edad (int): La edad del usuario.
            region (int): El código de la región a la que pertenece el usuario.
        """
        self.__correo = correo
        self.__edad = edad
        self.__region = region
        self.encuestas_participando = []  # Lista para almacenar las encuestas en las que participa el usuario

    @property
    def correo(self) -> str:
        """
        Obtiene el correo electrónico del usuario.

        Returns:
            str: El correo electrónico.
        """
        return self.__correo

    @correo.setter
    def correo(self, correo: str) -> None:
        """
        Establece el correo electrónico del usuario.

        Args:
            correo (str): El nuevo correo electrónico.
        """
        self.__correo = correo

    @property
    def edad(self) -> int:
        """
        Obtiene la edad del usuario.

        Returns:
            int: La edad.
        """
        return self.__edad

    @edad.setter
    def edad(self, edad: int) -> None:
        """
        Establece la edad del usuario.

        Args:
            edad (int): La nueva edad.
        """
        self.__edad = edad

    @property
    def region(self) -> int:
        """
        Obtiene el código de la región del usuario.

        Returns:
            int: El código de la región.
        """
        return self.__region

    @region.setter
    def region(self, region: int) -> None:
        """
        Establece el código de la región del usuario.

        Args:
            region (int): El nuevo código de la región.
        """
        self.__region = region

    def agregar_encuesta_participando(self, encuesta: Encuesta) -> None:
        """
        Agrega una encuesta a la lista de encuestas en las que participa el usuario.

        Args:
            encuesta (Encuesta): La encuesta a agregar.
        """
        self.encuestas_participando.append(encuesta)
