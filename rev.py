
class Veiculo:
    def __init__(self, marca, ano_fabricacao, cor, quantidade_portas, modelo):
        self.marca = marca
        self.ano_fabricacao = ano_fabricacao
        self.cor = cor
        self.quantidade_portas = quantidade_portas
        self.modelo = modelo

    def andar(self):
        print(f"{self.modelo} andando")

    def parar(self):
        print(f"{self.modelo} parado")

    def imprimir(self):
        print(""
        "O veículo tem características:\n"
        f"Modelo: {self.modelo}\nMarca: {self.marca}\nAno de Fabricação: {self.ano_fabricacao}\n"
        f"Cor: {self.cor}\nQtd de portas: {self.quantidade_portas}\n")

#funcao carro que herda de veiculo
class Carro(Veiculo):
    def __init__(self, marca, ano_fabricacao, cor, quantidade_portas, modelo):
        super().__init__(marca, ano_fabricacao, cor, quantidade_portas, modelo)

    def bater_o_carro(self):
        print(f"O carro {self.modelo} {self.cor} bateu!")

#funcao moto que herda de veiculo
class Moto(Veiculo):
    def __init__(self, marca, ano_fabricacao, cor, quantidade_portas, modelo, quantidade_rodas):
        super().__init__(marca, ano_fabricacao, cor, quantidade_portas, modelo)
        self.quantidade_rodas = quantidade_rodas

    def garupa(self, quantidade_garupa):
        self.quantidade_garupa = quantidade_garupa
        print(f"na moto {self.modelo}, com {self.quantidade_rodas} rodas, estou levando {quantidade_garupa} pessoas")

#funcao caminhao que herda de veiculo
class Caminhao(Veiculo):
    def __init__(self, marca, ano_fabricacao, cor, quantidade_portas, modelo, quantidade_rodas):
        super().__init__(marca, ano_fabricacao, cor, quantidade_portas, modelo)
        self.quantidade_rodas = quantidade_rodas

    def carretas(self, quantidade_rodas,quantidade_carretas):
        if quantidade_rodas > 4:
            self.quantidade_carretas = quantidade_carretas
            print(f"O caminhão {self.modelo} tem {self.quantidade_carretas} carretas")
        else:
            print(f"O caminhão {self.modelo} tem {quantidade_rodas} rodas")

#funcao para chamar os objetos
def main():
    carro1 = Carro("Toyota", 2008, "Azul", 4, "Corolla")
    moto1 = Moto("Yamaha", 2020, "Rosa", 0, "scooter", 2)
    caminhao1 = Caminhao("Mercedes", 2017, "Amarelo", 2, "Truck", 6)

    moto1.garupa(2)
    caminhao1.carretas(2, 1)
    carro1.bater_o_carro()
 


main()