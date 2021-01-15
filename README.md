# Alpaca Stock Streaming (SP500)

This will get you the basics for setting up the S&P 500 individual indexes. This only prints the info out to console for review. Currently Alpaca only allows trading data for 30 stocks at a time. However, you can also watch minute updates for unlimited stocks.

## Requirements
You need:

* An Alpaca Account
* python3 (ran with python 3.9)
* virtualenv to install packages

## Setup
Copy the `.env.sample` and save the copy as `.env`. Go to the Alpaca Paper account and fill in `ALPACA_PAPER_API` and `ALPACA_PAPER_SECRET`. Everything else should be ok as is.

Start by entering your virtual environment and running `python websocket_example.py`