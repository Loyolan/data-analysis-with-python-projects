import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers')
    else:
        np_array = np.array([list[:3], list[3:6], list[6:9]])
        mean = [np.mean(np_array, axis=0).tolist(), np.mean(np_array, axis=1).tolist(), np.mean(np_array.ravel())]
        variance = [np.var(np_array, axis=0).tolist(), np.var(np_array, axis=1).tolist(), np.var(np_array.ravel())]
        std = [np.std(np_array, axis=0).tolist(), np.std(np_array, axis=1).tolist(), np.std(np_array.ravel())]
        max = [np.max(np_array, axis=0).tolist(), np.max(np_array, axis=1).tolist(), np.max(np_array.ravel())]
        min = [np.min(np_array, axis=0).tolist(), np.min(np_array, axis=1).tolist(), np.min(np_array.ravel())]
        sum = [np.sum(np_array, axis=0).tolist(), np.sum(np_array, axis=1).tolist(), np.sum(np_array.ravel())]
        res = {
            'mean': mean,
            'variance': variance,
            'standard deviation': std,
            'max': max,
            'min': min,
            'sum': sum
        }
        return res
