import matplotlib.pyplot as plt
import mpld3
from numpy import mean


def generate_plot(data, size, data_range, user_selected=None***REMOVED***:
    ***REMOVED***
    Generates interactive plots of site data
    :param data:    Site data
    :param size:    Desired size of plot; 0 for small, 1 for large
    :param data_range   Selected timestamp range of data in integer form
    :return:        Interactive mpld3 plot
    ***REMOVED***


    # Load data
    x = [***REMOVED***
    y = [***REMOVED***
    for data in data:
        x.append(data.timestamp***REMOVED***
        y.append(float(data.load_time***REMOVED******REMOVED***

    # Average of data
    avg = mean(y***REMOVED***
    avg = float(round(avg, 3***REMOVED******REMOVED***
    avg_text = "Average: " + str(avg***REMOVED***

    figsize = [(6, 4.5***REMOVED***,(8, 6***REMOVED******REMOVED***

    print size, figsize[size***REMOVED***

    # Control size of output plot
    mpl_figure = plt.figure(figsize=figsize[size***REMOVED******REMOVED***

    title = "Page Load Times: "

    # Give title based on the selected data range
    if data_range == -1:
        title += user_selected

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

    font = {'fontname':'Helvetica'***REMOVED***

    plt.plot(x, y***REMOVED***
    plt.title(title, size=18, **font***REMOVED***
    plt.xlabel('Time', size=15, **font***REMOVED***
    plt.ylabel('Load Time (s***REMOVED***', size=15, **font***REMOVED***
    plt.annotate(avg_text, xy=(0.65, 0.92***REMOVED***, xycoords='axes fraction', size=16, **font***REMOVED***

    mpld3_plot = mpld3.fig_to_html(mpl_figure***REMOVED***

    plt.clf(***REMOVED***

    return mpld3_plot
