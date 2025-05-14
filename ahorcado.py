import random
import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def dibujar_ahorcado(intentos):
    """Dibuja el ahorcado según los intentos fallidos usando los dibujos proporcionados"""
    dibujos = [
        """
|---------| 
|         | 
|          
|          
|          
|          
|_________ 
""",
        """
|---------| 
|         | 
|         O 
|          
|          
|          
|_________ 
""",
        """
|---------| 
|         | 
|         O 
|         | 
|          
|          
|_________ 
""",
        """
|---------| 
|         | 
|         O 
|        /| 
|          
|          
|_________ 
""",
        """
|---------| 
|         | 
|         O 
|        /|\\
|          
|          
|_________ 
""",
        """
|---------| 
|         | 
|         O 
|        /|\\
|        /  
|          
|_________ 
""",
        """
|---------| 
|         | 
|         O 
|        /|\\
|        / \\
|          
|_________ 
"""
    ]
    
    # Retornamos el dibujo correspondiente
    return dibujos[intentos] if intentos < len(dibujos) else dibujos[-1]

def obtener_palabra():
    """Retorna una palabra aleatoria de una lista"""
    palabras = ["jirafa", "python", "codigo", "programa", "computadora", 
                "desarrollo", "algoritmo", "variable", "funcion", "sistema"]
    return random.choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas):
    """Muestra la palabra con guiones y letras adivinadas"""
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += "-"
    return resultado

def formatear_letras_dichas(letras_usadas):
    """Formatea """
    # Primera mitad del alfabeto (a-m)
    primera_linea = ""
    # Segunda mitad del alfabeto (n-z)
    segunda_linea = ""
    
    # Ordenamos las letras
    letras_ordenadas = sorted(letras_usadas)
    
    # formato
    for letra in "abcdefghijklm":
        if letra in letras_ordenadas:
            primera_linea += letra
        else:
            primera_linea += "-"
    
    for letra in "nopqrstuvwxyz":
        if letra in letras_ordenadas:
            segunda_linea += letra
        else:
            segunda_linea += "-"
    
    return primera_linea, segunda_linea

def juego_ahorcado():
    """Función principal del juego"""
    limpiar_pantalla()
    print("¡BIENVENIDO AL JUEGO DEL AHORCADO!")
    print("==================================")
    print("\nInstrucciones:")
    print("1. Adivina la palabra secreta letra por letra")
    print("2. Tienes 6 intentos fallidos antes de perder")
    print("3. Ingresa una letra minúscula en cada turno")
    print("\nPresiona Enter para comenzar...")
    input()
    
    # Obtenemos una palabra aleatoria
    palabra = obtener_palabra()
    
    # Inicializamos variables
    letras_adivinadas = set()
    letras_usadas = set()
    intentos = 0
    max_intentos = 6
    
    # Ciclo principal del juego
    while intentos < max_intentos:
        limpiar_pantalla()
        
        # Dibujamos el ahorcado
        print(dibujar_ahorcado(intentos))
        
        # Mostramos las letras usadas
        print("Letras ya dichas:")
        primera_linea, segunda_linea = formatear_letras_dichas(letras_usadas)
        print(primera_linea)
        print(segunda_linea)
        print()
        
        # Mostramos el estado de la palabra
        estado_palabra = mostrar_palabra(palabra, letras_adivinadas)
        print(f"Palabra: {estado_palabra}")
        
        # Verificamos si ganó
        if "-" not in estado_palabra:
            break
        
        # Pedimos una letra
        letra = input("\nIntroduce una letra: ").lower()
        
        # Validamos la entrada
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introduce una única letra.")
            input("Presiona Enter para continuar...")
            continue
        
        # Verificamos si la letra ya fue usada
        if letra in letras_usadas:
            print("Ya has usado esa letra.")
            input("Presiona Enter para continuar...")
            continue
        
        # Añadimos la letra a las usadas
        letras_usadas.add(letra)
        
        # Verificamos si la letra está en la palabra
        if letra in palabra:
            letras_adivinadas.add(letra)
        else:
            intentos += 1
    
    # Mostramos el resultado final
    limpiar_pantalla()
    print(dibujar_ahorcado(intentos))
    
    # Mostramos las letras usadas
    print("Letras ya dichas:")
    primera_linea, segunda_linea = formatear_letras_dichas(letras_usadas)
    print(primera_linea)
    print(segunda_linea)
    print()
    
    # Mostramos la palabra final
    estado_palabra = mostrar_palabra(palabra, letras_adivinadas)
    print(f"Palabra: {estado_palabra}")
    
    if "-" not in estado_palabra:
        print("\n¡Felicidades! ¡Has ganado!")
    else:
        print("\nPerdiste...")
        print(f"La palabra era: {palabra}")
    
    # Preguntamos si quiere jugar de nuevo
    return input("\n¿Jugar de nuevo? (s/n) ").lower() == "s"

def main():
    """Función principal que maneja múltiples partidas"""
    jugando = True
    while jugando:
        jugando = juego_ahorcado()
    
    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    main()