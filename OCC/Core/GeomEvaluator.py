# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

"""
GeomEvaluator module, see official documentation at
https://dev.opencascade.org/doc/occt-7.8.0/refman/html/package_geomevaluator.html
"""

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _GeomEvaluator
else:
    import _GeomEvaluator

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
    __swig_destroy__ = _GeomEvaluator.delete_SwigPyIterator

    def value(self):
        return _GeomEvaluator.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _GeomEvaluator.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _GeomEvaluator.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _GeomEvaluator.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _GeomEvaluator.SwigPyIterator_equal(self, x)

    def copy(self):
        return _GeomEvaluator.SwigPyIterator_copy(self)

    def next(self):
        return _GeomEvaluator.SwigPyIterator_next(self)

    def __next__(self):
        return _GeomEvaluator.SwigPyIterator___next__(self)

    def previous(self):
        return _GeomEvaluator.SwigPyIterator_previous(self)

    def advance(self, n):
        return _GeomEvaluator.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _GeomEvaluator.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _GeomEvaluator.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _GeomEvaluator.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _GeomEvaluator.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _GeomEvaluator.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _GeomEvaluator.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _GeomEvaluator:
_GeomEvaluator.SwigPyIterator_swigregister(SwigPyIterator)

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
    return _GeomEvaluator.process_exception(error, method_name, class_name)

import warnings
from odoo.addons.OCC.Wrapper.wrapper_utils import Proxy, deprecated

class ios_base(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    erase_event = _GeomEvaluator.ios_base_erase_event
    imbue_event = _GeomEvaluator.ios_base_imbue_event
    copyfmt_event = _GeomEvaluator.ios_base_copyfmt_event

    def register_callback(self, __fn, __index):
        return _GeomEvaluator.ios_base_register_callback(self, __fn, __index)

    def flags(self, *args):
        return _GeomEvaluator.ios_base_flags(self, *args)

    def setf(self, *args):
        return _GeomEvaluator.ios_base_setf(self, *args)

    def unsetf(self, __mask):
        return _GeomEvaluator.ios_base_unsetf(self, __mask)

    def precision(self, *args):
        return _GeomEvaluator.ios_base_precision(self, *args)

    def width(self, *args):
        return _GeomEvaluator.ios_base_width(self, *args)

    @staticmethod
    def sync_with_stdio(__sync=True):
        return _GeomEvaluator.ios_base_sync_with_stdio(__sync)

    def imbue(self, __loc):
        return _GeomEvaluator.ios_base_imbue(self, __loc)

    def getloc(self):
        return _GeomEvaluator.ios_base_getloc(self)

    @staticmethod
    def xalloc():
        return _GeomEvaluator.ios_base_xalloc()

    def iword(self, __ix):
        return _GeomEvaluator.ios_base_iword(self, __ix)

    def pword(self, __ix):
        return _GeomEvaluator.ios_base_pword(self, __ix)
    __swig_destroy__ = _GeomEvaluator.delete_ios_base

# Register ios_base in _GeomEvaluator:
_GeomEvaluator.ios_base_swigregister(ios_base)
cvar = _GeomEvaluator.cvar
ios_base.boolalpha = _GeomEvaluator.cvar.ios_base_boolalpha
ios_base.dec = _GeomEvaluator.cvar.ios_base_dec
ios_base.fixed = _GeomEvaluator.cvar.ios_base_fixed
ios_base.hex = _GeomEvaluator.cvar.ios_base_hex
ios_base.internal = _GeomEvaluator.cvar.ios_base_internal
ios_base.left = _GeomEvaluator.cvar.ios_base_left
ios_base.oct = _GeomEvaluator.cvar.ios_base_oct
ios_base.right = _GeomEvaluator.cvar.ios_base_right
ios_base.scientific = _GeomEvaluator.cvar.ios_base_scientific
ios_base.showbase = _GeomEvaluator.cvar.ios_base_showbase
ios_base.showpoint = _GeomEvaluator.cvar.ios_base_showpoint
ios_base.showpos = _GeomEvaluator.cvar.ios_base_showpos
ios_base.skipws = _GeomEvaluator.cvar.ios_base_skipws
ios_base.unitbuf = _GeomEvaluator.cvar.ios_base_unitbuf
ios_base.uppercase = _GeomEvaluator.cvar.ios_base_uppercase
ios_base.adjustfield = _GeomEvaluator.cvar.ios_base_adjustfield
ios_base.basefield = _GeomEvaluator.cvar.ios_base_basefield
ios_base.floatfield = _GeomEvaluator.cvar.ios_base_floatfield
ios_base.badbit = _GeomEvaluator.cvar.ios_base_badbit
ios_base.eofbit = _GeomEvaluator.cvar.ios_base_eofbit
ios_base.failbit = _GeomEvaluator.cvar.ios_base_failbit
ios_base.goodbit = _GeomEvaluator.cvar.ios_base_goodbit
ios_base.app = _GeomEvaluator.cvar.ios_base_app
ios_base.ate = _GeomEvaluator.cvar.ios_base_ate
ios_base.binary = _GeomEvaluator.cvar.ios_base_binary
ios_base.ios_base_in = _GeomEvaluator.cvar.ios_base_ios_base_in
ios_base.out = _GeomEvaluator.cvar.ios_base_out
ios_base.trunc = _GeomEvaluator.cvar.ios_base_trunc
ios_base.beg = _GeomEvaluator.cvar.ios_base_beg
ios_base.cur = _GeomEvaluator.cvar.ios_base_cur
ios_base.end = _GeomEvaluator.cvar.ios_base_end

class ios(ios_base):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def rdstate(self):
        return _GeomEvaluator.ios_rdstate(self)

    def clear(self, *args):
        return _GeomEvaluator.ios_clear(self, *args)

    def setstate(self, __state):
        return _GeomEvaluator.ios_setstate(self, __state)

    def good(self):
        return _GeomEvaluator.ios_good(self)

    def eof(self):
        return _GeomEvaluator.ios_eof(self)

    def fail(self):
        return _GeomEvaluator.ios_fail(self)

    def bad(self):
        return _GeomEvaluator.ios_bad(self)

    def exceptions(self, *args):
        return _GeomEvaluator.ios_exceptions(self, *args)

    def __init__(self, __sb):
        _GeomEvaluator.ios_swiginit(self, _GeomEvaluator.new_ios(__sb))
    __swig_destroy__ = _GeomEvaluator.delete_ios

    def tie(self, *args):
        return _GeomEvaluator.ios_tie(self, *args)

    def rdbuf(self, *args):
        return _GeomEvaluator.ios_rdbuf(self, *args)

    def copyfmt(self, __rhs):
        return _GeomEvaluator.ios_copyfmt(self, __rhs)

    def fill(self, *args):
        return _GeomEvaluator.ios_fill(self, *args)

    def imbue(self, __loc):
        return _GeomEvaluator.ios_imbue(self, __loc)

    def narrow(self, __c, __dfault):
        return _GeomEvaluator.ios_narrow(self, __c, __dfault)

    def widen(self, __c):
        return _GeomEvaluator.ios_widen(self, __c)

# Register ios in _GeomEvaluator:
_GeomEvaluator.ios_swigregister(ios)
class ostream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _GeomEvaluator.ostream_swiginit(self, _GeomEvaluator.new_ostream(__sb))
    __swig_destroy__ = _GeomEvaluator.delete_ostream

    def __lshift__(self, *args):
        return _GeomEvaluator.ostream___lshift__(self, *args)

    def put(self, __c):
        return _GeomEvaluator.ostream_put(self, __c)

    def write(self, __s, __n):
        return _GeomEvaluator.ostream_write(self, __s, __n)

    def flush(self):
        return _GeomEvaluator.ostream_flush(self)

    def tellp(self):
        return _GeomEvaluator.ostream_tellp(self)

    def seekp(self, *args):
        return _GeomEvaluator.ostream_seekp(self, *args)

# Register ostream in _GeomEvaluator:
_GeomEvaluator.ostream_swigregister(ostream)
class istream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _GeomEvaluator.istream_swiginit(self, _GeomEvaluator.new_istream(__sb))
    __swig_destroy__ = _GeomEvaluator.delete_istream

    def __rshift__(self, *args):
        return _GeomEvaluator.istream___rshift__(self, *args)

    def gcount(self):
        return _GeomEvaluator.istream_gcount(self)

    def get(self, *args):
        return _GeomEvaluator.istream_get(self, *args)

    def getline(self, *args):
        return _GeomEvaluator.istream_getline(self, *args)

    def ignore(self, *args):
        return _GeomEvaluator.istream_ignore(self, *args)

    def peek(self):
        return _GeomEvaluator.istream_peek(self)

    def read(self, __s, __n):
        return _GeomEvaluator.istream_read(self, __s, __n)

    def readsome(self, __s, __n):
        return _GeomEvaluator.istream_readsome(self, __s, __n)

    def putback(self, __c):
        return _GeomEvaluator.istream_putback(self, __c)

    def unget(self):
        return _GeomEvaluator.istream_unget(self)

    def sync(self):
        return _GeomEvaluator.istream_sync(self)

    def tellg(self):
        return _GeomEvaluator.istream_tellg(self)

    def seekg(self, *args):
        return _GeomEvaluator.istream_seekg(self, *args)

# Register istream in _GeomEvaluator:
_GeomEvaluator.istream_swigregister(istream)
class iostream(istream, ostream):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _GeomEvaluator.iostream_swiginit(self, _GeomEvaluator.new_iostream(__sb))
    __swig_destroy__ = _GeomEvaluator.delete_iostream

# Register iostream in _GeomEvaluator:
_GeomEvaluator.iostream_swigregister(iostream)
cin = cvar.cin
cout = cvar.cout
cerr = cvar.cerr
clog = cvar.clog

endl_cb_ptr = _GeomEvaluator.endl_cb_ptr
endl = _GeomEvaluator.endl
ends_cb_ptr = _GeomEvaluator.ends_cb_ptr
ends = _GeomEvaluator.ends
flush_cb_ptr = _GeomEvaluator.flush_cb_ptr
flush = _GeomEvaluator.flush
import odoo.addons.OCC.Core.Standard
import odoo.addons.OCC.Core.NCollection
import odoo.addons.OCC.Core.gp
import odoo.addons.OCC.Core.TColStd
import odoo.addons.OCC.Core.TCollection
import odoo.addons.OCC.Core.Geom
import odoo.addons.OCC.Core.GeomAbs
import odoo.addons.OCC.Core.TColgp
import odoo.addons.OCC.Core.GeomAdaptor
import odoo.addons.OCC.Core.Adaptor3d
import odoo.addons.OCC.Core.TopAbs
import odoo.addons.OCC.Core.Adaptor2d
import odoo.addons.OCC.Core.Geom2d
import odoo.addons.OCC.Core.math
import odoo.addons.OCC.Core.Message
import odoo.addons.OCC.Core.OSD

from enum import IntEnum
from odoo.addons.OCC.Core.Exception import *




def Handle_GeomEvaluator_Curve_Create():
    return _GeomEvaluator.Handle_GeomEvaluator_Curve_Create()

def Handle_GeomEvaluator_Curve_DownCast(t):
    return _GeomEvaluator.Handle_GeomEvaluator_Curve_DownCast(t)

def Handle_GeomEvaluator_Curve_IsNull(t):
    return _GeomEvaluator.Handle_GeomEvaluator_Curve_IsNull(t)

def Handle_GeomEvaluator_Surface_Create():
    return _GeomEvaluator.Handle_GeomEvaluator_Surface_Create()

def Handle_GeomEvaluator_Surface_DownCast(t):
    return _GeomEvaluator.Handle_GeomEvaluator_Surface_DownCast(t)

def Handle_GeomEvaluator_Surface_IsNull(t):
    return _GeomEvaluator.Handle_GeomEvaluator_Surface_IsNull(t)

def Handle_GeomEvaluator_OffsetCurve_Create():
    return _GeomEvaluator.Handle_GeomEvaluator_OffsetCurve_Create()

def Handle_GeomEvaluator_OffsetCurve_DownCast(t):
    return _GeomEvaluator.Handle_GeomEvaluator_OffsetCurve_DownCast(t)

def Handle_GeomEvaluator_OffsetCurve_IsNull(t):
    return _GeomEvaluator.Handle_GeomEvaluator_OffsetCurve_IsNull(t)

def Handle_GeomEvaluator_OffsetSurface_Create():
    return _GeomEvaluator.Handle_GeomEvaluator_OffsetSurface_Create()

def Handle_GeomEvaluator_OffsetSurface_DownCast(t):
    return _GeomEvaluator.Handle_GeomEvaluator_OffsetSurface_DownCast(t)

def Handle_GeomEvaluator_OffsetSurface_IsNull(t):
    return _GeomEvaluator.Handle_GeomEvaluator_OffsetSurface_IsNull(t)

def Handle_GeomEvaluator_SurfaceOfExtrusion_Create():
    return _GeomEvaluator.Handle_GeomEvaluator_SurfaceOfExtrusion_Create()

def Handle_GeomEvaluator_SurfaceOfExtrusion_DownCast(t):
    return _GeomEvaluator.Handle_GeomEvaluator_SurfaceOfExtrusion_DownCast(t)

def Handle_GeomEvaluator_SurfaceOfExtrusion_IsNull(t):
    return _GeomEvaluator.Handle_GeomEvaluator_SurfaceOfExtrusion_IsNull(t)

def Handle_GeomEvaluator_SurfaceOfRevolution_Create():
    return _GeomEvaluator.Handle_GeomEvaluator_SurfaceOfRevolution_Create()

def Handle_GeomEvaluator_SurfaceOfRevolution_DownCast(t):
    return _GeomEvaluator.Handle_GeomEvaluator_SurfaceOfRevolution_DownCast(t)

def Handle_GeomEvaluator_SurfaceOfRevolution_IsNull(t):
    return _GeomEvaluator.Handle_GeomEvaluator_SurfaceOfRevolution_IsNull(t)
class GeomEvaluator_Curve(odoo.addons.OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def D0(self, *args):
        r"""

        Parameters
        ----------
        theU: float
        theValue: gp_Pnt

        Return
        -------
        None

        Description
        -----------
        Value of 3d curve.

        """
        return _GeomEvaluator.GeomEvaluator_Curve_D0(self, *args)

    def D1(self, *args):
        r"""

        Parameters
        ----------
        theU: float
        theValue: gp_Pnt
        theD1: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Value and first derivatives of curve.

        """
        return _GeomEvaluator.GeomEvaluator_Curve_D1(self, *args)

    def D2(self, *args):
        r"""

        Parameters
        ----------
        theU: float
        theValue: gp_Pnt
        theD1: gp_Vec
        theD2: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Value, first and second derivatives of curve.

        """
        return _GeomEvaluator.GeomEvaluator_Curve_D2(self, *args)

    def D3(self, *args):
        r"""

        Parameters
        ----------
        theU: float
        theValue: gp_Pnt
        theD1: gp_Vec
        theD2: gp_Vec
        theD3: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Value, first, second and third derivatives of curve.

        """
        return _GeomEvaluator.GeomEvaluator_Curve_D3(self, *args)

    def DN(self, *args):
        r"""

        Parameters
        ----------
        theU: float
        theDerU: int

        Return
        -------
        gp_Vec

        Description
        -----------
        Calculates n-th derivatives of curve, where n = thederu. raises if n < 1.

        """
        return _GeomEvaluator.GeomEvaluator_Curve_DN(self, *args)

    def ShallowCopy(self, *args):
        r"""
        Return
        -------
        opencascade::handle<GeomEvaluator_Curve>

        Description
        -----------
        No available documentation.

        """
        return _GeomEvaluator.GeomEvaluator_Curve_ShallowCopy(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_GeomEvaluator_Curve_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomEvaluator.delete_GeomEvaluator_Curve

# Register GeomEvaluator_Curve in _GeomEvaluator:
_GeomEvaluator.GeomEvaluator_Curve_swigregister(GeomEvaluator_Curve)
class GeomEvaluator_Surface(odoo.addons.OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def D0(self, *args):
        r"""

        Parameters
        ----------
        theU: float
        theV: float
        theValue: gp_Pnt

        Return
        -------
        None

        Description
        -----------
        Value of surface.

        """
        return _GeomEvaluator.GeomEvaluator_Surface_D0(self, *args)

    def D1(self, *args):
        r"""

        Parameters
        ----------
        theU: float
        theV: float
        theValue: gp_Pnt
        theD1U: gp_Vec
        theD1V: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Value and first derivatives of surface.

        """
        return _GeomEvaluator.GeomEvaluator_Surface_D1(self, *args)

    def D2(self, *args):
        r"""

        Parameters
        ----------
        theU: float
        theV: float
        theValue: gp_Pnt
        theD1U: gp_Vec
        theD1V: gp_Vec
        theD2U: gp_Vec
        theD2V: gp_Vec
        theD2UV: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Value, first and second derivatives of surface.

        """
        return _GeomEvaluator.GeomEvaluator_Surface_D2(self, *args)

    def D3(self, *args):
        r"""

        Parameters
        ----------
        theU: float
        theV: float
        theValue: gp_Pnt
        theD1U: gp_Vec
        theD1V: gp_Vec
        theD2U: gp_Vec
        theD2V: gp_Vec
        theD2UV: gp_Vec
        theD3U: gp_Vec
        theD3V: gp_Vec
        theD3UUV: gp_Vec
        theD3UVV: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Value, first, second and third derivatives of surface.

        """
        return _GeomEvaluator.GeomEvaluator_Surface_D3(self, *args)

    def DN(self, *args):
        r"""

        Parameters
        ----------
        theU: float
        theV: float
        theDerU: int
        theDerV: int

        Return
        -------
        gp_Vec

        Description
        -----------
        Calculates n-th derivatives of surface, where n = thederu + thederv. //! raises if n < 1 or thederu < 0 or thederv < 0.

        """
        return _GeomEvaluator.GeomEvaluator_Surface_DN(self, *args)

    def ShallowCopy(self, *args):
        r"""
        Return
        -------
        opencascade::handle<GeomEvaluator_Surface>

        Description
        -----------
        No available documentation.

        """
        return _GeomEvaluator.GeomEvaluator_Surface_ShallowCopy(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_GeomEvaluator_Surface_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomEvaluator.delete_GeomEvaluator_Surface

# Register GeomEvaluator_Surface in _GeomEvaluator:
_GeomEvaluator.GeomEvaluator_Surface_swigregister(GeomEvaluator_Surface)
class GeomEvaluator_OffsetCurve(GeomEvaluator_Curve):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        theBase: Geom_Curve
        theOffset: float
        theDirection: gp_Dir

        Return
        -------
        None

        Description
        -----------
        Initialize evaluator by curve.

        Parameters
        ----------
        theBase: GeomAdaptor_Curve
        theOffset: float
        theDirection: gp_Dir

        Return
        -------
        None

        Description
        -----------
        Initialize evaluator by curve adaptor.

        """
        _GeomEvaluator.GeomEvaluator_OffsetCurve_swiginit(self, _GeomEvaluator.new_GeomEvaluator_OffsetCurve(*args))

    def SetOffsetDirection(self, *args):
        r"""

        Parameters
        ----------
        theDirection: gp_Dir

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        return _GeomEvaluator.GeomEvaluator_OffsetCurve_SetOffsetDirection(self, *args)

    def SetOffsetValue(self, *args):
        r"""

        Parameters
        ----------
        theOffset: float

        Return
        -------
        None

        Description
        -----------
        Change the offset value.

        """
        return _GeomEvaluator.GeomEvaluator_OffsetCurve_SetOffsetValue(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_GeomEvaluator_OffsetCurve_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomEvaluator.delete_GeomEvaluator_OffsetCurve

# Register GeomEvaluator_OffsetCurve in _GeomEvaluator:
_GeomEvaluator.GeomEvaluator_OffsetCurve_swigregister(GeomEvaluator_OffsetCurve)
class GeomEvaluator_OffsetSurface(GeomEvaluator_Surface):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        theBase: Geom_Surface
        theOffset: float
        theOscSurf: Geom_OsculatingSurface (optional, default to opencascade::handle<Geom_OsculatingSurface>())

        Return
        -------
        None

        Description
        -----------
        Initialize evaluator by surface.

        Parameters
        ----------
        theBase: GeomAdaptor_Surface
        theOffset: float
        theOscSurf: Geom_OsculatingSurface (optional, default to opencascade::handle<Geom_OsculatingSurface>())

        Return
        -------
        None

        Description
        -----------
        Initialize evaluator by surface adaptor.

        """
        _GeomEvaluator.GeomEvaluator_OffsetSurface_swiginit(self, _GeomEvaluator.new_GeomEvaluator_OffsetSurface(*args))

    def SetOffsetValue(self, *args):
        r"""

        Parameters
        ----------
        theOffset: float

        Return
        -------
        None

        Description
        -----------
        Change the offset value.

        """
        return _GeomEvaluator.GeomEvaluator_OffsetSurface_SetOffsetValue(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_GeomEvaluator_OffsetSurface_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomEvaluator.delete_GeomEvaluator_OffsetSurface

# Register GeomEvaluator_OffsetSurface in _GeomEvaluator:
_GeomEvaluator.GeomEvaluator_OffsetSurface_swigregister(GeomEvaluator_OffsetSurface)
class GeomEvaluator_SurfaceOfExtrusion(GeomEvaluator_Surface):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        theBase: Geom_Curve
        theExtrusionDir: gp_Dir

        Return
        -------
        None

        Description
        -----------
        Initialize evaluator by surface.

        Parameters
        ----------
        theBase: Adaptor3d_Curve
        theExtrusionDir: gp_Dir

        Return
        -------
        None

        Description
        -----------
        Initialize evaluator by surface adaptor.

        """
        _GeomEvaluator.GeomEvaluator_SurfaceOfExtrusion_swiginit(self, _GeomEvaluator.new_GeomEvaluator_SurfaceOfExtrusion(*args))

    def SetDirection(self, *args):
        r"""

        Parameters
        ----------
        theDirection: gp_Dir

        Return
        -------
        None

        Description
        -----------
        /changes the direction of extrusion.

        """
        return _GeomEvaluator.GeomEvaluator_SurfaceOfExtrusion_SetDirection(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_GeomEvaluator_SurfaceOfExtrusion_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomEvaluator.delete_GeomEvaluator_SurfaceOfExtrusion

# Register GeomEvaluator_SurfaceOfExtrusion in _GeomEvaluator:
_GeomEvaluator.GeomEvaluator_SurfaceOfExtrusion_swigregister(GeomEvaluator_SurfaceOfExtrusion)
class GeomEvaluator_SurfaceOfRevolution(GeomEvaluator_Surface):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        theBase: Geom_Curve
        theRevolDir: gp_Dir
        theRevolLoc: gp_Pnt

        Return
        -------
        None

        Description
        -----------
        Initialize evaluator by revolved curve, the axis of revolution and the location.

        Parameters
        ----------
        theBase: Adaptor3d_Curve
        theRevolDir: gp_Dir
        theRevolLoc: gp_Pnt

        Return
        -------
        None

        Description
        -----------
        Initialize evaluator by adaptor of the revolved curve, the axis of revolution and the location.

        """
        _GeomEvaluator.GeomEvaluator_SurfaceOfRevolution_swiginit(self, _GeomEvaluator.new_GeomEvaluator_SurfaceOfRevolution(*args))

    def SetAxis(self, *args):
        r"""

        Parameters
        ----------
        theAxis: gp_Ax1

        Return
        -------
        None

        Description
        -----------
        Change the axis of revolution.

        """
        return _GeomEvaluator.GeomEvaluator_SurfaceOfRevolution_SetAxis(self, *args)

    def SetDirection(self, *args):
        r"""

        Parameters
        ----------
        theDirection: gp_Dir

        Return
        -------
        None

        Description
        -----------
        Change direction of the axis of revolution.

        """
        return _GeomEvaluator.GeomEvaluator_SurfaceOfRevolution_SetDirection(self, *args)

    def SetLocation(self, *args):
        r"""

        Parameters
        ----------
        theLocation: gp_Pnt

        Return
        -------
        None

        Description
        -----------
        Change location of the axis of revolution.

        """
        return _GeomEvaluator.GeomEvaluator_SurfaceOfRevolution_SetLocation(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_GeomEvaluator_SurfaceOfRevolution_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomEvaluator.delete_GeomEvaluator_SurfaceOfRevolution

# Register GeomEvaluator_SurfaceOfRevolution in _GeomEvaluator:
_GeomEvaluator.GeomEvaluator_SurfaceOfRevolution_swigregister(GeomEvaluator_SurfaceOfRevolution)



