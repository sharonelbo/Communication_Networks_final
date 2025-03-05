import os
import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import alphas

csv_dir = "csv_files"
plot_dir = "../res"
individual_dir = os.path.join(plot_dir, "individual")

os.makedirs(plot_dir, exist_ok=True)
os.makedirs(individual_dir, exist_ok=True)

csv_files = [f for f in os.listdir(csv_dir) if f.endswith(".csv")]

# Combined Graph for All CSVs
plt.figure(figsize=(12, 6))
for file in csv_files:
    df = pd.read_csv(os.path.join(csv_dir, file), low_memory=False)
    df = df.sort_values(by="Time")
    inter_arrival = df["Time"].diff().dropna()
    plt.hist(inter_arrival, bins=50, alpha=0.5, label=file)


plt.xlabel("Inter-arrival Time (Seconds)")
plt.ylabel("Frequency")
plt.title("Inter-Arrival Time Distribution Across Files")
plt.legend(loc="upper right")
plt.grid()
plt.savefig(os.path.join(plot_dir, "inter_arrival_time_distribution.png"))
plt.close()

# Individual Graphs for Each CSV File
for file in csv_files:
    df = pd.read_csv(os.path.join(csv_dir, file), low_memory=False)
    df = df.sort_values(by="Time")
    inter_arrival = df["Time"].diff().dropna()

    plt.figure(figsize=(12, 6))
    plt.hist(inter_arrival, bins=50, alpha=0.5, label=file)  # Step histogram
    plt.xlabel("Inter-arrival Time (Seconds)")
    plt.ylabel("Frequency")
    plt.title(f"Inter-Arrival Time Distribution - {file}")
    plt.grid()
    plt.savefig(os.path.join(individual_dir, f"inter_arrival_time_distribution_{file}.png"))
    plt.close()

print("Inter-Arrival Time Distribution plots saved in 'res/'")
