import multiprocessing

import requests


def get_and_save_response(url):
    response = requests.get(url)
    with open("multiprocessing_responses.txt", "a") as file:
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

    processes = []

    for url in urls:
        process = multiprocessing.Process(target=get_and_save_response, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
