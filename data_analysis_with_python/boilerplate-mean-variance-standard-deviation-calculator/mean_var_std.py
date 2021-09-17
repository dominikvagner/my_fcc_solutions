import numpy as np

def calculate(list):
    input = np.array(list)
    if np.shape(input)[0] < 9:
        raise ValueError('List must contain nine numbers.')
    
    input = input.reshape((3,3))
    calculations = {'mean': [], 'variance': [], 'standard deviation': [], 'max': [], 'min': [], 'sum': []}

    calculations['mean'].append(np.mean(input, axis=0).tolist())
    calculations['mean'].append(np.mean(input, axis=1).tolist())
    calculations['mean'].append(np.mean(input).tolist())

    calculations['variance'].append(np.var(input, axis=0).tolist())
    calculations['variance'].append(np.var(input, axis=1).tolist())
    calculations['variance'].append(np.var(input).tolist())

    calculations['standard deviation'].append(np.std(input, axis=0).tolist())
    calculations['standard deviation'].append(np.std(input, axis=1).tolist())
    calculations['standard deviation'].append(np.std(input).tolist())
    
    calculations['max'].append(np.max(input, axis=0).tolist())
    calculations['max'].append(np.max(input, axis=1).tolist())
    calculations['max'].append(np.max(input).tolist())

    calculations['min'].append(np.min(input, axis=0).tolist())
    calculations['min'].append(np.min(input, axis=1).tolist())
    calculations['min'].append(np.min(input).tolist())

    calculations['sum'].append(np.sum(input, axis=0).tolist())
    calculations['sum'].append(np.sum(input, axis=1).tolist())
    calculations['sum'].append(np.sum(input).tolist())

    return calculations