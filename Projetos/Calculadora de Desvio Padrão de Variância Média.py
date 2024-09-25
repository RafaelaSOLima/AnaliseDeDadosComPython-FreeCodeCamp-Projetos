# Importa a biblioteca Numpy
import numpy as np

# INICIO - CRIA A FUNÇÃO CALCULATE PARA LISTAS
def calculate(lista):
    # Inicio - Erro 
    if len(lista) != 9: #Se o tamanho da lista não é igual a 9
        raise ValueError("O array deve conter nove números.") # Mostre o erro:"O array deve conter nove números."
    try: # Tenta converter os números para float
        lista_float = [float(num) for num in lista]
    except ValueError: # Se não der, mostre o erro: "Por favor, insira apenas números válidos."
        raise ValueError("Por favor, insira apenas números válidos.")
    # Fim - Erro 
    
    # Converte a lista em uma matriz 3x3
    matrix = np.array(lista_float).reshape(3, 3)

    # Inicio - calculos
    # Média: das colunas, das linhas, da matriz
    mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix.flatten()).tolist()]
    # Variancia: das colunas, das linhas, da matriz
    variance = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix.flatten()).tolist()]
    # Desvio Padrão: das colunas, das linhas, da matriz
    standard_deviation = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix.flatten()).tolist()]
    # Valor Máximo: das colunas, das linhas, da matriz
    max_value = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix.flatten()).tolist()]
    # Valor Minimo: das colunas, das linhas, da matriz
    min_value = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix.flatten()).tolist()]
    # Soma: das colunas, das linhas, da matriz
    sum_value = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix.flatten()).tolist()]
    # Fim - calculos

    # Cria o dicionário com os resultados ou seja o Dicionário
    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }
    
# FIM - CRIA A FUNÇÃO CALCULATE PARA LISTAS

# Chama a função e imprime a biblioteca ou mostra o erro
result = calculate([]) # Insira a lista separada por virgulas
print(result)
