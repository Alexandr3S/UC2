#
#
dados = {}
import pandas as pd 
roubo = [100,90,80,120,110,90,70]
furto = [80,60,70,60,100,50,30]
rec = [70,50,60,80,100,70,50]
print("--- Soma Diária Roubos e Furtos ---")
print(roubo+furto)
print("--- Total de Percentual Diário de Recuperação de Veículos ---")
print((rec / roubo) * 100)