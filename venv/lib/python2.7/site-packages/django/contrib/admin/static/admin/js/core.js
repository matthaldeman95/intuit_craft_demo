// Core javascript helper functions

// basic browser identification & version
var isOpera = (navigator.userAgent.indexOf("Opera"***REMOVED*** >= 0***REMOVED*** && parseFloat(navigator.appVersion***REMOVED***;
var isIE = ((document.all***REMOVED*** && (!isOpera***REMOVED******REMOVED*** && parseFloat(navigator.appVersion.split("MSIE "***REMOVED***[1***REMOVED***.split(";"***REMOVED***[0***REMOVED******REMOVED***;

// Cross-browser event handlers.
function addEvent(obj, evType, fn***REMOVED*** {
    'use strict';
    if (obj.addEventListener***REMOVED*** {
        obj.addEventListener(evType, fn, false***REMOVED***;
        return true;
***REMOVED*** else if (obj.attachEvent***REMOVED*** {
        var r = obj.attachEvent("on" + evType, fn***REMOVED***;
        return r;
***REMOVED*** else {
        return false;
***REMOVED***
***REMOVED***

function removeEvent(obj, evType, fn***REMOVED*** {
    'use strict';
    if (obj.removeEventListener***REMOVED*** {
        obj.removeEventListener(evType, fn, false***REMOVED***;
        return true;
***REMOVED*** else if (obj.detachEvent***REMOVED*** {
        obj.detachEvent("on" + evType, fn***REMOVED***;
        return true;
***REMOVED*** else {
        return false;
***REMOVED***
***REMOVED***

function cancelEventPropagation(e***REMOVED*** {
    'use strict';
    if (!e***REMOVED*** {
        e = window.event;
***REMOVED***
    e.cancelBubble = true;
    if (e.stopPropagation***REMOVED*** {
        e.stopPropagation(***REMOVED***;
***REMOVED***
***REMOVED***

// quickElement(tagType, parentReference [, textInChildNode, attribute, attributeValue ...***REMOVED******REMOVED***;
function quickElement(***REMOVED*** {
    'use strict';
    var obj = document.createElement(arguments[0***REMOVED******REMOVED***;
    if (arguments[2***REMOVED******REMOVED*** {
        var textNode = document.createTextNode(arguments[2***REMOVED******REMOVED***;
        obj.appendChild(textNode***REMOVED***;
***REMOVED***
    var len = arguments.length;
    for (var i = 3; i < len; i += 2***REMOVED*** {
        obj.setAttribute(arguments[i***REMOVED***, arguments[i + 1***REMOVED******REMOVED***;
***REMOVED***
    arguments[1***REMOVED***.appendChild(obj***REMOVED***;
    return obj;
***REMOVED***

// "a" is reference to an object
function removeChildren(a***REMOVED*** {
    'use strict';
    while (a.hasChildNodes(***REMOVED******REMOVED*** {
        a.removeChild(a.lastChild***REMOVED***;
***REMOVED***
***REMOVED***

// ----------------------------------------------------------------------------
// Find-position functions by PPK
// See http://www.quirksmode.org/js/findpos.html
// ----------------------------------------------------------------------------
function findPosX(obj***REMOVED*** {
    'use strict';
    var curleft = 0;
    if (obj.offsetParent***REMOVED*** {
        while (obj.offsetParent***REMOVED*** {
            curleft += obj.offsetLeft - ((isOpera***REMOVED*** ? 0 : obj.scrollLeft***REMOVED***;
            obj = obj.offsetParent;
    ***REMOVED***
        // IE offsetParent does not include the top-level
        if (isIE && obj.parentElement***REMOVED*** {
            curleft += obj.offsetLeft - obj.scrollLeft;
    ***REMOVED***
***REMOVED*** else if (obj.x***REMOVED*** {
        curleft += obj.x;
***REMOVED***
    return curleft;
***REMOVED***

function findPosY(obj***REMOVED*** {
    'use strict';
    var curtop = 0;
    if (obj.offsetParent***REMOVED*** {
        while (obj.offsetParent***REMOVED*** {
            curtop += obj.offsetTop - ((isOpera***REMOVED*** ? 0 : obj.scrollTop***REMOVED***;
            obj = obj.offsetParent;
    ***REMOVED***
        // IE offsetParent does not include the top-level
        if (isIE && obj.parentElement***REMOVED*** {
            curtop += obj.offsetTop - obj.scrollTop;
    ***REMOVED***
***REMOVED*** else if (obj.y***REMOVED*** {
        curtop += obj.y;
***REMOVED***
    return curtop;
***REMOVED***

//-----------------------------------------------------------------------------
// Date object extensions
// ----------------------------------------------------------------------------
(function(***REMOVED*** {
    'use strict';
    Date.prototype.getTwelveHours = function(***REMOVED*** {
        var hours = this.getHours(***REMOVED***;
        if (hours === 0***REMOVED*** {
            return 12;
    ***REMOVED***
        else {
            return hours <= 12 ? hours : hours - 12;
    ***REMOVED***
***REMOVED***;

    Date.prototype.getTwoDigitMonth = function(***REMOVED*** {
        return (this.getMonth(***REMOVED*** < 9***REMOVED*** ? '0' + (this.getMonth(***REMOVED*** + 1***REMOVED*** : (this.getMonth(***REMOVED*** + 1***REMOVED***;
***REMOVED***;

    Date.prototype.getTwoDigitDate = function(***REMOVED*** {
        return (this.getDate(***REMOVED*** < 10***REMOVED*** ? '0' + this.getDate(***REMOVED*** : this.getDate(***REMOVED***;
***REMOVED***;

    Date.prototype.getTwoDigitTwelveHour = function(***REMOVED*** {
        return (this.getTwelveHours(***REMOVED*** < 10***REMOVED*** ? '0' + this.getTwelveHours(***REMOVED*** : this.getTwelveHours(***REMOVED***;
***REMOVED***;

    Date.prototype.getTwoDigitHour = function(***REMOVED*** {
        return (this.getHours(***REMOVED*** < 10***REMOVED*** ? '0' + this.getHours(***REMOVED*** : this.getHours(***REMOVED***;
***REMOVED***;

    Date.prototype.getTwoDigitMinute = function(***REMOVED*** {
        return (this.getMinutes(***REMOVED*** < 10***REMOVED*** ? '0' + this.getMinutes(***REMOVED*** : this.getMinutes(***REMOVED***;
***REMOVED***;

    Date.prototype.getTwoDigitSecond = function(***REMOVED*** {
        return (this.getSeconds(***REMOVED*** < 10***REMOVED*** ? '0' + this.getSeconds(***REMOVED*** : this.getSeconds(***REMOVED***;
***REMOVED***;

    Date.prototype.getHourMinute = function(***REMOVED*** {
        return this.getTwoDigitHour(***REMOVED*** + ':' + this.getTwoDigitMinute(***REMOVED***;
***REMOVED***;

    Date.prototype.getHourMinuteSecond = function(***REMOVED*** {
        return this.getTwoDigitHour(***REMOVED*** + ':' + this.getTwoDigitMinute(***REMOVED*** + ':' + this.getTwoDigitSecond(***REMOVED***;
***REMOVED***;

    Date.prototype.getFullMonthName = function(***REMOVED*** {
        return typeof window.CalendarNamespace === "undefined"
            ? this.getTwoDigitMonth(***REMOVED***
            : window.CalendarNamespace.monthsOfYear[this.getMonth(***REMOVED******REMOVED***;
***REMOVED***;

    Date.prototype.strftime = function(format***REMOVED*** {
        var fields = {
            B: this.getFullMonthName(***REMOVED***,
            c: this.toString(***REMOVED***,
            d: this.getTwoDigitDate(***REMOVED***,
            H: this.getTwoDigitHour(***REMOVED***,
            I: this.getTwoDigitTwelveHour(***REMOVED***,
            m: this.getTwoDigitMonth(***REMOVED***,
            M: this.getTwoDigitMinute(***REMOVED***,
            p: (this.getHours(***REMOVED*** >= 12***REMOVED*** ? 'PM' : 'AM',
            S: this.getTwoDigitSecond(***REMOVED***,
            w: '0' + this.getDay(***REMOVED***,
            x: this.toLocaleDateString(***REMOVED***,
            X: this.toLocaleTimeString(***REMOVED***,
            y: ('' + this.getFullYear(***REMOVED******REMOVED***.substr(2, 4***REMOVED***,
            Y: '' + this.getFullYear(***REMOVED***,
            '%': '%'
    ***REMOVED***;
        var result = '', i = 0;
        while (i < format.length***REMOVED*** {
            if (format.charAt(i***REMOVED*** === '%'***REMOVED*** {
                result = result + fields[format.charAt(i + 1***REMOVED******REMOVED***;
                ++i;
        ***REMOVED***
            else {
                result = result + format.charAt(i***REMOVED***;
        ***REMOVED***
            ++i;
    ***REMOVED***
        return result;
***REMOVED***;

// ----------------------------------------------------------------------------
// String object extensions
// ----------------------------------------------------------------------------
    String.prototype.pad_left = function(pad_length, pad_string***REMOVED*** {
        var new_string = this;
        for (var i = 0; new_string.length < pad_length; i++***REMOVED*** {
            new_string = pad_string + new_string;
    ***REMOVED***
        return new_string;
***REMOVED***;

    String.prototype.strptime = function(format***REMOVED*** {
        var split_format = format.split(/[.\-/***REMOVED***/***REMOVED***;
        var date = this.split(/[.\-/***REMOVED***/***REMOVED***;
        var i = 0;
        var day, month, year;
        while (i < split_format.length***REMOVED*** {
            switch (split_format[i***REMOVED******REMOVED*** {
                case "%d":
                    day = date[i***REMOVED***;
                    break;
                case "%m":
                    month = date[i***REMOVED*** - 1;
                    break;
                case "%Y":
                    year = date[i***REMOVED***;
                    break;
                case "%y":
                    year = date[i***REMOVED***;
                    break;
        ***REMOVED***
            ++i;
    ***REMOVED***
        // Create Date object from UTC since the parsed value is supposed to be
        // in UTC, not local time. Also, the calendar uses UTC functions for
        // date extraction.
        return new Date(Date.UTC(year, month, day***REMOVED******REMOVED***;
***REMOVED***;

***REMOVED******REMOVED***(***REMOVED***;
// ----------------------------------------------------------------------------
// Get the computed style for and element
// ----------------------------------------------------------------------------
function getStyle(oElm, strCssRule***REMOVED*** {
    'use strict';
    var strValue = "";
    if(document.defaultView && document.defaultView.getComputedStyle***REMOVED*** {
        strValue = document.defaultView.getComputedStyle(oElm, ""***REMOVED***.getPropertyValue(strCssRule***REMOVED***;
***REMOVED***
    else if(oElm.currentStyle***REMOVED*** {
        strCssRule = strCssRule.replace(/\-(\w***REMOVED***/g, function(strMatch, p1***REMOVED*** {
            return p1.toUpperCase(***REMOVED***;
    ***REMOVED******REMOVED***;
        strValue = oElm.currentStyle[strCssRule***REMOVED***;
***REMOVED***
    return strValue;
***REMOVED***
