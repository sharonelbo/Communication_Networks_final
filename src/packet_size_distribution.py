import os
import pandas as pd
import matplotlib.pyplot as plt

csv_dir = "csv_files"
plot_dir = "../res"
individual_dir = os.path.join(plot_dir, "individual")

os.makedirs(plot_dir, exist_ok=True)
os.makedirs(individual_dir, exist_ok=True)

csv_files = [f for f in os.listdir(csv_dir) if f.endswith(".csv")]


def plot_packet_size(df, title, save_path):
    df = df[df["Length"].notna()]

    plt.figure(figsize=(12, 6))
    plt.hist(df["Length"], bins=range(0, 5000, 100), alpha=0.6)
    plt.xlabel("Packet Size (Bytes)")
    plt.ylabel("Packet Count")
    plt.title(title)
    plt.savefig(save_path)
    plt.close()


# Create a multi-subplot figure for better comparison
fig, axes = plt.subplots(len(csv_files), 1, figsize=(10, 12), sharex=True)

for i, file in enumerate(csv_files):
    df = pd.read_csv(os.path.join(csv_dir, file), low_memory=False)
    df = df[df["Length"].notna()]

    axes[i].hist(df["Length"], bins=range(0, 5000, 100), alpha=0.6, label=file)
    axes[i].set_ylabel("Packet Count")
    axes[i].legend()
    axes[i].grid(True)

axes[-1].set_xlabel("Packet Size (Bytes)")
fig.suptitle("Packet Size Distribution Across Applications")
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, "packet_size_distribution.png"))
plt.close()

for file in csv_files:
    df = pd.read_csv(os.path.join(csv_dir, file), low_memory=False)
    plot_packet_size(df, f"Packet Size Distribution - {file}",
                     os.path.join(individual_dir, f"packet_size_distribution_{file}.png"))

print("Packet Size Distribution plots saved in 'res/'")
