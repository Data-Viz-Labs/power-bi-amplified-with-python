# Power BI Amplified with Python

This repository contains a collection of Python scripts designed to complement and enhance data analysis capabilities, combining financial analysis, text processing, and data visualization.

## Overview

The project is organized into three main components:
- Financial data acquisition
- Data processing and analysis
- Results visualization

## Project Structure

### 1. Data Acquisition
- `001_obtaining_data.py`: Downloads historical stock data using yfinance
  - Retrieves NVIDIA (NVDA) data
  - Period: last 5 years
  - Includes historical prices and volume

### 2. Data Processing
- `002_munging_data_1.py`: Text Analysis
  - Calculates comment length
  - Text data preprocessing

- `003_munging_data_2.py`: Sentiment Analysis
  - Implements sentiment analysis using TextBlob
  - Generates polarity scores for comments

### 3. Data Visualization
- `004_render_data_0.py`: Sample Demographic Data
  - DataFrame with personal information
  - Variables: name, age, weight, gender, state, children, pets

- `005_render_data_1.py`: Scatter Plots
  - Age vs Weight relationship visualization
  - Implemented with matplotlib

- `006_render_data_2.py`: Bar Charts
  - Age by name visualization
  - Demographic comparisons

- `007_render_data_3.py`: Line Charts
  - Comparison of number of pets and children
  - Multiple visualization in a single plot

## Requirements

```python
pandas
matplotlib
pandas_datareader
yfinance
textblob
```

## Main Features

- Automatic financial data download
- Text sentiment analysis
- Multiple customizable visualizations
- Demographic data processing
- Comparative variable analysis

## Usage

The scripts are numbered sequentially to follow a logical workflow:
1. First, obtain financial data
2. Then, process and analyze the data
3. Finally, create visualizations

## Notes

- Ensure you have an internet connection for financial data download
- Visualization scripts can be modified to adapt to different datasets
- Sentiment analysis works best with English text

## Contributions

Contributions are welcome. Please feel free to:
- Report issues
- Suggest improvements
- Submit pull requests

