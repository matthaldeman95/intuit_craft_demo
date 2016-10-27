***REMOVED***
import sys
import warnings 
import imp
import opcode # opcode is not a virtualenv module, so we can use it to find the stdlib
              # Important! To work on pypy, this must be a module that resides in the
              # lib-python/modified-x.y.z directory

dirname = os.path.dirname

distutils_path = os.path.join(os.path.dirname(opcode.__file__***REMOVED***, 'distutils'***REMOVED***
if os.path.normpath(distutils_path***REMOVED*** == os.path.dirname(os.path.normpath(__file__***REMOVED******REMOVED***:
    warnings.warn(
        "The virtualenv distutils package at %s appears to be in the same location as the system distutils?"***REMOVED***
else:
    __path__.insert(0, distutils_path***REMOVED***
    real_distutils = imp.load_module("_virtualenv_distutils", None, distutils_path, ('', '', imp.PKG_DIRECTORY***REMOVED******REMOVED***
    # Copy the relevant attributes
    ***REMOVED***
        __revision__ = real_distutils.__revision__
    except AttributeError:
        pass
    __version__ = real_distutils.__version__

from distutils import dist, sysconfig

***REMOVED***
    basestring
except NameError:
    basestring = str

## patch build_ext (distutils doesn't know how to get the libs directory
## path on windows - it hardcodes the paths around the patched sys.prefix***REMOVED***

if sys.platform == 'win32':
    from distutils.command.build_ext import build_ext as old_build_ext
    class build_ext(old_build_ext***REMOVED***:
        def finalize_options (self***REMOVED***:
            if self.library_dirs is None:
                self.library_dirs = [***REMOVED***
            elif isinstance(self.library_dirs, basestring***REMOVED***:
                self.library_dirs = self.library_dirs.split(os.pathsep***REMOVED***
            
            self.library_dirs.insert(0, os.path.join(sys.real_prefix, "Libs"***REMOVED******REMOVED***
            old_build_ext.finalize_options(self***REMOVED***
            
    from distutils.command import build_ext as build_ext_module 
    build_ext_module.build_ext = build_ext

## distutils.dist patches:

old_find_config_files = dist.Distribution.find_config_files
def find_config_files(self***REMOVED***:
    found = old_find_config_files(self***REMOVED***
    system_distutils = os.path.join(distutils_path, 'distutils.cfg'***REMOVED***
    #if os.path.exists(system_distutils***REMOVED***:
    #    found.insert(0, system_distutils***REMOVED***
        # What to call the per-user config file
    if os.name == 'posix':
        user_filename = ".pydistutils.cfg"
    else:
        user_filename = "pydistutils.cfg"
    user_filename = os.path.join(sys.prefix, user_filename***REMOVED***
    if os.path.isfile(user_filename***REMOVED***:
        for item in list(found***REMOVED***:
            if item.endswith('pydistutils.cfg'***REMOVED***:
                found.remove(item***REMOVED***
        found.append(user_filename***REMOVED***
    return found
dist.Distribution.find_config_files = find_config_files

## distutils.sysconfig patches:

old_get_python_inc = sysconfig.get_python_inc
def sysconfig_get_python_inc(plat_specific=0, prefix=None***REMOVED***:
    if prefix is None:
        prefix = sys.real_prefix
    return old_get_python_inc(plat_specific, prefix***REMOVED***
sysconfig_get_python_inc.__doc__ = old_get_python_inc.__doc__
sysconfig.get_python_inc = sysconfig_get_python_inc

old_get_python_lib = sysconfig.get_python_lib
def sysconfig_get_python_lib(plat_specific=0, standard_lib=0, prefix=None***REMOVED***:
    if standard_lib and prefix is None:
        prefix = sys.real_prefix
    return old_get_python_lib(plat_specific, standard_lib, prefix***REMOVED***
sysconfig_get_python_lib.__doc__ = old_get_python_lib.__doc__
sysconfig.get_python_lib = sysconfig_get_python_lib

old_get_config_vars = sysconfig.get_config_vars
def sysconfig_get_config_vars(*args***REMOVED***:
    real_vars = old_get_config_vars(*args***REMOVED***
    if sys.platform == 'win32':
        lib_dir = os.path.join(sys.real_prefix, "libs"***REMOVED***
        if isinstance(real_vars, dict***REMOVED*** and 'LIBDIR' not in real_vars:
            real_vars['LIBDIR'***REMOVED*** = lib_dir # asked for all
        elif isinstance(real_vars, list***REMOVED*** and 'LIBDIR' in args:
            real_vars = real_vars + [lib_dir***REMOVED*** # asked for list
    return real_vars
sysconfig_get_config_vars.__doc__ = old_get_config_vars.__doc__
sysconfig.get_config_vars = sysconfig_get_config_vars
