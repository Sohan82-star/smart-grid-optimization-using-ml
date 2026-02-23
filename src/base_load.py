import numpy as np

def generate_base_load(hours=24):
    base = []
    for t in range(hours):
        morning = 25 * np.exp(-0.5 * (t - 8)**2 / 4)
        evening = 45 * np.exp(-0.5 * (t - 19)**2 / 4)
        night_valley = -10 * np.exp(-0.5 * (t - 2)**2 / 4)
        noise = np.random.normal(0, 2)
        base.append(45 + morning + evening + night_valley + noise)
    return np.array(base)