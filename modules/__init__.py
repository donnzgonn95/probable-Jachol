"""
Trading AI Analyzer Modules

This package contains all core modules for technical analysis and signal generation.

Modules:
- data_fetcher: Financial data retrieval from Yahoo Finance
- indicators: Technical indicators (EMA, ADX, RSI, MACD, ATR)
- levels: Support/Resistance level calculation using DBSCAN
- volume_analysis: Volume profiling and Point of Control
- anomaly_detector: Machine learning-based anomaly detection
- signal_generator: Trading signal generation and filtering
- visualizer: Interactive chart creation with Plotly
"""

__version__ = "2.0.0"
__author__ = "donnzgonn95"

__all__ = [
    'data_fetcher',
    'indicators',
    'levels',
    'volume_analysis',
    'anomaly_detector',
    'signal_generator',
    'visualizer',
]