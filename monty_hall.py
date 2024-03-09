# Bibliotecas
import pandas as pd
import random

# Modelo de Monty_Hall
def Monty_Hall():
    
    #Construindo o cenário do Jogo
    recompensas = ["vazio","vazio","R$: 1.000.000,00"]
    opcoes = {1:recompensas[0], 2:recompensas[1], 3:recompensas[2]}
    premio = set([ i  for i in opcoes if opcoes[i] == "R$: 1.000.000,00"])

    #Construindo as ações da primeira escolha
    random.shuffle(recompensas)
    escolha = set([random.randint(1,3)])
    abertura = set([random.choice(list(set(opcoes.keys()) - escolha - premio))])

    #Construindo as ações da segunda escolha
    nova_opcao = set([random.choice(list(set(opcoes.keys()) - abertura))])
    if escolha == nova_opcao:
        decisao = 'Manteve'
    else:
        decisao = 'Trocou'

    if nova_opcao == premio:
        resultado = 'Venceu'
    else:
        resultado = 'Perdeu'

    return decisao, resultado

#Resultado da partida
decisao, resultado = Monty_Hall()

#Criando um loop
def Loop(n=10000):
    decisao = []
    resultado = []

    for i in range(n):
        t, g = Monty_Hall()
        decisao.append(t)
        resultado.append(g)
    
    return pd.DataFrame({'Decisão': decisao, 'Resultado': resultado})

#Coletando os resultados
dados = Loop()
payoff = pd.crosstab(dados['Decisão'],dados['Resultado'])

# Analisando os resultados de manter
vitorias_manteve = payoff.loc['Manteve', 'Venceu']
derrotas_manteve = payoff.loc['Manteve', 'Perdeu']
total_manteve = vitorias_manteve + derrotas_manteve
porcentagem_vitorias_manteve = (vitorias_manteve / total_manteve) * 100
porcentagem_derrotas_manteve = (derrotas_manteve / total_manteve) * 100
novo_df = pd.DataFrame({
    'Decisão': ['Manteve'],
    'Porcentagem de Vitórias': [porcentagem_vitorias_manteve],
    'Porcentagem de Derrotas': [porcentagem_derrotas_manteve]
})

# Analisando os resultados de trocar
vitorias_trocou = payoff.loc['Trocou', 'Venceu']
derrotas_trocou = payoff.loc['Trocou', 'Perdeu']
total_trocou = vitorias_trocou + derrotas_trocou
porcentagem_vitorias_trocou = (vitorias_trocou / total_trocou) * 100
porcentagem_derrotas_trocou = (derrotas_trocou / total_trocou) * 100
novo_df = pd.DataFrame({
    'Decisão': ['Trocou'],
    'Porcentagem de Vitórias': [porcentagem_vitorias_trocou],
    'Porcentagem de Derrotas': [porcentagem_derrotas_trocou]
})