# Esto es un comentario
"""Esto es un DocString  """

l = [1,2,3,4,10,8,6]

for x in l:
    print(x)

for x in range(10):
    print("Linea ",x)

# for x in 7:
#     print("Linea ",x)

print("Longitud de la lista l:",len(l))
print("Max(l)",max(l))
print("Min(l)",min(l))
print(l.index(2))

lista = ["Managua","León","Rivas","Estelí","Chinandega"]
buscar = "Rivas"
print(buscar," se encuentra en la posición ",lista.index(buscar), "de la lista ",lista)