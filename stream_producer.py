""" 
stream_producer.py
------------------
Producer script for the Spark Structured Streaming Pipeline

Reads the power streaming dataset
Writes random 5-row batches as individual CSV files into stream_csv/ every 10 seconds

The running Spark readStream in the notebook will pick up these files and process 
them as they arrive

Usage:
Run this script in the terminal to start producing the stream of CSV files 
AFTER starting the Spark readStream in the notebook

python stream_producer.py

Requires:
- power_streaming.csv in the same directory as this script
- The stream_csv/ directory must already exist in the same directory as this script
- pandas library installed in the Python environment
"""

import os
import time
import pandas as pd

# ----------------------
# Configuration
# ----------------------

# Path to the input dataset
DATA_FILE = 'power_streaming_data.csv'

# Directory to write the streaming CSV files
WATCH_FOLDER = 'stream_csv'

# Number of batches to produce
NUM_BATCHES = 20

# Number of rows per batch
BATCH_SIZE = 5

# Seconds to wait between producing batches
SLEEP_SECONDS = 10

# ----------------------
# Setup
# ----------------------

# Create the watch folder if it does not already exist
# This is a redundancy to the code in the notebook
os.makedirs(WATCH_FOLDER, exist_ok=True)
print(f"Watch folder ready: '{WATCH_FOLDER}/'")

# Load the full streaming dataset into a pandas DataFrame once
print(f"Reading input dataset from {DATA_FILE}...")
stream_data = pd.read_csv(DATA_FILE)
print(f"Loaded {len(stream_data)} rows with columns: {list(stream_data.columns)}")

# ----------------------
# Producer Loop
# ----------------------

print(f"\nStarting producer, writing {NUM_BATCHES} batches "
      f"({BATCH_SIZE} rows each) every {SLEEP_SECONDS}s.\n")

for i in range(NUM_BATCHES):
    
    # Randomly sample with replacement
    sample = stream_data.sample(n=BATCH_SIZE, replace=True)
    
    # Build a unique file name for this batch
    output_path = os.path.join(WATCH_FOLDER, f"batch_{i:03d}.csv")
    
    # Write to CSV, including headers but excluding pands row index
    sample.to_csv(output_path, index=False)
    
    print(f"[Batch {i + 1:>2}/{NUM_BATCHES}] Wrote {BATCH_SIZE} rows to {output_path}")

    # Pause before the next batch
    if i < NUM_BATCHES - 1:
        time.sleep(SLEEP_SECONDS)
        
print("\nProducer finished, all batches have been written.")

