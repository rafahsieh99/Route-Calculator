# Route-Calculator
## Algoritmo A* para Búsqueda de Rutas en un Mapa
Este proyecto implementa el algoritmo A* para encontrar la ruta más corta en un mapa con obstáculos. 
El usuario puede crear un mapa, agregar diferentes tipos de obstáculos y encontrar la ruta más eficiente entre dos puntos especificados.

## Características

- **Crear Mapa:** Genera un mapa rectangular de tamaño especificado.
- **Agregar Obstáculos:** Permite al usuario agregar edificios, baches y agua al mapa.
- **Visualizar Mapa:** Muestra el mapa con los obstáculos y la ruta encontrada.
- **Búsqueda de Ruta:** Utiliza el algoritmo A* para encontrar la ruta más corta entre dos puntos.

## Uso
**Crear el Mapa:**
El script solicitará las dimensiones del mapa (número de filas y columnas).

**Añadir Obstáculos:**
Los usuarios pueden añadir los siguientes obstáculos:
X para edificios (costo muy alto)
#para baches (costo medio)
! para agua (costo medio)
Para finalizar la adición de obstáculos, escribe basta.

**Ingresar Coordenadas:**
El script solicitará las coordenadas del punto de inicio y del punto final.

Encontrar la Ruta:
El algoritmo A* calculará la ruta más corta y mostrará el mapa con la ruta encontrada.
