from preguntas import Pregunta # Importamos la clase Pregunta
from typing import Any

class Encuesta:
    def __init__(self, nombre: str, preguntas: list[dict[str, Any]]) -> None:
        """
        Crea una nueva encuesta con el nombre y las preguntas especificadas.

        Args:
            nombre (str): El nombre de la encuesta.
            preguntas (list[dict[str, Any]]): Lista de diccionarios representando las preguntas.
                Cada diccionario debe contener las claves 'enunciado', 'ayuda', 'requerida' y 'alternativas'.
        """
        self.nombre = nombre
        self.__preguntas = [Pregunta(p['enunciado'], p['ayuda'], p['requerida'], p['alternativas']) for p in preguntas]
        self.__respuestas = []

    def mostrar_encuesta(self) -> None:
        """
        Muestra el nombre de la encuesta y todas sus preguntas.
        """
        print(self.nombre)

        for p in self.__preguntas:
            p.mostrar_pregunta()

    def agregar_respuesta(self, respuesta) -> None:
        """
        Agrega una respuesta a la encuesta.

        Args:
            respuesta: La respuesta a agregar.
        """
        self.__respuestas.append(respuesta)
