import threading

import requests


def save_response(url):
    response = requests.get(url)
    with open("threading_responses.txt", "a") as file:
        file.write(f"URL: {url}\n")
        file.write(f"Response:\n{response.text}\n")
        file.write("\n")


if __name__ == "__main__":
    urls = [
        "https://docs.python.org",
        "https://auth0.com",
        "https://heroku.com",
        "https://uk.wikipedia.org",
        "https://www.work.ua",
    ]

    threads = []

    for url in urls:
        thread = threading.Thread(target=save_response, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
