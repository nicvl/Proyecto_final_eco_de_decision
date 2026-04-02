import pyttsx3

VOICE_INDEX = 0 
RATE = 150

def hablar(texto):
    """Reinicia el motor en cada llamada para asegurar que lea todo."""
    print("\n" + str(texto))
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if len(voices) > VOICE_INDEX:
            engine.setProperty('voice', voices[VOICE_INDEX].id)
        
        engine.setProperty('rate', RATE)
        engine.say(str(texto))
        engine.runAndWait()
        # Liberamos el motor para la siguiente frase
        engine.stop() 
    except Exception as e:
        print(f"Error de voz: {e}")

def obtener_opcion():
    while True:
        r = input("\n[Escribe A o B]: ").strip().lower()
        if r in ["a", "b"]:
            return r
        print("Por favor, elige solo A o B.")

# iniciar funcionamiento 
historial = []

hablar("Bienvenidos.")
hablar("Se encuentran en una experiencia inmersiva donde ustedes serán los que dirijan el transcurso de esta pieza.")
hablar("Yo, como máquina que se encuentra frente a ustedes, tendrán la posibilidad de usarme y responder una serie de preguntas.")
hablar("Donde el sonido modificará el movimiento.")
hablar("Para dichas intervenciones, seleccionarán A o B con el teclado.")
hablar("Empecemos.")
hablar(" 3... 2... 1...")

#Pregunta 1
hablar("El sonido altera el cuerpo. ¿Qué afecta primero?")
hablar("Opción A. La distancia.")
hablar("Opción B. El tiempo.")

r1 = obtener_opcion()
historial.append(r1.upper())

if r1 == "a":
    hablar("Eligieron la distancia.")
    hablar("La distancia se deforma.")
    hablar("Opción A. Es difícil separarse.")
    hablar("Opción B. Es fácil alejarse.")
    r2 = obtener_opcion()
    historial.append(r2.upper())
    final = "Atracción sonora" if r2 == "a" else "Fuga sonora"
else:
    hablar("Eligieron el tiempo.")
    hablar("El tiempo cambia.")
    hablar("Opción A. Algunas cosas se repiten.")
    hablar("Opción B. Nada vuelve a ocurrir.")
    r2 = obtener_opcion()
    historial.append(r2.upper())
    final = "Eco corporal" if r2 == "a" else "Tirmpo inestable"

# Final codigo
camino_texto = " luego ".join(historial)
hablar(f"Sus decisiones fueron: {camino_texto}")
hablar(f"Resultado final: {final}")
