import matplotlib.pyplot as plt
import mpld3
from numpy import mean
import datetime


def generate_plot(data, size, data_range, user_selected=None):
    """
    Generates interactive plots of site data
    :param data:    Site data
    :param size:    Desired size of plot; 0 for small, 1 for large
    :param data_range   Selected timestamp range of data in integer form
    :param user_selected:   Text indicating user selected time range (for title of plot)
    :return:        Interactive mpld3 plot
    """

    # Load data
    x = []
    y = []
    for data in data:
        time_stamp = data.timestamp - datetime.timedelta(hours=7)
        x.append(time_stamp)
        y.append(float(data.load_time))

    # Average of data
    avg = mean(y)
    avg = float(round(avg, 3))
    avg_text = "Average: " + str(avg)

    figsize = [(6, 4.5), (8, 6)]

    # Control size of output plot
    mpl_figure = plt.figure(figsize=figsize[size])

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

    plt.plot(x, y)
    plt.title(title, size=18)
    plt.xlabel('Time', size=15)
    plt.ylabel('Load Time (s)', size=15)
    plt.annotate(avg_text, xy=(0.65, 0.92), xycoords='axes fraction', size=16)

    mpld3_plot = mpld3.fig_to_html(mpl_figure)

    plt.clf()

    return mpld3_plot
