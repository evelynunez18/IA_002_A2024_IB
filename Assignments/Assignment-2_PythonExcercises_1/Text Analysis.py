import re
from collections import Counter

def analizar_documento(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Contar párrafos
    parrafos = contenido.split('\n\n')
    num_parrafos = len(parrafos)

    # Contar oraciones
    oraciones = re.split(r'[.!?]+', contenido)
    num_oraciones = len([s for s in oraciones if s.strip()])

    # Contar palabras
    palabras = re.findall(r'\b\w+\b', contenido)
    num_palabras = len(palabras)

    # Calcular promedio de longitud de palabras
    longitud_palabras = sum(len(palabra) for palabra in palabras)
    promedio_longitud = longitud_palabras / num_palabras if num_palabras > 0 else 0

    # Contar palabras más frecuentes
    contador_palabras = Counter(palabras)
    palabras_frecuentes = contador_palabras.most_common(5)

    # Mostrar resultados
    print(f"Número de palabras: {num_palabras}")
    print(f"Número de oraciones: {num_oraciones}")
    print(f"Número de párrafos: {num_parrafos}")
    print(f"Promedio de longitud de palabras: {promedio_longitud:.2f}")
    print("Palabras más frecuentes:")
    for palabra, frecuencia in palabras_frecuentes:
        print(f"{palabra}: {frecuencia}")

if __name__ == "__main__":
    ruta_archivo = "C:\\Users\\sofia\\Downloads\\texto.txt" 
    analizar_documento(ruta_archivo)
