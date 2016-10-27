(function(***REMOVED*** {
    'use strict';
    var timeParsePatterns = [
        // 9
    ***REMOVED***
            re: /^\d{1,2***REMOVED***$/i,
            handler: function(bits***REMOVED*** {
                if (bits[0***REMOVED***.length === 1***REMOVED*** {
                    return '0' + bits[0***REMOVED*** + ':00';
            ***REMOVED*** else {
                    return bits[0***REMOVED*** + ':00';
            ***REMOVED***
        ***REMOVED***
***REMOVED***
        // 13:00
    ***REMOVED***
            re: /^\d{2***REMOVED***[:.***REMOVED***\d{2***REMOVED***$/i,
            handler: function(bits***REMOVED*** {
                return bits[0***REMOVED***.replace('.', ':'***REMOVED***;
        ***REMOVED***
***REMOVED***
        // 9:00
    ***REMOVED***
            re: /^\d[:.***REMOVED***\d{2***REMOVED***$/i,
            handler: function(bits***REMOVED*** {
                return '0' + bits[0***REMOVED***.replace('.', ':'***REMOVED***;
        ***REMOVED***
***REMOVED***
        // 3 am / 3 a.m. / 3am
    ***REMOVED***
            re: /^(\d+***REMOVED***\s*([ap***REMOVED******REMOVED***(?:.?m.?***REMOVED***?$/i,
            handler: function(bits***REMOVED*** {
                var hour = parseInt(bits[1***REMOVED******REMOVED***;
                if (hour === 12***REMOVED*** {
                    hour = 0;
            ***REMOVED***
                if (bits[2***REMOVED***.toLowerCase(***REMOVED*** === 'p'***REMOVED*** {
                    if (hour === 12***REMOVED*** {
                        hour = 0;
                ***REMOVED***
                    return (hour + 12***REMOVED*** + ':00';
            ***REMOVED*** else {
                    if (hour < 10***REMOVED*** {
                        return '0' + hour + ':00';
                ***REMOVED*** else {
                        return hour + ':00';
                ***REMOVED***
            ***REMOVED***
        ***REMOVED***
***REMOVED***
        // 3.30 am / 3:15 a.m. / 3.00am
    ***REMOVED***
            re: /^(\d+***REMOVED***[.:***REMOVED***(\d{2***REMOVED******REMOVED***\s*([ap***REMOVED******REMOVED***.?m.?$/i,
            handler: function(bits***REMOVED*** {
                var hour = parseInt(bits[1***REMOVED******REMOVED***;
                var mins = parseInt(bits[2***REMOVED******REMOVED***;
                if (mins < 10***REMOVED*** {
                    mins = '0' + mins;
            ***REMOVED***
                if (hour === 12***REMOVED*** {
                    hour = 0;
            ***REMOVED***
                if (bits[3***REMOVED***.toLowerCase(***REMOVED*** === 'p'***REMOVED*** {
                    if (hour === 12***REMOVED*** {
                        hour = 0;
                ***REMOVED***
                    return (hour + 12***REMOVED*** + ':' + mins;
            ***REMOVED*** else {
                    if (hour < 10***REMOVED*** {
                        return '0' + hour + ':' + mins;
                ***REMOVED*** else {
                        return hour + ':' + mins;
                ***REMOVED***
            ***REMOVED***
        ***REMOVED***
***REMOVED***
        // noon
    ***REMOVED***
            re: /^no/i,
            handler: function(bits***REMOVED*** {
                return '12:00';
        ***REMOVED***
***REMOVED***
        // midnight
    ***REMOVED***
            re: /^mid/i,
            handler: function(bits***REMOVED*** {
                return '00:00';
        ***REMOVED***
    ***REMOVED***
    ***REMOVED***;

    function parseTimeString(s***REMOVED*** {
        for (var i = 0; i < timeParsePatterns.length; i++***REMOVED*** {
            var re = timeParsePatterns[i***REMOVED***.re;
            var handler = timeParsePatterns[i***REMOVED***.handler;
            var bits = re.exec(s***REMOVED***;
            if (bits***REMOVED*** {
                return handler(bits***REMOVED***;
        ***REMOVED***
    ***REMOVED***
        return s;
***REMOVED***

    window.parseTimeString = parseTimeString;
***REMOVED******REMOVED***(***REMOVED***;
