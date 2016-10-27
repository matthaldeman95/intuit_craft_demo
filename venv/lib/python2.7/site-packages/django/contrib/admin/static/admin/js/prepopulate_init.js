(function($***REMOVED*** {
    'use strict';
    var fields = $('#django-admin-prepopulated-fields-constants'***REMOVED***.data('prepopulatedFields'***REMOVED***;
    $.each(fields, function(index, field***REMOVED*** {
        $('.empty-form .form-row .field-' + field.name + ', .empty-form.form-row .field-' + field.name***REMOVED***.addClass('prepopulated_field'***REMOVED***;
        $(field.id***REMOVED***.data('dependency_list', field.dependency_list***REMOVED***.prepopulate(
            field.dependency_ids, field.maxLength, field.allowUnicode
        ***REMOVED***;
***REMOVED******REMOVED***;
***REMOVED******REMOVED***(django.jQuery***REMOVED***;
