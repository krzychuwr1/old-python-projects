import subprocess
import time


def one_thread(ops, pool):
    """
    Run task in main thread.
    :param ops: tuple
    :param pool: tuple
    :return: time
    """
    start = time.time()

    try:
        for operation, amount in zip(ops, pool["amount"]):
            if pool["language"] != "python":  # for other languages use subprocess
                for i in range(amount):
                    subprocess.check_call(operation)
            else:
                for i in range(amount):  # for python just call function
                    operation[0]()
    except subprocess.CalledProcessError:
        print("An error has occurred while executing subprograms using multiprocessing module")
        raise SystemExit
    end = time.time()

    return end-start
