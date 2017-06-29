from utils import *
import sys


try:
    settings = parsing.Settings('config.ini')  # parse config.ini and create settings object
except KeyboardInterrupt:
    sys.exit()
except Exception as e:
    try:
        exceptions.read_exception(e)
    finally:
        sys.exit()


"""
Creating 2 Data Frames, data_frames['astronomy'] contains DataFrame with astronomy related values,
data_frames['currency'] contains DataFrame with currency values
"""
try:
    data_frames = analyze.create_data_frames(settings)
except KeyboardInterrupt:
    sys.exit()
except Exception as e:
    try:
        exceptions.read_exception(e)
    finally:
        sys.exit()


"""
Create tops list which contains dictionaries.
Every Dictionary contains DataFrame, name of currency, 
name of astronomy data column and correlation.
Every DataFrame contains currency data and astronomy related data
"""
try:
    tops = analyze.get_top(data_frames['currency'], data_frames['astronomy'], settings.how_many_files)
except KeyboardInterrupt:
    sys.exit()
except:
    print("Some error has occured while trying to find best correlations.")
    sys.exit()

"""
Create plots and save them to files defined in config.ini
"""
try:
    plot.save_plots(tops, settings)
except KeyboardInterrupt:
    sys.exit()
except Exception as e:
    try:
        exceptions.read_exception(e)
    finally:
        sys.exit()
