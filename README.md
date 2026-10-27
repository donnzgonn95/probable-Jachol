# Trading AI Analyzer

**Language / Sprache / Język:** 🇬🇧 **English** · 🇩🇪 [Deutsch](README.de.md) · 🇵🇱 [Polski](README.pl.md)

A Python-based market analysis prototype combining technical indicators, support and resistance levels, volume analysis, anomaly detection and interactive visualizations.

## My first steps into coding

This repository marks an important point in my journey into software development: my first working code project.

I built the initial version in **Google Colab**, using access to **Google Labs beta-testing tools** as part of an AI-assisted development workflow. The experience was about learning through experimentation: turning an idea into a working prototype, testing the code, understanding how individual modules fit together, and iterating when something did not work.

The project helped me explore how data can be fetched, transformed, analysed and presented in a practical application. It also strengthened my interest in Python, data analysis, automation and using AI tools responsibly as a development aid.

This is an early learning and prototyping project. I do not claim that every line was written manually or that the prototype is production-ready.

## Features

- Market data retrieval with `yfinance`
- Technical indicators and market levels
- Support and resistance clustering with DBSCAN
- Volume spike analysis
- Anomaly detection using Isolation Forest
- Pattern-based signal generation
- Interactive charts with Plotly
- Streamlit interface

## Technology

Python · Google Colab · Streamlit · pandas · NumPy · scikit-learn · Plotly · yfinance

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

## Project modules

- `data_fetcher.py` — retrieves market data
- `indicators.py` — calculates technical indicators
- `levels.py` — identifies support and resistance levels using DBSCAN
- `volume_analysis.py` — analyses volume and detects spikes
- `anomaly_detector.py` — identifies unusual observations with Isolation Forest
- `signal_generator.py` — generates pattern-based signals
- `visualizer.py` — creates interactive Plotly charts
- `config.py` — contains configurable parameters

## Status

An experimental learning and prototyping project. Market signals are analytical outputs only and should not be treated as financial advice or as proof of a profitable trading strategy.
