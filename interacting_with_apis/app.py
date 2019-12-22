import time
from libs.openexchange import OpenExchangeClient

APP_ID = 'xxxx'

client = OpenExchangeClient(APP_ID)

thb_amount = 1000
start = time.time()
usd_amount = client.convert(thb_amount, "THB", "USD")
end = time.time()
print(end-start)

thb_amount = 500
start = time.time()
usd_amount = client.convert(thb_amount, "THB", "USD")
end = time.time()
print(end-start)

start = time.time()
usd_amount = client.convert(thb_amount, "THB", "USD")
end = time.time()
print(end-start)

start = time.time()
usd_amount = client.convert(thb_amount, "THB", "USD")
end = time.time()
print(end-start)
print(f"USD{usd_amount:.2f} is THB{thb_amount}")
