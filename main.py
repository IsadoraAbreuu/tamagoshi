import time
from tamagoshi import Tamagoshi
from tqdm import tqdm
from tamagoshiFilhos import TamagoshiCachorro, TamagoshiGato, TamagoshiPassaro
from time import sleep

#define cores 
azul = "\033[94m" #cachorro
rosa = "\033[95m" #gato
amarelo = "\033[93m" #amarelo
reset = "\033[0m" #reseta a cor após o uso

def main():
    print("\033c")
    print("********** BEM VINDO AO MUNDO DE TAMAGOSHIS ********** ")
    time.sleep(3)
    print("Mas antes de tudo...")
    time.sleep(1)
    nomeUsuario = input("Qual é seu nome? \nDigite aqui:")
    time.sleep(2)
    print(f"\nSeja Bem Vindo(a) {nomeUsuario}")
    print("--------------------------------------------------------\n")
    time.sleep(3)
    print("HORA DE ESCOLHER SEU TAMAGOSHI: ")
    print(" [1] Tamagoshi GATO\n [2] Tamagoshi CACHORRO\n [3] Tamagoshi PÁSSARO")
    escolhaTamagoshi = input("Digite aqui: ")

    tamagoshi = None
    if escolhaTamagoshi == "1":
        print(f"Ihu OK, você escolheu o {rosa}Tamagoshi GATO{reset}")
        time.sleep(1)
        nome = input(f"Qual será o nome de {rosa}Tamagoshi gatinho? {reset}")
        print(f"\nUm novo Tamagoshi está nascendo...")
        time.sleep(2)
        print(f"Preparando o mundo para receber o {nome}...")
        time.sleep(2)
        tempo()
        print(f"Parabéns! {rosa}{nome} acaba de chegar ao mundo Tamagoshi!{reset} 🐱🐱🐱")
        time.sleep(1)
        print(f"Vamos cuidar dele!! \n")
        time.sleep(1)
        tamagoshi = TamagoshiGato(nome)

    elif escolhaTamagoshi == "2":
        print(f"{azul}Ihu OK, você escolheu o {azul}Tamagoshi CACHORRO{reset}")
        time.sleep(1)
        nome = input(f"Qual será o nome de seu {azul}Tamagoshi cachorrinho? {reset}")
        print(f"\nUm novo Tamagoshi está nascendo...")
        time.sleep(2)
        print(f"Preparando o mundo para receber o {nome}...")
        time.sleep(2)
        tempo()
        print(f"Parabéns! {azul}{nome} acaba de chegar ao mundo Tamagoshi!{reset} 🐶🐶🐶")
        time.sleep(1)
        print(f"Vamos cuidar dele!! \n")
        time.sleep(1)
        tamagoshi = TamagoshiCachorro(nome)

    elif escolhaTamagoshi == "3":
        print(f"{amarelo}Ihu OK, você escolheu o {amarelo}Tamagoshi PÁSSARO{reset}")
        time.sleep(1)
        nome = input(f"Qual será o nome de seu {amarelo}Tamagoshi pássarozinho? {reset}")
        print(f"\nUm novo Tamagoshi está nascendo...")
        time.sleep(2)
        print(f"Preparando o mundo para receber o {nome}...")
        time.sleep(2)
        tempo()
        print(f"Parabéns! {amarelo}{nome} acaba de chegar ao mundo Tamagoshi!{reset} 🐦🐦🐦")
        time.sleep(1)
        print(f"Vamos cuidar dele!! \n")
        time.sleep(1)
        tamagoshi = TamagoshiPassaro(nome)
    else:
        print("Opção inválida. Tente novamente")
        return

    # loop interage com os tamagoshis
    while True:
        mostrar_status(tamagoshi)
        print("\n************ ❗ MENU ❗ ************")
        print(f"\nO que você quer fazer com {tamagoshi.nome}?")
        print("[0] Sair")
        print("[1] Alimentar")
        print("[2] Brincar")
        print("[3] Passar tempo")
        if isinstance(tamagoshi, TamagoshiGato):
            print("[4] Dar banho")
            print("[5] Alimentar (alimentação diferenciada)")
            print("[6] Ser legal e deixar arranhar o sofá")
        elif isinstance(tamagoshi, TamagoshiCachorro):
            print("[4] Tirar uma soneca")
            print("[5] Escolher acessório")
            print("[6] Brincar de pegar osso")
        elif isinstance(tamagoshi, TamagoshiPassaro):
            print("[4] Assobiar")
            print("[5] Mudar plumagem")
         
            
        opcao = input("Digite aqui a opção: \n")
        time.sleep(2)
        print("----------------------------\n")
        if opcao == "0":
            tempo()
            print(f"Saindo... {nome} está indo de berço")
            break
        elif opcao == "1":
            qtd_comida = input("Quanto deseja alimentar: ")
            tamagoshi.alimentar(qtd_comida)
            print(f"{tamagoshi.nome} foi alimentado!!!")
        elif opcao == "2":
            qtd_brincar = input("Quanto deseja brincar: ")
            tamagoshi.brincar(qtd_brincar)
            print(f"{tamagoshi.nome} brincou {qtd_brincar} vez(es)")
        elif opcao == "3":
            tamagoshi.tempoPassando()
            print("UOU")
            print("Você passou 5 anos para frente !!!!!!!!")

        if isinstance(tamagoshi, TamagoshiGato):
            if opcao == "4":
                tamagoshi.banho()
            elif opcao == "5":
                tamagoshi.comerRatoPodre()
            elif opcao == "6":
                tamagoshi.arranharSofa()
        elif isinstance(tamagoshi, TamagoshiCachorro):
            if opcao == "4":
                tamagoshi.soneca()
            elif opcao == "5":
                print(f"Os acessórios disponíveis são: {tamagoshi.acessorio}")
                definirAcessorio = input("Qual deseja escolher? ")
                tamagoshi.acessorio = definirAcessorio
                tamagoshi.estilo(tamagoshi.acessorio)
            elif opcao == "6":
                tamagoshi.pegarOsso()
        elif isinstance(tamagoshi, TamagoshiPassaro):  
            if opcao == "4":
                definirAssobio = input(f"Defina o assobio de {tamagoshi.nome}: ")  
                tamagoshi.assobio = definirAssobio
                tamagoshi.assobiar()
            elif opcao == "5":
                tamagoshi.mudancaPlumagem()
                
        
def mostrar_status(tamagoshi):
    print("\n************ 📋 STATUS DO TAMAGOSHI: ************")
    print(f"📍 Nome: {tamagoshi.nome}")
    print(f"🔞 Idade: {tamagoshi.idade}")
    print(f"🤕 Saúde: {tamagoshi.saude}")
    print(f"🍝 Fome: {tamagoshi.fome}")
    print(f"😒 Tédio: {tamagoshi.tedio}")
    if isinstance(tamagoshi, TamagoshiGato):
        print(f"🐱 Tipo:{rosa} Gato{reset}")
        print(f"🧼 Limpeza: {tamagoshi.limpeza}")
        print(f"⚡ Energia: {tamagoshi.energia}")
    elif isinstance(tamagoshi, TamagoshiCachorro):
        print(f"🐶 Tipo: {azul}Cachorro{reset}")
        print(f"💤 Está dormindo: {'Sim' if tamagoshi.estahDormindo else 'Não'}")
        print(f"🎒 Acessório: {tamagoshi.acessorio if hasattr(tamagoshi, 'acessorio') else 'Nenhum'}")
    elif isinstance(tamagoshi, TamagoshiPassaro):
        print(f"🐦 Tipo: {amarelo}Pássaro{reset}")
        print(f"💨 Assobio: {tamagoshi.assobio if getattr(tamagoshi, 'assobio', None) else 'Nenhum'}")
        print(f"🌈 Plumagem: {tamagoshi.plumagem}")

def tempo():
    for i in tqdm(range(100)):
        sleep(0.02)


main()

