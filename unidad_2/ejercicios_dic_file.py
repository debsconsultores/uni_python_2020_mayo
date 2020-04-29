f = open("datos_usuarios.txt","r")
nombre = f.readline()
edad   = f.readline()
dire   = f.readline()
tel    = f.readline()
f.close()

usuario = dict(nombre=nombre,edad=edad,direccion=dire,telefono=tel)
print(usuario)
print(usuario.get("nombre"),"tiene", \
    usuario.get("edad"),"vive en",usuario.get("direccion"), \
        "su num. teléfono es",usuario.get("telefono"))