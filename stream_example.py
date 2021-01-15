from alpaca_trade_api import StreamConn
from dotenv import load_dotenv
import os

load_dotenv()

conn = StreamConn(
    key_id=os.environ.get('ALPACA_PAPER_API'),
    secret_key=os.environ.get('ALPACA_PAPER_SECRET'), 
    base_url=os.environ.get('ALPACA_PAPER_URL'),
    data_url=os.environ.get('ALPACA_PAPER_URL'),
    #data_stream='alpacadatav1'
)
print(conn)


#@conn.on(r'^T.AAPL$')
#async def trade_info(conn, channel, bar):
    #print('bars', bar)
    #print(bar._raw)

@conn.on(r'^trade_updates$')
async def on_account_updates(conn, channel, account):
    print('account', account)

@conn.on(r'^status$')
async def on_status(conn, channel, data):
    print('polygon status update', data)

@conn.on(r'^AM$')
async def on_minute_bars(conn, channel, bar):
    print('bars', bar)

@conn.on(r'^A$')
async def on_second_bars(conn, channel, bar):
    print('bars', bar)

if __name__ == '__main__':
    print("start_streaming")
    print(os.environ.get('ALPACA_API_KEY'))
    # blocks forever
    #conn.run(['trade_updates', 'AM.*'])

    # if Data API streaming is enabled
    conn.run(['trade_updates', 'alpacadatav1/AM.SPY'])