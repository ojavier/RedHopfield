def crear_pesos(patrones):
	"""Crea la matriz de pesos con la regla de Hebb."""
	cantidad_neuronas = len(patrones[0])
	pesos = []

	# Inicializamos una matriz llena de ceros.
	for i in range(cantidad_neuronas):
		fila = []
		for j in range(cantidad_neuronas):
			fila.append(0)
		pesos.append(fila)

	# Sumamos el producto de cada patron por si mismo.
	for patron in patrones:
		for i in range(cantidad_neuronas):
			for j in range(cantidad_neuronas):
				pesos[i][j] += patron[i] * patron[j]

	# Una neurona no se conecta consigo misma.
	for i in range(cantidad_neuronas):
		pesos[i][i] = 0

	return pesos


def activar(valor, valor_anterior):
	# La funcion escalon usa el valor anterior cuando la suma es cero.
	if valor > 0:
		return 1
	elif valor < 0:
		return -1
	else:
		return valor_anterior


def recordar(patron, pesos, maximo_iteraciones=10):
	"""Actualiza el patron hasta que la red se estabiliza."""
	estado = patron[:]
	cantidad_neuronas = len(estado)

	for iteracion in range(maximo_iteraciones):
		nuevo_estado = []

		# Calculamos la entrada de cada neurona.
		for i in range(cantidad_neuronas):
			suma = 0
			for j in range(cantidad_neuronas):
				suma += pesos[i][j] * estado[j]
			nuevo_estado.append(activar(suma, estado[i]))

		if nuevo_estado == estado:
			return estado

		estado = nuevo_estado

	return estado


def mostrar_matriz(matriz):
	for fila in matriz:
		print(fila)


# Patrones que la red aprendera.
patrones = [
	[1, 1, 1, -1],
	[-1, -1, -1, 1],
]

pesos = crear_pesos(patrones)

print("Matriz de pesos:")
mostrar_matriz(pesos)

# Este patron tiene un valor cambiado y la red intenta corregirlo.
patron_ruidoso = [1, 1, -1, -1]
print("\nPatron de entrada:", patron_ruidoso)
resultado = recordar(patron_ruidoso, pesos)
print("Patron recuperado:", resultado)
