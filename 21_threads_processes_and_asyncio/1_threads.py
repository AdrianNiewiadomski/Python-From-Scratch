from time import sleep
from datetime import datetime
from threading import Thread


def send_request_to_server():
    print("Sending request.")
    sleep(2)  # While sending the request we basically wait for server response.
    print("Returning server response.")


def read_file():
    print("Reading a file.")
    sleep(1)
    print("Returning data from the file.")


if __name__ == "__main__":
    start = datetime.now()
    send_request_to_server()
    read_file()
    end = datetime.now()
    print("Execution time without threads: ", end - start, "s.\n")

    start = datetime.now()
    t1 = Thread(target=send_request_to_server)
    t2 = Thread(target=read_file)
    t1.start()
    t2.start()
    t1.join()  # To wait for the thread to finish its job use join function.
    t2.join()
    end = datetime.now()
    print("Execution time with threads: ", end - start, "s.")
