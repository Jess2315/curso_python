class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ruedas = 4
        self.en_marcha = False

    def encender(self):
        self.en_marcha = True
        print("Estoy encendido")

    def frenar(self):
        print("Estoy frenando")

    def acelerar(self):
        print("Estoy acelerando")

    def info(self):
        print(f"Mi vehículo marca: {self.marca}, modelo: {self.modelo}, ruedas: {self._ruedas}, en marcha: {self.en_marcha}")

class Moto(Vehiculo):
    def __int__(self, marca, modelo):
        super().__init__(marca, modelo)

    def caballito(self):
        print("Estoy haciendo caballito")

        print("Uso de clases")
v1 = Vehiculo("Ford", "F150")
v1.encender()
v1.acelerar()
v1.frenar()
v1.info()

v2 = Vehiculo("Mazda", "Modelo 1")
v2.acelerar()
v2.info()

v3 = Moto("Marca2", "modelo2")
v3.frenar()
v3.caballito()
v3.info()

