# Primer Ejercicio
print("----Primer Ejercicios ----")
asignaturas = ["PostgreSQL","Python+Django","UML","Git"]
for asignatura in asignaturas:
    print("Yo estudio",asignatura)

print("----Segundo Ejercicios ----")
asignaturas = ["PostgreSQL","Python+Django","UML","Git"]
notas = []
for asignatura in asignaturas:
    nota = input("Digite Nota para {} :".format(asignatura))
    notas.append(nota)

# print(notas)
# En <asignatura> tu nota es <nota>
print(asignaturas,notas)
for indice,asignatura in enumerate(asignaturas,0):
    print("En",asignatura,"tu nota es",notas[indice])
print("++++++++++++++++++++++++")
tam = len(asignaturas)
for i in range(tam):
    print("En",asignaturas[i],"tu nota es",notas[i])