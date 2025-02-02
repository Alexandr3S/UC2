import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_carga = df_ocorrencias[['munic','roubo_carga']]
df_roubo_carga = df_roubo_carga.groupby(['munic']).sum(['roubo_carga']).reset_index()

# Exibindo a base de dados roubo de carga
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_roubo_carga.head())

# Criando o array dos roubo de carga
array_roubo_carga = np.array(df_roubo_carga["roubo_carga"])

# Obtendo a média dos roubo de carga
media_roubo_carga = np.mean(array_roubo_carga)

# Obtendo a mediana dos roubo de carga
mediana_roubo_carga = np.median(array_roubo_carga)

# Obtendo a distância entre a média e a mediana dos roubo de carga
distancia_roubo_carga = abs((media_roubo_carga - mediana_roubo_carga) / mediana_roubo_carga)

# Obtendo o máximo e o mínimo dos roubo de carga
maximo_roubo_carga = np.max(array_roubo_carga)
minimo_roubo_carga = np.min(array_roubo_carga)

# Obtendo a amplitude dos roubo de carga
amplitude_roubo_carga = maximo_roubo_carga - minimo_roubo_carga

# Obtendo os Quartis dos roubo de carga - Método weibull
q1_roubo_carga = np.quantile(array_roubo_carga, 0.25, method='weibull')
q2_roubo_carga = np.quantile(array_roubo_carga, 0.50, method='weibull')
q3_roubo_carga = np.quantile(array_roubo_carga, 0.75, method='weibull')
iqr_roubo_carga = q3_roubo_carga - q1_roubo_carga

# Identificando os outliers superiores e inferiores dos roubo de carga
limite_superior_roubo_carga = q3_roubo_carga + (1.5 * iqr_roubo_carga)
limite_inferior_roubo_carga = q1_roubo_carga - (1.5 * iqr_roubo_carga)

# Filtrando o DataFrame roubo de carga
df_roubo_carga_outliers_superiores = df_roubo_carga[df_roubo_carga['roubo_carga'] > limite_superior_roubo_carga]
df_roubo_carga_outliers_inferiores = df_roubo_carga[df_roubo_carga['roubo_carga'] < limite_inferior_roubo_carga]



# Exibindo os dados sobre os roubo de carga
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS Roubos de Carga -----------")
print(f"A média dos roubo de carga é {media_roubo_carga:.0f}")
print(f"A mediana dos roubo de carga é {mediana_roubo_carga:.0f}")
print(f"A distância entre a média e a mediana é dos roubo de carga é {distancia_roubo_carga}")
print(f"O menor valor dos roubo de carga é {minimo_roubo_carga:.0f}")
print(f"O maior valor dos roubo de carga é {maximo_roubo_carga:.0f}")
print(f"A amplitude dos valores dos roubo de carga é {amplitude_roubo_carga:.0f}")
print(f"O valor do q1 - 25% dos roubo de carga é {q1_roubo_carga:.0f}")
print(f"O valor do q2 - 50% dos roubo de carga é {q2_roubo_carga:.0f}")
print(f"O valor do q3 - 75% dos roubo de carga é {q3_roubo_carga:.0f}")
print(f"O valor do iqr = q3 - q1 dos roubo de carga é {iqr_roubo_carga:.0f}")
print(f"O limite inferior dos roubo de carga é {limite_inferior_roubo_carga:.0f}")
print(f"O limite superior dos roubo de carga é {limite_superior_roubo_carga:.0f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_roubo_carga_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_carga_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_carga_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_carga_outliers_superiores)

# Visualizando os dados sobre roubos de carga
print("\nVISUALIZANDO OS DADOS...")
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre os Roubos de Carga por Municípios')

if len(df_roubo_carga_outliers_superiores) != 0 or len(df_roubo_carga_outliers_inferiores) != 0:
    # Posição 01: Gráfico dos roubo de carga
    plt.subplot(2,2,1)
    plt.title('BoxPlot dos roubos de carga')
    plt.boxplot(array_roubo_carga,vert=False,showmeans=True)

    # Posição 02: Histograma dos roubo de carga
    plt.subplot(2,2,2)
    plt.title('Histograma dos roubos de carga')
    plt.hist(array_roubo_carga,bins=100,edgecolor='black')

    # Posição 03: Lista de Municípios com Outliers
    df_roubo_carga_outliers_superiores_order = df_roubo_carga_outliers_superiores.sort_values(by='roubo_carga',ascending=True)
    plt.subplot(2,2,3)
    plt.title('Ranking dos Municípios com Outliers Superiores')
    plt.barh(df_roubo_carga_outliers_superiores_order['munic'],df_roubo_carga_outliers_superiores_order['roubo_carga'])

    # Posição 04: Medidas Descritivas dos roubos de carga
    plt.subplot(2,2,4)
    plt.title('Medidas Descritivas dos roubos de carga')
    plt.axis('off')
    plt.text(0.1,0.9,f'A média dos roubos de carga é {media_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.8,f'A mediana dos roubos de carga é {mediana_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.7,f'A distância entre a média e a mediana é dos roubos de carga é {distancia_roubo_carga}',fontsize=12)
    plt.text(0.1,0.6,f'O menor valor dos roubos de carga é {minimo_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.5,f'O maior valor dos roubos de carga é {maximo_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.4,f'A amplitude dos valores dos roubos de carga é {amplitude_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.3,f'O valor do q3 - 75% dos roubos de carga é {q3_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.2,f'O valor do iqr = q3 - q1 dos roubos de carga é {iqr_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.1,f'O limite superior dos roubos de carga é {limite_superior_roubo_carga:.0f}',fontsize=12)
else:
    # Posição 01: Gráfico dos roubo de carga
    df_roubo_carga_order = df_roubo_carga.sort_values(by='roubo_carga',ascending=True)
    plt.subplot(2,2,1)
    plt.xticks([])
    plt.title('Acumulado dos Valores dos Roubos de Carga')
    plt.bar(df_roubo_carga_order['munic'].astype(str),df_roubo_carga_order['roubo_carga'])

    # Posição 02: Histograma dos roubos de carga
    plt.subplot(2,2,2)
    plt.title('Histograma dos roubos de carga')
    plt.hist(array_roubo_carga,bins=100,edgecolor='black')

    # Posição 03: Medidas Descritivas dos roubos de carga
    plt.subplot(2,2,3)
    plt.title('Medidas Descritivas dos roubos de carga')
    plt.axis('off')
    plt.text(0.1,0.9,f'A média dos roubos de carga é {media_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.8,f'A mediana dos roubos de carga é {mediana_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.7,f'A distância entre a média e a mediana é dos roubos de carga é {distancia_roubo_carga}',fontsize=12)
    plt.text(0.1,0.6,f'O menor valor dos roubos de carga é {minimo_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.5,f'O maior valor dos roubos de carga é {maximo_roubo_carga:.0f}',fontsize=12)
    plt.text(0.1,0.4,f'A amplitude dos valores dos roubos de carga é {amplitude_roubo_carga:.0f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()