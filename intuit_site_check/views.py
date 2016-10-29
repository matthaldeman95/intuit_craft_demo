import datetime
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
import generate_plot
import site_check
from .models import WebSite, DataPoint
from tables import DataPointTable
from filters import filter_start_end_datetime, filter_timezone_range


def dashboard(request***REMOVED***:
    ***REMOVED***
    Main dashboard home page.  Two columns for two websites.  Displays site status, load time,
        any error messages, interactive pyplot, django_tables.  Last hour of data
    ***REMOVED***

    template = loader.get_template('intuit_site_check/dashboard.html'***REMOVED***

    current_time = timezone.now(***REMOVED***

    # Load each website data and save data points
    s = WebSite.objects.filter(site_id="turbotax"***REMOVED***[0***REMOVED***
    t_id = s.site_id
    t_http_code, t_load_time, t_email_sent = site_check.site_check(s***REMOVED***
    dp = DataPoint(website=s, timestamp=current_time, status_code=t_http_code,
                   load_time=t_load_time***REMOVED***
    dp.save(***REMOVED***

    s = WebSite.objects.filter(site_id="wikipedia"***REMOVED***[0***REMOVED***
    w_id = s.site_id
    w_http_code, w_load_time, w_email_sent = site_check.site_check(s***REMOVED***
    dp = DataPoint(website=s, timestamp=current_time, status_code=w_http_code,
                   load_time=w_load_time***REMOVED***
    dp.save(***REMOVED***

    # Load all datapoints for each site
    t_all_data = DataPoint.objects.filter(website=1***REMOVED***.order_by('-timestamp'***REMOVED***
    w_all_data = DataPoint.objects.filter(website=2***REMOVED***.order_by('-timestamp'***REMOVED***

    # Then filter only points in past hour
    time_delta = datetime.timedelta(hours=1***REMOVED***
    t_latest_data = filter_timezone_range(t_all_data, time_delta***REMOVED***
    w_latest_data = filter_timezone_range(w_all_data, time_delta***REMOVED***

    # Create django_tables of data, add pagination
    # TODO Fix pagination for two tables on same page (changing page on 1 changes both***REMOVED***
    t_table = DataPointTable(t_latest_data***REMOVED***
    # t_table.paginate(page=request.GET.get('page', 1***REMOVED***, per_page=10***REMOVED***
    w_table = DataPointTable(w_latest_data***REMOVED***
    # w_table.paginate(page=request.GET.get('page', 1***REMOVED***, per_page=10***REMOVED***

    # Create mpld3 plots of data
    t_plot = generate_plot.generate_plot(t_latest_data, 0, 3***REMOVED***
    w_plot = generate_plot.generate_plot(w_latest_data, 0, 3***REMOVED***

    # Pass all data to HTML template for page
    context = {
        'current_time': current_time,
        't_http_code': t_http_code,
        't_load_time': t_load_time,
        't_email_sent': int(t_email_sent***REMOVED***,
        't_latest_data': t_latest_data,
        't_plot': t_plot,
        't_table': t_table,
        't_id': t_id,
        'w_http_code': w_http_code,
        'w_load_time': w_load_time,
        'w_email_sent': int(w_email_sent***REMOVED***,
        'w_latest_data': w_latest_data,
        'w_plot': w_plot,
        'w_id': w_id,
        'w_table': w_table
           ***REMOVED***

    return HttpResponse(template.render(context, request***REMOVED******REMOVED***


def detail_page(request, site_id, data_range=3***REMOVED***:

    template = loader.get_template('intuit_site_check/detail_page.html'***REMOVED***
    s = WebSite.objects.filter(site_id=site_id***REMOVED***[0***REMOVED***
    site_name = s.site_name
    site_id = s.site_id
    current_time = timezone.now(***REMOVED***

    # Download data from website, create datapoint
    http_code, load_time, email_sent = site_check.site_check(s***REMOVED***
    dp = DataPoint(website=s, timestamp=current_time, status_code=http_code,
                   load_time=load_time***REMOVED***
    dp.save(***REMOVED***

    # Get HTML Post data for radio buttons
    data_range = request.POST.get('choice'***REMOVED***

    # Get HTML Post data for text entry boxes
    start_date_time = request.POST.get('start_date_time'***REMOVED***
    end_date_time = request.POST.get('end_date_time'***REMOVED***

    # Perform checks to make sure time range is valid
    # TODO Make this a function in the filters file
    valid_time_range = True
    invalid_range_message = ""

    if start_date_time:

        # If start time filled in but end is left blank:
        if not end_date_time:
            data_range = 3
            valid_time_range = False
            invalid_range_message = "Missing end date/time"

        # Create valid datetime objects using mask, if invalid, incorrect entry format
        else:
            ***REMOVED***
                start_date_time = datetime.datetime.strptime(str(start_date_time***REMOVED***, '%m/%d/%Y %I:%M %p'***REMOVED***
                end_date_time = datetime.datetime.strptime(str(end_date_time***REMOVED***, '%m/%d/%Y %I:%M %p'***REMOVED***

                # Check to make sure that start comes before end
                if start_date_time >= end_date_time:
                    data_range = 3
                    valid_time_range = False
                    invalid_range_message = "End date cannot be before start"
            except ValueError:
                data_range = 3
                valid_time_range = False
                invalid_range_message = "Incorrect entry format:  Use format 10/29/2016 7:18 PM"
    # End date is filled in but start is left empty
    elif end_date_time and not start_date_time:
        data_range = 3
        valid_time_range = False
        invalid_range_message = "Missing start date/time"

    # If a radio box was selected, use that
    if data_range:
        data_range = int(data_range***REMOVED***
    # If neither radio box or manual entry used, default to past hour data
    # if manual entry used, set data_range to -1 flag
    else:
        if start_date_time:
            data_range = -1
        else:
            data_range = 3

    # Choose preset data ranges if radio box
    if data_range == 1:
        time_delta = datetime.timedelta(minutes=5***REMOVED***
    elif data_range == 2:
        time_delta = datetime.timedelta(minutes=30***REMOVED***
    elif data_range == 3:
        time_delta = datetime.timedelta(hours=1***REMOVED***
    elif data_range == 4:
        time_delta = datetime.timedelta(hours=24***REMOVED***

    # Get data in selected data range
    all_data = DataPoint.objects.filter(website=s***REMOVED***.order_by('-timestamp'***REMOVED***

    data_range_text = ""
    if data_range == 5:
        requested_data = all_data
    elif data_range != -1:
        requested_data = filter_timezone_range(all_data, time_delta***REMOVED***
    else:
        if start_date_time:
            requested_data = filter_start_end_datetime(all_data,
                                                       start_date_time, end_date_time***REMOVED***
            data_range_text = str(start_date_time***REMOVED*** + " - " + str(end_date_time***REMOVED***
        else:
            requested_data = filter_timezone_range(all_data, datetime.timedelta(hours=24***REMOVED******REMOVED***

    # Create django_table and plot
    table = DataPointTable(requested_data***REMOVED***
    table.paginate(page=request.GET.get('page', 1***REMOVED***, per_page=13***REMOVED***

    plot = generate_plot.generate_plot(requested_data, 1, data_range, data_range_text***REMOVED***

    # Preset radio box options
    radio_options = [
        'Last 5 minutes',
        'Last 30 minutes',
        'Last hour',
        'Last day',
        'All time'
    ***REMOVED***

    context = {
        'site_id': site_id,
        'site_name': site_name,
        'http_code': http_code,
        'load_time': load_time,
        'email_sent': email_sent,
        'plot': plot,
        'radio_options': radio_options,
        'all_data': all_data,
        'table': table,
        'valid_time_range': int(valid_time_range***REMOVED***,
        'invalid_range_message': invalid_range_message
***REMOVED***
    return HttpResponse(template.render(context, request***REMOVED******REMOVED***
