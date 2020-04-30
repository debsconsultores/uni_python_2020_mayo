def calcular_iva(monto):
    return monto * 0.15

calc_iva = lambda monto:monto*0.15

def proceso():
    nombre = input("Nombre:")
    monto  = int(input("Valor:"))
    # iva    = calcular_iva(monto)
    iva    = calc_iva(monto)
    total  = monto + iva
    resultado = "{} \n\tValor = {}\n\tIva={}\n\tTotal={}". \
        format(nombre,monto,iva,total)
    print(resultado)
    f = open("salida_iva_1.txt","w")
    f.write(resultado)
    f.close()

proceso()