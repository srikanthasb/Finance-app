import pandas as pd

from ta.momentum import RSIIndicator
from ta.trend import (
    EMAIndicator,
    MACD,
    SMAIndicator,
)


def add_indicators(data: pd.DataFrame) -> pd.DataFrame:
    """Add technical indicators to OHLCV market data."""

    data = data.copy()

    close = data["Close"]

    # Moving averages
    data["SMA_20"] = SMAIndicator(
        close=close,
        window=20,
    ).sma_indicator()

    data["SMA_50"] = SMAIndicator(
        close=close,
        window=50,
    ).sma_indicator()

    data["EMA_20"] = EMAIndicator(
        close=close,
        window=20,
    ).ema_indicator()

    # RSI
    data["RSI_14"] = RSIIndicator(
        close=close,
        window=14,
    ).rsi()

    # MACD
    macd = MACD(close=close)

    data["MACD"] = macd.macd()
    data["MACD_SIGNAL"] = macd.macd_signal()
    data["MACD_HIST"] = macd.macd_diff()

    return data