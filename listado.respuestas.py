from usuarios import Usuario # Importamos la clase Usario

class ListadoRespuestas:
    def __init__(self, respuestas: list):
        """
        Crea un nuevo listado de respuestas con las respuestas especificadas.

        Args:
            respuestas (list): Una lista de respuestas iniciales.
        """
        self.respuestas = respuestas
        self.usuarios = []

    def agregar_usuario(self, correo: str, edad: int, region: int) -> None:
        """
        Agrega un nuevo usuario al listado.

        Args:
            correo (str): El correo electrónico del usuario.
            edad (int): La edad del usuario.
            region (int): El código de la región a la que pertenece el usuario.
        """
        self.usuarios.append(Usuario(correo, edad, region))

    @property
    def respuestas(self) -> list:
        """
        Obtiene la lista de respuestas en este listado.

        Returns:
            list: Lista de respuestas.
        """
        return self.__respuestas

    @respuestas.setter
    def respuestas(self, respuestas: list) -> None:
        """
        Establece las respuestas en este listado.

        Args:
            respuestas (list): Lista de respuestas.
        """
        self.__respuestas = respuestas
