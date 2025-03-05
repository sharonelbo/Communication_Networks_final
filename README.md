# Network Traffic Analysis

## Overview
This project analyzes network traffic characteristics.
You can find wireshark recordings and plots generated using this code in the following link:
[text](https://drive.google.com/drive/folders/1NJY5slNTTK31hDIk8PBgssdRkfvzqUY7)

## Installation
To run this project, install the required dependencies using:
```
pip install -r requirements.txt
```
## requirements
To run the code create wireshark recordings, then export the recordings to csv files via wireshark,
each csv must contain the following columns:
No., Time, Delta time, Src ip, Dest ip,	Protocol, Length, Info, Src port, Dest port

Lastly copy the all the csv files, navigate to the src folder and than to the folder called csv_files and paste the csv files.

## Files Description
- `main.py`: The main script to run the analysis.
- `inter_arrival_time.py`: Computes inter-arrival times of packets.
- `avg_packet_size.py`: Calculates the average packet size.
- `packet_size_distribution.py`: Analyzes the packet size distribution.
- `protocol_distribution.py`: Evaluates the distribution of different protocols in the traffic.

## Usage
Navigate to the src folder then, run the main script:
```
python3 main.py
```

You can also run each file seperatly to get only its related plots, for example:
```
python3 protocol_distribution.py
```

## results
To see the results head to the res folder than you should have graph that compare all the different csv files, you should also have a folder called individual, for individual graphs for each csv file
KEEP IN MIND that res will come with some plots already in it so, running the code could delete them.


## Dependencies
The project requires the following Python libraries:
- `matplotlib`
- `pandas`
- `pyparsing`

The project was build with python 3.10 interpeter

