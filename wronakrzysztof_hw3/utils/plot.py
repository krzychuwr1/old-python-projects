import matplotlib.pyplot as plt
import matplotlib.axes as axes
import matplotlib


# save_plots creates plots based on dataframes from tops and saves them to files defined in settings.
def save_plots(tops, settings):
    matplotlib.rc('xtick', labelsize=10)
    matplotlib.rc('ytick', labelsize=10)
    for top, file_name, number in zip(tops, settings.output_files_list, range(len(tops))):
        try:
            plt.figure(number)  # next figure
            astro_column = top['astro']  # contains the name of astronomy related data column
            curr_column = top['curr']  # contains the name of currency data column
            data = top['DataFrame']
            ax1 = getattr(data, astro_column).plot(label=astro_column)  # create axis with astronomy data
            ax2 = getattr(data, curr_column).plot(secondary_y=True, label='USD/'+curr_column)  # create currency axis
            ax1.set_ylabel(astro_column)
            ax2.set_ylabel('USD/'+curr_column)
            title = astro_column+" correlation to "+curr_column+", Corr: "+str(top['corr'])
            axes.Axes.set_title(ax1, title)
            handles, labels = ax1.get_legend_handles_labels()
            ax1.legend(handles, labels)  # set legend for axis1
            handles, labels = ax2.get_legend_handles_labels()
            ax2.legend(handles, labels, loc=2)  # set legend for axis2 in another corner
        except Exception as e:
            raise RuntimeError("An error has occurred while creating plot.") from e
        try:
            plt.savefig(file_name)  # save to plot to file_name file
            print(number+1, "Result plot has been saved to", file_name)
        except Exception as e:
            raise RuntimeError("An error has occured while saving plot to file.") from e
