
import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados BaseDPEvolucaoMensalCisp
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Delegacias - Roubo de Veículos
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_veiculo = df_ocorrencias[['cisp','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()

# Exibindo a base de dados Delegacias - Roubo de Veículos
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_roubo_veiculo.head())