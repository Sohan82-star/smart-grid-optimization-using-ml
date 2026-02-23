import matplotlib.pyplot as plt
import os

def plot_results(Base_Load, Solar_Forecast, Optimized_Total):

    os.makedirs("results", exist_ok=True)

    plt.figure(figsize=(12,6))
    plt.plot(Base_Load, label="Base Load")
    plt.plot(Solar_Forecast, label="Solar Forecast")
    plt.plot(Optimized_Total, label="Optimized Load")
    plt.legend()
    plt.title("Smart Grid Load Optimization")

    plt.savefig("results/load_curve.png")
    plt.close()