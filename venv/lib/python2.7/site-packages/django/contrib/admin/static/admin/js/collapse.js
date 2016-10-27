/*global gettext*/
(function($***REMOVED*** {
    'use strict';
    $(document***REMOVED***.ready(function(***REMOVED*** {
        // Add anchor tag for Show/Hide link
        $("fieldset.collapse"***REMOVED***.each(function(i, elem***REMOVED*** {
            // Don't hide if fields in this fieldset have errors
            if ($(elem***REMOVED***.find("div.errors"***REMOVED***.length === 0***REMOVED*** {
                $(elem***REMOVED***.addClass("collapsed"***REMOVED***.find("h2"***REMOVED***.first(***REMOVED***.append(' (<a id="fieldsetcollapser' +
                    i + '" class="collapse-toggle" href="#">' + gettext("Show"***REMOVED*** +
                    '</a>***REMOVED***'***REMOVED***;
        ***REMOVED***
    ***REMOVED******REMOVED***;
        // Add toggle to anchor tag
        $("fieldset.collapse a.collapse-toggle"***REMOVED***.click(function(ev***REMOVED*** {
            if ($(this***REMOVED***.closest("fieldset"***REMOVED***.hasClass("collapsed"***REMOVED******REMOVED*** {
                // Show
                $(this***REMOVED***.text(gettext("Hide"***REMOVED******REMOVED***.closest("fieldset"***REMOVED***.removeClass("collapsed"***REMOVED***.trigger("show.fieldset", [$(this***REMOVED***.attr("id"***REMOVED******REMOVED******REMOVED***;
        ***REMOVED*** else {
                // Hide
                $(this***REMOVED***.text(gettext("Show"***REMOVED******REMOVED***.closest("fieldset"***REMOVED***.addClass("collapsed"***REMOVED***.trigger("hide.fieldset", [$(this***REMOVED***.attr("id"***REMOVED******REMOVED******REMOVED***;
        ***REMOVED***
            return false;
    ***REMOVED******REMOVED***;
***REMOVED******REMOVED***;
***REMOVED******REMOVED***(django.jQuery***REMOVED***;
