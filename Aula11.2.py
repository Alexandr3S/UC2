import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_lesao_corp_dolosa = df_ocorrencias[['cisp','ano','lesao_corp_dolosa']]
df_lesao_corp_dolosa = df_lesao_corp_dolosa[df_lesao_corp_dolosa['ano'].isin([2022, 2023, 2024])]
df_lesao_corp_dolosa = df_lesao_corp_dolosa.groupby(['cisp']).sum(['lesao_corp_dolosa']).reset_index()

# Criando o DataFrame de Lesão Corporal Dolosa Ordenada
df_lesao_corp_dolosa_order = df_lesao_corp_dolosa.sort_values(by='lesao_corp_dolosa',ascending=True)

# Criando o DataFrame de Lesão Corporal Dolosa e Culposa
df_lesao_corp_dolosa_culposa = df_ocorrencias[['cisp','ano','lesao_corp_dolosa','lesao_corp_culposa']]
df_lesao_corp_dolosa_culposa = df_lesao_corp_dolosa_culposa[df_lesao_corp_dolosa_culposa['ano'].isin([2022, 2023, 2024])]
df_lesao_corp_dolosa_culposa = df_lesao_corp_dolosa_culposa.groupby(['cisp']).sum(['lesao_corp_dolosa','lesao_corp_culposa']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_lesao_corp_dolosa_order.head())

# Criando o array das Lesões Corporais Dolosas
array_lesao_corp_dolosa = np.array(df_lesao_corp_dolosa["lesao_corp_dolosa"])

# Obtendo a média das Lesões Corporais Dolosas e Culposas
media_lesao_corp_dolosa = np.mean(array_lesao_corp_dolosa)

# Obtendo a mediana das Lesões Corporais Dolosas
mediana_lesao_corp_dolosa = np.median(array_lesao_corp_dolosa)

# Obtendo a distância entre a média e a mediana das Lesões Corporais Dolosas
distancia_lesao_corp_dolosa = abs((media_lesao_corp_dolosa - mediana_lesao_corp_dolosa) / mediana_lesao_corp_dolosa) * 100

# Obtendo o máximo e o mínimo das Lesões Corporais Dolosas
maximo_lesao_corp_dolosa = np.max(array_lesao_corp_dolosa)
minimo_lesao_corp_dolosa = np.min(array_lesao_corp_dolosa)

# Obtendo a amplitude das Lesões Corporais Dolosas
amplitude_lesao_corp_dolosa = maximo_lesao_corp_dolosa - minimo_lesao_corp_dolosa

# Obtendo os Quartis das Lesões Corporais - Método weibull
q1_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.25, method='weibull')
q2_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.50, method='weibull')
q3_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.75, method='weibull')
iqr_lesao_corp_dolosa = q3_lesao_corp_dolosa - q1_lesao_corp_dolosa

# Identificando os outliers superiores e inferiores das Lesões Corporais
limite_superior_lesao_corp_dolosa = q3_lesao_corp_dolosa + (1.5 * iqr_lesao_corp_dolosa)
limite_inferior_lesao_corp_dolosa = q1_lesao_corp_dolosa - (1.5 * iqr_lesao_corp_dolosa)

# Filtrando o DataFrame das Lesões Corporais Dolosas
df_lesao_corp_dolosa_outliers_superiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] > limite_superior_lesao_corp_dolosa]
df_lesao_corp_dolosa_outliers_inferiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] < limite_inferior_lesao_corp_dolosa]

# Obtendo as medidas de dispersão das Lesões Corporais Dolosas
variancia_lesao_corp_dolosa = np.var(array_lesao_corp_dolosa)
distancia_var_lesao_corp_dolosa = variancia_lesao_corp_dolosa / (media_lesao_corp_dolosa**2)
desvio_padrao_lesao_corp_dolosa = np.std(array_lesao_corp_dolosa)
coeficiente_var_lesao_corp_dolosa = desvio_padrao_lesao_corp_dolosa / media_lesao_corp_dolosa

# Obtendo a correlação das Lesões Corporais
# 0,9 a 1,0 (positivo ou negativo): correlação muito forte;
# 0,7 a 0,9 (positivo ou negativo): correlação forte;
# 0,5 a 0,7 (positivo ou negativo): correlação moderada;
# 0,3 a 0,5 (positivo ou negativo): correlação fraca;
# 0,0 a 0,3 (positivo ou negativo): não possui correlação.
correlacao_lesao = np.corrcoef(df_lesao_corp_dolosa_culposa['lesao_corp_dolosa'],df_lesao_corp_dolosa_culposa['lesao_corp_culposa'])[0,1]

# Exibindo os dados sobre das Lesões Corporais
print("\n--- OBTENDO INFORMAÇÕES SOBRE AS LESÕES CORPORAIS DOLOSAS ---")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média das lesões corporais dolosas é {media_lesao_corp_dolosa:.0f}")
print(f"A mediana das lesões corporais dolosas é {mediana_lesao_corp_dolosa:.0f}")
print(f"A distância entre a média e a mediana é das lesões corporais dolosas é {distancia_lesao_corp_dolosa:.2f} %")
print(f"O menor valor das lesões corporais dolosas é {minimo_lesao_corp_dolosa:.0f}")
print(f"O maior valor das lesões corporais dolosas é {maximo_lesao_corp_dolosa:.0f}")
print(f"A amplitude dos valores das lesões corporais dolosas é {amplitude_lesao_corp_dolosa:.0f}")
print(f"O valor do q1 - 25% das lesões corporais dolosas é {q1_lesao_corp_dolosa:.0f}")
print(f"O valor do q2 - 50% das lesões corporais dolosas é {q2_lesao_corp_dolosa:.0f}")
print(f"O valor do q3 - 75% das lesões corporais dolosas é {q3_lesao_corp_dolosa:.0f}")
print(f"O valor do iqr = q3 - q1 das lesões corporais dolosas é {iqr_lesao_corp_dolosa:.0f}")
print(f"O limite inferior das lesões corporais dolosas é {limite_inferior_lesao_corp_dolosa:.0f}")
print(f"O limite superior das lesões corporais dolosas é {limite_superior_lesao_corp_dolosa:.0f}")
print(f"A variância das lesões corporais dolosas é {variancia_lesao_corp_dolosa:.0f}")
print(f"A distância da variância X média das lesões corporais dolosas é {distancia_var_lesao_corp_dolosa:.0f}")
print(f"O desvio padrão das lesões corporais dolosas é {desvio_padrao_lesao_corp_dolosa:.0f}")
print(f"O coeficiente de variação das lesões corporais dolosas é {coeficiente_var_lesao_corp_dolosa:.0f}")
print(f"A correlação das lesões corporais dolosas é {correlacao_lesao:.1f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_lesao_corp_dolosa_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_lesao_corp_dolosa_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_lesao_corp_dolosa_outliers_superiores) == 0:
    print("Não existem outliers superiores")
    controle_outliers_superiores = 0
else:
    controle_outliers_superiores = 1
    print(df_lesao_corp_dolosa_outliers_superiores)

# Visualizando os dados sobre das Lesões Corporais
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(3,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Lesões Corporais Dolosas e Culposas entre os Anos de 2022 e 2024')

# posição 01: BoxPlot das Lesões Corporais Dolosas
plt.subplot(3,2,1)
plt.title('BoxPlot das Lesões Corporais Dolosas')
plt.boxplot(array_lesao_corp_dolosa,vert=False,showmeans=True)

# posição 02: Dispersão entre as Lesões Corporais
plt.subplot(3,2,2)
plt.title('Comparativo das Lesões Corporais Dolosas e Culposas')
plt.scatter(df_lesao_corp_dolosa_culposa['lesao_corp_dolosa'],df_lesao_corp_dolosa_culposa['lesao_corp_culposa'])
plt.xlabel('Lesão Corporal Dolosa')
plt.ylabel('Lesão Corporal Culposa')

# posição 03: 
plt.subplot(3,2,3)
if controle_outliers_superiores == 0:
    # Não possui outliers - exibindo os dados completos
    df_lesao_corp_dolosa_order = df_lesao_corp_dolosa.sort_values(by='lesao_corp_dolosa',ascending=True)
    plt.title('Ranking das Delegacias')
    plt.barh(df_lesao_corp_dolosa_order['cisp'].astype(str),df_lesao_corp_dolosa_order['lesao_corp_dolosa'])
else:
    # Possui outliers - exibindo apenas os dados discrepantes
    df_lesao_corp_dolosa_outliers_superiores_order = df_lesao_corp_dolosa_outliers_superiores.sort_values(by='lesao_corp_dolosa',ascending=True)
    plt.title('Ranking das Delegacias com Outliers')
    plt.barh(df_lesao_corp_dolosa_outliers_superiores_order['cisp'].astype(str),df_lesao_corp_dolosa_outliers_superiores_order['lesao_corp_dolosa'])
    
plt.subplot(3,2,4)
df_lesao = df_lesao_corp_dolosa_order.head()
plt.title('Top 5 das Delegacias com Menores Valores')
plt.barh(df_lesao['cisp'].astype(str),df_lesao['lesao_corp_dolosa'])

plt.subplot(3,2,5)
plt.title('Histograma das Lesões Corporais Dolosas')
plt.hist(array_lesao_corp_dolosa,bins=100,edgecolor='black')

# posição 06: Medidas descritivas das Lesões Corporais Dolosas
plt.subplot(3,2,6)
plt.title('Medidas Descritivas das Lesões Corporais Dolosas')
plt.axis('off')
plt.text(0.1,0.9,f'Média das Lesões Corporais Dolosas: {media_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana das Lesões Corporais Dolosas: {mediana_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana das Lesões Corporais Dolosas: {distancia_lesao_corp_dolosa:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor das Lesões Corporais Dolosas: {maximo_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor das Lesões Corporais Dolosas: {minimo_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média das Lesões Corporais Dolosas: {distancia_var_lesao_corp_dolosa:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação das Lesões Corporais Dolosas: {coeficiente_var_lesao_corp_dolosa:.2f}',fontsize=12)
plt.text(0.1,0.2,f'Correlação entre as Lesões: {correlacao_lesao:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()