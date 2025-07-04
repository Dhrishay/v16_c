# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

"""
LocalAnalysis module, see official documentation at
https://dev.opencascade.org/doc/occt-7.8.0/refman/html/package_localanalysis.html
"""

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _LocalAnalysis
else:
    import _LocalAnalysis

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
    __swig_destroy__ = _LocalAnalysis.delete_SwigPyIterator

    def value(self):
        return _LocalAnalysis.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _LocalAnalysis.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _LocalAnalysis.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _LocalAnalysis.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _LocalAnalysis.SwigPyIterator_equal(self, x)

    def copy(self):
        return _LocalAnalysis.SwigPyIterator_copy(self)

    def next(self):
        return _LocalAnalysis.SwigPyIterator_next(self)

    def __next__(self):
        return _LocalAnalysis.SwigPyIterator___next__(self)

    def previous(self):
        return _LocalAnalysis.SwigPyIterator_previous(self)

    def advance(self, n):
        return _LocalAnalysis.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _LocalAnalysis.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _LocalAnalysis.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _LocalAnalysis.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _LocalAnalysis.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _LocalAnalysis.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _LocalAnalysis.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _LocalAnalysis:
_LocalAnalysis.SwigPyIterator_swigregister(SwigPyIterator)

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
    return _LocalAnalysis.process_exception(error, method_name, class_name)

import warnings
from odoo.addons.OCC.Wrapper.wrapper_utils import Proxy, deprecated

class ios_base(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    erase_event = _LocalAnalysis.ios_base_erase_event
    imbue_event = _LocalAnalysis.ios_base_imbue_event
    copyfmt_event = _LocalAnalysis.ios_base_copyfmt_event

    def register_callback(self, __fn, __index):
        return _LocalAnalysis.ios_base_register_callback(self, __fn, __index)

    def flags(self, *args):
        return _LocalAnalysis.ios_base_flags(self, *args)

    def setf(self, *args):
        return _LocalAnalysis.ios_base_setf(self, *args)

    def unsetf(self, __mask):
        return _LocalAnalysis.ios_base_unsetf(self, __mask)

    def precision(self, *args):
        return _LocalAnalysis.ios_base_precision(self, *args)

    def width(self, *args):
        return _LocalAnalysis.ios_base_width(self, *args)

    @staticmethod
    def sync_with_stdio(__sync=True):
        return _LocalAnalysis.ios_base_sync_with_stdio(__sync)

    def imbue(self, __loc):
        return _LocalAnalysis.ios_base_imbue(self, __loc)

    def getloc(self):
        return _LocalAnalysis.ios_base_getloc(self)

    @staticmethod
    def xalloc():
        return _LocalAnalysis.ios_base_xalloc()

    def iword(self, __ix):
        return _LocalAnalysis.ios_base_iword(self, __ix)

    def pword(self, __ix):
        return _LocalAnalysis.ios_base_pword(self, __ix)
    __swig_destroy__ = _LocalAnalysis.delete_ios_base

# Register ios_base in _LocalAnalysis:
_LocalAnalysis.ios_base_swigregister(ios_base)
cvar = _LocalAnalysis.cvar
ios_base.boolalpha = _LocalAnalysis.cvar.ios_base_boolalpha
ios_base.dec = _LocalAnalysis.cvar.ios_base_dec
ios_base.fixed = _LocalAnalysis.cvar.ios_base_fixed
ios_base.hex = _LocalAnalysis.cvar.ios_base_hex
ios_base.internal = _LocalAnalysis.cvar.ios_base_internal
ios_base.left = _LocalAnalysis.cvar.ios_base_left
ios_base.oct = _LocalAnalysis.cvar.ios_base_oct
ios_base.right = _LocalAnalysis.cvar.ios_base_right
ios_base.scientific = _LocalAnalysis.cvar.ios_base_scientific
ios_base.showbase = _LocalAnalysis.cvar.ios_base_showbase
ios_base.showpoint = _LocalAnalysis.cvar.ios_base_showpoint
ios_base.showpos = _LocalAnalysis.cvar.ios_base_showpos
ios_base.skipws = _LocalAnalysis.cvar.ios_base_skipws
ios_base.unitbuf = _LocalAnalysis.cvar.ios_base_unitbuf
ios_base.uppercase = _LocalAnalysis.cvar.ios_base_uppercase
ios_base.adjustfield = _LocalAnalysis.cvar.ios_base_adjustfield
ios_base.basefield = _LocalAnalysis.cvar.ios_base_basefield
ios_base.floatfield = _LocalAnalysis.cvar.ios_base_floatfield
ios_base.badbit = _LocalAnalysis.cvar.ios_base_badbit
ios_base.eofbit = _LocalAnalysis.cvar.ios_base_eofbit
ios_base.failbit = _LocalAnalysis.cvar.ios_base_failbit
ios_base.goodbit = _LocalAnalysis.cvar.ios_base_goodbit
ios_base.app = _LocalAnalysis.cvar.ios_base_app
ios_base.ate = _LocalAnalysis.cvar.ios_base_ate
ios_base.binary = _LocalAnalysis.cvar.ios_base_binary
ios_base.ios_base_in = _LocalAnalysis.cvar.ios_base_ios_base_in
ios_base.out = _LocalAnalysis.cvar.ios_base_out
ios_base.trunc = _LocalAnalysis.cvar.ios_base_trunc
ios_base.beg = _LocalAnalysis.cvar.ios_base_beg
ios_base.cur = _LocalAnalysis.cvar.ios_base_cur
ios_base.end = _LocalAnalysis.cvar.ios_base_end

class ios(ios_base):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def rdstate(self):
        return _LocalAnalysis.ios_rdstate(self)

    def clear(self, *args):
        return _LocalAnalysis.ios_clear(self, *args)

    def setstate(self, __state):
        return _LocalAnalysis.ios_setstate(self, __state)

    def good(self):
        return _LocalAnalysis.ios_good(self)

    def eof(self):
        return _LocalAnalysis.ios_eof(self)

    def fail(self):
        return _LocalAnalysis.ios_fail(self)

    def bad(self):
        return _LocalAnalysis.ios_bad(self)

    def exceptions(self, *args):
        return _LocalAnalysis.ios_exceptions(self, *args)

    def __init__(self, __sb):
        _LocalAnalysis.ios_swiginit(self, _LocalAnalysis.new_ios(__sb))
    __swig_destroy__ = _LocalAnalysis.delete_ios

    def tie(self, *args):
        return _LocalAnalysis.ios_tie(self, *args)

    def rdbuf(self, *args):
        return _LocalAnalysis.ios_rdbuf(self, *args)

    def copyfmt(self, __rhs):
        return _LocalAnalysis.ios_copyfmt(self, __rhs)

    def fill(self, *args):
        return _LocalAnalysis.ios_fill(self, *args)

    def imbue(self, __loc):
        return _LocalAnalysis.ios_imbue(self, __loc)

    def narrow(self, __c, __dfault):
        return _LocalAnalysis.ios_narrow(self, __c, __dfault)

    def widen(self, __c):
        return _LocalAnalysis.ios_widen(self, __c)

# Register ios in _LocalAnalysis:
_LocalAnalysis.ios_swigregister(ios)
class ostream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _LocalAnalysis.ostream_swiginit(self, _LocalAnalysis.new_ostream(__sb))
    __swig_destroy__ = _LocalAnalysis.delete_ostream

    def __lshift__(self, *args):
        return _LocalAnalysis.ostream___lshift__(self, *args)

    def put(self, __c):
        return _LocalAnalysis.ostream_put(self, __c)

    def write(self, __s, __n):
        return _LocalAnalysis.ostream_write(self, __s, __n)

    def flush(self):
        return _LocalAnalysis.ostream_flush(self)

    def tellp(self):
        return _LocalAnalysis.ostream_tellp(self)

    def seekp(self, *args):
        return _LocalAnalysis.ostream_seekp(self, *args)

# Register ostream in _LocalAnalysis:
_LocalAnalysis.ostream_swigregister(ostream)
class istream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _LocalAnalysis.istream_swiginit(self, _LocalAnalysis.new_istream(__sb))
    __swig_destroy__ = _LocalAnalysis.delete_istream

    def __rshift__(self, *args):
        return _LocalAnalysis.istream___rshift__(self, *args)

    def gcount(self):
        return _LocalAnalysis.istream_gcount(self)

    def get(self, *args):
        return _LocalAnalysis.istream_get(self, *args)

    def getline(self, *args):
        return _LocalAnalysis.istream_getline(self, *args)

    def ignore(self, *args):
        return _LocalAnalysis.istream_ignore(self, *args)

    def peek(self):
        return _LocalAnalysis.istream_peek(self)

    def read(self, __s, __n):
        return _LocalAnalysis.istream_read(self, __s, __n)

    def readsome(self, __s, __n):
        return _LocalAnalysis.istream_readsome(self, __s, __n)

    def putback(self, __c):
        return _LocalAnalysis.istream_putback(self, __c)

    def unget(self):
        return _LocalAnalysis.istream_unget(self)

    def sync(self):
        return _LocalAnalysis.istream_sync(self)

    def tellg(self):
        return _LocalAnalysis.istream_tellg(self)

    def seekg(self, *args):
        return _LocalAnalysis.istream_seekg(self, *args)

# Register istream in _LocalAnalysis:
_LocalAnalysis.istream_swigregister(istream)
class iostream(istream, ostream):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _LocalAnalysis.iostream_swiginit(self, _LocalAnalysis.new_iostream(__sb))
    __swig_destroy__ = _LocalAnalysis.delete_iostream

# Register iostream in _LocalAnalysis:
_LocalAnalysis.iostream_swigregister(iostream)
cin = cvar.cin
cout = cvar.cout
cerr = cvar.cerr
clog = cvar.clog

endl_cb_ptr = _LocalAnalysis.endl_cb_ptr
endl = _LocalAnalysis.endl
ends_cb_ptr = _LocalAnalysis.ends_cb_ptr
ends = _LocalAnalysis.ends
flush_cb_ptr = _LocalAnalysis.flush_cb_ptr
flush = _LocalAnalysis.flush
import odoo.addons.OCC.Core.Standard
import odoo.addons.OCC.Core.NCollection
import odoo.addons.OCC.Core.Geom
import odoo.addons.OCC.Core.gp
import odoo.addons.OCC.Core.TColStd
import odoo.addons.OCC.Core.TCollection
import odoo.addons.OCC.Core.GeomAbs
import odoo.addons.OCC.Core.TColgp
import odoo.addons.OCC.Core.Geom2d
import odoo.addons.OCC.Core.GeomLProp

from enum import IntEnum
from odoo.addons.OCC.Core.Exception import *

LocalAnalysis_NullFirstDerivative = _LocalAnalysis.LocalAnalysis_NullFirstDerivative
LocalAnalysis_NullSecondDerivative = _LocalAnalysis.LocalAnalysis_NullSecondDerivative
LocalAnalysis_TangentNotDefined = _LocalAnalysis.LocalAnalysis_TangentNotDefined
LocalAnalysis_NormalNotDefined = _LocalAnalysis.LocalAnalysis_NormalNotDefined
LocalAnalysis_CurvatureNotDefined = _LocalAnalysis.LocalAnalysis_CurvatureNotDefined


class LocalAnalysis_StatusErrorType(IntEnum):
	LocalAnalysis_NullFirstDerivative = 0
	LocalAnalysis_NullSecondDerivative = 1
	LocalAnalysis_TangentNotDefined = 2
	LocalAnalysis_NormalNotDefined = 3
	LocalAnalysis_CurvatureNotDefined = 4
LocalAnalysis_NullFirstDerivative = LocalAnalysis_StatusErrorType.LocalAnalysis_NullFirstDerivative
LocalAnalysis_NullSecondDerivative = LocalAnalysis_StatusErrorType.LocalAnalysis_NullSecondDerivative
LocalAnalysis_TangentNotDefined = LocalAnalysis_StatusErrorType.LocalAnalysis_TangentNotDefined
LocalAnalysis_NormalNotDefined = LocalAnalysis_StatusErrorType.LocalAnalysis_NormalNotDefined
LocalAnalysis_CurvatureNotDefined = LocalAnalysis_StatusErrorType.LocalAnalysis_CurvatureNotDefined

class localanalysis(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def Dump(*args):
        r"""

        Parameters
        ----------
        surfconti: LocalAnalysis_SurfaceContinuity

        Return
        -------
        o: Standard_OStream

        Description
        -----------
        This class compute s and gives tools to check the local continuity between two points situated on 2 curves. //! this function gives information about a variable curvecontinuity.

        Parameters
        ----------
        curvconti: LocalAnalysis_CurveContinuity

        Return
        -------
        o: Standard_OStream

        Description
        -----------
        This function gives information about a variable surfacecontinuity.

        """
        return _LocalAnalysis.localanalysis_Dump(*args)

    __repr__ = _dumps_object


    def __init__(self):
        _LocalAnalysis.localanalysis_swiginit(self, _LocalAnalysis.new_localanalysis())
    __swig_destroy__ = _LocalAnalysis.delete_localanalysis

# Register localanalysis in _LocalAnalysis:
_LocalAnalysis.localanalysis_swigregister(localanalysis)
class LocalAnalysis_CurveContinuity(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        Curv1: Geom_Curve
        u1: float
        Curv2: Geom_Curve
        u2: float
        Order: GeomAbs_Shape
        EpsNul: float (optional, default to 0.001)
        EpsC0: float (optional, default to 0.001)
        EpsC1: float (optional, default to 0.001)
        EpsC2: float (optional, default to 0.001)
        EpsG1: float (optional, default to 0.001)
        EpsG2: float (optional, default to 0.001)
        Percent: float (optional, default to 0.01)
        Maxlen: float (optional, default to 10000)

        Return
        -------
        None

        Description
        -----------
        -u1 is the parameter of the point on curv1 -u2 is the parameter of the point on curv2 -order is the required continuity: geomabs_c0 geomabs_c1 geomabs_c2 geomabs_g1 geomabs_g2 //! -epsnul is used to detect a a vector with nul magnitude (in mm) //! -epsc0 is used for c0 continuity to confuse two points (in mm) //! -epsc1 is an angular tolerance in radians used for c1 continuity to compare the angle between the first derivatives //! -epsc2 is an angular tolerance in radians used for c2 continuity to compare the angle between the second derivatives //! -epsg1 is an angular tolerance in radians used for g1 continuity to compare the angle between the tangents //! -epsg2 is an angular tolerance in radians used for g2 continuity to compare the angle between the normals //! - percent: percentage of curvature variation (unitless) used for g2 continuity //! - maxlen is the maximum length of curv1 or curv2 in meters used to detect nul curvature (in mm) //! the constructor computes the quantities which are necessary to check the continuity in the following cases: //! case c0 -------- - the distance between p1 and p2 with p1=curv1 (u1) and p2=curv2(u2) //! case c1 ------- //! - the angle between the first derivatives dcurv1(u1)  dcurv2(u2) -------- and --------- du  du //! - the ratio between the magnitudes of the first derivatives //! the angle value is between 0 and pi/2 //! case c2 ------- - the angle between the second derivatives 2  2 d curv1(u1) d curv2(u2) ---------- ---------- 2  2 du du //! the angle value is between 0 and pi/2 //! - the ratio between the magnitudes of the second derivatives //! case g1 ------- the angle between the tangents at each point //! the angle value is between 0 and pi/2 //! case g2 ------- -the angle between the normals at each point //! the angle value is between 0 and pi/2 //! - the relative variation of curvature: |curvat1-curvat2| ------------------ 1/2 (curvat1*curvat2) //! where curvat1 is the curvature at the first point and curvat2 the curvature at the second point.

        """
        _LocalAnalysis.LocalAnalysis_CurveContinuity_swiginit(self, _LocalAnalysis.new_LocalAnalysis_CurveContinuity(*args))

    def C0Value(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_C0Value(self, *args)

    def C1Angle(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_C1Angle(self, *args)

    def C1Ratio(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_C1Ratio(self, *args)

    def C2Angle(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_C2Angle(self, *args)

    def C2Ratio(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_C2Ratio(self, *args)

    def ContinuityStatus(self, *args):
        r"""
        Return
        -------
        GeomAbs_Shape

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_ContinuityStatus(self, *args)

    def G1Angle(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_G1Angle(self, *args)

    def G2Angle(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_G2Angle(self, *args)

    def G2CurvatureVariation(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_G2CurvatureVariation(self, *args)

    def IsC0(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsC0(self, *args)

    def IsC1(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsC1(self, *args)

    def IsC2(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsC2(self, *args)

    def IsDone(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsDone(self, *args)

    def IsG1(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsG1(self, *args)

    def IsG2(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsG2(self, *args)

    def StatusError(self, *args):
        r"""
        Return
        -------
        LocalAnalysis_StatusErrorType

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_StatusError(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _LocalAnalysis.delete_LocalAnalysis_CurveContinuity

# Register LocalAnalysis_CurveContinuity in _LocalAnalysis:
_LocalAnalysis.LocalAnalysis_CurveContinuity_swigregister(LocalAnalysis_CurveContinuity)
class LocalAnalysis_SurfaceContinuity(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        Surf1: Geom_Surface
        u1: float
        v1: float
        Surf2: Geom_Surface
        u2: float
        v2: float
        Order: GeomAbs_Shape
        EpsNul: float (optional, default to 0.001)
        EpsC0: float (optional, default to 0.001)
        EpsC1: float (optional, default to 0.001)
        EpsC2: float (optional, default to 0.001)
        EpsG1: float (optional, default to 0.001)
        Percent: float (optional, default to 0.01)
        Maxlen: float (optional, default to 10000)

        Return
        -------
        None

        Description
        -----------
        -u1,v1 are the parameters of the point on surf1 -u2,v2 are the parameters of the point on surf2 -order is the required continuity: geomabs_c0 geomabs_c1 geomabs_c2 geomabs_g1 geomabs_g2 //! -epsnul is used to detect a a vector with nul magnitude //! -epsc0 is used for c0 continuity to confuse two points (in mm) //! -epsc1 is an angular tolerance in radians used for c1 continuity to compare the angle between the first derivatives //! -epsc2 is an angular tolerance in radians used for c2 continuity to compare the angle between the second derivatives //! -epsg1 is an angular tolerance in radians used for g1 continuity to compare the angle between the normals //! -percent: percentage of curvature variation (unitless) used for g2 continuity //! - maxlen is the maximum length of surf1 or surf2 in meters used to detect null curvature (in mm) //! the constructor computes the quantities which are necessary to check the continuity in the following cases: //! case c0 -------- - the distance between p1 and p2 with p1=surf (u1,v1) and p2=surfv2(u2,v2) //! case c1 ------- //! - the angle between the first derivatives in u: //! dsurf1(u1,v1) dsurf2(u2,v2) ----------- and --------- du  du //! the angle value is between 0 and pi/2 //! - the angle between the first derivatives in v: //! dsurf1(u1,v1) dsurf2(u2,v2) -------- and --------- dv  dv //! - the ratio between the magnitudes of the first derivatives in u - the ratio between the magnitudes of the first derivatives in v //! the angle value is between 0 and pi/2 //! case c2 ------- - the angle between the second derivatives in u 2 2 d surf1(u1,v1) d surf2(u2,v2) ---------- ---------- 2 2 d u d u //! - the ratio between the magnitudes of the second derivatives in u - the ratio between the magnitudes of the second derivatives in v //! the angle value is between 0 and pi/2 //! case g1 ------- -the angle between the normals at each point the angle value is between 0 and pi/2 //! case g2 ------- - the maximum normal curvature gap between the two points.

        Parameters
        ----------
        curv1: Geom2d_Curve
        curv2: Geom2d_Curve
        U: float
        Surf1: Geom_Surface
        Surf2: Geom_Surface
        Order: GeomAbs_Shape
        EpsNul: float (optional, default to 0.001)
        EpsC0: float (optional, default to 0.001)
        EpsC1: float (optional, default to 0.001)
        EpsC2: float (optional, default to 0.001)
        EpsG1: float (optional, default to 0.001)
        Percent: float (optional, default to 0.01)
        Maxlen: float (optional, default to 10000)

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        Parameters
        ----------
        EpsNul: float (optional, default to 0.001)
        EpsC0: float (optional, default to 0.001)
        EpsC1: float (optional, default to 0.001)
        EpsC2: float (optional, default to 0.001)
        EpsG1: float (optional, default to 0.001)
        Percent: float (optional, default to 0.01)
        Maxlen: float (optional, default to 10000)

        Return
        -------
        None

        Description
        -----------
        This constructor is used when we want to compute many analysis. after we use the method computeanalysis.

        """
        _LocalAnalysis.LocalAnalysis_SurfaceContinuity_swiginit(self, _LocalAnalysis.new_LocalAnalysis_SurfaceContinuity(*args))

    def C0Value(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C0Value(self, *args)

    def C1UAngle(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1UAngle(self, *args)

    def C1URatio(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1URatio(self, *args)

    def C1VAngle(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1VAngle(self, *args)

    def C1VRatio(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1VRatio(self, *args)

    def C2UAngle(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2UAngle(self, *args)

    def C2URatio(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2URatio(self, *args)

    def C2VAngle(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2VAngle(self, *args)

    def C2VRatio(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2VRatio(self, *args)

    def ComputeAnalysis(self, *args):
        r"""

        Parameters
        ----------
        Surf1: GeomLProp_SLProps
        Surf2: GeomLProp_SLProps
        Order: GeomAbs_Shape

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_ComputeAnalysis(self, *args)

    def ContinuityStatus(self, *args):
        r"""
        Return
        -------
        GeomAbs_Shape

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_ContinuityStatus(self, *args)

    def G1Angle(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_G1Angle(self, *args)

    def G2CurvatureGap(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_G2CurvatureGap(self, *args)

    def IsC0(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsC0(self, *args)

    def IsC1(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsC1(self, *args)

    def IsC2(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsC2(self, *args)

    def IsDone(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsDone(self, *args)

    def IsG1(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsG1(self, *args)

    def IsG2(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsG2(self, *args)

    def StatusError(self, *args):
        r"""
        Return
        -------
        LocalAnalysis_StatusErrorType

        Description
        -----------
        No available documentation.

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_StatusError(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _LocalAnalysis.delete_LocalAnalysis_SurfaceContinuity

# Register LocalAnalysis_SurfaceContinuity in _LocalAnalysis:
_LocalAnalysis.LocalAnalysis_SurfaceContinuity_swigregister(LocalAnalysis_SurfaceContinuity)



@deprecated
def localanalysis_Dump(*args):
	return localanalysis.Dump(*args)

@deprecated
def localanalysis_Dump(*args):
	return localanalysis.Dump(*args)



