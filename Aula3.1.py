# Importando a Biblioteca
import pandas as pd

# Definindo a Função para Formatar
def formatar(valor):
    return "{:.2f}%".format(valor)

# Criando as Séries
vacinas = pd.Series([30000000,25000000,10000000,5000000])
populacao = pd.Series([213317639,214477744,215574303,216687971])

# Criando as Visualizações
print("------- Dados de Vacinação -------")
print(f"O Total de Pessoas Vacinadas foi: {vacinas.sum()}")
print(f"A Média de Pessoas Vacinadas foi: {vacinas.mean()}")

print("\n------- Dados da População -------")
print(f"O Total da População é: {populacao.sum()}")
print(f"A Média da População é: {populacao.mean()}")

tot_tx_vac = (vacinas.sum() / populacao.sum()) * 100
print(f"\nO Percentual de Pessoas Vacinadas foi: {tot_tx_vac:.2f}%")

tx_vac = ((vacinas / populacao) * 100).apply(formatar)
print("\n------- Percentual de Pessoas Vacinadas por Ano -------")
print(tx_vac)