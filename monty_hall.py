import random
import pandas as pd

def Monty_Hall():
    
    recompensas = ["vazio","vazio","R$: 1.000.000,00"]

    random.shuffle(recompensas)

    opcoes = {1:recompensas[0], 2:recompensas[1], 3:recompensas[2]}
    escolha = set([random.randint(1,3)])
    premio = set([ i  for i in opcoes if opcoes[i] == "R$: 1.000.000,00"])
    abertura = set([random.choice(list(set(opcoes.keys()) - escolha - premio))])
    nova_opcao = set([random.choice(list(set(opcoes.keys()) - abertura))])

    if escolha == nova_opcao:
        trocou = 0

    else:
        trocou = 1

    if nova_opcao == premio:
        ganhou = 1
    else:
        ganhou = 0

    return trocou, ganhou

def ite_run(n = 10000):
    trocas = []
    ganhos = []

    for i in range(n):
        
        t,g = Monty_Hall()
        trocas.append(t)
        ganhos.append(g)
    
    return pd.DataFrame({'trocas':trocas,"ganhos": ganhos})

df = ite_run( )