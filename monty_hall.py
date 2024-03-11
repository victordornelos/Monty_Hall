# Bibliotecas para o jogo
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
def Loop(n=100000):
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

resultado_payoff = pd.DataFrame({
    'Decisão': ['Manteve', 'Trocou'],
    'Porcentagem de Vitórias': [porcentagem_vitorias_manteve, porcentagem_vitorias_trocou],
    'Porcentagem de Derrotas': [porcentagem_derrotas_manteve, porcentagem_derrotas_trocou]
})

# Bibliotecas para os gráficos
import seaborn as sns
import matplotlib.pyplot as plt
import mplcyberpunk #Opcional
plt.style.use('cyberpunk')#Opcional

# Definindo as cores para cada resultado 
cores = ["#4B51FA", "#FA4BA3"]  # Cor para Vitória e Derrota, respectivamente 
#https://color.adobe.com/pt/create/color-wheel pode escolher as cores nesse site

#Criando o gráfico de manter a escolha

# Organizando os dados para o gráfico de manter
fim_manter = ['Vitória','Derrota']
porcentagem_manter = [porcentagem_vitorias_manteve, porcentagem_derrotas_manteve]
dados_grafico_manteve = dict(zip(fim_manter, porcentagem_manter))
fim_manter = list(dados_grafico_manteve.keys())
porcentagem_manter = list(dados_grafico_manteve.values())

# Configurando um gráfico de setores (pizza) para decisão de manter
sns.set_context("talk")
plt.figure(figsize=(15, 15))
plt.pie(porcentagem_manter, labels=fim_manter, autopct='%1.2f%%', startangle=0, colors=cores)
legenda = plt.legend(title="Resultado", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=14)
for text, color in zip(legenda.get_texts(), cores):
    text.set_color(color)
plt.setp(legenda.get_title(), fontsize=16, color='White')
plt.title('Comparação entre vitória e derrota no caso de manter', fontsize=24, fontweight='bold')
plt.axis('equal')
plt.show()

# Gráfico de trocar a escolha

# Organizando os dados para o gráfico
fim_trocou = ['Vitória','Derrota']
porcentagem_trocou = [porcentagem_vitorias_trocou, porcentagem_derrotas_trocou]
dados_grafico_trocou = dict(zip(fim_trocou, porcentagem_trocou))
fim_trocou= list(dados_grafico_trocou.keys())
porcentagem_trocou = list(dados_grafico_trocou.values())

# Configurando um gráfico de setores (pizza) para decisão de trocar
sns.set_context("talk")
plt.figure(figsize=(15, 15))
plt.pie(porcentagem_trocou, labels=fim_trocou, autopct='%1.2f%%', startangle=0, colors=cores)
legenda = plt.legend(title="Resultado:", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=14)
for text, color in zip(legenda.get_texts(), cores):
    text.set_color(color)
plt.setp(legenda.get_title(), fontsize=16, color='White')
plt.title('Comparação entre vitória e derrota no caso de trocar', fontsize=24, fontweight='bold')
plt.axis('equal')
plt.show()







