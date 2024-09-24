import numpy as np

def calculate(list):
    if len(list) != 9:  
        raise ValueError("List must contain nine numbers.")
    try:  
        lista_float = [float(num) for num in list]
    except ValueError:  
        raise ValueError("Please, insert only valid numbers.")
        
    matrix = np.array(lista_float).reshape(3, 3)

    mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix.flatten()).tolist()]
    variance = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix.flatten()).tolist()]
    standard_deviation = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix.flatten()).tolist()]
    max_value = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix.flatten()).tolist()]
    min_value = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix.flatten()).tolist()]
    sum_value = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix.flatten()).tolist()]
    
    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }

    return result  
