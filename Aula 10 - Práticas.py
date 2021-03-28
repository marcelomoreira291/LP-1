class Carro:
    def __init__(self, cor, marca, modelo, sitMotor=True, velocidade=0):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.sitMotor = sitMotor
        self.velocidade = velocidade
        
    def mostrar(self):
        print(f"""
               Cor: {self.cor}
               Marca: {self.marca}
               Modelo: {self.modelo} 
        
                """)

    def acelerar(self, acres_vel):
        if self.sitMotor == False:
            print("Carro Desligado")
        else:
            self.velocidade += acres_vel
            print(f"Velocidade: {self.velocidade} Km/h")

    def desligar(self):
        self.sitMotor = False

    def ligar(self):
        self.sitMotor = True

 
c1 = Carro("Azul", "Fiat", "Fiat Uno")
c2 = Carro("Vermelho", "Toyota", "Corola")
c1.acelerar(12)
c1.zer_vel()
for i in range(10):
    c1.acelerar(i)
    if c1.vel == 60:
        break