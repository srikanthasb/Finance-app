import os
from dotenv import load_dotenv
from kiteconnect import KiteTicker

load_dotenv()

API_KEY = os.getenv("ZERODHA_API_KEY")
ACCESS_TOKEN = os.getenv("ZERODHA_ACCESS_TOKEN")


class LiveMarket:
    def __init__(self):
        if not API_KEY:
            raise ValueError("ZERODHA_API_KEY is missing from .env")

        if not ACCESS_TOKEN:
            raise ValueError("ZERODHA_ACCESS_TOKEN is missing from .env")

        self.ticker = KiteTicker(
            API_KEY,
            ACCESS_TOKEN,
        )

    def start(self, instrument_tokens):
        """
        Start live market-data streaming.

        instrument_tokens:
            List of Zerodha instrument tokens.
        """

        def on_connect(ws, response):
            print("Connected to Zerodha WebSocket")

            ws.subscribe(instrument_tokens)

            ws.set_mode(
                ws.MODE_QUOTE,
                instrument_tokens,
            )

            print(
                f"Subscribed to {len(instrument_tokens)} instrument(s)"
            )

        def on_ticks(ws, ticks):
            for tick in ticks:
                print(tick)

        def on_close(ws, code, reason):
            print(
                f"WebSocket closed: {code} - {reason}"
            )

        def on_error(ws, code, reason):
            print(
                f"WebSocket error: {code} - {reason}"
            )

        self.ticker.on_connect = on_connect
        self.ticker.on_ticks = on_ticks
        self.ticker.on_close = on_close
        self.ticker.on_error = on_error

        self.ticker.connect()