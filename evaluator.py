#!/bin/env python3

import hashlib
from rich.console import Console
from rich.prompt import Prompt

console = Console()

# Hashes de respuestas correctas para cada pregunta de cada práctica
HASHES_PRACTICAS = {
    1: [
        hashlib.sha256(b"respuesta1_practica1").hexdigest(),
        hashlib.sha256(b"respuesta2_practica1").hexdigest(),
        hashlib.sha256(b"respuesta3_practica1").hexdigest(),
    ],
    2: [
        hashlib.sha256(b"respuesta1_practica2").hexdigest(),
        hashlib.sha256(b"respuesta2_practica2").hexdigest(),
    ],
    3: [
        hashlib.sha256(b"respuesta1_practica3").hexdigest(),
        hashlib.sha256(b"respuesta2_practica3").hexdigest(),
    ],
    4: [
        hashlib.sha256(b"respuesta1_practica4").hexdigest(),
        hashlib.sha256(b"respuesta2_practica4").hexdigest(),
    ],
    5: [
        hashlib.sha256(b"respuesta1_practica5").hexdigest(),
        hashlib.sha256(b"respuesta2_practica5").hexdigest(),
    ],
}

PREGUNTAS_PRACTICAS = {
    1: [
        "¿Cuál es el hash del tercer commit?",
        "¿Cuántos archivos fueron modificados en el segundo commit?",
        "¿Qué archivo ha sido modificado más veces?",
    ],
    2: [
        "¿Cómo se llama la rama que creaste para la nueva funcionalidad?",
        "¿Qué comando usaste para resolver el conflicto de fusión?",
    ],
    3: [
        "¿Cuál es el comando para clonar un repositorio usando SSH?",
        "¿Cómo añades un submódulo a un repositorio?",
    ],
    4: [
        "¿Cómo se hace un fork de un repositorio en GitHub?",
        "¿Cómo se crea un issue en GitHub?",
    ],
    5: [
        "¿Qué estructura de datos implementaste en la rama feature-a?",
        "¿Qué cambios realizaste en el pull request?",
    ],
}


def hash_respuesta(respuesta):
    return hashlib.sha256(respuesta.encode()).hexdigest()


def validar_respuesta(respuesta, hash_correcto):
    return hash_respuesta(respuesta) == hash_correcto


def seleccionar_practica():
    console.print("Selecciona la práctica que deseas cargar:", style="bold yellow")
    console.print("1) Práctica 1")
    console.print("2) Práctica 2")
    console.print("3) Práctica 3")
    console.print("4) Práctica 4")
    console.print("5) Práctica 5")
    seleccion = Prompt.ask(
        "Introduce el número de la práctica", choices=["1", "2", "3", "4", "5"]
    )
    return int(seleccion)


def cargar_practica(practica_num):
    preguntas = PREGUNTAS_PRACTICAS[practica_num]
    hashes = HASHES_PRACTICAS[practica_num]
    total_preguntas = len(preguntas)

    for idx, pregunta in enumerate(preguntas):
        while True:
            pregunta_con_progreso = f"{pregunta} ({idx + 1}/{total_preguntas})"
            respuesta = Prompt.ask(pregunta_con_progreso)
            if validar_respuesta(respuesta, hashes[idx]):
                console.print("Respuesta correcta!", style="bold green")
                break
            else:
                console.print(
                    "Respuesta incorrecta. Inténtalo de nuevo.", style="bold red"
                )


def main():
    practica_num = seleccionar_practica()
    console.clear()
    cargar_practica(practica_num)
    console.print("¡Has completado la práctica!", style="bold green")


if __name__ == "__main__":
    main()

