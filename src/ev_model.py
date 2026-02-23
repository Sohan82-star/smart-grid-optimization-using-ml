import numpy as np

def generate_evs(num_EVs=15):
    arrival = {}
    deadline = {}
    energy_needed = {}
    max_power = {}

    for i in range(num_EVs):
        arrival[i] = np.random.randint(17, 20)
        deadline[i] = np.random.randint(6, 9)
        energy_needed[i] = np.random.randint(15, 30)
        max_power[i] = 7

    return arrival, deadline, energy_needed, max_power