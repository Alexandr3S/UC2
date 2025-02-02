import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame recuperação de veículos
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_rec_veiculo = df_ocorrencias[['aisp','recuperacao_veiculos']]
df_rec_veiculo = df_rec_veiculo.groupby(['aisp']).sum(['recuperacao_veiculos']).reset_index()

# Criando o DataFrame roubo de veículos
df_roubo_veiculo = df_ocorrencias[['aisp','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['aisp']).sum(['roubo_veiculo']).reset_index()

# Criando o DataFrame recuperação de veículos e roubo de veículos
df_rec_roubo_veiculo = df_ocorrencias[['aisp','recuperacao_veiculos','roubo_veiculo']]
df_rec_roubo_veiculo = df_rec_roubo_veiculo.groupby(['aisp']).sum(['recuperacao_veiculos','roubo_veiculo']).reset_index()

# Exibindo a base de dados recuperação de veículos
print('\n---- EXIBINDO A BASE DE DADOS RECUPERAÇÃO DE VEÍCULOS -----')
print(df_rec_veiculo.head())

# Exibindo a base de dados recuperação de veículos e roubo de veículos
print('\n---- EXIBINDO A BASE DE DADOS RECUPERAÇÃO E ROUBO DE VEÍCULOS-----')
print(df_rec_roubo_veiculo.head())

# Criando o array da recuperação de veiculos
array_rec_veiculo = np.array(df_rec_veiculo["recuperacao_veiculos"])

# Obtendo a média dos recuperação de veiculos
media_rec_veiculo = np.mean(array_rec_veiculo)

# Obtendo a mediana dos recuperação de veiculos
mediana_rec_veiculo = np.median(array_rec_veiculo)

# Obtendo a distância entre a média e a mediana dos recuperação de veiculos
distancia_rec_veiculo = abs((media_rec_veiculo - mediana_rec_veiculo) / mediana_rec_veiculo) * 100

# Obtendo o máximo e o mínimo dos recuperação de veiculos
maximo_rec_veiculo = np.max(array_rec_veiculo)
minimo_rec_veiculo = np.min(array_rec_veiculo)

# Obtendo a amplitude dos recuperação de veiculos
amplitude_rec_veiculo = maximo_rec_veiculo - minimo_rec_veiculo

# Obtendo os Quartis dos recuperação de veiculos - Método weibull
q1_rec_veiculo = np.quantile(array_rec_veiculo, 0.25, method='weibull')
q2_rec_veiculo = np.quantile(array_rec_veiculo, 0.50, method='weibull')
q3_rec_veiculo = np.quantile(array_rec_veiculo, 0.75, method='weibull')
iqr_rec_veiculo = q3_rec_veiculo - q1_rec_veiculo

# Identificando os outliers superiores e inferiores dos recuperação de veículos
limite_superior_rec_veiculo = q3_rec_veiculo + (1.5 * iqr_rec_veiculo)
limite_inferior_rec_veiculo = q1_rec_veiculo - (1.5 * iqr_rec_veiculo)

# Filtrando o DataFrame recuperação de veículos
df_rec_veiculo_outliers_superiores = df_rec_veiculo[df_rec_veiculo['recuperacao_veiculos'] > limite_superior_rec_veiculo]
df_rec_veiculo_outliers_inferiores = df_rec_veiculo[df_rec_veiculo['recuperacao_veiculos'] < limite_inferior_rec_veiculo]

# Obtendo as medidas de dispersão dos recuperação de veículos
variancia_rec_veiculo = np.var(array_rec_veiculo)
distancia_var_rec_veiculo = variancia_rec_veiculo / (media_rec_veiculo**2)

desvio_padrao_rec_veiculo = np.std(array_rec_veiculo)
coeficiente_var_rec_veiculo = desvio_padrao_rec_veiculo / media_rec_veiculo

# Criando o array dos roubos de veiculos
array_roubo_veiculo = np.array(df_roubo_veiculo["roubo_veiculo"])

# Obtendo a média dos roubos de veiculos
media_roubo_veiculo = np.mean(array_roubo_veiculo)

# Obtendo a mediana dos roubos de veiculos
mediana_roubo_veiculo = np.median(array_roubo_veiculo)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_roubo_veiculo = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_roubo_veiculo = np.max(array_roubo_veiculo)
minimo_roubo_veiculo = np.min(array_roubo_veiculo)

# Obtendo a amplitude dos roubos de veiculos
amplitude_roubo_veiculo = maximo_roubo_veiculo - minimo_roubo_veiculo

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
q2_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
q3_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.75, method='weibull')
iqr_roubo_veiculo = q3_roubo_veiculo - q1_roubo_veiculo

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_roubo_veiculo = q3_roubo_veiculo + (1.5 * iqr_roubo_veiculo)
limite_inferior_roubo_veiculo = q1_roubo_veiculo - (1.5 * iqr_roubo_veiculo)

# Filtrando o DataFrame roubos de veículos
df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior_roubo_veiculo]
df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior_roubo_veiculo]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_roubo_veiculo = np.var(array_roubo_veiculo)
distancia_var_roubo_veiculo = variancia_roubo_veiculo / (media_roubo_veiculo**2)

desvio_padrao_roubo_veiculo = np.std(array_roubo_veiculo)
coeficiente_var_roubo_veiculo = desvio_padrao_roubo_veiculo / media_roubo_veiculo

# Obtendo a correlação entre as recuperações e os roubos de veículos
# 0.9 a 1.0 (positivo ou negativo) - muito forte
# 0.7 a 0.9 (positivo ou negativo) - forte
# 0.5 a 0.7 (positivo ou negativo) - moderada
# 0.3 a 0.5 (positivo ou negativo) - fraca
# 0.0 a 0.3 (positivo ou negativo) - não possui correlação
correl_rec_roubo_veiculo = np.corrcoef(df_rec_roubo_veiculo['recuperacao_veiculos'],df_rec_roubo_veiculo['roubo_veiculo'])[0,1]


# Exibindo os dados sobre as recuperações de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE AS RECUPERAÇÕES DE VEÍCULOS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média das recuperações de veículos é {media_rec_veiculo:.0f}")
print(f"A mediana das recuperações de veículos é {mediana_rec_veiculo:.0f}")
print(f"A distância entre a média e a mediana é das recuperações de veículos é {distancia_rec_veiculo:.2f} %")
print(f"O menor valor das recuperações de veículos é {minimo_rec_veiculo:.0f}")
print(f"O maior valor das recuperações de veículos é {maximo_rec_veiculo:.0f}")
print(f"A amplitude dos valores das recuperações de veículos é {amplitude_rec_veiculo:.0f}")
print(f"O valor do q1 - 25% das recuperações de veículos é {q1_rec_veiculo:.0f}")
print(f"O valor do q2 - 50% das recuperações de veículos é {q2_rec_veiculo:.0f}")
print(f"O valor do q3 - 75% das recuperações de veículos é {q3_rec_veiculo:.0f}")
print(f"O valor do iqr = q3 - q1 das recuperações de veículos é {iqr_rec_veiculo:.0f}")
print(f"O limite inferior das recuperações de veículos é {limite_inferior_rec_veiculo:.0f}")
print(f"O limite superior das recuperações de veículos é {limite_superior_rec_veiculo:.0f}")
print(f"A variância das recuperações de veículos é {variancia_rec_veiculo:.0f}")
print(f"A distância da variância X média das recuperações de veículos é {distancia_var_rec_veiculo:.0f}")
print(f"O desvio padrão das recuperações de veículos é {desvio_padrao_rec_veiculo:.0f}")
print(f"O coeficiente de variação das recuperações de veículos é {coeficiente_var_rec_veiculo:.0f}")
print(f"A correlação entre a recuperação e o roubo de veículos é {correl_rec_roubo_veiculo:.1f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_rec_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_rec_veiculo_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_rec_veiculo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_rec_veiculo_outliers_superiores)

# Exibindo os dados sobre os roubos de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS ROUBOS DE VEÍCULOS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos roubos de veículos é {media_roubo_veiculo:.0f}")
print(f"A mediana dos roubos de veículos é {mediana_roubo_veiculo:.0f}")
print(f"A distância entre a média e a mediana é dos roubos de veículos é {distancia_roubo_veiculo:.2f} %")
print(f"O menor valor dos roubos de veículos é {minimo_roubo_veiculo:.0f}")
print(f"O maior valor dos roubos de veículos é {maximo_roubo_veiculo:.0f}")
print(f"A amplitude dos valores dos roubos de veículos é {amplitude_roubo_veiculo:.0f}")
print(f"O valor do q1 - 25% dos roubos de veículos é {q1_roubo_veiculo:.0f}")
print(f"O valor do q2 - 50% dos roubos de veículos é {q2_roubo_veiculo:.0f}")
print(f"O valor do q3 - 75% dos roubos de veículos é {q3_roubo_veiculo:.0f}")
print(f"O valor do iqr = q3 - q1 dos roubos de veículos é {iqr_roubo_veiculo:.0f}")
print(f"O limite inferior dos roubos de veículos é {limite_inferior_roubo_veiculo:.0f}")
print(f"O limite superior dos roubos de veículos é {limite_superior_roubo_veiculo:.0f}")
print(f"A variância dos roubos de veículos é {variancia_roubo_veiculo:.0f}")
print(f"A distância da variância X média dos roubos de veículos é {distancia_var_roubo_veiculo:.0f}")
print(f"O desvio padrão dos roubos de veículos é {desvio_padrao_roubo_veiculo:.0f}")
print(f"O coeficiente de variação dos roubos de veículos é {coeficiente_var_roubo_veiculo:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_roubo_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_veiculo_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_veiculo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_veiculo_outliers_superiores)


# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,3,figsize=(23,8))
plt.suptitle('Análise dos Dados sobre Recuperação e Roubo de Veículos',fontsize=16)

# posição 01: BoxPlot das Recuperações de Veículos
plt.subplot(2,3,1)
plt.title('BoxPlot das Recuperações de Veículos')
plt.boxplot(array_rec_veiculo,vert=False,showmeans=True)

# posição 02: Ranking dos Batalhoes de PM com Outliers Superiores
plt.subplot(2,3,2)
df_rec_veiculo_outliers_superiores_order = df_rec_veiculo_outliers_superiores.sort_values(by='recuperacao_veiculos',ascending=True)
plt.title('Ranking dos Batalhoes de PM com Outliers Superiores')
plt.barh(df_rec_veiculo_outliers_superiores_order['aisp'].astype(str),df_rec_veiculo_outliers_superiores_order['recuperacao_veiculos'])

# posição 03: Histograma das Recuperações de Veículos
plt.subplot(2,3,3)
plt.title('Histograma das Recuperações de Veículos')
plt.hist(array_rec_veiculo,bins=100,edgecolor='black')

# posição 04: Correlação das Recuperações e Roubos de Veículos
plt.subplot(2,3,4)
plt.title('Comparativo das Recuperações e Roubos de Veículos')
plt.scatter(df_rec_roubo_veiculo['recuperacao_veiculos'],df_rec_roubo_veiculo['roubo_veiculo'])
plt.xlabel('Recuperação de Veículos')
plt.ylabel('Roubo de Veículos')

# posição 05: Medidas descritivas das Recuperações de Veículos
plt.subplot(2,3,5)
plt.title('Medidas Descritivas das Recuperações de Veículos')
plt.axis('off')
plt.text(0.0,0.9,f'Média das Recuperações de Veículos {media_rec_veiculo:.0f}',fontsize=12)
plt.text(0.0,0.8,f'Mediana das Recuperações de Veículos {mediana_rec_veiculo:.0f}',fontsize=12)
plt.text(0.0,0.7,f'Distância entre Média e Mediana das Recuperações de Veículos {distancia_rec_veiculo:.2f}%',fontsize=12)
plt.text(0.0,0.6,f'Maior valor das Recuperações de Veículos {maximo_rec_veiculo:.0f}',fontsize=12)
plt.text(0.0,0.5,f'Menor valor das Recuperações de Veículos {minimo_rec_veiculo:.0f}',fontsize=12)
plt.text(0.0,0.4,f'Distância entre a Variância e Média das Recuperações de Veículos {distancia_var_rec_veiculo:.2f}',fontsize=12)
plt.text(0.0,0.3,f'Coeficiente de variação das Recuperações de Veículos {coeficiente_var_rec_veiculo:.2f}',fontsize=12)

# posição 06: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,3,6)
plt.title('Medidas Descritivas dos Roubos de Veículos')
plt.axis('off')
plt.text(0.0,0.9,f'Média dos Roubos de Veículos {media_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.0,0.8,f'Mediana dos Roubos de Veículos {mediana_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.0,0.7,f'Distância entre Média e Mediana dos Roubos de Veículos {distancia_roubo_veiculo:.2f}%',fontsize=12)
plt.text(0.0,0.6,f'Maior valor dos Roubos de Veículos {maximo_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.0,0.5,f'Menor valor dos Roubos de Veículos {minimo_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.0,0.4,f'Distância entre a Variância e Média dos Roubos de Veículos {distancia_var_roubo_veiculo:.2f}',fontsize=12)
plt.text(0.0,0.3,f'Coeficiente de variação dos Roubos de Veículos {coeficiente_var_roubo_veiculo:.2f}',fontsize=12)


# Exibindo o Painel
plt.tight_layout()
plt.show()