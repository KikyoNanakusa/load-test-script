import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
import requests
import time

def send_request(url):
    response = requests.get(url)
    print(response.status_code)
    return response

def main():
    load_dotenv()
    print(os.getenv("TEST_URL"))

    urls = [os.getenv("TEST_URL") for _ in range(100)]
    requests_conut = 100
    print(f"Sending {len(urls)} requests with {requests_conut} threads")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=requests_conut) as executor:
        list(executor.map(send_request, urls)) 

    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")

if __name__ == "__main__":
    main()
