import os
import pandas as pd
import matplotlib.pyplot as plt

csv_dir = "csv_files"
plot_dir = "res"

os.makedirs(plot_dir, exist_ok=True)

csv_files = [f for f in os.listdir(csv_dir) if f.endswith(".csv")]
avg_sizes = {}

for file in csv_files:
    df = pd.read_csv(os.path.join(csv_dir, file), low_memory=False)
    avg_sizes[file] = df["Length"].mean()

plt.figure(figsize=(12, 6))
plt.bar(avg_sizes.keys(), avg_sizes.values(), color="skyblue")
plt.xlabel("CSV Files")
plt.ylabel("Average Packet Size (Bytes)")
plt.title("Average Packet Sizes Comparison")
plt.xticks(rotation=15)
plt.savefig(os.path.join(plot_dir, "avg_packet_size_comparison.png"))
plt.close()

print("Average Packet Size Comparison plot saved in 'res/'")
