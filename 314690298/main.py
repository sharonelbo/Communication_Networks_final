import subprocess

scripts = [
    "packet_size_distribution.py",
    "avg_packet_size.py",
    "inter_arrival_time.py",
    "protocol_distribution.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python3", script])

print("All analysis scripts have been executed.")
