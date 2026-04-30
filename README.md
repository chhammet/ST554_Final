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
| `produce_data.py` | Script that simulates a data stream by writing CSVs to a watched folder |
| `README.md` | This file |

## Data Sources

- **Training data:** `power_ml_data.csv` — [https://www4.stat.ncsu.edu/~online/datasets/power_ml_data.csv](https://www4.stat.ncsu.edu/~online/datasets/power_ml_data.csv)
- **Streaming data:** `power_streaming_data.csv` — [https://www4.stat.ncsu.edu/~online/datasets/power_streaming_data.csv](https://www4.stat.ncsu.edu/~online/datasets/power_streaming_data.csv)

> Download both files locally before running. The streaming data file should be in the same directory as `produce_data.py`.

## Modeling Pipeline (Part 1)

The pipeline and cross-validation are built entirely with PySpark MLlib:
