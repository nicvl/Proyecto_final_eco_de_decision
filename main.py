import pyttsx3
import pygame
import time
import os
import sys

# encuentra la ubicación entre los archivos y el script para evitar problemas de ruta
ruta_script = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(ruta_script)

# inicializar el mezclador de audio
pygame.mixer.init()

VOICE_INDEX = 0 
RATE = 150

def hablar(texto):
    #voz del computador 
    print("\n" + str(texto))
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if len(voices) > VOICE_INDEX:
            engine.setProperty('voice', voices[VOICE_INDEX].id)
        engine.setProperty('rate', RATE)
        engine.say(str(texto))
        engine.runAndWait()
        engine.stop() 
    except Exception as e:
        print(f"Error de voz: {e}")

def reproducir_y_esperar(archivo):
    #reproducir el audio y esperar a que termine antes de continuar
    try:
        if not os.path.exists(archivo):
            print(f"ALERTA: El archivo {archivo} no está en: {os.getcwd()}")
            return
        pygame.mixer.music.load(archivo)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)
    except Exception as e:
        print(f"Error al reproducir {archivo}: {e}")

def obtener_opcion():
    while True:
        r = input("\n[Escribe A o B]: ").strip().lower()
        if r in ["a", "b"]:
            return r
        print("Por favor, elige solo A o B.")

# iniciar la experiencia
historial = []

hablar("Bienvenidos.")
hablar("Se encuentran en una experiencia inmersiva donde ustedes serán los que dirijan el transcurso de esta pieza.")
hablar("Yo, como máquina que se encuentra frente a ustedes, tendrán la posibilidad de usarme y responder una serie de preguntas.")
hablar("Donde el sonido modificará el movimiento.")
hablar("Para dichas intervenciones, seleccionarán A o B con el teclado.")
hablar("Empecemos.")
hablar("3... 2... 1...")

# PREGUNTA 1 
hablar("El sonido altera el cuerpo. ¿Qué afecta primero?")
hablar("Opción A. La distancia.")
hablar("Opción B. El tiempo.")

r1 = obtener_opcion()
historial.append(r1.upper())

if r1 == "a":
    hablar("Eligieron la distancia.")
    reproducir_y_esperar("intervencion_1_distancia.mp3")
    hablar("La distancia se deforma.") #PREGUNTA 2
    hablar("Opción A. Es difícil distanciarse. ")
    hablar("Opción B. Es fácil alejarse.")
    
    r2 = obtener_opcion()
    historial.append(r2.upper())
    
    if r2 == "a":
        hablar("Eligieron difícil distanciarse.")
        reproducir_y_esperar("intervencion_dificil_distanciarse.mp3")
        final = "Atracción sonora"
        audio_final = "final_AA_atraccion_sonora.mp3"
    else:
        hablar("Eligieron fácil alejarse.")
        reproducir_y_esperar("intervencion_facil_alejarse.mp3")
        final = "Fuga sonora"
        audio_final = "final_AB_fuga_sonora.mp3"
else:
    hablar("Eligieron el tiempo.")
    reproducir_y_esperar("intervencion_1_tiempo.mp3")
    hablar("El tiempo cambia.") #PREGUNTA 3
    hablar("Opción A. Hay repeticiones.")
    hablar("Opción B. Nunca es igual.")
    
    r2 = obtener_opcion()
    historial.append(r2.upper())
    
    if r2 == "a":
        hablar("Eligieron repetición.")
        reproducir_y_esperar("intervencion_2_repeticion.mp3")
        final = "Eco corporal"
        audio_final = "final_BA_eco_corporal.mp3"
    else:
        hablar("Eligieron nunca es igual.")
        reproducir_y_esperar("intervencion_nunca_es_igual.mp3")
        final = "Tiempo inestable"
        audio_final = "final_BB_tiempo_inestable.mp3"

# Antes de reproducir el audio final, hacemos un resumen de las decisiones tomadas
camino_texto = " luego ".join(historial)
hablar(f"Sus decisiones fueron: {camino_texto}")
hablar(f"Resultado final: {final}")

time.sleep(1)
reproducir_y_esperar(audio_final)

hablar("La experiencia ha terminado. Muchas gracias por construir con nosotres esta pieza.")