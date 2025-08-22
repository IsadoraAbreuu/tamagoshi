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
            print("Eu morri ;-;")

    #função que chamas os métodos essenciais
    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5




#classe para Tamagoshi Gato
class TamagoshiGato(Tamagoshi):
    #atributos para Tamagoshi Gato
    def __init__(self, nome):
        super().__init__(nome) #puxa atributos da classe pai
        self.energia = 100
        self.limpeza = 0

    #métodos para tamagoshi gato
    def banho(self):
        self.limpeza += 100
        print(f"{self.nome} tomou banho e está cheiroso(a) limpinho(a) e divo(A) (ᵔ ͜ʖ ͡ᵔ)")

    def arranharSofa(self):
        self.energia -= 20
        print(f"{self.nome} está arranhando TODO O SOFÁ ¯\_( ͡🔥 ͜ʖ ͡🔥)_/¯")

    def comerRatoPodre(self):
        self.fome -= 40
        self.limpeza -= 30
        print(f"que nojeira, {self.nome} está saciando a fome com ratos podres")   




#classe para Tamagoshi Cachorro
class TamagoshiCachorro(Tamagoshi):
    #atributos para Tamagoshi Cachorro
    def __init__(self, nome, ):
        super().__init__(nome) #puxa atributos da classe pai
        self.estahDormindo = False
        self.acessorio = ["roupinha", "touquinha", "óculos escuros", "fraldas", "boné", "coleira com pingente fofo", "crocs"]

    def soneca(self):
        if self.estahDormindo:
            print(f"{self.nome} já está dormindo, shhh")
        else:
            print(f"{self.nome} estava cansado e foi dar uma dormidinha")
            self.estahDormindo = True

    def estilo(self, acessorio):
        if acessorio not in self.acessorios:
            print(f"Não tem o acessório '{acessorio}'.")
            return
        self.acessorioAtual = acessorio
        print(f"{self.nome} agora está usando {acessorio}!")
        if self.fome > 80:
           print(f"{self.nome} está com tanta fome que acabou comendo {self.acessorio}")

    def pegarOsso(self):
        print(f"{self.nome} está se preparando para ir pegar o osso...")
    


#def pegar osso



#classe para Tamagoshi Passaro
class TamagoshiPassaro(Tamagoshi):
    #atributos para Tamagoshi Passaro
    def __init__(self, nome, assobio, plumagem):
        super().__init__(nome) #puxa atributos da classe pai
        self.assobio = assobio 
        self.plumagem = plumagem
    

    #métodos para tamagoshis pássaros
    def assobiar(self):
        print(f"O pássaro {self.nome} está assobiando! {self.assobio}")

    def mudancaPlumagem(self):
        if self.fome < 50:
            self.plumagem = f"{self.plumagem} claro"
            print(f"O pássaro {self.nome} está {self.plumagem} de TANTA fome (◎ ͜ʖ ͡◎) (pálido!!!)")
    
    def voar(self):
        if self.idade > 18:
            self.fome += 1
            print(f"{self.nome} está voando livremente")
        else:
            print(f"{self.nome} está querendo voar mas ainda é novinho...")
        

    def assobiar(self):
        print(f"O pássaro {self.nome} está assobiando! {self.assobio}")
    



passaro1 = TamagoshiPassaro("luli", "piu piu piuuuu", "roxa")

passaro1.mudancaPlumagem()
passaro1.assobiar()

passaro1.assobiar()
