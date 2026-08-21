import streamlit as st
import plotly.graph_objects as go
from src.analysis.indicators import add_indicators
from src.data.market_data import get_market_data



st.set_page_config(
    page_title="AI Investment",
    layout="wide",
)

st.title("📈 AI Investment")

st.sidebar.header("Market")

STOCKS = {
    "NIFTY 50": "^NSEI",
    "BANK NIFTY": "^NSEBANK",
    "TCS": "TCS.NS",
    "INFOSYS": "INFY.NS",
    "RELIANCE": "RELIANCE.NS",
    "HDFC BANK": "HDFCBANK.NS",
    "ICICI BANK": "ICICIBANK.NS",
    "SBI": "SBIN.NS",
    "ITC": "ITC.NS",
    "BHARTI AIRTEL": "BHARTIARTL.NS",
    "L&T": "LT.NS",
    "AXIS BANK": "AXISBANK.NS",
    "KOTAK MAHINDRA BANK": "KOTAKBANK.NS",
    "HINDUSTAN UNILEVER": "HINDUNILVR.NS",
    "MARUTI SUZUKI": "MARUTI.NS",
    "SUN PHARMA": "SUNPHARMA.NS",
    "TATA MOTORS": "TATAMOTORS.NS",
    "TATA STEEL": "TATASTEEL.NS",
    "ADANI ENTERPRISES": "ADANIENT.NS",
    "ADANI PORTS": "ADANIPORTS.NS",
    "WIPRO": "WIPRO.NS",
    "HCL TECHNOLOGIES": "HCLTECH.NS",
}

selected_stock = st.sidebar.selectbox(
    "Stock",
    options=list(STOCKS.keys()),
    index=2,
)

ticker = STOCKS[selected_stock]

period = st.sidebar.selectbox(
    "Period",
    ["1mo", "3mo", "6mo", "1y", "2y", "5y"],
    index=2,
)

interval = st.sidebar.selectbox(
    "Interval",
    ["1d", "1wk", "1mo"],
)

if st.button("Load Stock"):

    try:
        data = get_market_data(
            ticker=ticker,
            period=period,
            interval=interval,
        )
        data = add_indicators(data)

        st.subheader(selected_stock)

        latest_price = float(data["Close"].iloc[-1])

        st.metric(
            "Latest Close",
            f"₹{latest_price:,.2f}",
        )

        figure = go.Figure(
            data=[
                go.Candlestick(
                    x=data.index,
                    open=data["Open"],
                    high=data["High"],
                    low=data["Low"],
                    close=data["Close"],
                    name=selected_stock,
                )
            ]
        )

        figure.update_layout(
            xaxis_rangeslider_visible=False,
            height=600,
        )

        st.plotly_chart(
            figure,
            use_container_width=True,
        )

        st.subheader("Technical Indicators")

        latest = data.iloc[-1]

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "RSI (14)",
            f"{latest['RSI_14']:.2f}"
        )

        col2.metric(
            "SMA (20)",
            f"₹{latest['SMA_20']:.2f}"
        )

        col3.metric(
            "SMA (50)",
            f"₹{latest['SMA_50']:.2f}"
        )

        col4.metric(
            "EMA (20)",
            f"₹{latest['EMA_20']:.2f}"
        )

        col5, col6, col7 = st.columns(3)

        col5.metric(
            "MACD",
            f"{latest['MACD']:.2f}"
        )

        col6.metric(
            "MACD Signal",
            f"{latest['MACD_SIGNAL']:.2f}"
        )

        col7.metric(
            "MACD Histogram",
            f"{latest['MACD_HIST']:.2f}"
        )





        st.subheader("Market Data")

        st.dataframe(
            data.tail(20),
            use_container_width=True,
        )

    except Exception as error:
        st.error(str(error))