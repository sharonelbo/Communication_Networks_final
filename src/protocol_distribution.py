import os
import pandas as pd
import matplotlib.pyplot as plt

csv_dir = "csv_files"
plot_dir = "../res"
individual_dir = os.path.join(plot_dir, "individual")

os.makedirs(plot_dir, exist_ok=True)
os.makedirs(individual_dir, exist_ok=True)

csv_files = [f for f in os.listdir(csv_dir) if f.endswith(".csv")]

def plot_protocol_distribution(protocol_counts, title, save_path):
    plt.figure(figsize=(12, 6))  # Wider for readability
    protocol_counts = protocol_counts.sort_values(ascending=False)[:10]  # Show top 10 protocols only
    plt.bar(protocol_counts.index, protocol_counts.values, alpha=0.6)
    plt.xlabel("Protocol")
    plt.ylabel("Count")
    plt.title(title)
    plt.xticks(rotation=25)
    plt.savefig(save_path)
    plt.close()


plt.figure(figsize=(12, 6))
for file in csv_files:
    df = pd.read_csv(os.path.join(csv_dir, file), low_memory=False)
    protocol_counts = df["Protocol"].value_counts()
    plt.bar(protocol_counts.index, protocol_counts.values, alpha=0.6, label=file)

plt.xlabel("Protocol")
plt.ylabel("Count")
plt.title("Protocol Distribution Across CSV Files")
plt.xticks(rotation=25)
if plt.gca().has_data():
    plt.legend()
plt.savefig(os.path.join(plot_dir, "protocol_distribution.png"))
plt.close()


for file in csv_files:
    df = pd.read_csv(os.path.join(csv_dir, file), low_memory=False)
    protocol_counts = df["Protocol"].value_counts()
    plot_protocol_distribution(protocol_counts, f"Protocol Distribution - {file}", os.path.join(individual_dir, f"protocol_distribution_{file}.png"))

print("Protocol Distribution plots saved in 'res/'")
