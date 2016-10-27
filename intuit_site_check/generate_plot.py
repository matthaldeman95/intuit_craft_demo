from matplotlib import dates
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import numpy as np
import mpld3
from numpy import mean


def generate_plot(data, size, data_range***REMOVED***:
    ***REMOVED***
    Generates interactive plots of site data
    :param data:    Site data
    :return:        Interactive mpld3 plot
    ***REMOVED***
    x = [***REMOVED***
    y = [***REMOVED***
    for data in data:
        x.append(data.timestamp***REMOVED***
        print type(data.timestamp***REMOVED***
        y.append(data.load_time***REMOVED***

    avg = mean(y***REMOVED***
    avg = float(round(avg, 3***REMOVED******REMOVED***
    avg_text = "Average: " + str(avg***REMOVED***
    print avg_text

    if size == 0:
        mpl_figure = plt.figure(1, figsize=(5,4***REMOVED******REMOVED***
    elif size == 1:
        mpl_figure = plt.figure(1, figsize=(8,6***REMOVED******REMOVED***

    title = "Site Load Times: "

    if data_range == -1:
        title += "User Defined"

    elif data_range == 1:
        title += "Last 5 minutes"

    elif data_range == 2:
        title += "Last 30 minutes"

    elif data_range == 3:
        title += "Last hour"

    elif data_range == 4:
        title += "Last day"

    elif data_range == 5:
        title += "All time"

    plt.plot(x, y***REMOVED***
    plt.title(title, size=18***REMOVED***
    plt.xlabel('Time', size=15***REMOVED***
    plt.ylabel('Load Time (s***REMOVED***', size=15***REMOVED***
    plt.annotate(avg_text, xy=(0.65, 0.85***REMOVED***, xycoords='axes fraction', size=16***REMOVED***

    mpld3_plot = mpld3.fig_to_html(mpl_figure***REMOVED***

    plt.clf(***REMOVED***

    return mpld3_plot

