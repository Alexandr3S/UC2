# Importando a Biblioteca Pandas e Numpy
import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a Base de Dados
endereco_dados = 'BASES\Funcionarios.csv'

# Criando o DataFrame Ocorrências
df_funcionarios = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

# Os arrays são estruturas de dados que armazenam uma coleção de dados e computacionalmente mais eficiente para cálculos estatísticos. Faz parte da biblioteca numpy.
# Criando um array do salário
array_funcionarios_salario = np.array(df_funcionarios['Salário'])

# Criando um array da idade
array_funcionarios_idade = np.array(df_funcionarios['Idade'])

# Criando um array do tempo de empresa
array_funcionarios_tempo = np.array(df_funcionarios['Tempo'])

# Obtendo os resultados solicitados
media_salario = np.mean(array_funcionarios_salario)
maior_salario = np.max(array_funcionarios_salario)
menor_salario = np.min(array_funcionarios_salario)
amplitude_salario = maior_salario - menor_salario
mediana_salario = np.median(array_funcionarios_salario)
distancia_salario = abs((media_salario - mediana_salario) / mediana_salario)
q1_salario = np.quantile(array_funcionarios_salario, 0.25, method='weibull')
q2_salario = np.quantile(array_funcionarios_salario, 0.50, method='weibull')
q3_salario = np.quantile(array_funcionarios_salario, 0.75, method='weibull')
iqr_salario = q3_salario - q1_salario
limite_superior_salario = q3_salario + (1.5 * iqr_salario)
limite_inferior_salario = q1_salario - (1.5 * iqr_salario)
df_funcionarios_outliers_inferiores_salario = df_funcionarios[df_funcionarios['Salário'] < limite_inferior_salario]
df_funcionarios_outliers_superiores_salario = df_funcionarios[df_funcionarios['Salário'] > limite_superior_salario]


media_idade = np.mean(array_funcionarios_idade)
maior_idade = np.max(array_funcionarios_idade)
menor_idade = np.min(array_funcionarios_idade)
amplitude_idade = maior_idade - menor_idade
mediana_idade = np.median(array_funcionarios_idade)
distancia_idade = abs((media_idade - mediana_idade) / mediana_idade)
q1_idade = np.quantile(array_funcionarios_idade, 0.25, method='weibull')
q2_idade = np.quantile(array_funcionarios_idade, 0.50, method='weibull')
q3_idade = np.quantile(array_funcionarios_idade, 0.75, method='weibull')
iqr_idade = q3_idade - q1_idade
limite_superior_idade = q3_idade + (1.5 * iqr_idade)
limite_inferior_idade = q1_idade - (1.5 * iqr_idade)
df_funcionarios_outliers_inferiores_idade = df_funcionarios[df_funcionarios['Idade'] < limite_inferior_idade]
df_funcionarios_outliers_superiores_idade = df_funcionarios[df_funcionarios['Idade'] > limite_superior_idade]
#nome_func_novo = df_funcionarios[df_funcionarios['Idade'] == menor_idade]['Nome']
#nome_func_antigo = df_funcionarios[df_funcionarios['Idade'] == maior_idade]['Nome']


maior_tempo = np.max(array_funcionarios_tempo)
menor_tempo = np.min(array_funcionarios_tempo)
amplitude_tempo = maior_tempo - menor_tempo
media_tempo = np.mean(array_funcionarios_tempo)
mediana_tempo = np.median(array_funcionarios_tempo)
distancia_tempo = abs((media_tempo - mediana_tempo) / mediana_tempo)
q1_tempo = np.quantile(array_funcionarios_tempo, 0.25, method='weibull')
q2_tempo = np.quantile(array_funcionarios_tempo, 0.50, method='weibull')
q3_tempo = np.quantile(array_funcionarios_tempo, 0.75, method='weibull')
iqr_tempo = q3_tempo - q1_tempo
limite_superior_tempo = q3_tempo + (1.5 * iqr_tempo)
limite_inferior_tempo = q1_tempo - (1.5 * iqr_tempo)
df_funcionarios_outliers_inferiores_tempo = df_funcionarios[df_funcionarios['Tempo'] < limite_inferior_tempo]
df_funcionarios_outliers_superiores_tempo = df_funcionarios[df_funcionarios['Tempo'] > limite_superior_tempo]


qtd_funcionarios = np.count_nonzero(array_funcionarios_idade)


# Exibindo o DataFrame Funcionários
print("------- Tabela Funcionários ------")
print(df_funcionarios)

# Exibindo os resultados da idade
print("\n------- Resultados da Idade ------")
print(f"A média de idade dos funcionários da empresa é {media_idade} anos.")
print(f"A mediana de idade dos funcionários da empresa é {mediana_idade} anos.")
print(f"A distância entre a média e a mediana das idades é {distancia_idade}")
print(f"A maior de idade dos funcionários da empresa é {maior_idade} anos.")
print(f"A menor de idade dos funcionários da empresa é {menor_idade} anos.")
print(f"A amplitude das idades dos funcionários da empresa é {amplitude_idade} anos.")
print(f"O valor do quartil 1 é {q1_idade}")
print(f"O valor do quartil 2 é {q2_idade}")
print(f"O valor do quartil 3 é {q3_idade}")
print(f"O valor do iqr é {iqr_idade}")
print(f"O limite inferior é {limite_inferior_idade}")
print(f"O limite superior é {limite_superior_idade}")
if len(df_funcionarios_outliers_inferiores_idade) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_funcionarios_outliers_inferiores_idade)
if len(df_funcionarios_outliers_superiores_idade) == 0:
    print("Não existem outliers superiores")
else:
    print(df_funcionarios_outliers_superiores_idade)
#print(f"O funcionário com mais idade é {nome_func_antigo.values[0]}")
#print(f"O funcionário com menos idade é {nome_func_novo.values[0]}")


# Exibindo os resultados dos salários
print("\n------- Resultados dos Salários ------")
print(f"A média salarial da empresa é R$ {media_salario:.2f}")
print(f"A mediana salarial da empresa é R$ {mediana_salario:.2f}")
print(f"A distância entre a média e a mediana dos salários é {distancia_salario}")
print(f"O maior salário da empresa é R$ {maior_salario}")
print(f"O menor salário da empresa é R$ {menor_salario}")
print(f"A amplitude dos salários da empresa é {amplitude_salario}")
print(f"O valor do quartil 1 é {q1_salario}")
print(f"O valor do quartil 2 é {q2_salario}")
print(f"O valor do quartil 3 é {q3_salario}")
print(f"O valor do iqr é {iqr_salario}")
print(f"O limite inferior é {limite_inferior_salario}")
print(f"O limite superior é {limite_superior_salario}")
if len(df_funcionarios_outliers_inferiores_salario) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_funcionarios_outliers_inferiores_salario)
if len(df_funcionarios_outliers_superiores_salario) == 0:
    print("Não existem outliers superiores")
else:
    print(df_funcionarios_outliers_superiores_salario)


# Exibindo os resultados do tempo de empresa
print("\n------- Resultados do Tempo de Empresa ------")
print(f"A média do tempo de empresa é {media_tempo} anos.")
print(f"A mediana do tempo de empresa é {mediana_tempo} anos.")
print(f"A distância entre a média e a mediana do tempo é {distancia_tempo}")
print(f"O maior tempo de empresa é {maior_tempo} anos.")
print(f"O menor tempo de empresa é {menor_tempo} anos.")
print(f"A amplitude do tempo de empresa é {amplitude_tempo} anos.")
print(f"O valor do quartil 1 é {q1_tempo}")
print(f"O valor do quartil 2 é {q2_tempo}")
print(f"O valor do quartil 3 é {q3_tempo}")
print(f"O valor do iqr é {iqr_tempo}")
print(f"O limite inferior é {limite_inferior_tempo}")
print(f"O limite superior é {limite_superior_tempo}")
if len(df_funcionarios_outliers_inferiores_tempo) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_funcionarios_outliers_inferiores_tempo)
if len(df_funcionarios_outliers_superiores_tempo) == 0:
    print("Não existem outliers superiores")
else:
    print(df_funcionarios_outliers_superiores_tempo)


print(f"\nA quantidade de funcionários na empresa é {qtd_funcionarios}")