/*global opener */
(function(***REMOVED*** {
    'use strict';
    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants'***REMOVED***.dataset.popupResponse***REMOVED***;
    switch(initData.action***REMOVED*** {
    case 'change':
        opener.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value***REMOVED***;
        break;
    case 'delete':
        opener.dismissDeleteRelatedObjectPopup(window, initData.value***REMOVED***;
        break;
    default:
        opener.dismissAddRelatedObjectPopup(window, initData.value, initData.obj***REMOVED***;
        break;
***REMOVED***
***REMOVED******REMOVED***(***REMOVED***;
