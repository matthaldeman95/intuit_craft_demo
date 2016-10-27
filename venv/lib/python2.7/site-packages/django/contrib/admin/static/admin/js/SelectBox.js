(function($***REMOVED*** {
    'use strict';
    var SelectBox = {
        cache: {***REMOVED***,
        init: function(id***REMOVED*** {
            var box = document.getElementById(id***REMOVED***;
            var node;
            SelectBox.cache[id***REMOVED*** = [***REMOVED***;
            var cache = SelectBox.cache[id***REMOVED***;
            var boxOptions = box.options;
            var boxOptionsLength = boxOptions.length;
            for (var i = 0, j = boxOptionsLength; i < j; i++***REMOVED*** {
                node = boxOptions[i***REMOVED***;
                cache.push({value: node.value, text: node.text, displayed: 1***REMOVED******REMOVED***;
        ***REMOVED***
***REMOVED***
        redisplay: function(id***REMOVED*** {
            // Repopulate HTML select box from cache
            var box = document.getElementById(id***REMOVED***;
            var node;
            $(box***REMOVED***.empty(***REMOVED***; // clear all options
            var new_options = box.outerHTML.slice(0, -9***REMOVED***;  // grab just the opening tag
            var cache = SelectBox.cache[id***REMOVED***;
            for (var i = 0, j = cache.length; i < j; i++***REMOVED*** {
                node = cache[i***REMOVED***;
                if (node.displayed***REMOVED*** {
                    var new_option = new Option(node.text, node.value, false, false***REMOVED***;
                    // Shows a tooltip when hovering over the option
                    new_option.setAttribute("title", node.text***REMOVED***;
                    new_options += new_option.outerHTML;
            ***REMOVED***
        ***REMOVED***
            new_options += '</select>';
            box.outerHTML = new_options;
***REMOVED***
        filter: function(id, text***REMOVED*** {
            // Redisplay the HTML select box, displaying only the choices containing ALL
            // the words in text. (It's an AND search.***REMOVED***
            var tokens = text.toLowerCase(***REMOVED***.split(/\s+/***REMOVED***;
            var node, token;
            var cache = SelectBox.cache[id***REMOVED***;
            for (var i = 0, j = cache.length; i < j; i++***REMOVED*** {
                node = cache[i***REMOVED***;
                node.displayed = 1;
                var node_text = node.text.toLowerCase(***REMOVED***;
                var numTokens = tokens.length;
                for (var k = 0; k < numTokens; k++***REMOVED*** {
                    token = tokens[k***REMOVED***;
                    if (node_text.indexOf(token***REMOVED*** === -1***REMOVED*** {
                        node.displayed = 0;
                        break;  // Once the first token isn't found we're done
                ***REMOVED***
            ***REMOVED***
        ***REMOVED***
            SelectBox.redisplay(id***REMOVED***;
***REMOVED***
        delete_from_cache: function(id, value***REMOVED*** {
            var node, delete_index = null;
            var cache = SelectBox.cache[id***REMOVED***;
            for (var i = 0, j = cache.length; i < j; i++***REMOVED*** {
                node = cache[i***REMOVED***;
                if (node.value === value***REMOVED*** {
                    delete_index = i;
                    break;
            ***REMOVED***
        ***REMOVED***
            cache.splice(delete_index, 1***REMOVED***;
***REMOVED***
        add_to_cache: function(id, option***REMOVED*** {
            SelectBox.cache[id***REMOVED***.push({value: option.value, text: option.text, displayed: 1***REMOVED******REMOVED***;
***REMOVED***
        cache_contains: function(id, value***REMOVED*** {
            // Check if an item is contained in the cache
            var node;
            var cache = SelectBox.cache[id***REMOVED***;
            for (var i = 0, j = cache.length; i < j; i++***REMOVED*** {
                node = cache[i***REMOVED***;
                if (node.value === value***REMOVED*** {
                    return true;
            ***REMOVED***
        ***REMOVED***
            return false;
***REMOVED***
        move: function(from, to***REMOVED*** {
            var from_box = document.getElementById(from***REMOVED***;
            var option;
            var boxOptions = from_box.options;
            var boxOptionsLength = boxOptions.length;
            for (var i = 0, j = boxOptionsLength; i < j; i++***REMOVED*** {
                option = boxOptions[i***REMOVED***;
                var option_value = option.value;
                if (option.selected && SelectBox.cache_contains(from, option_value***REMOVED******REMOVED*** {
                    SelectBox.add_to_cache(to, {value: option_value, text: option.text, displayed: 1***REMOVED******REMOVED***;
                    SelectBox.delete_from_cache(from, option_value***REMOVED***;
            ***REMOVED***
        ***REMOVED***
            SelectBox.redisplay(from***REMOVED***;
            SelectBox.redisplay(to***REMOVED***;
***REMOVED***
        move_all: function(from, to***REMOVED*** {
            var from_box = document.getElementById(from***REMOVED***;
            var option;
            var boxOptions = from_box.options;
            var boxOptionsLength = boxOptions.length;
            for (var i = 0, j = boxOptionsLength; i < j; i++***REMOVED*** {
                option = boxOptions[i***REMOVED***;
                var option_value = option.value;
                if (SelectBox.cache_contains(from, option_value***REMOVED******REMOVED*** {
                    SelectBox.add_to_cache(to, {value: option_value, text: option.text, displayed: 1***REMOVED******REMOVED***;
                    SelectBox.delete_from_cache(from, option_value***REMOVED***;
            ***REMOVED***
        ***REMOVED***
            SelectBox.redisplay(from***REMOVED***;
            SelectBox.redisplay(to***REMOVED***;
***REMOVED***
        sort: function(id***REMOVED*** {
            SelectBox.cache[id***REMOVED***.sort(function(a, b***REMOVED*** {
                a = a.text.toLowerCase(***REMOVED***;
                b = b.text.toLowerCase(***REMOVED***;
                try {
                    if (a > b***REMOVED*** {
                        return 1;
                ***REMOVED***
                    if (a < b***REMOVED*** {
                        return -1;
                ***REMOVED***
            ***REMOVED***
                catch (e***REMOVED*** {
                    // silently fail on IE 'unknown' exception
            ***REMOVED***
                return 0;
        ***REMOVED*** ***REMOVED***;
***REMOVED***
        select_all: function(id***REMOVED*** {
            var box = document.getElementById(id***REMOVED***;
            var boxOptions = box.options;
            var boxOptionsLength = boxOptions.length;
            for (var i = 0; i < boxOptionsLength; i++***REMOVED*** {
                boxOptions[i***REMOVED***.selected = 'selected';
        ***REMOVED***
    ***REMOVED***
***REMOVED***;
    window.SelectBox = SelectBox;
***REMOVED******REMOVED***(django.jQuery***REMOVED***;
