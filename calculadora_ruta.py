import heapq  # Importa la biblioteca heapq para trabajar con colas de prioridad

# Función para crear un mapa con dimensiones especificadas
def crear_mapa(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]

# Función para mostrar el mapa en la consola
def mostrar_mapa(mapa, inicio=None, fin=None, camino=None):
    for i, fila in enumerate(mapa):
        for j, celda in enumerate(fila):
            if inicio and (i, j) == inicio:
                print("E", end="")  # Marca el punto de inicio con "E"
            elif fin and (i, j) == fin:
                print("S", end="")  # Marca el punto final con "S"
            elif celda == 999:
                print("X", end="")  # Marca los edificios con "X"
            elif celda == 2:
                print("#", end="")  # Marca los baches con "#"
            elif celda == 3:
                print("!", end="")  # Marca el agua con "!"
            elif camino and (i, j) in camino:
                print("*", end="")  # Marca el camino con "*"
            else:
                print(".", end="")  # Marca los espacios libres con "."
        print()  # Nueva línea al final de cada fila

# Función para permitir al usuario agregar obstáculos al mapa
def agregar_obstaculos(mapa):
    while True:
        tipo_obstaculo = input("Ingrese el tipo de obstáculo (X para edificio, # para bache, ! para agua) o basta para continuar ")
        tipo_obstaculo = tipo_obstaculo.lower()  # Convertir la entrada a minúsculas
        if tipo_obstaculo == 'basta':
            break  # Termina si el usuario ingresa "basta"
        if tipo_obstaculo not in ["x", "#", "!"]:
            print("Tipo de obstáculo inválido, pruebe devuelta")
            continue

        while True:
            coord = input("Ingrese las coordenadas del obstáculo (x,y): ")
            try:
                x, y = map(int, coord.split(","))  # Convierte la entrada del usuario en coordenadas x, y
                if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]):
                    if mapa[x][y] == 0:  # Verifica que no haya ya un obstáculo
                        if tipo_obstaculo == "x":
                            mapa[x][y] = 999  # Edificio, costo muy alto
                        elif tipo_obstaculo == "#":
                            mapa[x][y] = 2  # Bache, costo medio
                        elif tipo_obstaculo == "!":
                            mapa[x][y] = 3  # Agua, costo medio
                        break
                    else:
                        print("Ya existe un obstáculo en esa coordenada, proba de nuevo.")
                else:
                    print("Las coordernadas estan fuera del rango del mapa, proba de nuevo.")
            except ValueError:
                print("El formato de coordenadas es invalido, proba de nuevo.")
    mostrar_mapa(mapa)  # Muestra el mapa actualizado

# Función para obtener coordenadas del usuario asegurando que sean válidas y transitables
def obtener_coordenadas(mensaje, mapa):
    while True:
        coord = input(mensaje)  # Solicita al usuario que ingrese las coordenadas
        try:
            x, y = map(int, coord.split(","))  # Convierte la entrada del usuario en coordenadas x, y
            if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] == 0:
                return (x, y)  # Retorna las coordenadas si son válidas
            else:
                print("Coordenadas inválidas o en un obstáculo, intente de nuevo.")
        except ValueError:
            print("El formato de coordenadas es invalido, proba de nuevo.")

# Función de heurística de Manhattan para el algoritmo A*
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Calcula la distancia de Manhattan entre dos puntos

# Función para obtener vecinos transitables del nodo actual en el mapa
def vecinos(nodo, mapa):
    x, y = nodo
    # Posibles movimientos: abajo, arriba, derecha, izquierda
    resultados = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    # Filtra posiciones dentro del rango del mapa
    resultados = filter(lambda pos: 0 <= pos[0] < len(mapa) and 0 <= pos[1] < len(mapa[0]), resultados)
    # Filtra posiciones transitables
    return filter(lambda pos: mapa[pos[0]][pos[1]] != 999, resultados)

# Implementación del algoritmo A* para encontrar la ruta más corta en el mapa
def a_estrella(mapa, inicio, fin):
    cola = []  # Cola de prioridad para explorar nodos según su costo estimado
    heapq.heappush(cola, (0, inicio))  # Agregar el nodo de inicio con costo inicial 0 a la cola
    costos = {inicio: 0}  # Diccionario para almacenar los costos mínimos conocidos para cada nodo
    caminos = {inicio: None}  # Diccionario para almacenar el camino hacia cada nodo

    while cola:
        costo, actual = heapq.heappop(cola)  # Obtener el nodo actual de la cola según su costo estimado

        if actual == fin:
            camino = []
            while actual:
                camino.append(actual)  # Construir el camino desde el fin hasta el inicio
                actual = caminos[actual]
            camino.reverse()  # Invertir el camino para mostrarlo desde el inicio hasta el fin
            return camino, costo  # Retornar el camino y su costo total

        for vecino in vecinos(actual, mapa):
            nuevo_costo = costos[actual] + (mapa[vecino[0]][vecino[1]] if mapa[vecino[0]][vecino[1]] != 0 else 1)  # Costo acumulado para llegar al vecino
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo  # Actualizar el costo mínimo conocido para el vecino
                prioridad = nuevo_costo + heuristica(fin, vecino)  # Calcular la prioridad para el vecino
                heapq.heappush(cola, (prioridad, vecino))  # Agregar el vecino a la cola con su prioridad
                caminos[vecino] = actual  # Registrar el camino hacia el vecino

    return None, 0  # Retornar None si no se encontró ruta, con costo 0

# Crear un mapa de ejemplo de 10x10
mapa = crear_mapa(10, 10)
mostrar_mapa(mapa)

# Permitir al usuario agregar obstáculos al mapa
agregar_obstaculos(mapa)

# Obtener coordenadas del punto de inicio y fin del usuario
inicio = obtener_coordenadas("Ingrese las coordenadas del inicio (x,y): ", mapa)
fin = obtener_coordenadas("Ingrese las coordenadas del final (x,y): ", mapa)

# Encontrar la ruta más corta utilizando el algoritmo A*
ruta, costo = a_estrella(mapa, inicio, fin)
if ruta:
    print(f"Se encontro una ruta, el costo total de la ruta será de: {costo}")
    for paso in ruta:
        print(paso)
else:
    print("Lastimosamente no se encontro ninguna ruta.")

# Mostrar el mapa con el camino encontrado
mostrar_mapa(mapa, inicio, fin, ruta)
