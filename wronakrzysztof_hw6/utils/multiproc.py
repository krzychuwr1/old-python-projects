import  subprocess
import multiprocessing
import time


def multiprocessing_process(task, language):
    """
    :param task: list
    :param language:
    :return:
    """
    if language == "python":  # if its in python just do task[0]()
        task[0]()
    else:
        subprocess.check_call(task)  # else its a list which has to be called in subprocess


def many_threads_multip(ops, pool):
    """
    :param ops: tuple
    :param pool: tuple
    :return: time
    """
    start = time.time()
    processes = []
    for operation, amount in zip(ops, pool["amount"]):
        for i in range(amount):  # create processes.
            process = multiprocessing.Process(target = multiprocessing_process, args=(operation, pool["language"]))
            processes.append(process)
    try:
        for process in processes:
            process.start()  # start all processes
    except subprocess.CalledProcessError:
        print("An error has occurred while executing subprograms using multiprocessing module")
        raise SystemExit
    for process in processes:
        process.join()  # join all processes to wait for them to finish.

    end = time.time()
    return end-start