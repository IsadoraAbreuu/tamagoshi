

#classe Tamagoshi - classe pai
class Tamagoshi:
    #atributos do Tamagoshi normal - padrão
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    #métodos essenciais para todos os Tamagoshis
    def alimentar(self, quantidade):
        if quantidade < 0:
            self.fome = 0
        elif (quantidade <= 100):
            self.fome -= 10
            print(f"Você alimentou {self.nome}")

    def brincar(self):
        if self.tedio < 0:
            self.tedio = 0
        elif self.tedio <= 100:
            self.tedio -= 20
            print(f"Você brincou com {self.nome}")
    
    def vida(self):
        self.fome = max(0, min(self.fome, 100))
        self.tedio = max(0, min(self.tedio, 100))
        if 50 < self.fome <= 60 or 50 < self.tedio <= 60:
            self.saude -= 10
        elif 60 < self.fome <= 80 or 60 < self.tedio <= 80:
            self.saude -= 30
        elif 80 < self.fome <= 90 or 80 < self.tedio <= 90:
            self.saude -= 50
        elif self.fome > 90 or self.tedio > 90:
            self.saude -= 70
            print(" Estou morrendo... AAAAAAAAH")
        if self.fome >= 100 or self.tedio >= 100 or self.saude <= 0:
            self.saude = 0
            print(" Eu morri 💀")


    #função que chama os métodos essenciais
    def tempoPassando(self):
        self.idade += 5
        self.tedio += 10
        self.fome += 20
        self.vida()










