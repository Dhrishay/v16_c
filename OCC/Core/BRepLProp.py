# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

"""
BRepLProp module, see official documentation at
https://dev.opencascade.org/doc/occt-7.8.0/refman/html/package_breplprop.html
"""

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _BRepLProp
else:
    import _BRepLProp

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
    __swig_destroy__ = _BRepLProp.delete_SwigPyIterator

    def value(self):
        return _BRepLProp.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _BRepLProp.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _BRepLProp.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _BRepLProp.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _BRepLProp.SwigPyIterator_equal(self, x)

    def copy(self):
        return _BRepLProp.SwigPyIterator_copy(self)

    def next(self):
        return _BRepLProp.SwigPyIterator_next(self)

    def __next__(self):
        return _BRepLProp.SwigPyIterator___next__(self)

    def previous(self):
        return _BRepLProp.SwigPyIterator_previous(self)

    def advance(self, n):
        return _BRepLProp.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _BRepLProp.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _BRepLProp.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _BRepLProp.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _BRepLProp.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _BRepLProp.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _BRepLProp.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _BRepLProp:
_BRepLProp.SwigPyIterator_swigregister(SwigPyIterator)

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
    return _BRepLProp.process_exception(error, method_name, class_name)

import warnings
from odoo.addons.OCC.Wrapper.wrapper_utils import Proxy, deprecated

class ios_base(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    erase_event = _BRepLProp.ios_base_erase_event
    imbue_event = _BRepLProp.ios_base_imbue_event
    copyfmt_event = _BRepLProp.ios_base_copyfmt_event

    def register_callback(self, __fn, __index):
        return _BRepLProp.ios_base_register_callback(self, __fn, __index)

    def flags(self, *args):
        return _BRepLProp.ios_base_flags(self, *args)

    def setf(self, *args):
        return _BRepLProp.ios_base_setf(self, *args)

    def unsetf(self, __mask):
        return _BRepLProp.ios_base_unsetf(self, __mask)

    def precision(self, *args):
        return _BRepLProp.ios_base_precision(self, *args)

    def width(self, *args):
        return _BRepLProp.ios_base_width(self, *args)

    @staticmethod
    def sync_with_stdio(__sync=True):
        return _BRepLProp.ios_base_sync_with_stdio(__sync)

    def imbue(self, __loc):
        return _BRepLProp.ios_base_imbue(self, __loc)

    def getloc(self):
        return _BRepLProp.ios_base_getloc(self)

    @staticmethod
    def xalloc():
        return _BRepLProp.ios_base_xalloc()

    def iword(self, __ix):
        return _BRepLProp.ios_base_iword(self, __ix)

    def pword(self, __ix):
        return _BRepLProp.ios_base_pword(self, __ix)
    __swig_destroy__ = _BRepLProp.delete_ios_base

# Register ios_base in _BRepLProp:
_BRepLProp.ios_base_swigregister(ios_base)
cvar = _BRepLProp.cvar
ios_base.boolalpha = _BRepLProp.cvar.ios_base_boolalpha
ios_base.dec = _BRepLProp.cvar.ios_base_dec
ios_base.fixed = _BRepLProp.cvar.ios_base_fixed
ios_base.hex = _BRepLProp.cvar.ios_base_hex
ios_base.internal = _BRepLProp.cvar.ios_base_internal
ios_base.left = _BRepLProp.cvar.ios_base_left
ios_base.oct = _BRepLProp.cvar.ios_base_oct
ios_base.right = _BRepLProp.cvar.ios_base_right
ios_base.scientific = _BRepLProp.cvar.ios_base_scientific
ios_base.showbase = _BRepLProp.cvar.ios_base_showbase
ios_base.showpoint = _BRepLProp.cvar.ios_base_showpoint
ios_base.showpos = _BRepLProp.cvar.ios_base_showpos
ios_base.skipws = _BRepLProp.cvar.ios_base_skipws
ios_base.unitbuf = _BRepLProp.cvar.ios_base_unitbuf
ios_base.uppercase = _BRepLProp.cvar.ios_base_uppercase
ios_base.adjustfield = _BRepLProp.cvar.ios_base_adjustfield
ios_base.basefield = _BRepLProp.cvar.ios_base_basefield
ios_base.floatfield = _BRepLProp.cvar.ios_base_floatfield
ios_base.badbit = _BRepLProp.cvar.ios_base_badbit
ios_base.eofbit = _BRepLProp.cvar.ios_base_eofbit
ios_base.failbit = _BRepLProp.cvar.ios_base_failbit
ios_base.goodbit = _BRepLProp.cvar.ios_base_goodbit
ios_base.app = _BRepLProp.cvar.ios_base_app
ios_base.ate = _BRepLProp.cvar.ios_base_ate
ios_base.binary = _BRepLProp.cvar.ios_base_binary
ios_base.ios_base_in = _BRepLProp.cvar.ios_base_ios_base_in
ios_base.out = _BRepLProp.cvar.ios_base_out
ios_base.trunc = _BRepLProp.cvar.ios_base_trunc
ios_base.beg = _BRepLProp.cvar.ios_base_beg
ios_base.cur = _BRepLProp.cvar.ios_base_cur
ios_base.end = _BRepLProp.cvar.ios_base_end

class ios(ios_base):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def rdstate(self):
        return _BRepLProp.ios_rdstate(self)

    def clear(self, *args):
        return _BRepLProp.ios_clear(self, *args)

    def setstate(self, __state):
        return _BRepLProp.ios_setstate(self, __state)

    def good(self):
        return _BRepLProp.ios_good(self)

    def eof(self):
        return _BRepLProp.ios_eof(self)

    def fail(self):
        return _BRepLProp.ios_fail(self)

    def bad(self):
        return _BRepLProp.ios_bad(self)

    def exceptions(self, *args):
        return _BRepLProp.ios_exceptions(self, *args)

    def __init__(self, __sb):
        _BRepLProp.ios_swiginit(self, _BRepLProp.new_ios(__sb))
    __swig_destroy__ = _BRepLProp.delete_ios

    def tie(self, *args):
        return _BRepLProp.ios_tie(self, *args)

    def rdbuf(self, *args):
        return _BRepLProp.ios_rdbuf(self, *args)

    def copyfmt(self, __rhs):
        return _BRepLProp.ios_copyfmt(self, __rhs)

    def fill(self, *args):
        return _BRepLProp.ios_fill(self, *args)

    def imbue(self, __loc):
        return _BRepLProp.ios_imbue(self, __loc)

    def narrow(self, __c, __dfault):
        return _BRepLProp.ios_narrow(self, __c, __dfault)

    def widen(self, __c):
        return _BRepLProp.ios_widen(self, __c)

# Register ios in _BRepLProp:
_BRepLProp.ios_swigregister(ios)
class ostream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _BRepLProp.ostream_swiginit(self, _BRepLProp.new_ostream(__sb))
    __swig_destroy__ = _BRepLProp.delete_ostream

    def __lshift__(self, *args):
        return _BRepLProp.ostream___lshift__(self, *args)

    def put(self, __c):
        return _BRepLProp.ostream_put(self, __c)

    def write(self, __s, __n):
        return _BRepLProp.ostream_write(self, __s, __n)

    def flush(self):
        return _BRepLProp.ostream_flush(self)

    def tellp(self):
        return _BRepLProp.ostream_tellp(self)

    def seekp(self, *args):
        return _BRepLProp.ostream_seekp(self, *args)

# Register ostream in _BRepLProp:
_BRepLProp.ostream_swigregister(ostream)
class istream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _BRepLProp.istream_swiginit(self, _BRepLProp.new_istream(__sb))
    __swig_destroy__ = _BRepLProp.delete_istream

    def __rshift__(self, *args):
        return _BRepLProp.istream___rshift__(self, *args)

    def gcount(self):
        return _BRepLProp.istream_gcount(self)

    def get(self, *args):
        return _BRepLProp.istream_get(self, *args)

    def getline(self, *args):
        return _BRepLProp.istream_getline(self, *args)

    def ignore(self, *args):
        return _BRepLProp.istream_ignore(self, *args)

    def peek(self):
        return _BRepLProp.istream_peek(self)

    def read(self, __s, __n):
        return _BRepLProp.istream_read(self, __s, __n)

    def readsome(self, __s, __n):
        return _BRepLProp.istream_readsome(self, __s, __n)

    def putback(self, __c):
        return _BRepLProp.istream_putback(self, __c)

    def unget(self):
        return _BRepLProp.istream_unget(self)

    def sync(self):
        return _BRepLProp.istream_sync(self)

    def tellg(self):
        return _BRepLProp.istream_tellg(self)

    def seekg(self, *args):
        return _BRepLProp.istream_seekg(self, *args)

# Register istream in _BRepLProp:
_BRepLProp.istream_swigregister(istream)
class iostream(istream, ostream):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _BRepLProp.iostream_swiginit(self, _BRepLProp.new_iostream(__sb))
    __swig_destroy__ = _BRepLProp.delete_iostream

# Register iostream in _BRepLProp:
_BRepLProp.iostream_swigregister(iostream)
cin = cvar.cin
cout = cvar.cout
cerr = cvar.cerr
clog = cvar.clog

endl_cb_ptr = _BRepLProp.endl_cb_ptr
endl = _BRepLProp.endl
ends_cb_ptr = _BRepLProp.ends_cb_ptr
ends = _BRepLProp.ends
flush_cb_ptr = _BRepLProp.flush_cb_ptr
flush = _BRepLProp.flush
import odoo.addons.OCC.Core.Standard
import odoo.addons.OCC.Core.NCollection
import odoo.addons.OCC.Core.BRepAdaptor
import odoo.addons.OCC.Core.Adaptor3d
import odoo.addons.OCC.Core.Geom
import odoo.addons.OCC.Core.gp
import odoo.addons.OCC.Core.TColStd
import odoo.addons.OCC.Core.TCollection
import odoo.addons.OCC.Core.GeomAbs
import odoo.addons.OCC.Core.TColgp
import odoo.addons.OCC.Core.TopAbs
import odoo.addons.OCC.Core.Adaptor2d
import odoo.addons.OCC.Core.Geom2d
import odoo.addons.OCC.Core.math
import odoo.addons.OCC.Core.Message
import odoo.addons.OCC.Core.OSD
import odoo.addons.OCC.Core.TopoDS
import odoo.addons.OCC.Core.TopLoc
import odoo.addons.OCC.Core.Geom2dAdaptor
import odoo.addons.OCC.Core.GeomAdaptor

from enum import IntEnum
from odoo.addons.OCC.Core.Exception import *



class breplprop(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def Continuity(*args):
        r"""

        Parameters
        ----------
        C1: BRepAdaptor_Curve
        C2: BRepAdaptor_Curve
        u1: float
        u2: float
        tl: float
        ta: float

        Return
        -------
        GeomAbs_Shape

        Description
        -----------
        Computes the regularity at the junction between c1 and c2. the point u1 on c1 and the point u2 on c2 must be confused. tl and ta are the linear and angular tolerance used two compare the derivative.

        Parameters
        ----------
        C1: BRepAdaptor_Curve
        C2: BRepAdaptor_Curve
        u1: float
        u2: float

        Return
        -------
        GeomAbs_Shape

        Description
        -----------
        The same as preceding but using the standard tolerances from package precision.

        """
        return _BRepLProp.breplprop_Continuity(*args)

    __repr__ = _dumps_object


    def __init__(self):
        _BRepLProp.breplprop_swiginit(self, _BRepLProp.new_breplprop())
    __swig_destroy__ = _BRepLProp.delete_breplprop

# Register breplprop in _BRepLProp:
_BRepLProp.breplprop_swigregister(breplprop)
class BRepLProp_CLProps(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        C: BRepAdaptor_Curve
        N: int
        Resolution: float

        Return
        -------
        None

        Description
        -----------
        Initializes the local properties of the curve <c> the current point and the derivatives are computed at the same time, which allows an optimization of the computation time. <n> indicates the maximum number of derivations to be done (0, 1, 2 or 3). for example, to compute only the tangent, n should be equal to 1. <resolution> is the linear tolerance (it is used to test if a vector is null).

        Parameters
        ----------
        C: BRepAdaptor_Curve
        U: float
        N: int
        Resolution: float

        Return
        -------
        None

        Description
        -----------
        Same as previous constructor but here the parameter is set to the value <u>. all the computations done will be related to <c> and <u>.

        Parameters
        ----------
        N: int
        Resolution: float

        Return
        -------
        None

        Description
        -----------
        Same as previous constructor but here the parameter is set to the value <u> and the curve is set with setcurve. the curve can have a empty constructor all the computations done will be related to <c> and <u> when the functions 'set' will be done.

        """
        _BRepLProp.BRepLProp_CLProps_swiginit(self, _BRepLProp.new_BRepLProp_CLProps(*args))

    def CentreOfCurvature(self, *args):
        r"""

        Parameters
        ----------
        P: gp_Pnt

        Return
        -------
        None

        Description
        -----------
        Returns the centre of curvature <p>.

        """
        return _BRepLProp.BRepLProp_CLProps_CentreOfCurvature(self, *args)

    def Curvature(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        Returns the curvature.

        """
        return _BRepLProp.BRepLProp_CLProps_Curvature(self, *args)

    def D1(self, *args):
        r"""
        Return
        -------
        gp_Vec

        Description
        -----------
        Returns the first derivative. the derivative is computed if it has not been yet.

        """
        return _BRepLProp.BRepLProp_CLProps_D1(self, *args)

    def D2(self, *args):
        r"""
        Return
        -------
        gp_Vec

        Description
        -----------
        Returns the second derivative. the derivative is computed if it has not been yet.

        """
        return _BRepLProp.BRepLProp_CLProps_D2(self, *args)

    def D3(self, *args):
        r"""
        Return
        -------
        gp_Vec

        Description
        -----------
        Returns the third derivative. the derivative is computed if it has not been yet.

        """
        return _BRepLProp.BRepLProp_CLProps_D3(self, *args)

    def IsTangentDefined(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        Returns true if the tangent is defined. for example, the tangent is not defined if the three first derivatives are all null.

        """
        return _BRepLProp.BRepLProp_CLProps_IsTangentDefined(self, *args)

    def Normal(self, *args):
        r"""

        Parameters
        ----------
        N: gp_Dir

        Return
        -------
        None

        Description
        -----------
        Returns the normal direction <n>.

        """
        return _BRepLProp.BRepLProp_CLProps_Normal(self, *args)

    def SetCurve(self, *args):
        r"""

        Parameters
        ----------
        C: BRepAdaptor_Curve

        Return
        -------
        None

        Description
        -----------
        Initializes the local properties of the curve for the new curve.

        """
        return _BRepLProp.BRepLProp_CLProps_SetCurve(self, *args)

    def SetParameter(self, *args):
        r"""

        Parameters
        ----------
        U: float

        Return
        -------
        None

        Description
        -----------
        Initializes the local properties of the curve for the parameter value <u>.

        """
        return _BRepLProp.BRepLProp_CLProps_SetParameter(self, *args)

    def Tangent(self, *args):
        r"""

        Parameters
        ----------
        D: gp_Dir

        Return
        -------
        None

        Description
        -----------
        Output the tangent direction <d>.

        """
        return _BRepLProp.BRepLProp_CLProps_Tangent(self, *args)

    def Value(self, *args):
        r"""
        Return
        -------
        gp_Pnt

        Description
        -----------
        Returns the point.

        """
        return _BRepLProp.BRepLProp_CLProps_Value(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepLProp.delete_BRepLProp_CLProps

# Register BRepLProp_CLProps in _BRepLProp:
_BRepLProp.BRepLProp_CLProps_swigregister(BRepLProp_CLProps)
class BRepLProp_CurveTool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def Continuity(*args):
        r"""

        Parameters
        ----------
        C: BRepAdaptor_Curve

        Return
        -------
        int

        Description
        -----------
        Returns the order of continuity of the curve <c>. returns 1: first derivative only is computable returns 2: first and second derivative only are computable. returns 3: first, second and third are computable.

        """
        return _BRepLProp.BRepLProp_CurveTool_Continuity(*args)

    @staticmethod
    def D1(*args):
        r"""

        Parameters
        ----------
        C: BRepAdaptor_Curve
        U: float
        P: gp_Pnt
        V1: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Computes the point <p> and first derivative <v1> of parameter <u> on the curve <c>.

        """
        return _BRepLProp.BRepLProp_CurveTool_D1(*args)

    @staticmethod
    def D2(*args):
        r"""

        Parameters
        ----------
        C: BRepAdaptor_Curve
        U: float
        P: gp_Pnt
        V1: gp_Vec
        V2: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Computes the point <p>, the first derivative <v1> and second derivative <v2> of parameter <u> on the curve <c>.

        """
        return _BRepLProp.BRepLProp_CurveTool_D2(*args)

    @staticmethod
    def D3(*args):
        r"""

        Parameters
        ----------
        C: BRepAdaptor_Curve
        U: float
        P: gp_Pnt
        V1: gp_Vec
        V2: gp_Vec
        V3: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Computes the point <p>, the first derivative <v1>, the second derivative <v2> and third derivative <v3> of parameter <u> on the curve <c>.

        """
        return _BRepLProp.BRepLProp_CurveTool_D3(*args)

    @staticmethod
    def FirstParameter(*args):
        r"""

        Parameters
        ----------
        C: BRepAdaptor_Curve

        Return
        -------
        float

        Description
        -----------
        Returns the first parameter bound of the curve.

        """
        return _BRepLProp.BRepLProp_CurveTool_FirstParameter(*args)

    @staticmethod
    def LastParameter(*args):
        r"""

        Parameters
        ----------
        C: BRepAdaptor_Curve

        Return
        -------
        float

        Description
        -----------
        Returns the last parameter bound of the curve. firstparameter must be less than lastparamenter.

        """
        return _BRepLProp.BRepLProp_CurveTool_LastParameter(*args)

    @staticmethod
    def Value(*args):
        r"""

        Parameters
        ----------
        C: BRepAdaptor_Curve
        U: float
        P: gp_Pnt

        Return
        -------
        None

        Description
        -----------
        Computes the point <p> of parameter <u> on the curve <c>.

        """
        return _BRepLProp.BRepLProp_CurveTool_Value(*args)

    __repr__ = _dumps_object


    def __init__(self):
        _BRepLProp.BRepLProp_CurveTool_swiginit(self, _BRepLProp.new_BRepLProp_CurveTool())
    __swig_destroy__ = _BRepLProp.delete_BRepLProp_CurveTool

# Register BRepLProp_CurveTool in _BRepLProp:
_BRepLProp.BRepLProp_CurveTool_swigregister(BRepLProp_CurveTool)
class BRepLProp_SLProps(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        S: BRepAdaptor_Surface
        U: float
        V: float
        N: int
        Resolution: float

        Return
        -------
        None

        Description
        -----------
        Initializes the local properties of the surface <s> for the parameter values (<u>, <v>). the current point and the derivatives are computed at the same time, which allows an optimization of the computation time. <n> indicates the maximum number of derivations to be done (0, 1, or 2). for example, to compute only the tangent, n should be equal to 1. <resolution> is the linear tolerance (it is used to test if a vector is null).

        Parameters
        ----------
        S: BRepAdaptor_Surface
        N: int
        Resolution: float

        Return
        -------
        None

        Description
        -----------
        Idem as previous constructor but without setting the value of parameters <u> and <v>.

        Parameters
        ----------
        N: int
        Resolution: float

        Return
        -------
        None

        Description
        -----------
        Idem as previous constructor but without setting the value of parameters <u> and <v> and the surface. the surface can have an empty constructor.

        """
        _BRepLProp.BRepLProp_SLProps_swiginit(self, _BRepLProp.new_BRepLProp_SLProps(*args))

    def CurvatureDirections(self, *args):
        r"""

        Parameters
        ----------
        MaxD: gp_Dir
        MinD: gp_Dir

        Return
        -------
        None

        Description
        -----------
        Returns the direction of the maximum and minimum curvature <maxd> and <mind>.

        """
        return _BRepLProp.BRepLProp_SLProps_CurvatureDirections(self, *args)

    def D1U(self, *args):
        r"""
        Return
        -------
        gp_Vec

        Description
        -----------
        Returns the first u derivative. the derivative is computed if it has not been yet.

        """
        return _BRepLProp.BRepLProp_SLProps_D1U(self, *args)

    def D1V(self, *args):
        r"""
        Return
        -------
        gp_Vec

        Description
        -----------
        Returns the first v derivative. the derivative is computed if it has not been yet.

        """
        return _BRepLProp.BRepLProp_SLProps_D1V(self, *args)

    def D2U(self, *args):
        r"""
        Return
        -------
        gp_Vec

        Description
        -----------
        Returns the second u derivatives the derivative is computed if it has not been yet.

        """
        return _BRepLProp.BRepLProp_SLProps_D2U(self, *args)

    def D2V(self, *args):
        r"""
        Return
        -------
        gp_Vec

        Description
        -----------
        Returns the second v derivative. the derivative is computed if it has not been yet.

        """
        return _BRepLProp.BRepLProp_SLProps_D2V(self, *args)

    def DUV(self, *args):
        r"""
        Return
        -------
        gp_Vec

        Description
        -----------
        Returns the second uv cross-derivative. the derivative is computed if it has not been yet.

        """
        return _BRepLProp.BRepLProp_SLProps_DUV(self, *args)

    def GaussianCurvature(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        Returns the gaussian curvature.

        """
        return _BRepLProp.BRepLProp_SLProps_GaussianCurvature(self, *args)

    def IsCurvatureDefined(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        Returns true if the curvature is defined.

        """
        return _BRepLProp.BRepLProp_SLProps_IsCurvatureDefined(self, *args)

    def IsNormalDefined(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        Tells if the normal is defined.

        """
        return _BRepLProp.BRepLProp_SLProps_IsNormalDefined(self, *args)

    def IsTangentUDefined(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        Returns true if the u tangent is defined. for example, the tangent is not defined if the two first u derivatives are null.

        """
        return _BRepLProp.BRepLProp_SLProps_IsTangentUDefined(self, *args)

    def IsTangentVDefined(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        Returns if the v tangent is defined. for example, the tangent is not defined if the two first v derivatives are null.

        """
        return _BRepLProp.BRepLProp_SLProps_IsTangentVDefined(self, *args)

    def IsUmbilic(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        Returns true if the point is umbilic (i.e. if the curvature is constant).

        """
        return _BRepLProp.BRepLProp_SLProps_IsUmbilic(self, *args)

    def MaxCurvature(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        Returns the maximum curvature.

        """
        return _BRepLProp.BRepLProp_SLProps_MaxCurvature(self, *args)

    def MeanCurvature(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        Returns the mean curvature.

        """
        return _BRepLProp.BRepLProp_SLProps_MeanCurvature(self, *args)

    def MinCurvature(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        Returns the minimum curvature.

        """
        return _BRepLProp.BRepLProp_SLProps_MinCurvature(self, *args)

    def Normal(self, *args):
        r"""
        Return
        -------
        gp_Dir

        Description
        -----------
        Returns the normal direction.

        """
        return _BRepLProp.BRepLProp_SLProps_Normal(self, *args)

    def SetParameters(self, *args):
        r"""

        Parameters
        ----------
        U: float
        V: float

        Return
        -------
        None

        Description
        -----------
        Initializes the local properties of the surface s for the new parameter values (<u>, <v>).

        """
        return _BRepLProp.BRepLProp_SLProps_SetParameters(self, *args)

    def SetSurface(self, *args):
        r"""

        Parameters
        ----------
        S: BRepAdaptor_Surface

        Return
        -------
        None

        Description
        -----------
        Initializes the local properties of the surface s for the new surface.

        """
        return _BRepLProp.BRepLProp_SLProps_SetSurface(self, *args)

    def TangentU(self, *args):
        r"""

        Parameters
        ----------
        D: gp_Dir

        Return
        -------
        None

        Description
        -----------
        Returns the tangent direction <d> on the iso-v.

        """
        return _BRepLProp.BRepLProp_SLProps_TangentU(self, *args)

    def TangentV(self, *args):
        r"""

        Parameters
        ----------
        D: gp_Dir

        Return
        -------
        None

        Description
        -----------
        Returns the tangent direction <d> on the iso-v.

        """
        return _BRepLProp.BRepLProp_SLProps_TangentV(self, *args)

    def Value(self, *args):
        r"""
        Return
        -------
        gp_Pnt

        Description
        -----------
        Returns the point.

        """
        return _BRepLProp.BRepLProp_SLProps_Value(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepLProp.delete_BRepLProp_SLProps

# Register BRepLProp_SLProps in _BRepLProp:
_BRepLProp.BRepLProp_SLProps_swigregister(BRepLProp_SLProps)
class BRepLProp_SurfaceTool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def Bounds(*args):
        r"""

        Parameters
        ----------
        S: BRepAdaptor_Surface

        Return
        -------
        U1: float
        V1: float
        U2: float
        V2: float

        Description
        -----------
        Returns the bounds of the surface.

        """
        return _BRepLProp.BRepLProp_SurfaceTool_Bounds(*args)

    @staticmethod
    def Continuity(*args):
        r"""

        Parameters
        ----------
        S: BRepAdaptor_Surface

        Return
        -------
        int

        Description
        -----------
        Returns the order of continuity of the surface <s>. returns 1: first derivative only is computable returns 2: first and second derivative only are computable.

        """
        return _BRepLProp.BRepLProp_SurfaceTool_Continuity(*args)

    @staticmethod
    def D1(*args):
        r"""

        Parameters
        ----------
        S: BRepAdaptor_Surface
        U: float
        V: float
        P: gp_Pnt
        D1U: gp_Vec
        D1V: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Computes the point <p> and first derivative <d1*> of parameter <u> and <v> on the surface <s>.

        """
        return _BRepLProp.BRepLProp_SurfaceTool_D1(*args)

    @staticmethod
    def D2(*args):
        r"""

        Parameters
        ----------
        S: BRepAdaptor_Surface
        U: float
        V: float
        P: gp_Pnt
        D1U: gp_Vec
        D1V: gp_Vec
        D2U: gp_Vec
        D2V: gp_Vec
        DUV: gp_Vec

        Return
        -------
        None

        Description
        -----------
        Computes the point <p>, the first derivative <d1*> and second derivative <d2*> of parameter <u> and <v> on the surface <s>.

        """
        return _BRepLProp.BRepLProp_SurfaceTool_D2(*args)

    @staticmethod
    def DN(*args):
        r"""

        Parameters
        ----------
        S: BRepAdaptor_Surface
        U: float
        V: float
        IU: int
        IV: int

        Return
        -------
        gp_Vec

        Description
        -----------
        No available documentation.

        """
        return _BRepLProp.BRepLProp_SurfaceTool_DN(*args)

    @staticmethod
    def Value(*args):
        r"""

        Parameters
        ----------
        S: BRepAdaptor_Surface
        U: float
        V: float
        P: gp_Pnt

        Return
        -------
        None

        Description
        -----------
        Computes the point <p> of parameter <u> and <v> on the surface <s>.

        """
        return _BRepLProp.BRepLProp_SurfaceTool_Value(*args)

    __repr__ = _dumps_object


    def __init__(self):
        _BRepLProp.BRepLProp_SurfaceTool_swiginit(self, _BRepLProp.new_BRepLProp_SurfaceTool())
    __swig_destroy__ = _BRepLProp.delete_BRepLProp_SurfaceTool

# Register BRepLProp_SurfaceTool in _BRepLProp:
_BRepLProp.BRepLProp_SurfaceTool_swigregister(BRepLProp_SurfaceTool)



@deprecated
def breplprop_Continuity(*args):
	return breplprop.Continuity(*args)

@deprecated
def breplprop_Continuity(*args):
	return breplprop.Continuity(*args)

@deprecated
def BRepLProp_CurveTool_Continuity(*args):
	return BRepLProp_CurveTool.Continuity(*args)

@deprecated
def BRepLProp_CurveTool_D1(*args):
	return BRepLProp_CurveTool.D1(*args)

@deprecated
def BRepLProp_CurveTool_D2(*args):
	return BRepLProp_CurveTool.D2(*args)

@deprecated
def BRepLProp_CurveTool_D3(*args):
	return BRepLProp_CurveTool.D3(*args)

@deprecated
def BRepLProp_CurveTool_FirstParameter(*args):
	return BRepLProp_CurveTool.FirstParameter(*args)

@deprecated
def BRepLProp_CurveTool_LastParameter(*args):
	return BRepLProp_CurveTool.LastParameter(*args)

@deprecated
def BRepLProp_CurveTool_Value(*args):
	return BRepLProp_CurveTool.Value(*args)

@deprecated
def BRepLProp_SurfaceTool_Bounds(*args):
	return BRepLProp_SurfaceTool.Bounds(*args)

@deprecated
def BRepLProp_SurfaceTool_Continuity(*args):
	return BRepLProp_SurfaceTool.Continuity(*args)

@deprecated
def BRepLProp_SurfaceTool_D1(*args):
	return BRepLProp_SurfaceTool.D1(*args)

@deprecated
def BRepLProp_SurfaceTool_D2(*args):
	return BRepLProp_SurfaceTool.D2(*args)

@deprecated
def BRepLProp_SurfaceTool_DN(*args):
	return BRepLProp_SurfaceTool.DN(*args)

@deprecated
def BRepLProp_SurfaceTool_Value(*args):
	return BRepLProp_SurfaceTool.Value(*args)



