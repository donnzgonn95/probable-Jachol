"""
Support and Resistance levels calculation using DBSCAN clustering
"""

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from config import DBSCAN_ATR_MULTIPLIER, DBSCAN_MIN_SAMPLES, MIN_LEVELS_REQUIRED


def calculate_support_resistance(df: pd.DataFrame, atr_multiplier: float = DBSCAN_ATR_MULTIPLIER) -> list:
    """
    Calculate support and resistance levels using DBSCAN clustering.
    
    Args:
        df (pd.DataFrame): OHLCV data with ATR calculated
        atr_multiplier (float): Multiplier for ATR to determine clustering radius
    
    Returns:
        list: Sorted list of support/resistance price levels
    """
    try:
        # Find local highs and lows
        df['Local_High'] = df['High'][
            (df['High'].shift(1) < df['High']) & 
            (df['High'].shift(-1) < df['High'])
        ]
        df['Local_Low'] = df['Low'][
            (df['Low'].shift(1) > df['Low']) & 
            (df['Low'].shift(-1) > df['Low'])
        ]
        
        # Combine into levels array
        levels = pd.concat([
            df['Local_High'].dropna(), 
            df['Local_Low'].dropna()
        ]).values.reshape(-1, 1)
        
        if len(levels) < MIN_LEVELS_REQUIRED:
            return []
        
        # Calculate clustering radius based on recent volatility
        recent_atr = df['ATR'].tail(14).mean()
        eps = recent_atr * atr_multiplier
        
        # Apply DBSCAN clustering
        clustering = DBSCAN(eps=eps, min_samples=DBSCAN_MIN_SAMPLES).fit(levels)
        labels = clustering.labels_
        
        # Extract cluster centers as support/resistance zones
        support_resistance_zones = []
        for label in set(labels):
            if label != -1:  # -1 is noise
                zone_prices = levels[labels == label].flatten()
                support_resistance_zones.append(np.mean(zone_prices))
        
        return sorted(support_resistance_zones)
    
    except Exception as e:
        print(f"Error calculating S/R levels: {e}")
        return []


def get_nearest_level(price: float, levels: list) -> float:
    """
    Get the nearest support/resistance level to current price.
    
    Args:
        price (float): Current price
        levels (list): List of S/R levels
    
    Returns:
        float: Nearest level or None
    """
    if not levels:
        return None
    
    levels_array = np.array(levels)
    nearest_idx = np.argmin(np.abs(levels_array - price))
    return levels_array[nearest_idx]