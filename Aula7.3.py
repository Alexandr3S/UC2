
import pandas as pd
import numpy as np

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/UppEvolucaoMensalDeTitulos.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_hom_doloso = df_ocorrencias[['upp','hom_doloso']]
df_hom_doloso = df_hom_doloso.groupby(['upp']).sum(['hom_doloso']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_hom_doloso.head())

# Criando o array dos homicídios dolosos
array_hom_doloso = np.array(df_hom_doloso["hom_doloso"])

# Obtendo a média dos homicídios dolosos
media_hom_doloso = np.mean(array_hom_doloso)

# Obtendo a mediana dos homicídios dolosos
mediana_hom_doloso = np.median(array_hom_doloso)

# Obtendo a distância entre a média e a mediana dos homicídios dolosos
distancia_hom_doloso = abs((media_hom_doloso - mediana_hom_doloso) / mediana_hom_doloso)

# Obtendo o máximo e o mínimo dos homicídios dolosos
maximo_hom_doloso = np.max(array_hom_doloso)
minimo_hom_doloso = np.min(array_hom_doloso)

# Obtendo a amplitude dos homicídios dolosos
amplitude_hom_doloso = maximo_hom_doloso - minimo_hom_doloso

# Obtendo os Quartis dos homicídios dolosos - Método weibull
q1_hom_doloso = np.quantile(array_hom_doloso, 0.25, method='weibull')
q2_hom_doloso = np.quantile(array_hom_doloso, 0.50, method='weibull')
q3_hom_doloso = np.quantile(array_hom_doloso, 0.75, method='weibull')
iqr_hom_doloso = q3_hom_doloso - q1_hom_doloso

# Identificando os outliers superiores e inferiores dos homicídios dolosos
limite_superior_hom_doloso = q3_hom_doloso + (1.5 * iqr_hom_doloso)
limite_inferior_hom_doloso = q1_hom_doloso - (1.5 * iqr_hom_doloso)

# Filtrando o DataFrame homicídios dolosos
df_hom_doloso_outliers_superiores = df_hom_doloso[df_hom_doloso['hom_doloso'] > limite_superior_hom_doloso]
df_hom_doloso_outliers_inferiores = df_hom_doloso[df_hom_doloso['hom_doloso'] < limite_inferior_hom_doloso]



# Exibindo os dados sobre os homicídios dolosos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS HOMICÍDIOS DOLOSOS -----------")
print(f"A média dos homicídios dolosos é {media_hom_doloso:.0f}")
print(f"A mediana dos homicídios dolosos é {mediana_hom_doloso:.0f}")
print(f"A distância entre a média e a mediana é dos homicídios dolosos é {distancia_hom_doloso}")
print(f"O menor valor dos homicídios dolosos é {minimo_hom_doloso:.0f}")
print(f"O maior valor dos homicídios dolosos é {maximo_hom_doloso:.0f}")
print(f"A amplitude dos valores dos homicídios dolosos é {amplitude_hom_doloso:.0f}")
print(f"O valor do q1 - 25% dos homicídios dolosos é {q1_hom_doloso:.0f}")
print(f"O valor do q2 - 50% dos homicídios dolosos é {q2_hom_doloso:.0f}")
print(f"O valor do q3 - 75% dos homicídios dolosos é {q3_hom_doloso:.0f}")
print(f"O valor do iqr = q3 - q1 dos homicídios dolosos é {iqr_hom_doloso:.0f}")
print(f"O limite inferior dos homicídios dolosos é {limite_inferior_hom_doloso:.0f}")
print(f"O limite superior dos homicídios dolosos é {limite_superior_hom_doloso:.0f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_hom_doloso_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_hom_doloso_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_hom_doloso_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_hom_doloso_outliers_superiores)

