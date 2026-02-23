import numpy as np
import pulp

def run_optimization(Base_Load, Solar_Forecast, Price,
                     arrival, deadline, energy_needed, max_power):

    hours = 24
    time_slots = range(hours)
    EVs = arrival.keys()

    model = pulp.LpProblem("Smart_Grid", pulp.LpMinimize)

    x = pulp.LpVariable.dicts("EV", (EVs, time_slots), lowBound=0)
    Z = pulp.LpVariable("Peak", lowBound=0)

    model += Z

    for t in time_slots:
        total = Base_Load[t] + pulp.lpSum(x[i][t] for i in EVs) - Solar_Forecast[t]
        model += total <= Z

    for i in EVs:
        valid_hours = list(range(arrival[i], 24)) + list(range(0, deadline[i]))
        model += pulp.lpSum(x[i][t] for t in valid_hours) == energy_needed[i]

    model.solve()

    load = np.zeros(hours)
    for i in EVs:
        for t in time_slots:
            load[t] += pulp.value(x[i][t])

    return load