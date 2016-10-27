/*global URLify*/
(function($***REMOVED*** {
    'use strict';
    $.fn.prepopulate = function(dependencies, maxLength, allowUnicode***REMOVED*** {
        /*
            Depends on urlify.js
            Populates a selected field with the values of the dependent fields,
            URLifies and shortens the string.
            dependencies - array of dependent fields ids
            maxLength - maximum length of the URLify'd string
            allowUnicode - Unicode support of the URLify'd string
        */
        return this.each(function(***REMOVED*** {
            var prepopulatedField = $(this***REMOVED***;

            var populate = function(***REMOVED*** {
                // Bail if the field's value has been changed by the user
                if (prepopulatedField.data('_changed'***REMOVED******REMOVED*** {
                    return;
            ***REMOVED***

                var values = [***REMOVED***;
                $.each(dependencies, function(i, field***REMOVED*** {
                    field = $(field***REMOVED***;
                    if (field.val(***REMOVED***.length > 0***REMOVED*** {
                        values.push(field.val(***REMOVED******REMOVED***;
                ***REMOVED***
            ***REMOVED******REMOVED***;
                prepopulatedField.val(URLify(values.join(' '***REMOVED***, maxLength, allowUnicode***REMOVED******REMOVED***;
        ***REMOVED***;

            prepopulatedField.data('_changed', false***REMOVED***;
            prepopulatedField.change(function(***REMOVED*** {
                prepopulatedField.data('_changed', true***REMOVED***;
        ***REMOVED******REMOVED***;

            if (!prepopulatedField.val(***REMOVED******REMOVED*** {
                $(dependencies.join(','***REMOVED******REMOVED***.keyup(populate***REMOVED***.change(populate***REMOVED***.focus(populate***REMOVED***;
        ***REMOVED***
    ***REMOVED******REMOVED***;
***REMOVED***;
***REMOVED******REMOVED***(django.jQuery***REMOVED***;
