***REMOVED***Append module search paths for third-party packages to sys.path.

****************************************************************
* This module is automatically imported during initialization. *
****************************************************************

In earlier versions of Python (up to 1.5a3***REMOVED***, scripts or modules that
needed to use site-specific modules would place ``import site''
somewhere near the top of their code.  Because of the automatic
import, this is no longer necessary (but code that does it still
works***REMOVED***.

This will append site-specific paths to the module search path.  On
Unix, it starts with sys.prefix and sys.exec_prefix (if different***REMOVED*** and
appends lib/python<version>/site-packages as well as lib/site-python.
It also supports the Debian convention of
lib/python<version>/dist-packages.  On other platforms (mainly Mac and
Windows***REMOVED***, it uses just sys.prefix (and sys.exec_prefix, if different,
but this is unlikely***REMOVED***.  The resulting directories, if they exist, are
appended to sys.path, and also inspected for path configuration files.

FOR DEBIAN, this sys.path is augmented with directories in /usr/local.
Local addons go into /usr/local/lib/python<version>/site-packages
(resp. /usr/local/lib/site-python***REMOVED***, Debian addons install into
/usr/{lib,share***REMOVED***/python<version>/dist-packages.

A path configuration file is a file whose name has the form
<package>.pth; its contents are additional directories (one per line***REMOVED***
to be added to sys.path.  Non-existing directories (or
non-directories***REMOVED*** are never added to sys.path; no directory is added to
sys.path more than once.  Blank lines and lines beginning with
'#' are skipped. Lines starting with 'import' are executed.

For example, suppose sys.prefix and sys.exec_prefix are set to
/usr/local and there is a directory /usr/local/lib/python2.X/site-packages
with three subdirectories, foo, bar and spam, and two path
configuration files, foo.pth and bar.pth.  Assume foo.pth contains the
following:

  # foo package configuration
  foo
  bar
  bletch

and bar.pth contains:

  # bar package configuration
  bar

Then the following directories are added to sys.path, in this order:

  /usr/local/lib/python2.X/site-packages/bar
  /usr/local/lib/python2.X/site-packages/foo

Note that bletch is omitted because it doesn't exist; bar precedes foo
because bar.pth comes alphabetically before foo.pth; and spam is
omitted because it is not mentioned in either path configuration file.

After these path manipulations, an attempt is made to import a module
named sitecustomize, which can perform arbitrary additional
site-specific customizations.  If this import fails with an
ImportError exception, it is silently ignored.

***REMOVED***

import sys
***REMOVED***
***REMOVED***
    import __builtin__ as builtins
except ImportError:
    import builtins
***REMOVED***
    set
except NameError:
    from sets import Set as set

# Prefixes for site-packages; add additional prefixes like /usr/local here
PREFIXES = [sys.prefix, sys.exec_prefix***REMOVED***
# Enable per user site-packages directory
# set it to False to disable the feature or True to force the feature
ENABLE_USER_SITE = None
# for distutils.commands.install
USER_SITE = None
USER_BASE = None

_is_64bit = (getattr(sys, 'maxsize', None***REMOVED*** or getattr(sys, 'maxint'***REMOVED******REMOVED*** > 2**32
_is_pypy = hasattr(sys, 'pypy_version_info'***REMOVED***
_is_jython = sys.platform[:4***REMOVED*** == 'java'
if _is_jython:
    ModuleType = type(os***REMOVED***

def makepath(*paths***REMOVED***:
    dir = os.path.join(*paths***REMOVED***
    if _is_jython and (dir == '__classpath__' or
                       dir.startswith('__pyclasspath__'***REMOVED******REMOVED***:
        return dir, dir
    dir = os.path.abspath(dir***REMOVED***
    return dir, os.path.normcase(dir***REMOVED***

def abs__file__(***REMOVED***:
    ***REMOVED***Set all module' __file__ attribute to an absolute path***REMOVED***
    for m in sys.modules.values(***REMOVED***:
        if ((_is_jython and not isinstance(m, ModuleType***REMOVED******REMOVED*** or
            hasattr(m, '__loader__'***REMOVED******REMOVED***:
            # only modules need the abspath in Jython. and don't mess
            # with a PEP 302-supplied __file__
            continue
        f = getattr(m, '__file__', None***REMOVED***
        if f is None:
            continue
        m.__file__ = os.path.abspath(f***REMOVED***

def removeduppaths(***REMOVED***:
    ***REMOVED*** Remove duplicate entries from sys.path along with making them
    absolute***REMOVED***
    # This ensures that the initial path provided by the interpreter contains
    # only absolute pathnames, even if we're running from the build directory.
    L = [***REMOVED***
    known_paths = set(***REMOVED***
    for dir in sys.path:
        # Filter out duplicate paths (on case-insensitive file systems also
        # if they only differ in case***REMOVED***; turn relative paths into absolute
        # paths.
        dir, dircase = makepath(dir***REMOVED***
        if not dircase in known_paths:
            L.append(dir***REMOVED***
            known_paths.add(dircase***REMOVED***
    sys.path[:***REMOVED*** = L
    return known_paths

# XXX This should not be part of site.py, since it is needed even when
# using the -S option for Python.  See http://www.python.org/sf/586680
def addbuilddir(***REMOVED***:
    ***REMOVED***Append ./build/lib.<platform> in case we're running in the build dir
    (especially for Guido :-***REMOVED******REMOVED***
    from distutils.util import get_platform
    s = "build/lib.%s-%.3s" % (get_platform(***REMOVED***, sys.version***REMOVED***
    if hasattr(sys, 'gettotalrefcount'***REMOVED***:
        s += '-pydebug'
    s = os.path.join(os.path.dirname(sys.path[-1***REMOVED******REMOVED***, s***REMOVED***
    sys.path.append(s***REMOVED***

def _init_pathinfo(***REMOVED***:
    ***REMOVED***Return a set containing all existing directory entries from sys.path***REMOVED***
    d = set(***REMOVED***
    for dir in sys.path:
        ***REMOVED***
            if os.path.isdir(dir***REMOVED***:
                dir, dircase = makepath(dir***REMOVED***
                d.add(dircase***REMOVED***
        except TypeError:
            continue
    return d

def addpackage(sitedir, name, known_paths***REMOVED***:
    ***REMOVED***Add a new path to known_paths by combining sitedir and 'name' or execute
    sitedir if it starts with 'import'***REMOVED***
    if known_paths is None:
        _init_pathinfo(***REMOVED***
        reset = 1
    else:
        reset = 0
    fullname = os.path.join(sitedir, name***REMOVED***
    ***REMOVED***
        f = open(fullname, "rU"***REMOVED***
    except IOError:
        return
    ***REMOVED***
        for line in f:
            if line.startswith("#"***REMOVED***:
                continue
            if line.startswith("import"***REMOVED***:
                exec(line***REMOVED***
                continue
            line = line.rstrip(***REMOVED***
            dir, dircase = makepath(sitedir, line***REMOVED***
            if not dircase in known_paths and os.path.exists(dir***REMOVED***:
                sys.path.append(dir***REMOVED***
                known_paths.add(dircase***REMOVED***
    finally:
        f.close(***REMOVED***
    if reset:
        known_paths = None
    return known_paths

def addsitedir(sitedir, known_paths=None***REMOVED***:
    ***REMOVED***Add 'sitedir' argument to sys.path if missing and handle .pth files in
    'sitedir'***REMOVED***
    if known_paths is None:
        known_paths = _init_pathinfo(***REMOVED***
        reset = 1
    else:
        reset = 0
    sitedir, sitedircase = makepath(sitedir***REMOVED***
    if not sitedircase in known_paths:
        sys.path.append(sitedir***REMOVED***        # Add path component
    ***REMOVED***
        names = os.listdir(sitedir***REMOVED***
    except os.error:
        return
    names.sort(***REMOVED***
    for name in names:
        if name.endswith(os.extsep + "pth"***REMOVED***:
            addpackage(sitedir, name, known_paths***REMOVED***
    if reset:
        known_paths = None
    return known_paths

def addsitepackages(known_paths, sys_prefix=sys.prefix, exec_prefix=sys.exec_prefix***REMOVED***:
    ***REMOVED***Add site-packages (and possibly site-python***REMOVED*** to sys.path***REMOVED***
    prefixes = [os.path.join(sys_prefix, "local"***REMOVED***, sys_prefix***REMOVED***
    if exec_prefix != sys_prefix:
        prefixes.append(os.path.join(exec_prefix, "local"***REMOVED******REMOVED***

    for prefix in prefixes:
        if prefix:
            if sys.platform in ('os2emx', 'riscos'***REMOVED*** or _is_jython:
                sitedirs = [os.path.join(prefix, "Lib", "site-packages"***REMOVED******REMOVED***
            elif _is_pypy:
                sitedirs = [os.path.join(prefix, 'site-packages'***REMOVED******REMOVED***
            elif sys.platform == 'darwin' and prefix == sys_prefix:

                if prefix.startswith("/System/Library/Frameworks/"***REMOVED***: # Apple's Python

                    sitedirs = [os.path.join("/Library/Python", sys.version[:3***REMOVED***, "site-packages"***REMOVED***,
                                os.path.join(prefix, "Extras", "lib", "python"***REMOVED******REMOVED***

                else: # any other Python distros on OSX work this way
                    sitedirs = [os.path.join(prefix, "lib",
                                             "python" + sys.version[:3***REMOVED***, "site-packages"***REMOVED******REMOVED***

            elif os.sep == '/':
                sitedirs = [os.path.join(prefix,
                                         "lib",
                                         "python" + sys.version[:3***REMOVED***,
                                         "site-packages"***REMOVED***,
                            os.path.join(prefix, "lib", "site-python"***REMOVED***,
                            os.path.join(prefix, "python" + sys.version[:3***REMOVED***, "lib-dynload"***REMOVED******REMOVED***
                lib64_dir = os.path.join(prefix, "lib64", "python" + sys.version[:3***REMOVED***, "site-packages"***REMOVED***
                if (os.path.exists(lib64_dir***REMOVED*** and
                    os.path.realpath(lib64_dir***REMOVED*** not in [os.path.realpath(p***REMOVED*** for p in sitedirs***REMOVED******REMOVED***:
                    if _is_64bit:
                        sitedirs.insert(0, lib64_dir***REMOVED***
                    else:
                        sitedirs.append(lib64_dir***REMOVED***
                ***REMOVED***
                    # sys.getobjects only available in --with-pydebug build
                    sys.getobjects
                    sitedirs.insert(0, os.path.join(sitedirs[0***REMOVED***, 'debug'***REMOVED******REMOVED***
                except AttributeError:
                    pass
                # Debian-specific dist-packages directories:
                sitedirs.append(os.path.join(prefix, "local/lib",
                                             "python" + sys.version[:3***REMOVED***,
                                             "dist-packages"***REMOVED******REMOVED***
                if sys.version[0***REMOVED*** == '2':
                    sitedirs.append(os.path.join(prefix, "lib",
                                                 "python" + sys.version[:3***REMOVED***,
                                                 "dist-packages"***REMOVED******REMOVED***
                else:
                    sitedirs.append(os.path.join(prefix, "lib",
                                                 "python" + sys.version[0***REMOVED***,
                                                 "dist-packages"***REMOVED******REMOVED***
                sitedirs.append(os.path.join(prefix, "lib", "dist-python"***REMOVED******REMOVED***
            else:
                sitedirs = [prefix, os.path.join(prefix, "lib", "site-packages"***REMOVED******REMOVED***
            if sys.platform == 'darwin':
                # for framework builds *only* we add the standard Apple
                # locations. Currently only per-user, but /Library and
                # /Network/Library could be added too
                if 'Python.framework' in prefix:
                    home = os.environ.get('HOME'***REMOVED***
                    if home:
                        sitedirs.append(
                            os.path.join(home,
                                         'Library',
                                         'Python',
                                         sys.version[:3***REMOVED***,
                                         'site-packages'***REMOVED******REMOVED***
            for sitedir in sitedirs:
                if os.path.isdir(sitedir***REMOVED***:
                    addsitedir(sitedir, known_paths***REMOVED***
    return None

def check_enableusersite(***REMOVED***:
    ***REMOVED***Check if user site directory is safe for inclusion

    The function tests for the command line flag (including environment var***REMOVED***,
    process uid/gid equal to effective uid/gid.

    None: Disabled for security reasons
    False: Disabled by user (command line option***REMOVED***
    True: Safe and enabled
    ***REMOVED***
    if hasattr(sys, 'flags'***REMOVED*** and getattr(sys.flags, 'no_user_site', False***REMOVED***:
        return False

    if hasattr(os, "getuid"***REMOVED*** and hasattr(os, "geteuid"***REMOVED***:
        # check process uid == effective uid
        if os.geteuid(***REMOVED*** != os.getuid(***REMOVED***:
            return None
    if hasattr(os, "getgid"***REMOVED*** and hasattr(os, "getegid"***REMOVED***:
        # check process gid == effective gid
        if os.getegid(***REMOVED*** != os.getgid(***REMOVED***:
            return None

    return True

def addusersitepackages(known_paths***REMOVED***:
    ***REMOVED***Add a per user site-package to sys.path

    Each user has its own python directory with site-packages in the
    home directory.

    USER_BASE is the root directory for all Python versions

    USER_SITE is the user specific site-packages directory

    USER_SITE/.. can be used for data.
    ***REMOVED***
    global USER_BASE, USER_SITE, ENABLE_USER_SITE
    env_base = os.environ.get("PYTHONUSERBASE", None***REMOVED***

    def joinuser(*args***REMOVED***:
        return os.path.expanduser(os.path.join(*args***REMOVED******REMOVED***

    #if sys.platform in ('os2emx', 'riscos'***REMOVED***:
    #    # Don't know what to put here
    #    USER_BASE = ''
    #    USER_SITE = ''
    if os.name == "nt":
        base = os.environ.get("APPDATA"***REMOVED*** or "~"
        if env_base:
            USER_BASE = env_base
        else:
            USER_BASE = joinuser(base, "Python"***REMOVED***
        USER_SITE = os.path.join(USER_BASE,
                                 "Python" + sys.version[0***REMOVED*** + sys.version[2***REMOVED***,
                                 "site-packages"***REMOVED***
    else:
        if env_base:
            USER_BASE = env_base
        else:
            USER_BASE = joinuser("~", ".local"***REMOVED***
        USER_SITE = os.path.join(USER_BASE, "lib",
                                 "python" + sys.version[:3***REMOVED***,
                                 "site-packages"***REMOVED***

    if ENABLE_USER_SITE and os.path.isdir(USER_SITE***REMOVED***:
        addsitedir(USER_SITE, known_paths***REMOVED***
    if ENABLE_USER_SITE:
        for dist_libdir in ("lib", "local/lib"***REMOVED***:
            user_site = os.path.join(USER_BASE, dist_libdir,
                                     "python" + sys.version[:3***REMOVED***,
                                     "dist-packages"***REMOVED***
            if os.path.isdir(user_site***REMOVED***:
                addsitedir(user_site, known_paths***REMOVED***
    return known_paths



def setBEGINLIBPATH(***REMOVED***:
    ***REMOVED***The OS/2 EMX port has optional extension modules that do double duty
    as DLLs (and must use the .DLL file extension***REMOVED*** for other extensions.
    The library search path needs to be amended so these will be found
    during module import.  Use BEGINLIBPATH so that these are at the start
    of the library search path.

    ***REMOVED***
    dllpath = os.path.join(sys.prefix, "Lib", "lib-dynload"***REMOVED***
    libpath = os.environ['BEGINLIBPATH'***REMOVED***.split(';'***REMOVED***
    if libpath[-1***REMOVED***:
        libpath.append(dllpath***REMOVED***
    else:
        libpath[-1***REMOVED*** = dllpath
    os.environ['BEGINLIBPATH'***REMOVED*** = ';'.join(libpath***REMOVED***


def setquit(***REMOVED***:
    ***REMOVED***Define new built-ins 'quit' and 'exit'.
    These are simply strings that display a hint on how to exit.

    ***REMOVED***
    if os.sep == ':':
        eof = 'Cmd-Q'
    elif os.sep == '\\':
        eof = 'Ctrl-Z plus Return'
    else:
        eof = 'Ctrl-D (i.e. EOF***REMOVED***'

    class Quitter(object***REMOVED***:
        def __init__(self, name***REMOVED***:
            self.name = name
        def __repr__(self***REMOVED***:
            return 'Use %s(***REMOVED*** or %s to exit' % (self.name, eof***REMOVED***
        def __call__(self, code=None***REMOVED***:
            # Shells like IDLE catch the SystemExit, but listen when their
            # stdin wrapper is closed.
            ***REMOVED***
                sys.stdin.close(***REMOVED***
            ***REMOVED***
                pass
            raise SystemExit(code***REMOVED***
    builtins.quit = Quitter('quit'***REMOVED***
    builtins.exit = Quitter('exit'***REMOVED***


class _Printer(object***REMOVED***:
    ***REMOVED***interactive prompt objects for printing the license text, a list of
    contributors and the copyright notice.***REMOVED***

    MAXLINES = 23

    def __init__(self, name, data, files=(***REMOVED***, dirs=(***REMOVED******REMOVED***:
        self.__name = name
        self.__data = data
        self.__files = files
        self.__dirs = dirs
        self.__lines = None

    def __setup(self***REMOVED***:
        if self.__lines:
            return
        data = None
        for dir in self.__dirs:
            for filename in self.__files:
                filename = os.path.join(dir, filename***REMOVED***
                ***REMOVED***
                    fp = open(filename, "rU"***REMOVED***
                    data = fp.read(***REMOVED***
                    fp.close(***REMOVED***
                    break
                except IOError:
                    pass
            if data:
                break
        if not data:
            data = self.__data
        self.__lines = data.split('\n'***REMOVED***
        self.__linecnt = len(self.__lines***REMOVED***

    def __repr__(self***REMOVED***:
        self.__setup(***REMOVED***
        if len(self.__lines***REMOVED*** <= self.MAXLINES:
            return "\n".join(self.__lines***REMOVED***
        else:
            return "Type %s(***REMOVED*** to see the full %s text" % ((self.__name,***REMOVED****2***REMOVED***

    def __call__(self***REMOVED***:
        self.__setup(***REMOVED***
        prompt = 'Hit Return for more, or q (and Return***REMOVED*** to quit: '
        lineno = 0
        while 1:
            ***REMOVED***
                for i in range(lineno, lineno + self.MAXLINES***REMOVED***:
                    print(self.__lines[i***REMOVED******REMOVED***
            except IndexError:
                break
            else:
                lineno += self.MAXLINES
                key = None
                while key is None:
                    ***REMOVED***
                        key = raw_input(prompt***REMOVED***
                    except NameError:
                        key = input(prompt***REMOVED***
                    if key not in ('', 'q'***REMOVED***:
                        key = None
                if key == 'q':
                    break

def setcopyright(***REMOVED***:
    ***REMOVED***Set 'copyright' and 'credits' in __builtin__***REMOVED***
    builtins.copyright = _Printer("copyright", sys.copyright***REMOVED***
    if _is_jython:
        builtins.credits = _Printer(
            "credits",
            "Jython is maintained by the Jython developers (www.jython.org***REMOVED***."***REMOVED***
    elif _is_pypy:
        builtins.credits = _Printer(
            "credits",
            "PyPy is maintained by the PyPy developers: http://pypy.org/"***REMOVED***
    else:
        builtins.credits = _Printer("credits", ***REMOVED***\
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.***REMOVED******REMOVED***
    here = os.path.dirname(os.__file__***REMOVED***
    builtins.license = _Printer(
        "license", "See http://www.python.org/%.3s/license.html" % sys.version,
        ["LICENSE.txt", "LICENSE"***REMOVED***,
        [os.path.join(here, os.pardir***REMOVED***, here, os.curdir***REMOVED******REMOVED***


class _Helper(object***REMOVED***:
    ***REMOVED***Define the built-in 'help'.
    This is a wrapper around pydoc.help (with a twist***REMOVED***.

    ***REMOVED***

    def __repr__(self***REMOVED***:
        return "Type help(***REMOVED*** for interactive help, " \
               "or help(object***REMOVED*** for help about object."
    def __call__(self, *args, **kwds***REMOVED***:
        import pydoc
        return pydoc.help(*args, **kwds***REMOVED***

def sethelper(***REMOVED***:
    builtins.help = _Helper(***REMOVED***

def aliasmbcs(***REMOVED***:
    ***REMOVED***On Windows, some default encodings are not provided by Python,
    while they are always available as "mbcs" in each locale. Make
    them usable by aliasing to "mbcs" in such a case.***REMOVED***
    if sys.platform == 'win32':
        import locale, codecs
        enc = locale.getdefaultlocale(***REMOVED***[1***REMOVED***
        if enc.startswith('cp'***REMOVED***:            # "cp***" ?
            ***REMOVED***
                codecs.lookup(enc***REMOVED***
            except LookupError:
                import encodings
                encodings._cache[enc***REMOVED*** = encodings._unknown
                encodings.aliases.aliases[enc***REMOVED*** = 'mbcs'

def setencoding(***REMOVED***:
    ***REMOVED***Set the string encoding used by the Unicode implementation.  The
    default is 'ascii', but if you're willing to experiment, you can
    change this.***REMOVED***
    encoding = "ascii" # Default value set by _PyUnicode_Init(***REMOVED***
    if 0:
        # Enable to support locale aware default string encodings.
        import locale
        loc = locale.getdefaultlocale(***REMOVED***
        if loc[1***REMOVED***:
            encoding = loc[1***REMOVED***
    if 0:
        # Enable to switch off string to Unicode coercion and implicit
        # Unicode to string conversion.
        encoding = "undefined"
    if encoding != "ascii":
        # On Non-Unicode builds this will raise an AttributeError...
        sys.setdefaultencoding(encoding***REMOVED*** # Needs Python Unicode build !


def execsitecustomize(***REMOVED***:
    ***REMOVED***Run custom site specific code, if available.***REMOVED***
    ***REMOVED***
        import sitecustomize
    except ImportError:
        pass

def virtual_install_main_packages(***REMOVED***:
    f = open(os.path.join(os.path.dirname(__file__***REMOVED***, 'orig-prefix.txt'***REMOVED******REMOVED***
    sys.real_prefix = f.read(***REMOVED***.strip(***REMOVED***
    f.close(***REMOVED***
    pos = 2
    hardcoded_relative_dirs = [***REMOVED***
    if sys.path[0***REMOVED*** == '':
        pos += 1
    if _is_jython:
        paths = [os.path.join(sys.real_prefix, 'Lib'***REMOVED******REMOVED***
    elif _is_pypy:
        if sys.version_info > (3, 2***REMOVED***:
            cpyver = '%d' % sys.version_info[0***REMOVED***
        elif sys.pypy_version_info >= (1, 5***REMOVED***:
            cpyver = '%d.%d' % sys.version_info[:2***REMOVED***
        else:
            cpyver = '%d.%d.%d' % sys.version_info[:3***REMOVED***
        paths = [os.path.join(sys.real_prefix, 'lib_pypy'***REMOVED***,
                 os.path.join(sys.real_prefix, 'lib-python', cpyver***REMOVED******REMOVED***
        if sys.pypy_version_info < (1, 9***REMOVED***:
            paths.insert(1, os.path.join(sys.real_prefix,
                                         'lib-python', 'modified-%s' % cpyver***REMOVED******REMOVED***
        hardcoded_relative_dirs = paths[:***REMOVED*** # for the special 'darwin' case below
        #
        # This is hardcoded in the Python executable, but relative to sys.prefix:
        for path in paths[:***REMOVED***:
            plat_path = os.path.join(path, 'plat-%s' % sys.platform***REMOVED***
            if os.path.exists(plat_path***REMOVED***:
                paths.append(plat_path***REMOVED***
    elif sys.platform == 'win32':
        paths = [os.path.join(sys.real_prefix, 'Lib'***REMOVED***, os.path.join(sys.real_prefix, 'DLLs'***REMOVED******REMOVED***
    else:
        paths = [os.path.join(sys.real_prefix, 'lib', 'python'+sys.version[:3***REMOVED******REMOVED******REMOVED***
        hardcoded_relative_dirs = paths[:***REMOVED*** # for the special 'darwin' case below
        lib64_path = os.path.join(sys.real_prefix, 'lib64', 'python'+sys.version[:3***REMOVED******REMOVED***
        if os.path.exists(lib64_path***REMOVED***:
            if _is_64bit:
                paths.insert(0, lib64_path***REMOVED***
            else:
                paths.append(lib64_path***REMOVED***
        # This is hardcoded in the Python executable, but relative to
        # sys.prefix.  Debian change: we need to add the multiarch triplet
        # here, which is where the real stuff lives.  As per PEP 421, in
        # Python 3.3+, this lives in sys.implementation, while in Python 2.7
        # it lives in sys.
        ***REMOVED***
            arch = getattr(sys, 'implementation', sys***REMOVED***._multiarch
        except AttributeError:
            # This is a non-multiarch aware Python.  Fallback to the old way.
            arch = sys.platform
        plat_path = os.path.join(sys.real_prefix, 'lib',
                                 'python'+sys.version[:3***REMOVED***,
                                 'plat-%s' % arch***REMOVED***
        if os.path.exists(plat_path***REMOVED***:
            paths.append(plat_path***REMOVED***
    # This is hardcoded in the Python executable, but
    # relative to sys.prefix, so we have to fix up:
    for path in list(paths***REMOVED***:
        tk_dir = os.path.join(path, 'lib-tk'***REMOVED***
        if os.path.exists(tk_dir***REMOVED***:
            paths.append(tk_dir***REMOVED***

    # These are hardcoded in the Apple's Python executable,
    # but relative to sys.prefix, so we have to fix them up:
    if sys.platform == 'darwin':
        hardcoded_paths = [os.path.join(relative_dir, module***REMOVED***
                           for relative_dir in hardcoded_relative_dirs
                           for module in ('plat-darwin', 'plat-mac', 'plat-mac/lib-scriptpackages'***REMOVED******REMOVED***

        for path in hardcoded_paths:
            if os.path.exists(path***REMOVED***:
                paths.append(path***REMOVED***

    sys.path.extend(paths***REMOVED***

def force_global_eggs_after_local_site_packages(***REMOVED***:
    ***REMOVED***
    Force easy_installed eggs in the global environment to get placed
    in sys.path after all packages inside the virtualenv.  This
    maintains the "least surprise" result that packages in the
    virtualenv always mask global packages, never the other way
    around.

    ***REMOVED***
    egginsert = getattr(sys, '__egginsert', 0***REMOVED***
    for i, path in enumerate(sys.path***REMOVED***:
        if i > egginsert and path.startswith(sys.prefix***REMOVED***:
            egginsert = i
    sys.__egginsert = egginsert + 1

def virtual_addsitepackages(known_paths***REMOVED***:
    force_global_eggs_after_local_site_packages(***REMOVED***
    return addsitepackages(known_paths, sys_prefix=sys.real_prefix***REMOVED***

def fixclasspath(***REMOVED***:
    ***REMOVED***Adjust the special classpath sys.path entries for Jython. These
    entries should follow the base virtualenv lib directories.
    ***REMOVED***
    paths = [***REMOVED***
    classpaths = [***REMOVED***
    for path in sys.path:
        if path == '__classpath__' or path.startswith('__pyclasspath__'***REMOVED***:
            classpaths.append(path***REMOVED***
        else:
            paths.append(path***REMOVED***
    sys.path = paths
    sys.path.extend(classpaths***REMOVED***

def execusercustomize(***REMOVED***:
    ***REMOVED***Run custom user specific code, if available.***REMOVED***
    ***REMOVED***
        import usercustomize
    except ImportError:
        pass


def main(***REMOVED***:
    global ENABLE_USER_SITE
    virtual_install_main_packages(***REMOVED***
    abs__file__(***REMOVED***
    paths_in_sys = removeduppaths(***REMOVED***
    if (os.name == "posix" and sys.path and
        os.path.basename(sys.path[-1***REMOVED******REMOVED*** == "Modules"***REMOVED***:
        addbuilddir(***REMOVED***
    if _is_jython:
        fixclasspath(***REMOVED***
    GLOBAL_SITE_PACKAGES = not os.path.exists(os.path.join(os.path.dirname(__file__***REMOVED***, 'no-global-site-packages.txt'***REMOVED******REMOVED***
    if not GLOBAL_SITE_PACKAGES:
        ENABLE_USER_SITE = False
    if ENABLE_USER_SITE is None:
        ENABLE_USER_SITE = check_enableusersite(***REMOVED***
    paths_in_sys = addsitepackages(paths_in_sys***REMOVED***
    paths_in_sys = addusersitepackages(paths_in_sys***REMOVED***
    if GLOBAL_SITE_PACKAGES:
        paths_in_sys = virtual_addsitepackages(paths_in_sys***REMOVED***
    if sys.platform == 'os2emx':
        setBEGINLIBPATH(***REMOVED***
    setquit(***REMOVED***
    setcopyright(***REMOVED***
    sethelper(***REMOVED***
    aliasmbcs(***REMOVED***
    setencoding(***REMOVED***
    execsitecustomize(***REMOVED***
    if ENABLE_USER_SITE:
        execusercustomize(***REMOVED***
    # Remove sys.setdefaultencoding(***REMOVED*** so that users cannot change the
    # encoding after initialization.  The test for presence is needed when
    # this module is run as a script, because this code is executed twice.
    if hasattr(sys, "setdefaultencoding"***REMOVED***:
        del sys.setdefaultencoding

main(***REMOVED***

def _script(***REMOVED***:
    help = ***REMOVED***\
    %s [--user-base***REMOVED*** [--user-site***REMOVED***

    Without arguments print some useful information
    With arguments print the value of USER_BASE and/or USER_SITE separated
    by '%s'.

    Exit codes with --user-base or --user-site:
      0 - user site directory is enabled
      1 - user site directory is disabled by user
      2 - uses site directory is disabled by super user
          or for security reasons
     >2 - unknown error
    ***REMOVED***
    args = sys.argv[1:***REMOVED***
    if not args:
        print("sys.path = ["***REMOVED***
        for dir in sys.path:
            print("    %r," % (dir,***REMOVED******REMOVED***
        print("***REMOVED***"***REMOVED***
        def exists(path***REMOVED***:
            if os.path.isdir(path***REMOVED***:
                return "exists"
            else:
                return "doesn't exist"
        print("USER_BASE: %r (%s***REMOVED***" % (USER_BASE, exists(USER_BASE***REMOVED******REMOVED******REMOVED***
        print("USER_SITE: %r (%s***REMOVED***" % (USER_SITE, exists(USER_BASE***REMOVED******REMOVED******REMOVED***
        print("ENABLE_USER_SITE: %r" %  ENABLE_USER_SITE***REMOVED***
        sys.exit(0***REMOVED***

    buffer = [***REMOVED***
    if '--user-base' in args:
        buffer.append(USER_BASE***REMOVED***
    if '--user-site' in args:
        buffer.append(USER_SITE***REMOVED***

    if buffer:
        print(os.pathsep.join(buffer***REMOVED******REMOVED***
        if ENABLE_USER_SITE:
            sys.exit(0***REMOVED***
        elif ENABLE_USER_SITE is False:
            sys.exit(1***REMOVED***
        elif ENABLE_USER_SITE is None:
            sys.exit(2***REMOVED***
        else:
            sys.exit(3***REMOVED***
    else:
        import textwrap
        print(textwrap.dedent(help % (sys.argv[0***REMOVED***, os.pathsep***REMOVED******REMOVED******REMOVED***
        sys.exit(10***REMOVED***

if __name__ == '__main__':
    _script(***REMOVED***
