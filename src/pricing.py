import numpy as np

def generate_price(hours=24):
    price = []
    for t in range(hours):
        if 17 <= t <= 21:
            price.append(18)
        elif 0 <= t <= 5:
            price.append(4)
        elif 10 <= t <= 15:
            price.append(6)
        else:
            price.append(9)
    return np.array(price)