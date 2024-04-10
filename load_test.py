import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
import requests

load_dotenv()
print(os.getenv("TEST_URL"))


def send_request(url):
    response = requests.get(url)
    print(response.status_code)
    return response


def main():
    urls = [os.getenv("TEST_URL") for _ in range(100)]
    requests_conut = 100

    with ThreadPoolExecutor(max_workers=requests_conut) as executor:
        for _ in range(requests_conut):
            executor.map(send_request, urls * requests_conut)


if __name__ == "__main__":
    main()
