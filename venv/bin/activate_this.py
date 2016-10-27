***REMOVED***By using execfile(this_file, dict(__file__=this_file***REMOVED******REMOVED*** you will
activate this virtualenv environment.

This can be used when you must use an existing Python interpreter, not
the virtualenv bin/python
***REMOVED***

***REMOVED***
    __file__
except NameError:
    raise AssertionError(
        "You must run this like execfile('path/to/activate_this.py', dict(__file__='path/to/activate_this.py'***REMOVED******REMOVED***"***REMOVED***
import sys
***REMOVED***

old_os_path = os.environ.get('PATH', ''***REMOVED***
os.environ['PATH'***REMOVED*** = os.path.dirname(os.path.abspath(__file__***REMOVED******REMOVED*** + os.pathsep + old_os_path
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__***REMOVED******REMOVED******REMOVED***
if sys.platform == 'win32':
    site_packages = os.path.join(base, 'Lib', 'site-packages'***REMOVED***
else:
    site_packages = os.path.join(base, 'lib', 'python%s' % sys.version[:3***REMOVED***, 'site-packages'***REMOVED***
prev_sys_path = list(sys.path***REMOVED***
import site
site.addsitedir(site_packages***REMOVED***
sys.real_prefix = sys.prefix
sys.prefix = base
# Move the added items to the front of the path:
new_sys_path = [***REMOVED***
for item in list(sys.path***REMOVED***:
    if item not in prev_sys_path:
        new_sys_path.append(item***REMOVED***
        sys.path.remove(item***REMOVED***
sys.path[:0***REMOVED*** = new_sys_path
