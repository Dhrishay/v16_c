# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

"""
XCAFApp module, see official documentation at
https://dev.opencascade.org/doc/occt-7.8.0/refman/html/package_xcafapp.html
"""

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _XCAFApp
else:
    import _XCAFApp

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _XCAFApp.delete_SwigPyIterator

    def value(self):
        return _XCAFApp.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _XCAFApp.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _XCAFApp.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _XCAFApp.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _XCAFApp.SwigPyIterator_equal(self, x)

    def copy(self):
        return _XCAFApp.SwigPyIterator_copy(self)

    def next(self):
        return _XCAFApp.SwigPyIterator_next(self)

    def __next__(self):
        return _XCAFApp.SwigPyIterator___next__(self)

    def previous(self):
        return _XCAFApp.SwigPyIterator_previous(self)

    def advance(self, n):
        return _XCAFApp.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _XCAFApp.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _XCAFApp.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _XCAFApp.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _XCAFApp.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _XCAFApp.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _XCAFApp.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _XCAFApp:
_XCAFApp.SwigPyIterator_swigregister(SwigPyIterator)

def _dumps_object(klass):
    """ Overwrite default string output for any wrapped object.
    By default, __repr__ method returns something like:
    <OCC.Core.TopoDS.TopoDS_Shape; proxy of <Swig Object of type 'TopoDS_Shape *' at 0x02BB0758> >
    This is too much verbose.
    We prefer :
    <class 'gp_Pnt'>
    or
    <class 'TopoDS_Shape'>
    """
    klass_name = str(klass.__class__).split(".")[3].split("'")[0]
    repr_string = "<class '" + klass_name + "'"
# for TopoDS_Shape, we also look for the base type
    if klass_name == "TopoDS_Shape":
        if klass.IsNull():
            repr_string += ": Null>"
            return repr_string
        st = klass.ShapeType()
        types = {OCC.Core.TopAbs.TopAbs_VERTEX: "Vertex",
                 OCC.Core.TopAbs.TopAbs_SOLID: "Solid",
                 OCC.Core.TopAbs.TopAbs_EDGE: "Edge",
                 OCC.Core.TopAbs.TopAbs_FACE: "Face",
                 OCC.Core.TopAbs.TopAbs_SHELL: "Shell",
                 OCC.Core.TopAbs.TopAbs_WIRE: "Wire",
                 OCC.Core.TopAbs.TopAbs_COMPOUND: "Compound",
                 OCC.Core.TopAbs.TopAbs_COMPSOLID: "Compsolid"}
        repr_string += "; Type:%s" % types[st]        
    elif hasattr(klass, "IsNull"):
        if klass.IsNull():
            repr_string += "; Null"
    repr_string += ">"
    return repr_string


def process_exception(error, method_name, class_name):
    return _XCAFApp.process_exception(error, method_name, class_name)

import warnings
from odoo.addons.OCC.Wrapper.wrapper_utils import Proxy, deprecated

class ios_base(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    erase_event = _XCAFApp.ios_base_erase_event
    imbue_event = _XCAFApp.ios_base_imbue_event
    copyfmt_event = _XCAFApp.ios_base_copyfmt_event

    def register_callback(self, __fn, __index):
        return _XCAFApp.ios_base_register_callback(self, __fn, __index)

    def flags(self, *args):
        return _XCAFApp.ios_base_flags(self, *args)

    def setf(self, *args):
        return _XCAFApp.ios_base_setf(self, *args)

    def unsetf(self, __mask):
        return _XCAFApp.ios_base_unsetf(self, __mask)

    def precision(self, *args):
        return _XCAFApp.ios_base_precision(self, *args)

    def width(self, *args):
        return _XCAFApp.ios_base_width(self, *args)

    @staticmethod
    def sync_with_stdio(__sync=True):
        return _XCAFApp.ios_base_sync_with_stdio(__sync)

    def imbue(self, __loc):
        return _XCAFApp.ios_base_imbue(self, __loc)

    def getloc(self):
        return _XCAFApp.ios_base_getloc(self)

    @staticmethod
    def xalloc():
        return _XCAFApp.ios_base_xalloc()

    def iword(self, __ix):
        return _XCAFApp.ios_base_iword(self, __ix)

    def pword(self, __ix):
        return _XCAFApp.ios_base_pword(self, __ix)
    __swig_destroy__ = _XCAFApp.delete_ios_base

# Register ios_base in _XCAFApp:
_XCAFApp.ios_base_swigregister(ios_base)
cvar = _XCAFApp.cvar
ios_base.boolalpha = _XCAFApp.cvar.ios_base_boolalpha
ios_base.dec = _XCAFApp.cvar.ios_base_dec
ios_base.fixed = _XCAFApp.cvar.ios_base_fixed
ios_base.hex = _XCAFApp.cvar.ios_base_hex
ios_base.internal = _XCAFApp.cvar.ios_base_internal
ios_base.left = _XCAFApp.cvar.ios_base_left
ios_base.oct = _XCAFApp.cvar.ios_base_oct
ios_base.right = _XCAFApp.cvar.ios_base_right
ios_base.scientific = _XCAFApp.cvar.ios_base_scientific
ios_base.showbase = _XCAFApp.cvar.ios_base_showbase
ios_base.showpoint = _XCAFApp.cvar.ios_base_showpoint
ios_base.showpos = _XCAFApp.cvar.ios_base_showpos
ios_base.skipws = _XCAFApp.cvar.ios_base_skipws
ios_base.unitbuf = _XCAFApp.cvar.ios_base_unitbuf
ios_base.uppercase = _XCAFApp.cvar.ios_base_uppercase
ios_base.adjustfield = _XCAFApp.cvar.ios_base_adjustfield
ios_base.basefield = _XCAFApp.cvar.ios_base_basefield
ios_base.floatfield = _XCAFApp.cvar.ios_base_floatfield
ios_base.badbit = _XCAFApp.cvar.ios_base_badbit
ios_base.eofbit = _XCAFApp.cvar.ios_base_eofbit
ios_base.failbit = _XCAFApp.cvar.ios_base_failbit
ios_base.goodbit = _XCAFApp.cvar.ios_base_goodbit
ios_base.app = _XCAFApp.cvar.ios_base_app
ios_base.ate = _XCAFApp.cvar.ios_base_ate
ios_base.binary = _XCAFApp.cvar.ios_base_binary
ios_base.ios_base_in = _XCAFApp.cvar.ios_base_ios_base_in
ios_base.out = _XCAFApp.cvar.ios_base_out
ios_base.trunc = _XCAFApp.cvar.ios_base_trunc
ios_base.beg = _XCAFApp.cvar.ios_base_beg
ios_base.cur = _XCAFApp.cvar.ios_base_cur
ios_base.end = _XCAFApp.cvar.ios_base_end

class ios(ios_base):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def rdstate(self):
        return _XCAFApp.ios_rdstate(self)

    def clear(self, *args):
        return _XCAFApp.ios_clear(self, *args)

    def setstate(self, __state):
        return _XCAFApp.ios_setstate(self, __state)

    def good(self):
        return _XCAFApp.ios_good(self)

    def eof(self):
        return _XCAFApp.ios_eof(self)

    def fail(self):
        return _XCAFApp.ios_fail(self)

    def bad(self):
        return _XCAFApp.ios_bad(self)

    def exceptions(self, *args):
        return _XCAFApp.ios_exceptions(self, *args)

    def __init__(self, __sb):
        _XCAFApp.ios_swiginit(self, _XCAFApp.new_ios(__sb))
    __swig_destroy__ = _XCAFApp.delete_ios

    def tie(self, *args):
        return _XCAFApp.ios_tie(self, *args)

    def rdbuf(self, *args):
        return _XCAFApp.ios_rdbuf(self, *args)

    def copyfmt(self, __rhs):
        return _XCAFApp.ios_copyfmt(self, __rhs)

    def fill(self, *args):
        return _XCAFApp.ios_fill(self, *args)

    def imbue(self, __loc):
        return _XCAFApp.ios_imbue(self, __loc)

    def narrow(self, __c, __dfault):
        return _XCAFApp.ios_narrow(self, __c, __dfault)

    def widen(self, __c):
        return _XCAFApp.ios_widen(self, __c)

# Register ios in _XCAFApp:
_XCAFApp.ios_swigregister(ios)
class ostream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _XCAFApp.ostream_swiginit(self, _XCAFApp.new_ostream(__sb))
    __swig_destroy__ = _XCAFApp.delete_ostream

    def __lshift__(self, *args):
        return _XCAFApp.ostream___lshift__(self, *args)

    def put(self, __c):
        return _XCAFApp.ostream_put(self, __c)

    def write(self, __s, __n):
        return _XCAFApp.ostream_write(self, __s, __n)

    def flush(self):
        return _XCAFApp.ostream_flush(self)

    def tellp(self):
        return _XCAFApp.ostream_tellp(self)

    def seekp(self, *args):
        return _XCAFApp.ostream_seekp(self, *args)

# Register ostream in _XCAFApp:
_XCAFApp.ostream_swigregister(ostream)
class istream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _XCAFApp.istream_swiginit(self, _XCAFApp.new_istream(__sb))
    __swig_destroy__ = _XCAFApp.delete_istream

    def __rshift__(self, *args):
        return _XCAFApp.istream___rshift__(self, *args)

    def gcount(self):
        return _XCAFApp.istream_gcount(self)

    def get(self, *args):
        return _XCAFApp.istream_get(self, *args)

    def getline(self, *args):
        return _XCAFApp.istream_getline(self, *args)

    def ignore(self, *args):
        return _XCAFApp.istream_ignore(self, *args)

    def peek(self):
        return _XCAFApp.istream_peek(self)

    def read(self, __s, __n):
        return _XCAFApp.istream_read(self, __s, __n)

    def readsome(self, __s, __n):
        return _XCAFApp.istream_readsome(self, __s, __n)

    def putback(self, __c):
        return _XCAFApp.istream_putback(self, __c)

    def unget(self):
        return _XCAFApp.istream_unget(self)

    def sync(self):
        return _XCAFApp.istream_sync(self)

    def tellg(self):
        return _XCAFApp.istream_tellg(self)

    def seekg(self, *args):
        return _XCAFApp.istream_seekg(self, *args)

# Register istream in _XCAFApp:
_XCAFApp.istream_swigregister(istream)
class iostream(istream, ostream):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _XCAFApp.iostream_swiginit(self, _XCAFApp.new_iostream(__sb))
    __swig_destroy__ = _XCAFApp.delete_iostream

# Register iostream in _XCAFApp:
_XCAFApp.iostream_swigregister(iostream)
cin = cvar.cin
cout = cvar.cout
cerr = cvar.cerr
clog = cvar.clog

endl_cb_ptr = _XCAFApp.endl_cb_ptr
endl = _XCAFApp.endl
ends_cb_ptr = _XCAFApp.ends_cb_ptr
ends = _XCAFApp.ends
flush_cb_ptr = _XCAFApp.flush_cb_ptr
flush = _XCAFApp.flush
import odoo.addons.OCC.Core.Standard
import odoo.addons.OCC.Core.NCollection
import odoo.addons.OCC.Core.TDocStd
import odoo.addons.OCC.Core.TDF
import odoo.addons.OCC.Core.TCollection
import odoo.addons.OCC.Core.TColStd
import odoo.addons.OCC.Core.CDF
import odoo.addons.OCC.Core.CDM
import odoo.addons.OCC.Core.Message
import odoo.addons.OCC.Core.OSD
import odoo.addons.OCC.Core.Resource
import odoo.addons.OCC.Core.PCDM
import odoo.addons.OCC.Core.Storage

from enum import IntEnum
from odoo.addons.OCC.Core.Exception import *




def Handle_XCAFApp_Application_Create():
    return _XCAFApp.Handle_XCAFApp_Application_Create()

def Handle_XCAFApp_Application_DownCast(t):
    return _XCAFApp.Handle_XCAFApp_Application_DownCast(t)

def Handle_XCAFApp_Application_IsNull(t):
    return _XCAFApp.Handle_XCAFApp_Application_IsNull(t)
class XCAFApp_Application(odoo.addons.OCC.Core.TDocStd.TDocStd_Application):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def DumpJson(self, depth=-1):
        r"""

        Parameters
        ----------
        depth: int, default=-1

        Return
        -------
        str

        Description
        -----------
        Dump the object to JSON string.

        Parameters
        ----------
        depth: int, default=-1

        Return
        -------
        str

        Description
        -----------
        Dump the object to JSON string.

        """
        return _XCAFApp.XCAFApp_Application_DumpJson(self, depth)

    @staticmethod
    def GetApplication(*args):
        r"""
        Return
        -------
        opencascade::handle<XCAFApp_Application>

        Description
        -----------
        Initializes (for the first time) and returns the static object (xcafapp_application) this is the only valid method to get xcafapp_application object, and it should be called at least once before any actions with documents in order to init application.

        """
        return _XCAFApp.XCAFApp_Application_GetApplication(*args)


    @staticmethod
    def DownCast(t):
      return Handle_XCAFApp_Application_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _XCAFApp.delete_XCAFApp_Application

# Register XCAFApp_Application in _XCAFApp:
_XCAFApp.XCAFApp_Application_swigregister(XCAFApp_Application)



@deprecated
def XCAFApp_Application_GetApplication(*args):
	return XCAFApp_Application.GetApplication(*args)



