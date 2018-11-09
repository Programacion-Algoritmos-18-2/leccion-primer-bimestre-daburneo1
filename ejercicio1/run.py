#Crear empleado
from mipaquete.modelo import *
e = Empleado()
e.agregar_nombre("Luis")
e.agregar_apellido("Benitez")
e.agregar_cedula("1110001")

print(e.presentar_datos())

e1 = EmpleadoPorHoras()
nombre = input ("Ingrese su nombre ")
e1.agregar_nombre(nombre)
e1.agregar_apellido("andrade")
e1.agregar_cedula("112235")
e1.agregar_comision_fija(50)
e1.agregar_valor_hora(20.2)
e1.agregar_numero_horas(15)
print(e1.presentar_datos())

e2 = EmpleadoFijo()
e2.agregar_sueldo_fijo(300.2)
e2.agregar_descuento_seguro(10) #Porcentaje
comision = input("ingrese comision \n")
comision = float(comision) #Conversion de dato tipo cadena a float
e2.agregar_comision_fija(comision)
e2.nombre = "Ana"
e2.apellido = "Diaz"
print(e2.presentar_datos())

#e3 = EmpleadoPorSemana()
#e3.agregar_numero_semanas(5)
#e3.agregar_valor_semanal(40)
#e3.nombre = "Juan"
#e3.apellido = "Perez"
#print(e3.presentar_datos())