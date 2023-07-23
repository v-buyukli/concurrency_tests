import multiprocessing


def calculate_sum_squares(start, end, result):
    for j in range(500_000):
        sum_squares = 0
        for i in range(start, end + 1):
            sum_squares += i * i
    result.value = sum_squares


if __name__ == "__main__":
    result1 = multiprocessing.Value("i", 0)
    result2 = multiprocessing.Value("i", 0)
    result3 = multiprocessing.Value("i", 0)
    result4 = multiprocessing.Value("i", 0)
    ranges = [(1, 250), (251, 500), (501, 750), (751, 1000)]

    processes = [
        multiprocessing.Process(target=calculate_sum_squares, args=(start, end, result))
        for (start, end), result in zip(ranges, [result1, result2, result3, result4])
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    total_sum_squares = result1.value + result2.value + result3.value + result4.value
    print("Загальна сума квадратів:", total_sum_squares)
