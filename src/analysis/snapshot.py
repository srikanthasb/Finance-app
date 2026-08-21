import pandas as pd


def create_market_snapshot(
    data: pd.DataFrame,
    symbol: str,
) -> dict:
    """
    Create a compact snapshot of the latest market conditions.

    The numerical calculations are performed by indicators.py.
    This function only extracts the latest relevant values.
    """

    if data.empty:
        raise ValueError("Market data is empty.")

    latest = data.iloc[-1]

    snapshot = {
        "symbol": symbol,
        "date": str(data.index[-1]),

        "price": float(latest["Close"]),
        "open": float(latest["Open"]),
        "high": float(latest["High"]),
        "low": float(latest["Low"]),
        "volume": int(latest["Volume"]),

        "sma_20": float(latest["SMA_20"]),
        "sma_50": float(latest["SMA_50"]),
        "ema_20": float(latest["EMA_20"]),

        "rsi_14": float(latest["RSI_14"]),

        "macd": float(latest["MACD"]),
        "macd_signal": float(latest["MACD_SIGNAL"]),
        "macd_histogram": float(latest["MACD_HIST"]),
    }

    return snapshot