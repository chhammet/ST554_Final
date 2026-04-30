# ST554_Final
Final project for ST554: Analysis of Big Data at NC State University, Spring 2026

Creator: Cole Hammett

Purpose: Predicting power consumption (Zone 3) for Tetouan City using PySpark MLlib and Structured Streaming.

Date: 30th of April, 2026

Instructor: Justin Post

## Project Overview

This project builds an Elastic Net regression model on historical power consumption data, then applies that model in real time to a simulated stream of incoming CSV files.

## Repository Contents

| File | Description |
|------|-------------|
| `final_project.ipynb` | Main Jupyter notebook: model fitting + streaming pipeline |
| `stream_producer.py` | Script that simulates a data stream by writing CSVs to a watched folder |
| `README.md` | This file |

## Data Sources

- **Training data:** `power_ml_data.csv` — [https://www4.stat.ncsu.edu/~online/datasets/power_ml_data.csv](https://www4.stat.ncsu.edu/~online/datasets/power_ml_data.csv)
- **Streaming data:** `power_streaming_data.csv` — [https://www4.stat.ncsu.edu/~online/datasets/power_streaming_data.csv](https://www4.stat.ncsu.edu/~online/datasets/power_streaming_data.csv)

> Download both files locally before running. The streaming data file should be in the same directory as `produce_data.py`.

## Modeling Pipeline (Part 1)

The pipeline and cross-validation are built entirely with PySpark MLlib:

1. Cast `Hour` to `DoubleType` via SQL transformer
2. Binarize `Hour` (threshold = 6.5, i.e. night vs. day)
3. One-hot encode `Month`
4. PCA (2 components) on `Temperature`, `Humidity`, `Wind_Speed`, `General_Diffuse_Flows`, `Diffuse_Flows`
5. Assemble final feature vector
6. Fit Elastic Net regression via 5-fold `CrossValidator`

Tuning grid:
- `regParam`: 0, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.98, 0.99, 1
- `elasticNetParam`: 0, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.98, 0.99, 1

Response variable: `Power_Zone_3`

## Streaming Pipeline (Part 2)

1. Watch a local folder for incoming CSV files
2. Apply the fitted model to each micro-batch to generate predictions
3. Compute residuals (`label - prediction`)
4. Join predictions back to the stream on `label`
5. Write results to the console in **append** mode

## How to Run

### 1. Install dependencies

```bash
pip install pyspark pandas
```

### 2. Run the notebook

Open `final_project.ipynb` in JupyterLab and run all cells. The streaming query will start watching for files.

### 3. Simulate the stream

In a separate terminal:

```bash
python stream_producer.py
```

This samples 5 random rows every 10 seconds (20 iterations) and writes them as CSV files to the watched folder. Output will appear in the notebook console.

## Requirements

- Python 3.8+
- PySpark 3.x
- pandas
- JupyterLab or Jupyter Notebook
