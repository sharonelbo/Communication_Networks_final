# Communication Networks

## Overview
This project analyzes network traffic characteristics.

## Installation
To run this project first navigate to the src folder inside 314690298 folder, than in a command line install the required dependencies using:
```
pip install -r requirements.txt
```
## requirements
To run the code create wireshark recordings, then export the recordings to csv files via wireshark each csv file must contain the following columns:
No., Time, Delta time, Src ip, Dest ip,	Protocol, Length, Info, Src port, Dest port

after that, copy the all the csv files to the folder called csv_files.

## Files Description
- `main.py`: The main script to run the analysis.
- `inter_arrival_time.py`: Computes inter-arrival times of packets.
- `avg_packet_size.py`: Calculates the average packet size.
- `packet_size_distribution.py`: Analyzes the packet size distribution.
- `protocol_distribution.py`: Evaluates the distribution of different protocols in the traffic.

## Usage
Navigate to the src folder and run the main script:
```
python3 main.py
```

You can also run each file seperatly to get only its related plots, for example:
```
python3 protocol_distribution.py
```


## Dependencies
The project requires the following Python libraries:
- `matplotlib`
- `pandas`
- `pyparsing`

