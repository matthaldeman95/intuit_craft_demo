from matplotlib import dates
import matplotlib.pyplot as plt
import numpy as np
import mpld3

def generate_plot(data, size***REMOVED***:
    ***REMOVED***
    Generates interactive plots of site data
    :param data:    Site data
    :return:        Interactive mpld3 plot
    ***REMOVED***
    x = [***REMOVED***
    y = [***REMOVED***
    for data in data:
        x.append(data.timestamp***REMOVED***
        y.append(data.load_time***REMOVED***
    if size == 0:
        mpl_figure = plt.figure(1, figsize=(5,4***REMOVED******REMOVED***
    elif size == 1:
        mpl_figure = plt.figure(1, figsize=(8,6***REMOVED******REMOVED***
    plt.plot(x, y***REMOVED***
    mpld3_plot = mpld3.fig_to_html(mpl_figure***REMOVED***

    plt.clf(***REMOVED***

    return mpld3_plot

