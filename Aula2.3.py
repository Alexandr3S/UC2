#Executar as 4 operações matemáticas usando séries 
import pandas as pd 
n1 = pd.Series ([80,90,100,10,20,70,50,65,15,95])
n2 = pd.Series([40,30,10,60,10,90,55,60,30,100])
print("---soma das séries ---")
print(n1+n2)
print("\n--- Subtração das Séries---")
print(n1 - n2)
print("\n--- Multiplicação das Séries---")
print(n1 * n2)
print("\n--- Divisão das Séries---")
print(n1 / n2)