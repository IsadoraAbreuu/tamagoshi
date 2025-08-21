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
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade /100)

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade/100)

    def getHumor(self):
        return 100 - ((self.fome + self.tedio)/2)
    
    def vida(self):
        if (self.fome > 50 and self.fome <= 60) or (self.tedio > 50 and self.tedio <=60):
            self.saude -= 10
        elif (self.fome > 60 and self.fome <= 80) or (self.tedio > 60 and self.tedio <=80):
            self.saude -= 30
        elif (self.fome > 80 and self.fome <= 90) or (self.tedio > 80 and self.tedio <=90):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            self.saude -= 70   
            print("Estou morrendo... AAAAAAAAH")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0   
            print("Seu bichinho morreu T_T")

    #função que chamas os métodos essenciais
    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5


#classe para Tamagoshi Gato
class TamagoshiGato(Tamagoshi):
    #atributos para Tamagoshi Gato
    def __init__(self, nome, energia, banho):
        super().__init__(self, nome) #puxa atributos da classe pai
        self.energia = energia
        self.banho = banho

    #m


#classe para Tamagoshi Cachorro
class TamagoshiCachorro(Tamagoshi):
    #atributos para Tamagoshi Cachorro
    def __init__(self, nome, passear, treinar):
        super().__init__(self, nome) #puxa atributos da classe pai
        self.passear = passear
        self.treinar = treinar


#classe para Tamagoshi Passaro
class TamagoshiPassaro(Tamagoshi):
    #atributos para Tamagoshi Passaro
    def __init__(self, nome, assobio, plumagem):
        super().__init__(nome) #puxa atributos da classe pai
        self.assobio = assobio 
        self.plumagem = plumagem
    
    def assobiar(self):
        print(f"O pássaro {self.nome} está assobiando! {self.assobio}")
    



passaro1 = TamagoshiPassaro("luli", "piu piu piuuuu", "roxa")

passaro1.assobiar()
