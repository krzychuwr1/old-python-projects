from utils import compilation
from utils import one_thread
from utils import many_threads
from utils import multiproc
from utils import plot
from utils import IO_CPU


# tuple of all operations.
operations = (
        ["java", "-cp", "java/", "IO1"],
        ["java", "-cp", "java/", "IO2"],
        ["java", "-cp", "java/", "CPU1"],
        ["java", "-cp", "java/", "CPU2"],
        ["./c++/IO1"],
        ["./c++/IO2"],
        ["./c++/CPU1"],
        ["./c++/CPU2"],
        [IO_CPU.IO1],
        [IO_CPU.IO2],
        [IO_CPU.CPU1],
        [IO_CPU.CPU2]
        )

# tuple of all pools. pools["amount"] has a tuple with actual pool. first 4 numbers are java, then c++, then python
pools = (
        {"name": "javaIO", "language": "java", "amount": (15, 15)+(0,)*10},
        {"name": "javaCPU", "language": "java", "amount": (0, 0, 15, 15)+(0,)*8},
        {"name": "javaMixed", "language": "java", "amount": (7, 8, 7, 8)+(0,)*8},
        {"name": "c++IO", "language": "c++", "amount": (0,)*4+(15, 15)+(0,)*6},
        {"name": "c++CPU", "language": "c++", "amount": (0,)*6+(15, 15)+(0,)*4},
        {"name": "c++Mixed", "language": "c++", "amount": (0,)*4+(7, 8, 7, 8)+(0,)*4},
        {"name": "pythonIO", "language": "python", "amount": (0,)*8+(15, 15, 0, 0)},
        {"name": "pythonCPU", "language": "python", "amount": (0,)*8+(0, 0, 15, 15)},
        {"name": "pythonMixed", "language": "python", "amount": (0,)*8+(7,8, 7, 8)}
        )

if __name__ == "__main__":
    # compile c++ and java sources.
    compilation.do()
    
    one_thread_times = []
    threading_times = []
    multiprocessing_times = []

    # iterate over pools, get times of one thread execution, threading and multiprocessing for each pool.
    for pool in pools:
        one_thread_times.append(one_thread.one_thread(operations, pool))
        threading_times.append(many_threads.many_threads(operations, pool))
        multiprocessing_times.append(multiproc.many_threads_multip(operations, pool))

    # create plot
    try:
        plot.make_plot(one_thread_times, threading_times, multiprocessing_times, pools)
    except Exception as e:
        print("An error has occured")
        print(e)

