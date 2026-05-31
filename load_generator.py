import time
import requests

# Target URL to request
URL = "http://tdojo-elb-573227631.eu-central-1.elb.amazonaws.com/"

# Requests per second
RPS = 1

# Prevent divide-by-zero
if RPS <= 0:
    raise ValueError("RPS must be > 0")

# Use a single Session for connection pooling
session = requests.Session()

# Time between requests
interval = 1.0 / RPS

try:
    # Loop: send a GET, print short status, then sleep
    while True:
        try:
            session.get(URL, timeout=2)
            print(f"Requested {URL}")
        except Exception as e:
            # Print network or timeout errors
            print("ERR:", e)
        # Fixed delay between requests
        time.sleep(interval)
except KeyboardInterrupt:
    # Graceful stop on Ctrl+C
    print("Stopped by user")