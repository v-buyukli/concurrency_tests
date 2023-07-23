import threading


def calculate_sum_squares(start, end, result):
    for j in range(500_000):
        sum_squares = 0
        for i in range(start, end + 1):
            sum_squares += i * i
    result.append(sum_squares)


if __name__ == "__main__":
    ranges = [(1, 250), (251, 500), (501, 750), (751, 1000)]
    results = []

    threads = [
        threading.Thread(target=calculate_sum_squares, args=(start, end, results))
        for start, end in ranges
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    total_sum_squares = sum(results)
    print("Загальна сума квадратів:", total_sum_squares)
