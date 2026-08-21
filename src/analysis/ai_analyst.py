from src.ai.llm import llm


def analyze_market(snapshot: dict) -> str:
    """
    Send the calculated market snapshot to Groq
    and obtain an investment analysis.
    """

    prompt = f"""
You are an AI financial market analyst.

Analyze the following market data for {snapshot["symbol"]}.

MARKET DATA
-----------
Date: {snapshot["date"]}

Price: ₹{snapshot["price"]:.2f}
Open: ₹{snapshot["open"]:.2f}
High: ₹{snapshot["high"]:.2f}
Low: ₹{snapshot["low"]:.2f}
Volume: {snapshot["volume"]:,}

Technical Indicators
--------------------
SMA 20: ₹{snapshot["sma_20"]:.2f}
SMA 50: ₹{snapshot["sma_50"]:.2f}
EMA 20: ₹{snapshot["ema_20"]:.2f}

RSI 14: {snapshot["rsi_14"]:.2f}

MACD: {snapshot["macd"]:.2f}
MACD Signal: {snapshot["macd_signal"]:.2f}
MACD Histogram: {snapshot["macd_histogram"]:.2f}


YOUR TASK
---------

Analyze the technical condition of the stock.

Determine:

1. Overall technical trend:
   - Bullish
   - Bearish
   - Neutral

2. Momentum:
   - Strong
   - Moderate
   - Weak

3. RSI interpretation.

4. MACD interpretation.

5. Moving-average interpretation.

6. Overall assessment:
   - BUY candidate
   - HOLD
   - SELL candidate
   - WAIT

7. Confidence level from 0 to 100.

8. Important risks.

9. What conditions would invalidate the current assessment?

10. Explain your reasoning clearly.

IMPORTANT:
- Do not claim that the stock will definitely rise or fall.
- Do not present predictions as certainty.
- Do not invent financial data that is not supplied.
- Distinguish technical analysis from guaranteed investment results.
- A BUY/SELL/HOLD assessment is an analytical signal, not a guaranteed recommendation.

Return the analysis in a clear, structured format.
"""

    response = llm.invoke(prompt)

    return response.content