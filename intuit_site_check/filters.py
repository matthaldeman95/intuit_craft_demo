from django.utils import timezone
import datetime


def filter_timezone_range(data_set, td***REMOVED***:
    ***REMOVED***
    Filters data to return only data within given time delta from current time
    :param data_set:    Data to filter
    :param td:          datatime.timedelta object with desired time range
    :return:            Data only within that timedelta
    ***REMOVED***

    filtered_data = [***REMOVED***
    for data in data_set:
        if data.timestamp >= timezone.now(***REMOVED*** - td:
            filtered_data.append(data***REMOVED***

    return filtered_data


def filter_start_end_datetime(data_set, start, end***REMOVED***:
    ***REMOVED***
    Filters data between two date/times
    :param data_set:    Data to filter
    :param start:       Start time, must be in format matching mask below
    :param end:         End time, same condition
    :return:            Filtered data
    ***REMOVED***

    # Add timezones to timezone-naive data
    start = timezone.make_aware(start***REMOVED***
    end = timezone.make_aware(end***REMOVED***

    filtered_data = [***REMOVED***
    for data in data_set:
        if start <= data.timestamp <= end:
            filtered_data.append(data***REMOVED***

    return filtered_data

