# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

"""
ChFi2d module, see official documentation at
https://dev.opencascade.org/doc/occt-7.8.0/refman/html/package_chfi2d.html
"""

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ChFi2d
else:
    import _ChFi2d

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
    __swig_destroy__ = _ChFi2d.delete_SwigPyIterator

    def value(self):
        return _ChFi2d.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _ChFi2d.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _ChFi2d.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _ChFi2d.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _ChFi2d.SwigPyIterator_equal(self, x)

    def copy(self):
        return _ChFi2d.SwigPyIterator_copy(self)

    def next(self):
        return _ChFi2d.SwigPyIterator_next(self)

    def __next__(self):
        return _ChFi2d.SwigPyIterator___next__(self)

    def previous(self):
        return _ChFi2d.SwigPyIterator_previous(self)

    def advance(self, n):
        return _ChFi2d.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _ChFi2d.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _ChFi2d.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _ChFi2d.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _ChFi2d.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _ChFi2d.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _ChFi2d.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _ChFi2d:
_ChFi2d.SwigPyIterator_swigregister(SwigPyIterator)

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
    return _ChFi2d.process_exception(error, method_name, class_name)

import warnings
from odoo.addons.OCC.Wrapper.wrapper_utils import Proxy, deprecated

class ios_base(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    erase_event = _ChFi2d.ios_base_erase_event
    imbue_event = _ChFi2d.ios_base_imbue_event
    copyfmt_event = _ChFi2d.ios_base_copyfmt_event

    def register_callback(self, __fn, __index):
        return _ChFi2d.ios_base_register_callback(self, __fn, __index)

    def flags(self, *args):
        return _ChFi2d.ios_base_flags(self, *args)

    def setf(self, *args):
        return _ChFi2d.ios_base_setf(self, *args)

    def unsetf(self, __mask):
        return _ChFi2d.ios_base_unsetf(self, __mask)

    def precision(self, *args):
        return _ChFi2d.ios_base_precision(self, *args)

    def width(self, *args):
        return _ChFi2d.ios_base_width(self, *args)

    @staticmethod
    def sync_with_stdio(__sync=True):
        return _ChFi2d.ios_base_sync_with_stdio(__sync)

    def imbue(self, __loc):
        return _ChFi2d.ios_base_imbue(self, __loc)

    def getloc(self):
        return _ChFi2d.ios_base_getloc(self)

    @staticmethod
    def xalloc():
        return _ChFi2d.ios_base_xalloc()

    def iword(self, __ix):
        return _ChFi2d.ios_base_iword(self, __ix)

    def pword(self, __ix):
        return _ChFi2d.ios_base_pword(self, __ix)
    __swig_destroy__ = _ChFi2d.delete_ios_base

# Register ios_base in _ChFi2d:
_ChFi2d.ios_base_swigregister(ios_base)
cvar = _ChFi2d.cvar
ios_base.boolalpha = _ChFi2d.cvar.ios_base_boolalpha
ios_base.dec = _ChFi2d.cvar.ios_base_dec
ios_base.fixed = _ChFi2d.cvar.ios_base_fixed
ios_base.hex = _ChFi2d.cvar.ios_base_hex
ios_base.internal = _ChFi2d.cvar.ios_base_internal
ios_base.left = _ChFi2d.cvar.ios_base_left
ios_base.oct = _ChFi2d.cvar.ios_base_oct
ios_base.right = _ChFi2d.cvar.ios_base_right
ios_base.scientific = _ChFi2d.cvar.ios_base_scientific
ios_base.showbase = _ChFi2d.cvar.ios_base_showbase
ios_base.showpoint = _ChFi2d.cvar.ios_base_showpoint
ios_base.showpos = _ChFi2d.cvar.ios_base_showpos
ios_base.skipws = _ChFi2d.cvar.ios_base_skipws
ios_base.unitbuf = _ChFi2d.cvar.ios_base_unitbuf
ios_base.uppercase = _ChFi2d.cvar.ios_base_uppercase
ios_base.adjustfield = _ChFi2d.cvar.ios_base_adjustfield
ios_base.basefield = _ChFi2d.cvar.ios_base_basefield
ios_base.floatfield = _ChFi2d.cvar.ios_base_floatfield
ios_base.badbit = _ChFi2d.cvar.ios_base_badbit
ios_base.eofbit = _ChFi2d.cvar.ios_base_eofbit
ios_base.failbit = _ChFi2d.cvar.ios_base_failbit
ios_base.goodbit = _ChFi2d.cvar.ios_base_goodbit
ios_base.app = _ChFi2d.cvar.ios_base_app
ios_base.ate = _ChFi2d.cvar.ios_base_ate
ios_base.binary = _ChFi2d.cvar.ios_base_binary
ios_base.ios_base_in = _ChFi2d.cvar.ios_base_ios_base_in
ios_base.out = _ChFi2d.cvar.ios_base_out
ios_base.trunc = _ChFi2d.cvar.ios_base_trunc
ios_base.beg = _ChFi2d.cvar.ios_base_beg
ios_base.cur = _ChFi2d.cvar.ios_base_cur
ios_base.end = _ChFi2d.cvar.ios_base_end

class ios(ios_base):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def rdstate(self):
        return _ChFi2d.ios_rdstate(self)

    def clear(self, *args):
        return _ChFi2d.ios_clear(self, *args)

    def setstate(self, __state):
        return _ChFi2d.ios_setstate(self, __state)

    def good(self):
        return _ChFi2d.ios_good(self)

    def eof(self):
        return _ChFi2d.ios_eof(self)

    def fail(self):
        return _ChFi2d.ios_fail(self)

    def bad(self):
        return _ChFi2d.ios_bad(self)

    def exceptions(self, *args):
        return _ChFi2d.ios_exceptions(self, *args)

    def __init__(self, __sb):
        _ChFi2d.ios_swiginit(self, _ChFi2d.new_ios(__sb))
    __swig_destroy__ = _ChFi2d.delete_ios

    def tie(self, *args):
        return _ChFi2d.ios_tie(self, *args)

    def rdbuf(self, *args):
        return _ChFi2d.ios_rdbuf(self, *args)

    def copyfmt(self, __rhs):
        return _ChFi2d.ios_copyfmt(self, __rhs)

    def fill(self, *args):
        return _ChFi2d.ios_fill(self, *args)

    def imbue(self, __loc):
        return _ChFi2d.ios_imbue(self, __loc)

    def narrow(self, __c, __dfault):
        return _ChFi2d.ios_narrow(self, __c, __dfault)

    def widen(self, __c):
        return _ChFi2d.ios_widen(self, __c)

# Register ios in _ChFi2d:
_ChFi2d.ios_swigregister(ios)
class ostream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _ChFi2d.ostream_swiginit(self, _ChFi2d.new_ostream(__sb))
    __swig_destroy__ = _ChFi2d.delete_ostream

    def __lshift__(self, *args):
        return _ChFi2d.ostream___lshift__(self, *args)

    def put(self, __c):
        return _ChFi2d.ostream_put(self, __c)

    def write(self, __s, __n):
        return _ChFi2d.ostream_write(self, __s, __n)

    def flush(self):
        return _ChFi2d.ostream_flush(self)

    def tellp(self):
        return _ChFi2d.ostream_tellp(self)

    def seekp(self, *args):
        return _ChFi2d.ostream_seekp(self, *args)

# Register ostream in _ChFi2d:
_ChFi2d.ostream_swigregister(ostream)
class istream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _ChFi2d.istream_swiginit(self, _ChFi2d.new_istream(__sb))
    __swig_destroy__ = _ChFi2d.delete_istream

    def __rshift__(self, *args):
        return _ChFi2d.istream___rshift__(self, *args)

    def gcount(self):
        return _ChFi2d.istream_gcount(self)

    def get(self, *args):
        return _ChFi2d.istream_get(self, *args)

    def getline(self, *args):
        return _ChFi2d.istream_getline(self, *args)

    def ignore(self, *args):
        return _ChFi2d.istream_ignore(self, *args)

    def peek(self):
        return _ChFi2d.istream_peek(self)

    def read(self, __s, __n):
        return _ChFi2d.istream_read(self, __s, __n)

    def readsome(self, __s, __n):
        return _ChFi2d.istream_readsome(self, __s, __n)

    def putback(self, __c):
        return _ChFi2d.istream_putback(self, __c)

    def unget(self):
        return _ChFi2d.istream_unget(self)

    def sync(self):
        return _ChFi2d.istream_sync(self)

    def tellg(self):
        return _ChFi2d.istream_tellg(self)

    def seekg(self, *args):
        return _ChFi2d.istream_seekg(self, *args)

# Register istream in _ChFi2d:
_ChFi2d.istream_swigregister(istream)
class iostream(istream, ostream):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _ChFi2d.iostream_swiginit(self, _ChFi2d.new_iostream(__sb))
    __swig_destroy__ = _ChFi2d.delete_iostream

# Register iostream in _ChFi2d:
_ChFi2d.iostream_swigregister(iostream)
cin = cvar.cin
cout = cvar.cout
cerr = cvar.cerr
clog = cvar.clog

endl_cb_ptr = _ChFi2d.endl_cb_ptr
endl = _ChFi2d.endl
ends_cb_ptr = _ChFi2d.ends_cb_ptr
ends = _ChFi2d.ends
flush_cb_ptr = _ChFi2d.flush_cb_ptr
flush = _ChFi2d.flush
import odoo.addons.OCC.Core.Standard
import odoo.addons.OCC.Core.NCollection
import odoo.addons.OCC.Core.TopoDS
import odoo.addons.OCC.Core.Message
import odoo.addons.OCC.Core.TCollection
import odoo.addons.OCC.Core.OSD
import odoo.addons.OCC.Core.TColStd
import odoo.addons.OCC.Core.TopAbs
import odoo.addons.OCC.Core.TopLoc
import odoo.addons.OCC.Core.gp
import odoo.addons.OCC.Core.TopTools

from enum import IntEnum
from odoo.addons.OCC.Core.Exception import *

ChFi2d_NotPlanar = _ChFi2d.ChFi2d_NotPlanar
ChFi2d_NoFace = _ChFi2d.ChFi2d_NoFace
ChFi2d_InitialisationError = _ChFi2d.ChFi2d_InitialisationError
ChFi2d_ParametersError = _ChFi2d.ChFi2d_ParametersError
ChFi2d_Ready = _ChFi2d.ChFi2d_Ready
ChFi2d_IsDone = _ChFi2d.ChFi2d_IsDone
ChFi2d_ComputationError = _ChFi2d.ChFi2d_ComputationError
ChFi2d_ConnexionError = _ChFi2d.ChFi2d_ConnexionError
ChFi2d_TangencyError = _ChFi2d.ChFi2d_TangencyError
ChFi2d_FirstEdgeDegenerated = _ChFi2d.ChFi2d_FirstEdgeDegenerated
ChFi2d_LastEdgeDegenerated = _ChFi2d.ChFi2d_LastEdgeDegenerated
ChFi2d_BothEdgesDegenerated = _ChFi2d.ChFi2d_BothEdgesDegenerated
ChFi2d_NotAuthorized = _ChFi2d.ChFi2d_NotAuthorized


class ChFi2d_ConstructionError(IntEnum):
	ChFi2d_NotPlanar = 0
	ChFi2d_NoFace = 1
	ChFi2d_InitialisationError = 2
	ChFi2d_ParametersError = 3
	ChFi2d_Ready = 4
	ChFi2d_IsDone = 5
	ChFi2d_ComputationError = 6
	ChFi2d_ConnexionError = 7
	ChFi2d_TangencyError = 8
	ChFi2d_FirstEdgeDegenerated = 9
	ChFi2d_LastEdgeDegenerated = 10
	ChFi2d_BothEdgesDegenerated = 11
	ChFi2d_NotAuthorized = 12
ChFi2d_NotPlanar = ChFi2d_ConstructionError.ChFi2d_NotPlanar
ChFi2d_NoFace = ChFi2d_ConstructionError.ChFi2d_NoFace
ChFi2d_InitialisationError = ChFi2d_ConstructionError.ChFi2d_InitialisationError
ChFi2d_ParametersError = ChFi2d_ConstructionError.ChFi2d_ParametersError
ChFi2d_Ready = ChFi2d_ConstructionError.ChFi2d_Ready
ChFi2d_IsDone = ChFi2d_ConstructionError.ChFi2d_IsDone
ChFi2d_ComputationError = ChFi2d_ConstructionError.ChFi2d_ComputationError
ChFi2d_ConnexionError = ChFi2d_ConstructionError.ChFi2d_ConnexionError
ChFi2d_TangencyError = ChFi2d_ConstructionError.ChFi2d_TangencyError
ChFi2d_FirstEdgeDegenerated = ChFi2d_ConstructionError.ChFi2d_FirstEdgeDegenerated
ChFi2d_LastEdgeDegenerated = ChFi2d_ConstructionError.ChFi2d_LastEdgeDegenerated
ChFi2d_BothEdgesDegenerated = ChFi2d_ConstructionError.ChFi2d_BothEdgesDegenerated
ChFi2d_NotAuthorized = ChFi2d_ConstructionError.ChFi2d_NotAuthorized

class chfi2d(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def CommonVertex(*args):
        r"""

        Parameters
        ----------
        E1: TopoDS_Edge
        E2: TopoDS_Edge
        V: TopoDS_Vertex

        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _ChFi2d.chfi2d_CommonVertex(*args)

    @staticmethod
    def FindConnectedEdges(*args):
        r"""

        Parameters
        ----------
        F: TopoDS_Face
        V: TopoDS_Vertex
        E1: TopoDS_Edge
        E2: TopoDS_Edge

        Return
        -------
        ChFi2d_ConstructionError

        Description
        -----------
        No available documentation.

        """
        return _ChFi2d.chfi2d_FindConnectedEdges(*args)

    __repr__ = _dumps_object


    def __init__(self):
        _ChFi2d.chfi2d_swiginit(self, _ChFi2d.new_chfi2d())
    __swig_destroy__ = _ChFi2d.delete_chfi2d

# Register chfi2d in _ChFi2d:
_ChFi2d.chfi2d_swigregister(chfi2d)
class ChFi2d_AnaFilletAlgo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        Return
        -------
        None

        Description
        -----------
        An empty constructor. use the method init() to initialize the class.

        Parameters
        ----------
        theWire: TopoDS_Wire
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        A constructor. it expects a wire consisting of two edges of type (any combination of): - segment - arc of circle.

        Parameters
        ----------
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        A constructor. it expects two edges having a common point of type: - segment - arc of circle.

        """
        _ChFi2d.ChFi2d_AnaFilletAlgo_swiginit(self, _ChFi2d.new_ChFi2d_AnaFilletAlgo(*args))

    def Init(self, *args):
        r"""

        Parameters
        ----------
        theWire: TopoDS_Wire
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        Initializes the class by a wire consisting of two edges.

        Parameters
        ----------
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        Initializes the class by two edges.

        """
        return _ChFi2d.ChFi2d_AnaFilletAlgo_Init(self, *args)

    def Perform(self, *args):
        r"""

        Parameters
        ----------
        radius: float

        Return
        -------
        bool

        Description
        -----------
        Calculates a fillet.

        """
        return _ChFi2d.ChFi2d_AnaFilletAlgo_Perform(self, *args)

    def Result(self, *args):
        r"""

        Parameters
        ----------
        e1: TopoDS_Edge
        e2: TopoDS_Edge

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Retrieves a result (fillet and shrinked neighbours).

        """
        return _ChFi2d.ChFi2d_AnaFilletAlgo_Result(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _ChFi2d.delete_ChFi2d_AnaFilletAlgo

# Register ChFi2d_AnaFilletAlgo in _ChFi2d:
_ChFi2d.ChFi2d_AnaFilletAlgo_swigregister(ChFi2d_AnaFilletAlgo)
class ChFi2d_Builder(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        Return
        -------
        None

        Description
        -----------
        No available documentation.

        Parameters
        ----------
        F: TopoDS_Face

        Return
        -------
        None

        Description
        -----------
        The face <f> can be build on a closed or an open wire.

        """
        _ChFi2d.ChFi2d_Builder_swiginit(self, _ChFi2d.new_ChFi2d_Builder(*args))

    def AddChamfer(self, *args):
        r"""

        Parameters
        ----------
        E1: TopoDS_Edge
        E2: TopoDS_Edge
        D1: float
        D2: float

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Add a chamfer on the wire between the two edges connected <e1> and <e2>. <addchamfer> returns the chamfer edge. this edge has sense only if the status <status> is <isdone>.

        Parameters
        ----------
        E: TopoDS_Edge
        V: TopoDS_Vertex
        D: float
        Ang: float

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Add a chamfer on the wire between the two edges connected to the vertex <v>. the chamfer will make an angle <ang> with the edge <e>, and one of its extremities will be on <e> at distance <d>. the returned edge has sense only if the status <status> is <isdone>. warning: the value of <ang> must be expressed in radian.

        """
        return _ChFi2d.ChFi2d_Builder_AddChamfer(self, *args)

    def AddFillet(self, *args):
        r"""

        Parameters
        ----------
        V: TopoDS_Vertex
        Radius: float

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Add a fillet of radius <radius> on the wire between the two edges connected to the vertex <v>. <addfillet> returns the fillet edge. the returned edge has sense only if the status <status> is <isdone>.

        """
        return _ChFi2d.ChFi2d_Builder_AddFillet(self, *args)

    def BasisEdge(self, *args):
        r"""

        Parameters
        ----------
        E: TopoDS_Edge

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Returns the parent edge of <e> warning: if <e>is a basis edge, the returned edge would be equal to <e>.

        """
        return _ChFi2d.ChFi2d_Builder_BasisEdge(self, *args)

    def ChamferEdges(self, *args):
        r"""
        Return
        -------
        TopTools_SequenceOfShape

        Description
        -----------
        Returns the list of new edges.

        """
        return _ChFi2d.ChFi2d_Builder_ChamferEdges(self, *args)

    def DescendantEdge(self, *args):
        r"""

        Parameters
        ----------
        E: TopoDS_Edge

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Returns the modified edge if <e> has descendant or <e> in the other case.

        """
        return _ChFi2d.ChFi2d_Builder_DescendantEdge(self, *args)

    def FilletEdges(self, *args):
        r"""
        Return
        -------
        TopTools_SequenceOfShape

        Description
        -----------
        Returns the list of new edges.

        """
        return _ChFi2d.ChFi2d_Builder_FilletEdges(self, *args)

    def HasDescendant(self, *args):
        r"""

        Parameters
        ----------
        E: TopoDS_Edge

        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _ChFi2d.ChFi2d_Builder_HasDescendant(self, *args)

    def Init(self, *args):
        r"""

        Parameters
        ----------
        F: TopoDS_Face

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        Parameters
        ----------
        RefFace: TopoDS_Face
        ModFace: TopoDS_Face

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        return _ChFi2d.ChFi2d_Builder_Init(self, *args)

    def IsModified(self, *args):
        r"""

        Parameters
        ----------
        E: TopoDS_Edge

        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        """
        return _ChFi2d.ChFi2d_Builder_IsModified(self, *args)

    def ModifyChamfer(self, *args):
        r"""

        Parameters
        ----------
        Chamfer: TopoDS_Edge
        E1: TopoDS_Edge
        E2: TopoDS_Edge
        D1: float
        D2: float

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Modify the chamfer <chamfer> and returns the new chamfer edge. this edge as sense only if the status <status> is <isdone>.

        Parameters
        ----------
        Chamfer: TopoDS_Edge
        E: TopoDS_Edge
        D: float
        Ang: float

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Modify the chamfer <chamfer> and returns the new chamfer edge. this edge as sense only if the status <status> is <isdone>. warning: the value of <ang> must be expressed in radian.

        """
        return _ChFi2d.ChFi2d_Builder_ModifyChamfer(self, *args)

    def ModifyFillet(self, *args):
        r"""

        Parameters
        ----------
        Fillet: TopoDS_Edge
        Radius: float

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Modify the fillet radius and return the new fillet edge. this edge has sense only if the status <status> is <isdone>.

        """
        return _ChFi2d.ChFi2d_Builder_ModifyFillet(self, *args)

    def NbChamfer(self, *args):
        r"""
        Return
        -------
        int

        Description
        -----------
        No available documentation.

        """
        return _ChFi2d.ChFi2d_Builder_NbChamfer(self, *args)

    def NbFillet(self, *args):
        r"""
        Return
        -------
        int

        Description
        -----------
        No available documentation.

        """
        return _ChFi2d.ChFi2d_Builder_NbFillet(self, *args)

    def RemoveChamfer(self, *args):
        r"""

        Parameters
        ----------
        Chamfer: TopoDS_Edge

        Return
        -------
        TopoDS_Vertex

        Description
        -----------
        Removes the chamfer <chamfer> and returns the vertex connecting the two adjacent edges to this chamfer.

        """
        return _ChFi2d.ChFi2d_Builder_RemoveChamfer(self, *args)

    def RemoveFillet(self, *args):
        r"""

        Parameters
        ----------
        Fillet: TopoDS_Edge

        Return
        -------
        TopoDS_Vertex

        Description
        -----------
        Removes the fillet <fillet> and returns the vertex connecting the two adjacent edges to this fillet.

        """
        return _ChFi2d.ChFi2d_Builder_RemoveFillet(self, *args)

    def Result(self, *args):
        r"""
        Return
        -------
        TopoDS_Face

        Description
        -----------
        Returns the modified face.

        """
        return _ChFi2d.ChFi2d_Builder_Result(self, *args)

    def Status(self, *args):
        r"""
        Return
        -------
        ChFi2d_ConstructionError

        Description
        -----------
        No available documentation.

        """
        return _ChFi2d.ChFi2d_Builder_Status(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _ChFi2d.delete_ChFi2d_Builder

# Register ChFi2d_Builder in _ChFi2d:
_ChFi2d.ChFi2d_Builder_swigregister(ChFi2d_Builder)
class ChFi2d_ChamferAPI(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        Return
        -------
        None

        Description
        -----------
        An empty constructor.

        Parameters
        ----------
        theWire: TopoDS_Wire

        Return
        -------
        None

        Description
        -----------
        A constructor accepting a wire consisting of two linear edges.

        Parameters
        ----------
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge

        Return
        -------
        None

        Description
        -----------
        A constructor accepting two linear edges.

        """
        _ChFi2d.ChFi2d_ChamferAPI_swiginit(self, _ChFi2d.new_ChFi2d_ChamferAPI(*args))

    def Init(self, *args):
        r"""

        Parameters
        ----------
        theWire: TopoDS_Wire

        Return
        -------
        None

        Description
        -----------
        Initializes the class by a wire consisting of two libear edges.

        Parameters
        ----------
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge

        Return
        -------
        None

        Description
        -----------
        Initializes the class by two linear edges.

        """
        return _ChFi2d.ChFi2d_ChamferAPI_Init(self, *args)

    def Perform(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        Constructs a chamfer edge. returns true if the edge is constructed.

        """
        return _ChFi2d.ChFi2d_ChamferAPI_Perform(self, *args)

    def Result(self, *args):
        r"""

        Parameters
        ----------
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge
        theLength1: float
        theLength2: float

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        No available documentation.

        """
        return _ChFi2d.ChFi2d_ChamferAPI_Result(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _ChFi2d.delete_ChFi2d_ChamferAPI

# Register ChFi2d_ChamferAPI in _ChFi2d:
_ChFi2d.ChFi2d_ChamferAPI_swigregister(ChFi2d_ChamferAPI)
class ChFi2d_FilletAPI(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        Return
        -------
        None

        Description
        -----------
        An empty constructor of the fillet algorithm. call a method init() to initialize the algorithm before calling of a perform() method.

        Parameters
        ----------
        theWire: TopoDS_Wire
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        A constructor of a fillet algorithm: accepts a wire consisting of two edges in a plane.

        Parameters
        ----------
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        A constructor of a fillet algorithm: accepts two edges in a plane.

        """
        _ChFi2d.ChFi2d_FilletAPI_swiginit(self, _ChFi2d.new_ChFi2d_FilletAPI(*args))

    def Init(self, *args):
        r"""

        Parameters
        ----------
        theWire: TopoDS_Wire
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        Initializes a fillet algorithm: accepts a wire consisting of two edges in a plane.

        Parameters
        ----------
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        Initializes a fillet algorithm: accepts two edges in a plane.

        """
        return _ChFi2d.ChFi2d_FilletAPI_Init(self, *args)

    def NbResults(self, *args):
        r"""

        Parameters
        ----------
        thePoint: gp_Pnt

        Return
        -------
        int

        Description
        -----------
        Returns number of possible solutions. <thepoint> chooses a particular fillet in case of several fillets may be constructed (for example, a circle intersecting a segment in 2 points). put the intersecting (or common) point of the edges.

        """
        return _ChFi2d.ChFi2d_FilletAPI_NbResults(self, *args)

    def Perform(self, *args):
        r"""

        Parameters
        ----------
        theRadius: float

        Return
        -------
        bool

        Description
        -----------
        Constructs a fillet edge. returns true if at least one result was found.

        """
        return _ChFi2d.ChFi2d_FilletAPI_Perform(self, *args)

    def Result(self, *args):
        r"""

        Parameters
        ----------
        thePoint: gp_Pnt
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge
        iSolution: int (optional, default to -1)

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Returns result (fillet edge, modified edge1, modified edge2), nearest to the given point <thepoint> if isolution == -1 <thepoint> chooses a particular fillet in case of several fillets may be constructed (for example, a circle intersecting a segment in 2 points). put the intersecting (or common) point of the edges.

        """
        return _ChFi2d.ChFi2d_FilletAPI_Result(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _ChFi2d.delete_ChFi2d_FilletAPI

# Register ChFi2d_FilletAPI in _ChFi2d:
_ChFi2d.ChFi2d_FilletAPI_swigregister(ChFi2d_FilletAPI)
class ChFi2d_FilletAlgo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        Return
        -------
        None

        Description
        -----------
        An empty constructor of the fillet algorithm. call a method init() to initialize the algorithm before calling of a perform() method.

        Parameters
        ----------
        theWire: TopoDS_Wire
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        A constructor of a fillet algorithm: accepts a wire consisting of two edges in a plane.

        Parameters
        ----------
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        A constructor of a fillet algorithm: accepts two edges in a plane.

        """
        _ChFi2d.ChFi2d_FilletAlgo_swiginit(self, _ChFi2d.new_ChFi2d_FilletAlgo(*args))

    def Init(self, *args):
        r"""

        Parameters
        ----------
        theWire: TopoDS_Wire
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        Initializes a fillet algorithm: accepts a wire consisting of two edges in a plane.

        Parameters
        ----------
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge
        thePlane: gp_Pln

        Return
        -------
        None

        Description
        -----------
        Initializes a fillet algorithm: accepts two edges in a plane.

        """
        return _ChFi2d.ChFi2d_FilletAlgo_Init(self, *args)

    def NbResults(self, *args):
        r"""

        Parameters
        ----------
        thePoint: gp_Pnt

        Return
        -------
        int

        Description
        -----------
        Returns number of possible solutions. <thepoint> chooses a particular fillet in case of several fillets may be constructed (for example, a circle intersecting a segment in 2 points). put the intersecting (or common) point of the edges.

        """
        return _ChFi2d.ChFi2d_FilletAlgo_NbResults(self, *args)

    def Perform(self, *args):
        r"""

        Parameters
        ----------
        theRadius: float

        Return
        -------
        bool

        Description
        -----------
        Constructs a fillet edge. returns true, if at least one result was found.

        """
        return _ChFi2d.ChFi2d_FilletAlgo_Perform(self, *args)

    def Result(self, *args):
        r"""

        Parameters
        ----------
        thePoint: gp_Pnt
        theEdge1: TopoDS_Edge
        theEdge2: TopoDS_Edge
        iSolution: int (optional, default to -1)

        Return
        -------
        TopoDS_Edge

        Description
        -----------
        Returns result (fillet edge, modified edge1, modified edge2), nearest to the given point <thepoint> if isolution == -1. <thepoint> chooses a particular fillet in case of several fillets may be constructed (for example, a circle intersecting a segment in 2 points). put the intersecting (or common) point of the edges.

        """
        return _ChFi2d.ChFi2d_FilletAlgo_Result(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _ChFi2d.delete_ChFi2d_FilletAlgo

# Register ChFi2d_FilletAlgo in _ChFi2d:
_ChFi2d.ChFi2d_FilletAlgo_swigregister(ChFi2d_FilletAlgo)



@deprecated
def chfi2d_CommonVertex(*args):
	return chfi2d.CommonVertex(*args)

@deprecated
def chfi2d_FindConnectedEdges(*args):
	return chfi2d.FindConnectedEdges(*args)



