from django.utils import timezone


def filter_timezone_range(data_set, td):
    """
    Filters data to return only data within given time delta from current time
    :param data_set:    Data to filter
    :param td:          datatime.timedelta object with desired time range
    :return:            Data only within that timedelta
    """

    filtered_data = []
    for data in data_set:
        if data.timestamp >= timezone.now() - td:
            filtered_data.append(data)

    return filtered_data


def filter_start_end_datetime(data_set, start, end):
    """
    Filters data between two date/times
    :param data_set:    Data to filter
    :param start:       Start time, must be in format matching mask below
    :param end:         End time, same condition
    :return:            Filtered data
    """

    # Add timezones to timezone-naive data
    start = timezone.make_aware(start)
    end = timezone.make_aware(end)

    filtered_data = []
    for data in data_set:
        if start <= data.timestamp <= end:
            filtered_data.append(data)

    return filtered_data
