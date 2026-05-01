# Trading AI Analyzer

This repository contains a complete trading AI analyzer built with various modules for data fetching, indicators, volume analysis, anomaly detection, and more.

## Installation

Run the following command to install the required packages:
```
pip install -r requirements.txt
```

## Usage

Launch the Streamlit app using:
```
streamlit run app.py
```

## Modules

- `data_fetcher.py`: Fetches market data using yfinance.
- `indicators.py`: Contains functions for various technical indicators.
- `levels.py`: Computes support/resistance levels using DBSCAN.
- `volume_analysis.py`: Analyzes volume data and detects spikes.
- `anomaly_detector.py`: Implements Isolation Forest for detecting anomalies.
- `signal_generator.py`: Generates trading signals based on patterns.
- `visualizer.py`: Creates interactive charts using Plotly.

## Configuration

Configuration parameters can be customized in `config.py`.