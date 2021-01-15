from alpaca_trade_api import StreamConn
from alpaca_trade_api.common import URL

from dotenv import load_dotenv
import os

load_dotenv()

ALPACA_API_KEY=os.environ.get('ALPACA_PAPER_API')
ALPACA_SECRET_KEY=os.environ.get('ALPACA_PAPER_SECRET')


if __name__ == '__main__':
    import logging

    with open('spindexes.csv') as fid:
        indexes = fid.readlines()

    indexes = [i.strip() for i in indexes]

    run_idx = ['alpacadatav1/T.' + i for i in indexes]
    am_idx =  ['alpacadatav1/AM.' + i for i in indexes]

    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    conn = StreamConn(
            ALPACA_API_KEY,
            ALPACA_SECRET_KEY,
            base_url=URL('https://paper-api.alpaca.markets'),
            data_url=URL('https://data.alpaca.markets'),
            data_stream='alpacadatav1'
        )
    @conn.on(r'^AM\..+$')
    async def on_minute_bars(conn, channel, bar):
        print('bars', bar)

    quote_count = 0  # don't print too much quotes
    @conn.on(r'Q\..+')
    async def on_quotes(conn, channel, quote):
        global quote_count
        if quote_count % 10 == 0:
            print('quote', quote)
        quote_count += 1

    @conn.on(r'T\..+')
    async def on_trades(conn, channel, trade):
        print('trade', trade)


    # these won't work:
    # conn.run(['T.*'])
    # conn.run(['Q.*'])
    # conn.run(['alpacadatav1/Q.*'])
    # conn.run(['T.TSLA'])
    # conn.run(['Q.TSLA'])

    # these are fine:
    # conn.run(['AM.*'])
    # conn.run(['alpacadatav1/AM.*'])

    # conn.run(['alpacadatav1/AM.TSLA'])
    # conn.run(['alpacadatav1/Q.GOOG'])
    conn.run(am_idx + run_idx[:30])

