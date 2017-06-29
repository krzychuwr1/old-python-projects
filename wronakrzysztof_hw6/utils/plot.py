import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def make_plot(one_thread_times, threading_times, multiprocessing_times, pools):
    """
    Creates a plot and saves it to plot.png file
    :param one_thread_times: list
    :param threading_times: list
    :param multiprocessing_times: list
    :param pools: tuple
    :return: none
    """
    matplotlib.rc('xtick', labelsize=9)
    ind = np.arange(len(pools))  # the x locations for the groups
    width = 0.25
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, one_thread_times, width, color='r',)

    rects2 = ax.bar(ind + width, threading_times, width, color='y')

    rects3 = ax.bar(ind + 2*width, multiprocessing_times, width, color='b')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Time in seconds')
    ax.set_title('Times')
    ax.set_xticks(ind + width)
    ax.set_xticklabels([i["name"] for i in pools])

    ax.legend((rects1[0], rects2[0], rects3[0]), ('1CPU', 'Threading', 'Multiprocessing'))


    def autolabel(rects):
        """
        Attaches labels.
        :param rects:
        :return:
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.savefig("plot.png")