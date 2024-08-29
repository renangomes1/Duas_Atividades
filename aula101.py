import statistics

def calcular_estatisticas(salarios):
    media = statistics.mean(salarios)
    moda = statistics.mode(salarios)
    mediana = statistics.median(salarios)
    desvio_padrao = statistics.stdev(salarios)
    variancia = statistics.variance(salarios)
    
    return media, moda, mediana, desvio_padrao, variancia


empresa1 = [1000,6000,1200,8000,1400]

empresa2 = [5000,4000,3000,2000,7000]

empresa3 = [1200,1300,8000,3000,15000]

empresa4 = [1400,1750,2000,4500,5900]



media1, moda1, mediana1, desvio_padrao1, variancia1 = calcular_estatisticas(empresa1)
media2, moda2, mediana2, desvio_padrao2, variancia2 = calcular_estatisticas(empresa2)
media3, moda3, mediana3, desvio_padrao3, variancia3 = calcular_estatisticas(empresa3)
media4, moda4, mediana4, desvio_padrao4, variancia4 = calcular_estatisticas(empresa4)


print('Empresa1')
print(f'Média: {media1}, Moda: {moda1}, Mediana: {mediana1}, Desvio Padrão: {desvio_padrao1},Variança {variancia1} ')
print()
print("Empresa2")
print(f'Média: {media2},  Moda: {moda2}, Mediana: {mediana2}, Desvio Padrão: {desvio_padrao2}, Variança {variancia2} ')
print()
print("Empresa3")
print(f'Média: {media3},  Moda: {moda3}, Mediana: {mediana3}, Desvio Padrão: {desvio_padrao3}, Variança {variancia3} ')
print() 
print("Empresa4")
print(f"Média: {media4},  Moda: {moda4},  Mediana: {mediana4},Desvio Padrão:  {desvio_padrao4}, Variança {variancia4} ")
print()


 # Qual empresa escolheria? Eu escolheria a Empresa número 2
# Porquê? A Empresa 2 parece uma boa escolha por conta da base na média mais alta