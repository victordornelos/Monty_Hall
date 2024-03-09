import plotly.graph_objs as go
import pandas as pd
import random

# Função para simular o problema de Monty Hall
def Monty_Hall():
    recompensas = ["vazio", "vazio", "R$ 1.000.000,00"]
    opcoes = {1: recompensas[0], 2: recompensas[1], 3: recompensas[2]}
    premio = set([i for i in opcoes if opcoes[i] == "R$ 1.000.000,00"])

    random.shuffle(recompensas)
    escolha = set([random.randint(1, 3)])
    abertura = set([random.choice(list(set(opcoes.keys()) - escolha - premio))])

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

# Função para realizar a simulação e coletar os dados
def realizar_simulacao(n):
    decisao = []
    resultado = []

    for _ in range(n):
        t, g = Monty_Hall()
        decisao.append(t)
        resultado.append(g)
    
    df = pd.DataFrame({'Decisão': decisao, 'Resultado': resultado})
    payoff = pd.crosstab(df['Decisão'], df['Resultado'])
    return payoff

# Realiza a simulação
payoff = realizar_simulacao(10000)

# Cria o gráfico de pizza interativo
fig = go.Figure()

fig.add_trace(go.Pie(
    labels=['Vitórias', 'Derrotas'],
    values=payoff.loc['Manteve', ['Venceu', 'Perdeu']],
    name='Manteve',
    hoverinfo='label+percent',
    textinfo='value+percent',
    hole=0.3,
    marker=dict(colors=['#36D9FC', '#FF5733']),
    domain=dict(x=[0, 0.5])
))

fig.add_trace(go.Pie(
    labels=['Vitórias', 'Derrotas'],
    values=payoff.loc['Trocou', ['Venceu', 'Perdeu']],
    name='Trocou',
    hoverinfo='label+percent',
    textinfo='value+percent',
    hole=0.3,
    marker=dict(colors=['#36D9FC', '#FF5733']),
    domain=dict(x=[0.5, 1])
))

fig.update_layout(
    title='Porcentagem de Vitórias e Derrotas',
    annotations=[
        dict(text='Manteve', x=0.2, y=0.5, font_size=12, showarrow=False),
        dict(text='Trocou', x=0.8, y=0.5, font_size=12, showarrow=False)
    ]
)

fig.show()
