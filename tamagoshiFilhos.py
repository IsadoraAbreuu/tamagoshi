import time
import random
from tamagoshi import Tamagoshi


#classe para Tamagoshi Gato
class TamagoshiGato(Tamagoshi):
    #atributos para Tamagoshi Gato
    def __init__(self, nome):
        super().__init__(nome) #puxa atributos da classe pai
        self.energia = 100
        self.limpeza = 0

    #métodos para tamagoshi gato
    def banho(self):  
        print("ligando a torneira 💧")
        time.sleep(1)
        print("esquentando água....")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print(f"a naaaaao, {self.nome} está fugindo")
        fugiu = input("conseguiu pegá-lo? \n[1] sim\n[2] não aquele safado(a) escapou")
        if fugiu == "2":
            print(f"BANHO CANCELADO, tente novamente outra hora, quando{self.nome} estiver mais calmo")
        elif fugiu == "1":
            self.limpeza += 100
            print(f"{self.nome} tomou banho e está cheiroso(a) limpinho(a) e divo(A) (ᵔ ͜ʖ ͡ᵔ)")

    def arranharSofa(self):
        self.energia -= 20
        print(f"{self.nome} está arranhando TODO O SOFÁ ( ͡🔥 ͜ʖ ͡🔥)")

    def comerRatoPodre(self):
        self.fome -= 20
        self.limpeza -= 30
        print(f"{self.nome} está comendo !!!")
        time.sleep(1)
        print("comendo ainda...")
        time.sleep(1)
        print("....")
        time.sleep(2)
        print("OPS")
        time.sleep(1)
        print(f"que nojeira, {self.nome} está saciando a fome com ratos podres")
        time.sleep(3)
        print("Agora está saciado, vamos relevar o que foi ingerido apenas \_(°o°)_/")   


#classe para Tamagoshi Cachorro
class TamagoshiCachorro(Tamagoshi):
    #atributos para Tamagoshi Cachorro
    def __init__(self, nome):
        super().__init__(nome) #puxa atributos da classe pai
        self.estahDormindo = False
        self.acessorio = ["roupinha", "touquinha", "óculos escuros", "fraldas", "boné", "coleira com pingente fofo", "crocs"]

    #métodos para tamagoshi cachorro
    def soneca(self):
        if self.estahDormindo:
            print(f"{self.nome} já está dormindo... shhh ")
            for _ in range(3):
                time.sleep(1)
                print("💤...")
            print("Acordou! Bom dia!")
            self.estahDormindo = False
        else:
            print(f"{self.nome} estava cansado e foi tirar uma sonequinha")
            self.estahDormindo = True
            for _ in range(3):
                time.sleep(1)
                print("💤...")
            print("uaaaaa (se espreguiçando)")
            print(f"{self.nome} acordou bem descansado(a)! ")
            self.estahDormindo = False

    def estilo(self, acessorio):
        print(f"{self.nome} está muito fof(o ou a) usando {self.acessorio}")
        if acessorio not in self.acessorio:
            print(f"Não tem o acessório '{acessorio}'.")
            return
        self.acessorioAtual = acessorio
        print(f"{self.nome} agora está usando {acessorio}!")
        if self.fome > 80:
           print(f"{self.nome} está com tanta fome que acabou comendo {self.acessorio}")

    def pegarOsso(self):
        while True:
            if not self.estahDormindo and self.fome < 60:
                print(f"{self.nome} está se preparando para ir pegar o osso...")
                time.sleep(2)
                print(f"{self.nome} saiu correndo igual doido atrás do osso omgggg")
                time.sleep(3)
                print(f"IHUUUUU {self.nome} pegou o osso!!!!")
                time.sleep(2)
                print(f"{self.nome} voltou com o osso todo bonitinho :)")
                time.sleep(2)
                self.fome -= 5
                print("----------------------------------------------------")
                continuarBrincando = input(f"Quer continuar brincando com {self.nome}?\n[1] SIMMMM\n[2] NÃO CANSEI\n")
                if continuarBrincando == 1:
                    continue
                else:
                    print("Você parou de brincar")
                    break
            else:
                print(f"Tente brincar de buscar o osso outra hora, agora {self.nome} está sleepando ou com fome :/")
                break

    

#classe para Tamagoshi Passaro
class TamagoshiPassaro(Tamagoshi):
    #atributos para Tamagoshi Passaro
    def __init__(self, nome, assobio=None):
        super().__init__(nome) #puxa atributos da classe pai
        self.assobio = assobio 
        self.plumagem = ["azul", "rosa", "laranja", "verde", "amarelo", "roxo", "vermelho", "preto", "branco"]

    #métodos para tamagoshis pássaros
    def assobiar(self):
        if self.assobio:
            print(f"O pássaro {self.nome} está assobiando!")
            time.sleep(2)
            print(f"{self.assobio} ...")
            time.sleep(2)
            print(f"{self.assobio} ...")
            time.sleep(2)
            print(f"{self.assobio} ...")
        else:
            print("O assobio ainda não foi definido :(")

    def mudancaPlumagem(self):
        sortearPlumagem =  random.choice(self.plumagem)
        print(f"{self.nome} agora é {sortearPlumagem}!!!!")
        if self.fome < 50:
            self.plumagem = f"{self.plumagem} claro"
            print(f"O pássaro {self.nome} está {self.plumagem} de TANTA fome (pálido!!!)")
    
    def voar(self):
        if self.idade > 18:
            self.fome += 1
            print(f"{self.nome} está voando livremente")
        else:
            print(f"{self.nome} está querendo voar mas ainda é novinho...")
        

    