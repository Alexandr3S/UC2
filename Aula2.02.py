# Código usando séries 
import pandas as pd
media = pd.Series([80,90,100,10,20,70,50,65,15,95])
ap = media [media >= 70]
rp = media [media < 70]
print("--- Notas Maiores que 70 ---")
print(ap)
print("\n--- Notas Menores que 70 ---")
print(rp)