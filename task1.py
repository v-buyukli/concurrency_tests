import threading


def even_numbers():
    for number in range(2, 21, 2):
        print(number)


def odd_numbers():
    for number in range(1, 20, 2):
        print(number)


if __name__ == "__main__":
    t1 = threading.Thread(target=even_numbers)
    t2 = threading.Thread(target=odd_numbers)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
