#Faça um programa que leia duas séries com 10 números inteiros cada e ao final mostre a soma, a subtração, a multiplicação e a divisão entre elas.
#Executar as 4 operações matemáticas usando séries

import pandas as pd
s1 = pd.Series([80,90,100,10,20,70,50,65,15,95])
s2 = pd.Series([50,20,80,90,10,70,40,30,25,60])
print("\n--- Soma das Séries ---")
print(s1 + s2)
print("\n--- Subtração Das Séries ---")
print(s1 - s2)
print("\n--- Divisão Das Séries ---")
print(s1 / s2)