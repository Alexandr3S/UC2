import pandas as pd

# Função para formatar o valor como porcentagem com 2 casas decimais

def formatar(valor):
    return "{:.2f}%".format(valor)

# Dados de roubos, furtos e recuperação de veículos
roubo = pd.Series([100, 90, 80, 120, 110, 90, 70])
furto = pd.Series([80, 60, 70, 60, 100, 50, 30])
rec = pd.Series([70, 50, 60, 80, 100, 70, 50])

# Exibir soma diária de roubos e furtos de veículos
print("--- Soma Diária de Roubos e Furtos de Veículos ---")
print(roubo + furto)

# Exibir percentual diário de recuperação de veículos
print("\n--- Percentual Diário de Recuperação de Veículos ---")
tx_rec = ((rec / roubo) * 100).apply(formatar)
print(tx_rec)

# Exibir totais
print(f"\nTotal de Roubos de Veículos: {roubo.sum()}")
print(f"\nTotal de Furtos de Veículos: {furto.sum()}")
print(f"\nTotal de Recuperação de Veículos: {rec.sum()}")

# Exibir percentual total de recuperação de veículos
tot_tx_rec = (rec.sum() / roubo.sum()) * 100
print(f"\nPerceptual Total de Recuperação de Veículos: {formatar(tot_tx_rec)}")
