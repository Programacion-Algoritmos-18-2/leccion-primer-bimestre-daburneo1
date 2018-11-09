class Empleado(object):
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.cedula = 0
        self.comision_fija = 0
#Metodos agragar y obtener para nombre, apellido, cedula y comision
    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_apellido(self, a):
        self.apellido = a

    def obtener_apellido(self):
        return self.apellido

    def agregar_cedula(self, c):
        self.cedula = c

    def obtener_cedula(self):
        return self.cedula

    def agregar_comision_fija(self,cf):
        self.comision_fija = cf

    def obtener_comision_fija(self):
        return self.comision_fija
#Se presentan los datos principales
    def presentar_datos(self):
        return "%s-%s-%s-%s" % (self.obtener_nombre(), self.apellido, self.cedula, self.comision_fija)
#Clase para realizar el calculo del empleado por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self):
        super(EmpleadoPorHoras, self).__init__() 
        #Nuevos atributos
        self.numero_horas = 0
        self.valor_hora = 0
    #Metodos agregar y obtener    
    def agregar_numero_horas(self, nh):
        self.numero_horas = nh

    def obtener_numero_horas(self):
        return self.numero_horas

    def agregar_valor_hora(self, vh):
        self.valor_hora = vh

    def obtener_valor_hora(self):
        return self.valor_hora
    #Se realiza el calculo del sueldo final
    def calcular_valor_sueldo_final(self):
        
        sueldo_final = (self.obtener_numero_horas() * self.obtener_valor_hora()) + (self.obtener_comision_fija()) #Primero realizo la multiplicacipon del numero de horas por el precio de cada hora y luego le aumento el valor de la comision fija
        return sueldo_final #Enviar el valor
    #Presento los datos resultantes
    def presentar_datos(self):
        cadena = "%s \n numero_horas: %s \n valor_hora: %s \n sueldo_final: %s" % (super(EmpleadoPorHoras, self).presentar_datos(), self.obtener_numero_horas(), self.obtener_valor_hora(), self.calcular_valor_sueldo_final())
        return cadena
#Clase para empleado fijo
class EmpleadoFijo(Empleado):
    def __init__(self):
        super(EmpleadoFijo, self).__init__()
        #Nuevos atributos
        self.sueldo_fijo = 0
        self.descuento_seguro = 0
    #Metodos agregar y obtener para los nuevos atributos
    def agregar_sueldo_fijo(self, sf):
        self.sueldo_fijo = sf

    def obtener_sueldo_fijo(self):
        return self.sueldo_fijo

    def agregar_descuento_seguro(self, ds):
        self.descuento_seguro = ds

    def obtener_descuento_seguro(self):
        return self.descuento_seguro

   #Calculo del sueldo final
    def calcular_valor_sueldo_final(self):
        sueldo_final = (self.obtener_sueldo_fijo() + self.obtener_comision_fija()) - (self.obtener_sueldo_fijo() * (self.obtener_descuento_seguro() / 100)) #Primero sumo el sueldo inicial y la commision fija, y luego le resto el resultado de la multiplicacion de sueldoo fijo y descuento dividido para 100 para restar el porcentaje
        return sueldo_final
    #Presento los datos resultantes
    def presentar_datos(self):
        cadena = "%s\n sueldo_fijo: %s \n descuento_seguro: %s \n Sueldo_final: %s" % (super(EmpleadoFijo, self).presentar_datos(), self.obtener_sueldo_fijo(), self.obtener_descuento_seguro(), self.calcular_valor_sueldo_final())
        return cadena

class EmpleadoPorSemana(Empleado):
    def __init__(self):
        super(EmpleadoPorSemana, self).__init__()
        #Nuevos atributos
        self.numero_Semanas = 0
        self.valor_semanal = 0

    def agregar_numero_semanas(self, ns): 
        self.numero_Semanas = ns

    def obtener_numero_semanas(self):
        return self.numero_Semanas

    def agregar_valor_semanal(self, vs):
        self.valor_semanal = vs

    def obtener_valor_semanal(self):
        return self.valor_semanal
        #Calculo del sueldo final
    def calcular_valor_sueldo_final(self):
        sueldo_final = self.numero_Semanas() * self.valor_semanal() #Multiplicar el numero de semanas por el valor semanal
        #Oresentar datos
    def presentar_datos(self):
        cadena = "%s ln numero_Semanas: %s ln valor_semanal: %s ln Sueldo_final: %s" % (super(EmpleadoPorSemana,self).presentar_datos(), self.obtener_numero_semanas(), self.obtener_valor_semanal(), self.calcular_valor_sueldo_final())
        return cadena



