import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('---- OBTENDO DADOS ----')

# Importando a base de dados Financeira.csv
endereco_dados = 'BASES\Financeira.csv'

# Criando o DataFrame Financeira
df_financeira = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')
df_financeira_renda_emprestimo = df_financeira[['Id_cliente','Renda','Vlr_emprestado']]

# Exibindo a base de dados Financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_financeira_renda_emprestimo.head())

# Os arrays são estruturas de dados que armazenam uma coleção de dados e computacionalmente mais eficiente para cálculos estatísticos. Faz parte da biblioteca numpy.
# Criando o array do valor da renda e do vlr_emprestado
array_financeira_renda = np.array(df_financeira_renda_emprestimo['Renda'])
array_financeira_vlr_emprestado = np.array(df_financeira_renda_emprestimo['Vlr_emprestado'])

# Obtendo a média do valor da renda e do vlr_emprestado
media_renda = np.mean(array_financeira_renda)
media_vlr_emprestado = np.mean(array_financeira_vlr_emprestado)

# Obtendo a mediana do valor da renda e do vlr_emprestado
mediana_renda = np.median(array_financeira_renda)
mediana_vlr_emprestado = np.median(array_financeira_vlr_emprestado)

# Obtendo a distância entre a média e a mediana do valor da renda e do vlr_emprestado
distancia_renda = abs((media_renda - mediana_renda) / mediana_renda)
distancia_vlr_emprestado = abs((media_vlr_emprestado - mediana_vlr_emprestado) / mediana_vlr_emprestado)

# Obtendo o máximo e o mínimo do valor da renda e do vlr_emprestado
maximo_renda = np.max(array_financeira_renda)
minimo_renda = np.min(array_financeira_renda)
maximo_vlr_emprestado = np.max(array_financeira_vlr_emprestado)
minimo_vlr_emprestado = np.min(array_financeira_vlr_emprestado)

# Obtendo a amplitude do valor da renda e do vlr_emprestado
amplitude_renda = maximo_renda - minimo_renda
amplitude_vlr_emprestado = maximo_vlr_emprestado - minimo_vlr_emprestado

# Obtendo os Quartis da renda e do vlr_emprestado - Método weibull
q1_renda = np.quantile(array_financeira_renda, 0.25, method='weibull')
q2_renda = np.quantile(array_financeira_renda, 0.50, method='weibull')
q3_renda = np.quantile(array_financeira_renda, 0.75, method='weibull')
iqr_renda = q3_renda - q1_renda

q1_vlr_emprestado = np.quantile(array_financeira_vlr_emprestado, 0.25, method='weibull')
q2_vlr_emprestado = np.quantile(array_financeira_vlr_emprestado, 0.50, method='weibull')
q3_vlr_emprestado = np.quantile(array_financeira_vlr_emprestado, 0.75, method='weibull')
iqr_vlr_emprestado = q3_vlr_emprestado - q1_vlr_emprestado

# Identificando os outliers superiores e inferiores da renda e do vlr_emprestado
limite_superior_renda = q3_renda + (1.5 * iqr_renda)
limite_inferior_renda = q1_renda - (1.5 * iqr_renda)

limite_superior_vlr_emprestado = q3_vlr_emprestado + (1.5 * iqr_vlr_emprestado)
limite_inferior_vlr_emprestado = q1_vlr_emprestado - (1.5 * iqr_vlr_emprestado)

# Filtrando o DataFrame Financeira
df_financeira_renda_outliers_superiores = df_financeira_renda_emprestimo[df_financeira_renda_emprestimo['Renda'] > limite_superior_renda ]
df_financeira_renda_outliers_inferiores = df_financeira_renda_emprestimo[df_financeira_renda_emprestimo['Renda'] < limite_inferior_renda ]

df_financeira_vlr_emprestado_outliers_superiores = df_financeira_renda_emprestimo[df_financeira_renda_emprestimo['Vlr_emprestado'] > limite_superior_vlr_emprestado ]
df_financeira_vlr_emprestado_outliers_inferiores = df_financeira_renda_emprestimo[df_financeira_renda_emprestimo['Vlr_emprestado'] < limite_inferior_vlr_emprestado ]

# Exibindo os dados sobre o valor das rendas
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS RENDAS --")
print(f"O Valor Médio das Rendas dos Clientes é {media_renda:.2f}")
print(f"O Valor da Mediana das Rendas dos Clientes é {mediana_renda:.2f}")
print(f"A Distância entre a Média e a Mediana das Rendas dos Clientes é {distancia_renda}")
print(f"O Valor Máximo das Rendas dos Clientes é {maximo_renda:.2f}")
print(f"O Valor Mínimo das Rendas dos Clientes é {minimo_renda:.2f}")
print(f"A Amplitude das Rendas dos Clientes é {amplitude_renda:.2f}")
if len(df_financeira_renda_outliers_inferiores) == 0:
    print('Não Existem Outliers Inferiores')
else:
    print(df_financeira_renda_outliers_inferiores)

if len(df_financeira_renda_outliers_superiores) == 0:
    print('Não Existem Outliers Superiores')
else:
    print(df_financeira_renda_outliers_superiores)


# Exibindo os dados sobre os valores emprestados
print("\n-- OBTENDO INFORMAÇÕES SOBRE OS VALORES EMPRESTADOS --")
print(f"O Valor Médio dos Empréstimos dos Clientes é {media_vlr_emprestado:.2f}")
print(f"O Valor da Mediana dos Empréstimos dos Clientes é {mediana_vlr_emprestado:.2f}")
print(f"A Distância entre a Média e a Mediana dos Empréstimos dos Clientes é {distancia_vlr_emprestado}")
print(f"O Valor Máximo dos Empréstimos dos Clientes é {maximo_vlr_emprestado:.2f}")
print(f"O Valor Mínimo dos Empréstimos dos Clientes é {minimo_vlr_emprestado:.2f}")
print(f"A Amplitude dos Empréstimos dos Clientes é {amplitude_vlr_emprestado:.2f}")
if len(df_financeira_vlr_emprestado_outliers_inferiores) == 0:
    print('Não Existem Outliers Inferiores')
else:
    print(df_financeira_vlr_emprestado_outliers_inferiores)

if len(df_financeira_vlr_emprestado_outliers_superiores) == 0:
    print('Não Existem Outliers Superiores')
else:
    print(df_financeira_vlr_emprestado_outliers_superiores)

# Visualizando os dados sobre Renda e Valor Emprestado
print("\nVISUALIZANDO OS DADOS...")
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Renda e Valor Emprestado')

# Posição 01: Gráfico das Rendas
df_financeira_renda_emprestimo_order = df_financeira_renda_emprestimo.sort_values(by='Renda',ascending=True)
plt.subplot(2,2,1)
plt.xticks([])
plt.title('Acumulado dos Valores da Renda')
plt.bar(df_financeira_renda_emprestimo_order['Id_cliente'].astype(str),df_financeira_renda_emprestimo_order['Renda'])

# Posição 02: Gráfico dos Valores Emprestados
df_financeira_renda_emprestimo_order = df_financeira_renda_emprestimo.sort_values(by='Vlr_emprestado',ascending=True)
plt.subplot(2,2,2)
plt.xticks([])
plt.title('Acumulado dos Valores de Empréstimo')
plt.bar(df_financeira_renda_emprestimo_order['Id_cliente'].astype(str),df_financeira_renda_emprestimo_order['Vlr_emprestado'])

# Posição 03: Medidas Descritivas dos Valores da Renda
plt.subplot(2,2,3)
plt.title('Medidas Descritivas dos Valores de Renda')
plt.axis('off')
plt.text(0.1,0.9,f'Valor Médio das Rendas é {media_renda:.2f}',fontsize=12)
plt.text(0.1,0.8,f'Valor da Mediana das Rendas é {mediana_renda:.2f}',fontsize=12)
plt.text(0.1,0.7,f'Distância Média X Mediana das Rendas é {distancia_renda:.2f}',fontsize=12)
plt.text(0.1,0.6,f'Valor Mínimo das Rendas é {minimo_renda:.2f}',fontsize=12)
plt.text(0.1,0.5,f'Valor Máximo das Rendas é {maximo_renda:.2f}',fontsize=12)
plt.text(0.1,0.4,f'Amplitude Máximo das Rendas é {amplitude_renda:.2f}',fontsize=12)

# Posição 04: Medidas Descritivas dos Valores Emprestados
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Valores Emprestados')
plt.axis('off')
plt.text(0.1,0.9,f'Valor Médio do Valor Emprestado é {media_vlr_emprestado:.2f}',fontsize=12)
plt.text(0.1,0.8,f'Valor da Mediana do Valor Emprestado é {mediana_vlr_emprestado:.2f}',fontsize=12)
plt.text(0.1,0.7,f'Distância Média X Mediana do Valor Emprestado é {distancia_vlr_emprestado:.2f}',fontsize=12)
plt.text(0.1,0.6,f'Valor Mínimo do Valor Emprestado é {minimo_vlr_emprestado:.2f}',fontsize=12)
plt.text(0.1,0.5,f'Valor Máximo do Valor Emprestado é {maximo_vlr_emprestado:.2f}',fontsize=12)
plt.text(0.1,0.4,f'Amplitude Máximo do Valor Emprestado é {amplitude_vlr_emprestado:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()