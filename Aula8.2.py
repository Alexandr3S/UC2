import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Visualizando os dados sobre Homicídio Doloso
print("\nVISUALIZANDO OS DADOS...")
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre os Homicídios Dolosos por UPP´S')

# Posição 01: Gráfico dos Homicídios Dolosos
plt.subplot(2,2,1)
plt.title('BoxPlot dos Homicídios Dolosos')
plt.boxplot(array_hom_doloso,vert=False,showmeans=True)

# Posição 02: Histograma dos Homicídios Dolosos
plt.subplot(2,2,2)
plt.title('Histograma dos Homicídios Dolosos')
plt.hist(array_hom_doloso,bins=100,edgecolor='black')

# Posição 03: Lista de UPP´s com Outliers
df_hom_doloso_outliers_superiores_order = df_hom_doloso_outliers_superiores.sort_values(by='hom_doloso',ascending=True)
plt.subplot(2,2,3)
plt.title('Ranking das UPP´s com Outliers Superiores')
plt.barh(df_hom_doloso_outliers_superiores_order['upp'],df_hom_doloso_outliers_superiores_order['hom_doloso'])

# Posição 04: Medidas Descritivas dos Homicídios Dolosos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Homicídios Dolosos')
plt.axis('off')
plt.text(0.1,0.9,f'A média dos homicídios dolosos é {media_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.8,f'A mediana dos homicídios dolosos é {mediana_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.7,f'A distância entre a média e a mediana é dos homicídios dolosos é {distancia_hom_doloso}',fontsize=12)
plt.text(0.1,0.6,f'O menor valor dos homicídios dolosos é {minimo_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.5,f'O maior valor dos homicídios dolosos é {maximo_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.4,f'A amplitude dos valores dos homicídios dolosos é {amplitude_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.3,f'O valor do q3 - 75% dos homicídios dolosos é {q3_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.2,f'O valor do iqr = q3 - q1 dos homicídios dolosos é {iqr_hom_doloso:.0f}',fontsize=12)
plt.text(0.1,0.1,f'O limite superior dos homicídios dolosos é {limite_superior_hom_doloso:.0f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()