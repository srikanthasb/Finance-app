from src.data.market_data import get_market_data
from src.analysis.indicators import add_indicators
from src.analysis.snapshot import create_market_snapshot
from src.analysis.ai_analyst import analyze_market


data = get_market_data(
    ticker="TCS.NS",
    period="6mo",
    interval="1d",
)

data = add_indicators(data)

snapshot = create_market_snapshot(
    data=data,
    symbol="TCS.NS",
)

analysis = analyze_market(snapshot)

print("\n")
print("=" * 60)
print("AI INVESTMENT ANALYSIS")
print("=" * 60)
print(analysis)
print("=" * 60)