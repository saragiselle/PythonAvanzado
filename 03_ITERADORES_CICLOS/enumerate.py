"""enumerate(iterable, start=0)"""

nombres  = ["Paco", "Emilio", "Javier", "Ana"]
nombres_enumerados = enumerate(nombres, start = 5)

for indice, elemento in enumerate(nombres):
    print(indice, elemento)