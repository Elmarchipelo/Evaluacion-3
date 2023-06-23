from msilib.schema import SelfReg
from typing import Self


class vehiculo:
    def __init__(self, tipo, patente, marca, precio, multas, fecharegistro, nombredueño):
        if isinstance(tipo,str):
            self.tipo = tipo

        else:
            raise
        TypeError("El tipo debe ser definido")
        if isinstance(patente,str) and len(patente) == 6:
            self.patente = patente

        else:
            raise
        ValueError("La patente debe ser de 6 caracter")
        if isinstance(marca,str) and 2 <= 15:
           self.marca = marca 

        else:
            raise
        ValueError("La marca debe tener entre 2 a 15 caracter")
        if isinstance(precio,int) and precio>5000000:
            self.precio = precio 

        else:
            raise
        ValueError("Debe tener un valor de 5 millones")
        if isinstance(multas,list):
            for multa in multas:
                if isinstance(multa,tuple) and len(multa) == 2:
                    monto,fecha = multa
                    if isinstance(monto, int) and isinstance(fecha, str):
                        pass 
                    else:
                        raise

                    ValueError("La multa debe ser con un numero entero")
                    if isinstance(fecharegistro, str):
                        pass
                    self.fecharegistro= fecharegistro
                else:
                    raise

                TypeError("La Fecha debe ser la correcta")
                if isinstance(nombredueño, str): 
                    self.nombredueño = nombredueño
                else:
                    raise

                TypeError("Debe colocar un nombre valido")
def imprimircertificado(self):
    import random 
    monto = random.randint(1500, 3500)

    print (f"El certificado tiene un costo de{monto}")

    print (f"Patente del vehiculo: {self.patente}")

    print (f"Datos del dueño:{self.nombredueño}")
    if self.multas:

        print(f"El vehiculo tiene{len(self.multas)}multas vigente")
for multa in SelfReg.multas:
    
    print(f"Multa de {multa[0]}pesos el {multa[1]}")
else:
    print(f"El vehiculo no tiene multas actuales")

                
                
