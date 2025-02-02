#Código usando séries 
import pandas as pd 

# Criando a Series
media = pd.Series([80, 90, 100, 10, 20, 70, 50, 65, 15, 95])

# Filtrando as notas maiores ou iguais a 70
ap = media[media >= 70]

# Filtrando as notas menores ou iguais a 70
rp = media[media <= 70]

# Exibindo os resultados
print("--- Notas Maiores que 70 ---")
print(ap)
print("\n--- Notas Menores que 70 ---")
print(rp)
