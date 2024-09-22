def calcular_descuento(monto_total, porcentaje_descuento=22):

    #Esto para saber el descuento
    descuento= (monto_total * porcentaje_descuento) / 100
    return descuento

def main():
    #Llamada uno (monto total)
    monto1= 440
    descuento1= calcular_descuento(monto1)
    monto_final1= monto1 - descuento1

    print(f"El monto total es: ${monto1:.2f}")
    print(f"Descuento especial: ${descuento1:.2f}")
    print(f"Valor final a pagar: ${monto_final1:.2f}")
    print() #Esto para separar

    #Segunda llamada (monto total y porcentaje de descuento)
    monto2= 5250  #Otro ejemplo
    porcentaje2= 30
    descuento2= calcular_descuento(monto2, porcentaje2)
    monto_final2= monto2 - descuento2

    print(f"Valor total: ${monto2:.2f}")
    print(f"Descuento: ${descuento2:.2f}")
    print(f"El monto final a pagar: ${monto_final2:.2f}")
#Llamar a la función principal
if __name__ == "__main__":
    main()


