import numpy as np

def calculate(list):
    # Inicio - Erro 
    if len(list) != 9:  # Se o tamanho da lista não é igual a 9
        raise ValueError("O array deve conter nove números.")  # Mostre o erro: "O array deve conter nove números."
    try:  # Tenta converter os números para float
        lista_float = [float(num) for num in list]
    except ValueError:  # Se não der, mostre o erro: "Por favor, insira apenas números válidos."
        raise ValueError("Por favor, insira apenas números válidos.")
    # Fim - Erro 
    
    # Converte a lista em uma matriz 3x3
    matrix = np.array(lista_float).reshape(3, 3)

    # Inicio - calculos
    mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix.flatten()).tolist()]
    variance = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix.flatten()).tolist()]
    standard_deviation = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix.flatten()).tolist()]
    max_value = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix.flatten()).tolist()]
    min_value = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix.flatten()).tolist()]
    sum_value = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix.flatten()).tolist()]
    # Fim - calculos

    # Cria o dicionário com os resultados
    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }

    return result  # Retorna os resultados
