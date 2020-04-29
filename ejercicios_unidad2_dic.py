lista = {"Euro":"€","Dollar":"$","Yen":"Y"}
moneda = input("Digite moneda:")
valor = lista.get(moneda)
if valor:
    print("Moneda:",moneda,"-Símbolo",valor)
else:
    print("La moneda",moneda,"no se encuentra registrada")

print("+++++++++++++++++++++++++++")
nombre = input("Nombre:")
edad   = input("Edad:")
dire   = input("Dirección:")
tel    = input("Teléfono:")

usuario = dict(nombre=nombre,edad=edad,direccion=dire,telefono=tel)
print(usuario)
print(usuario.get("nombre"),"tiene", \
    usuario.get("edad"),"vive en",usuario.get("direccion"), \
        "su num. teléfono es",usuario.get("telefono"))