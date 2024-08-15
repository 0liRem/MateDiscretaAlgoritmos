'''MATE DISCRETA

FECHA 13/8/2024

PROGRAMADOR: Olivier Viau
DESCRIPCION: Utilizando python realizar un programa capaz de generar numeros pseudoaleatorios
Recusros: ChatGPT, w3schools

Historial de modificaciones

[000] 13/08/2024
[001] 15/08/2024
'''

def generar_numeros_pseudoaleatorios(m, a, c, semilla, n):
    numeros_pseudoaleatorios = [semilla]
    
    # Generar los números pseudoaleatorios
    for _ in range(n - 1):
        nuevo_numero = (a * numeros_pseudoaleatorios[-1] + c) % m
        numeros_pseudoaleatorios.append(nuevo_numero)
    
    return numeros_pseudoaleatorios

# Parámetros
try:
    m=int(input("Ingrese el modulo \n")) 
    a=int(input("Ingrese el multiplicador \n"))
    c=int(input("Ingrese el incremento \n"))
    semilla=int(input("Ingrese la semilla \n"))
    n=int(input("Ingrese cuantos numeros quiere generar \n")) 
    print(generar_numeros_pseudoaleatorios(m, a, c, semilla, n))
except:
    print("Error ocurrio algo inesperado")