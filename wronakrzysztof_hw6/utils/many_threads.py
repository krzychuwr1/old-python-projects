import threading
import subprocess
import time


class MyThread (threading.Thread):
    """
    Thread contains that has to be done in it.
    """
    def __init__(self, task, language):
        threading.Thread.__init__(self)
        self.task = task
        self.language = language

    def run(self):
        if self.language == "python":  # if it's python task, then just do task[0]() it because it's a function.
            self.task[0]()
        else:
            subprocess.check_call(self.task)  # if it's in another language, its list of parameters


def many_threads(ops, pool):
    """

    :param ops: tuple
    :param pool: dictionary
    :return: time
    """
    start = time.time()
    threads = []
    for operation, amount in zip(ops, pool["amount"]):  # iterate over operations and corresponding amounts.
        for i in range(amount):
            threads.append(MyThread(operation, pool["language"]))  # create a thread for each operation.
    try:
        for thread in threads:
                thread.start()  # start all of them.
    except subprocess.CalledProcessError:
        print("An error has occurred while executing subprograms using Threading.")
        raise SystemExit
    for thread in threads:
            thread.join()  # join all so that the main thread waits for all of them to finish.

    end = time.time()
    return end-start