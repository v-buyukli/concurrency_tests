import concurrent.futures
import time

import requests


def get_response(url):
    r = requests.get(url).content
    return r


def sequential_requests(url, num):
    start_time = time.time()

    for _ in range(num):
        response = get_response(url)
        print(f"Request {url}. Response: {response}")

    elapsed = time.time() - start_time
    print(f"Sequential: {elapsed:.2f} s")


def thread_pool_requests(url, num):
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_response, url) for _ in range(num)]
        for future in concurrent.futures.as_completed(futures):
            response = future.result()
            print(f"Request: {url}. Response: {response}")

    elapsed = time.time() - start_time
    print(f"ThreadPoolExecutor. Time: {elapsed:.2f} s")


def process_pool_requests(url, num):
    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(get_response, url) for _ in range(num)]
        for future in concurrent.futures.as_completed(futures):
            response = future.result()
            print(f"Request: {url}. Response: {response}")

    elapsed = time.time() - start_time
    print(f"ProcessPoolExecutor. Time: {elapsed:.2f} s")


if __name__ == "__main__":
    url = "https://hub.dummyapis.com/delay?seconds=3"
    num_requests = 5

    print("Sequential:")
    sequential_requests(url, num_requests)

    print("\nconcurrent.futures.ThreadPoolExecutor:")
    thread_pool_requests(url, num_requests)

    print("\nconcurrent.futures.ProcessPoolExecutor:")
    thread_pool_requests(url, num_requests)
