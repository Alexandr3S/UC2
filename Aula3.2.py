# Importando a Biblioteca 

import pandas as pd

#Criando a Tabela Vendedor
vendedores = (
    ["Maria",800,700,1000,900,1200,600,600],
    ["João",900,500,1100,1000,900,500,700],
    ["Manoel",700,600,900,1200,900,700,400]

)
#Criando as colunas da Tabela Vendedor

colunas = ["Nome","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho"]

#Criando o Dataframe Vendedores

df_vendedores = pd.DataFrame(vendedores,columns=colunas)

#Exibindo o Dataframe
print(df_vendedores)

#Realizando os Cálculos 
soma_janeiro = df_vendedores["Janeiro"].sum()
media_janeiro = df_vendedores["Janeiro"].sum()
maior_janeiro = df_vendedores["Janeiro"].sum()
menor_janeiro = df_vendedores["Janeiro"].sum()
nome_maior_janeiro = df_vendedores[df_vendedores['Janeiro'] == maior_janeiro]['Nome']

#Exibindo os Resultados 
print(f"\no Total do Mês de Janeiro foi: R$ {soma_janeiro:.2f}")
print(f"\nA Média do Mês de Janeiro foi: R$ {media_janeiro:.2f}")
print(f"\nO Maior Valor do Mês de Janeiro foi: R$ {maior_janeiro:.2f}")
print(f"\nO Menor Valor do Mês de Janeiro foi: R$ {menor_janeiro:.2f}")
print(f"\nO Vendedor com Maior Venda foi: (nome_maior_janeiro.values[0]")