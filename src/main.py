from data_loader import load_solar_data
from solar_forecasting import solar_forecast
from base_load import generate_base_load
from ev_model import generate_evs
from pricing import generate_price
from optimization import run_optimization
from visualization import plot_results

df = load_solar_data()

solar = solar_forecast(df)
base = generate_base_load()
arrival, deadline, energy, power = generate_evs()
price = generate_price()

ev_load = run_optimization(base, solar, price, arrival, deadline, energy, power)

total = base + ev_load - solar

plot_results(base, solar, total)