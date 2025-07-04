# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

"""
Intrv module, see official documentation at
https://dev.opencascade.org/doc/occt-7.8.0/refman/html/package_intrv.html
"""

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Intrv
else:
    import _Intrv

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
    __swig_destroy__ = _Intrv.delete_SwigPyIterator

    def value(self):
        return _Intrv.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _Intrv.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _Intrv.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _Intrv.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _Intrv.SwigPyIterator_equal(self, x)

    def copy(self):
        return _Intrv.SwigPyIterator_copy(self)

    def next(self):
        return _Intrv.SwigPyIterator_next(self)

    def __next__(self):
        return _Intrv.SwigPyIterator___next__(self)

    def previous(self):
        return _Intrv.SwigPyIterator_previous(self)

    def advance(self, n):
        return _Intrv.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _Intrv.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _Intrv.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _Intrv.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _Intrv.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _Intrv.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _Intrv.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Intrv:
_Intrv.SwigPyIterator_swigregister(SwigPyIterator)

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
    return _Intrv.process_exception(error, method_name, class_name)

import warnings
from odoo.addons.OCC.Wrapper.wrapper_utils import Proxy, deprecated

class ios_base(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    erase_event = _Intrv.ios_base_erase_event
    imbue_event = _Intrv.ios_base_imbue_event
    copyfmt_event = _Intrv.ios_base_copyfmt_event

    def register_callback(self, __fn, __index):
        return _Intrv.ios_base_register_callback(self, __fn, __index)

    def flags(self, *args):
        return _Intrv.ios_base_flags(self, *args)

    def setf(self, *args):
        return _Intrv.ios_base_setf(self, *args)

    def unsetf(self, __mask):
        return _Intrv.ios_base_unsetf(self, __mask)

    def precision(self, *args):
        return _Intrv.ios_base_precision(self, *args)

    def width(self, *args):
        return _Intrv.ios_base_width(self, *args)

    @staticmethod
    def sync_with_stdio(__sync=True):
        return _Intrv.ios_base_sync_with_stdio(__sync)

    def imbue(self, __loc):
        return _Intrv.ios_base_imbue(self, __loc)

    def getloc(self):
        return _Intrv.ios_base_getloc(self)

    @staticmethod
    def xalloc():
        return _Intrv.ios_base_xalloc()

    def iword(self, __ix):
        return _Intrv.ios_base_iword(self, __ix)

    def pword(self, __ix):
        return _Intrv.ios_base_pword(self, __ix)
    __swig_destroy__ = _Intrv.delete_ios_base

# Register ios_base in _Intrv:
_Intrv.ios_base_swigregister(ios_base)
cvar = _Intrv.cvar
ios_base.boolalpha = _Intrv.cvar.ios_base_boolalpha
ios_base.dec = _Intrv.cvar.ios_base_dec
ios_base.fixed = _Intrv.cvar.ios_base_fixed
ios_base.hex = _Intrv.cvar.ios_base_hex
ios_base.internal = _Intrv.cvar.ios_base_internal
ios_base.left = _Intrv.cvar.ios_base_left
ios_base.oct = _Intrv.cvar.ios_base_oct
ios_base.right = _Intrv.cvar.ios_base_right
ios_base.scientific = _Intrv.cvar.ios_base_scientific
ios_base.showbase = _Intrv.cvar.ios_base_showbase
ios_base.showpoint = _Intrv.cvar.ios_base_showpoint
ios_base.showpos = _Intrv.cvar.ios_base_showpos
ios_base.skipws = _Intrv.cvar.ios_base_skipws
ios_base.unitbuf = _Intrv.cvar.ios_base_unitbuf
ios_base.uppercase = _Intrv.cvar.ios_base_uppercase
ios_base.adjustfield = _Intrv.cvar.ios_base_adjustfield
ios_base.basefield = _Intrv.cvar.ios_base_basefield
ios_base.floatfield = _Intrv.cvar.ios_base_floatfield
ios_base.badbit = _Intrv.cvar.ios_base_badbit
ios_base.eofbit = _Intrv.cvar.ios_base_eofbit
ios_base.failbit = _Intrv.cvar.ios_base_failbit
ios_base.goodbit = _Intrv.cvar.ios_base_goodbit
ios_base.app = _Intrv.cvar.ios_base_app
ios_base.ate = _Intrv.cvar.ios_base_ate
ios_base.binary = _Intrv.cvar.ios_base_binary
ios_base.ios_base_in = _Intrv.cvar.ios_base_ios_base_in
ios_base.out = _Intrv.cvar.ios_base_out
ios_base.trunc = _Intrv.cvar.ios_base_trunc
ios_base.beg = _Intrv.cvar.ios_base_beg
ios_base.cur = _Intrv.cvar.ios_base_cur
ios_base.end = _Intrv.cvar.ios_base_end

class ios(ios_base):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def rdstate(self):
        return _Intrv.ios_rdstate(self)

    def clear(self, *args):
        return _Intrv.ios_clear(self, *args)

    def setstate(self, __state):
        return _Intrv.ios_setstate(self, __state)

    def good(self):
        return _Intrv.ios_good(self)

    def eof(self):
        return _Intrv.ios_eof(self)

    def fail(self):
        return _Intrv.ios_fail(self)

    def bad(self):
        return _Intrv.ios_bad(self)

    def exceptions(self, *args):
        return _Intrv.ios_exceptions(self, *args)

    def __init__(self, __sb):
        _Intrv.ios_swiginit(self, _Intrv.new_ios(__sb))
    __swig_destroy__ = _Intrv.delete_ios

    def tie(self, *args):
        return _Intrv.ios_tie(self, *args)

    def rdbuf(self, *args):
        return _Intrv.ios_rdbuf(self, *args)

    def copyfmt(self, __rhs):
        return _Intrv.ios_copyfmt(self, __rhs)

    def fill(self, *args):
        return _Intrv.ios_fill(self, *args)

    def imbue(self, __loc):
        return _Intrv.ios_imbue(self, __loc)

    def narrow(self, __c, __dfault):
        return _Intrv.ios_narrow(self, __c, __dfault)

    def widen(self, __c):
        return _Intrv.ios_widen(self, __c)

# Register ios in _Intrv:
_Intrv.ios_swigregister(ios)
class ostream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _Intrv.ostream_swiginit(self, _Intrv.new_ostream(__sb))
    __swig_destroy__ = _Intrv.delete_ostream

    def __lshift__(self, *args):
        return _Intrv.ostream___lshift__(self, *args)

    def put(self, __c):
        return _Intrv.ostream_put(self, __c)

    def write(self, __s, __n):
        return _Intrv.ostream_write(self, __s, __n)

    def flush(self):
        return _Intrv.ostream_flush(self)

    def tellp(self):
        return _Intrv.ostream_tellp(self)

    def seekp(self, *args):
        return _Intrv.ostream_seekp(self, *args)

# Register ostream in _Intrv:
_Intrv.ostream_swigregister(ostream)
class istream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _Intrv.istream_swiginit(self, _Intrv.new_istream(__sb))
    __swig_destroy__ = _Intrv.delete_istream

    def __rshift__(self, *args):
        return _Intrv.istream___rshift__(self, *args)

    def gcount(self):
        return _Intrv.istream_gcount(self)

    def get(self, *args):
        return _Intrv.istream_get(self, *args)

    def getline(self, *args):
        return _Intrv.istream_getline(self, *args)

    def ignore(self, *args):
        return _Intrv.istream_ignore(self, *args)

    def peek(self):
        return _Intrv.istream_peek(self)

    def read(self, __s, __n):
        return _Intrv.istream_read(self, __s, __n)

    def readsome(self, __s, __n):
        return _Intrv.istream_readsome(self, __s, __n)

    def putback(self, __c):
        return _Intrv.istream_putback(self, __c)

    def unget(self):
        return _Intrv.istream_unget(self)

    def sync(self):
        return _Intrv.istream_sync(self)

    def tellg(self):
        return _Intrv.istream_tellg(self)

    def seekg(self, *args):
        return _Intrv.istream_seekg(self, *args)

# Register istream in _Intrv:
_Intrv.istream_swigregister(istream)
class iostream(istream, ostream):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _Intrv.iostream_swiginit(self, _Intrv.new_iostream(__sb))
    __swig_destroy__ = _Intrv.delete_iostream

# Register iostream in _Intrv:
_Intrv.iostream_swigregister(iostream)
cin = cvar.cin
cout = cvar.cout
cerr = cvar.cerr
clog = cvar.clog

endl_cb_ptr = _Intrv.endl_cb_ptr
endl = _Intrv.endl
ends_cb_ptr = _Intrv.ends_cb_ptr
ends = _Intrv.ends
flush_cb_ptr = _Intrv.flush_cb_ptr
flush = _Intrv.flush
import odoo.addons.OCC.Core.Standard
import odoo.addons.OCC.Core.NCollection

from enum import IntEnum
from odoo.addons.OCC.Core.Exception import *

Intrv_Before = _Intrv.Intrv_Before
Intrv_JustBefore = _Intrv.Intrv_JustBefore
Intrv_OverlappingAtStart = _Intrv.Intrv_OverlappingAtStart
Intrv_JustEnclosingAtEnd = _Intrv.Intrv_JustEnclosingAtEnd
Intrv_Enclosing = _Intrv.Intrv_Enclosing
Intrv_JustOverlappingAtStart = _Intrv.Intrv_JustOverlappingAtStart
Intrv_Similar = _Intrv.Intrv_Similar
Intrv_JustEnclosingAtStart = _Intrv.Intrv_JustEnclosingAtStart
Intrv_Inside = _Intrv.Intrv_Inside
Intrv_JustOverlappingAtEnd = _Intrv.Intrv_JustOverlappingAtEnd
Intrv_OverlappingAtEnd = _Intrv.Intrv_OverlappingAtEnd
Intrv_JustAfter = _Intrv.Intrv_JustAfter
Intrv_After = _Intrv.Intrv_After


class Intrv_Position(IntEnum):
	Intrv_Before = 0
	Intrv_JustBefore = 1
	Intrv_OverlappingAtStart = 2
	Intrv_JustEnclosingAtEnd = 3
	Intrv_Enclosing = 4
	Intrv_JustOverlappingAtStart = 5
	Intrv_Similar = 6
	Intrv_JustEnclosingAtStart = 7
	Intrv_Inside = 8
	Intrv_JustOverlappingAtEnd = 9
	Intrv_OverlappingAtEnd = 10
	Intrv_JustAfter = 11
	Intrv_After = 12
Intrv_Before = Intrv_Position.Intrv_Before
Intrv_JustBefore = Intrv_Position.Intrv_JustBefore
Intrv_OverlappingAtStart = Intrv_Position.Intrv_OverlappingAtStart
Intrv_JustEnclosingAtEnd = Intrv_Position.Intrv_JustEnclosingAtEnd
Intrv_Enclosing = Intrv_Position.Intrv_Enclosing
Intrv_JustOverlappingAtStart = Intrv_Position.Intrv_JustOverlappingAtStart
Intrv_Similar = Intrv_Position.Intrv_Similar
Intrv_JustEnclosingAtStart = Intrv_Position.Intrv_JustEnclosingAtStart
Intrv_Inside = Intrv_Position.Intrv_Inside
Intrv_JustOverlappingAtEnd = Intrv_Position.Intrv_JustOverlappingAtEnd
Intrv_OverlappingAtEnd = Intrv_Position.Intrv_OverlappingAtEnd
Intrv_JustAfter = Intrv_Position.Intrv_JustAfter
Intrv_After = Intrv_Position.Intrv_After

class Intrv_SequenceOfInterval(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def begin(self):
        return _Intrv.Intrv_SequenceOfInterval_begin(self)

    def end(self):
        return _Intrv.Intrv_SequenceOfInterval_end(self)

    def cbegin(self):
        return _Intrv.Intrv_SequenceOfInterval_cbegin(self)

    def cend(self):
        return _Intrv.Intrv_SequenceOfInterval_cend(self)

    def __init__(self, *args):
        _Intrv.Intrv_SequenceOfInterval_swiginit(self, _Intrv.new_Intrv_SequenceOfInterval(*args))

    def Size(self):
        return _Intrv.Intrv_SequenceOfInterval_Size(self)

    def Length(self):
        return _Intrv.Intrv_SequenceOfInterval_Length(self)

    def Lower(self):
        return _Intrv.Intrv_SequenceOfInterval_Lower(self)

    def Upper(self):
        return _Intrv.Intrv_SequenceOfInterval_Upper(self)

    def IsEmpty(self):
        return _Intrv.Intrv_SequenceOfInterval_IsEmpty(self)

    def Reverse(self):
        return _Intrv.Intrv_SequenceOfInterval_Reverse(self)

    def Exchange(self, I, J):
        return _Intrv.Intrv_SequenceOfInterval_Exchange(self, I, J)

    @staticmethod
    def delNode(theNode, theAl):
        return _Intrv.Intrv_SequenceOfInterval_delNode(theNode, theAl)

    def Clear(self, theAllocator=0):
        return _Intrv.Intrv_SequenceOfInterval_Clear(self, theAllocator)

    def Assign(self, theOther):
        return _Intrv.Intrv_SequenceOfInterval_Assign(self, theOther)

    def Set(self, *args):
        return _Intrv.Intrv_SequenceOfInterval_Set(self, *args)

    def Remove(self, *args):
        return _Intrv.Intrv_SequenceOfInterval_Remove(self, *args)

    def Append(self, *args):
        return _Intrv.Intrv_SequenceOfInterval_Append(self, *args)

    def Prepend(self, *args):
        return _Intrv.Intrv_SequenceOfInterval_Prepend(self, *args)

    def InsertBefore(self, *args):
        return _Intrv.Intrv_SequenceOfInterval_InsertBefore(self, *args)

    def InsertAfter(self, *args):
        return _Intrv.Intrv_SequenceOfInterval_InsertAfter(self, *args)

    def Split(self, theIndex, theSeq):
        return _Intrv.Intrv_SequenceOfInterval_Split(self, theIndex, theSeq)

    def First(self):
        return _Intrv.Intrv_SequenceOfInterval_First(self)

    def ChangeFirst(self):
        return _Intrv.Intrv_SequenceOfInterval_ChangeFirst(self)

    def Last(self):
        return _Intrv.Intrv_SequenceOfInterval_Last(self)

    def ChangeLast(self):
        return _Intrv.Intrv_SequenceOfInterval_ChangeLast(self)

    def Value(self, theIndex):
        return _Intrv.Intrv_SequenceOfInterval_Value(self, theIndex)

    def ChangeValue(self, theIndex):
        return _Intrv.Intrv_SequenceOfInterval_ChangeValue(self, theIndex)

    def __call__(self, *args):
        return _Intrv.Intrv_SequenceOfInterval___call__(self, *args)

    def SetValue(self, theIndex, theItem):
        return _Intrv.Intrv_SequenceOfInterval_SetValue(self, theIndex, theItem)
    __swig_destroy__ = _Intrv.delete_Intrv_SequenceOfInterval

    def __len__(self):
        return self.Size()


# Register Intrv_SequenceOfInterval in _Intrv:
_Intrv.Intrv_SequenceOfInterval_swigregister(Intrv_SequenceOfInterval)
class Intrv_Interval(object):
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
        Start: float
        End: float

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        Parameters
        ----------
        Start: float
        TolStart: float
        End: float
        TolEnd: float

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        _Intrv.Intrv_Interval_swiginit(self, _Intrv.new_Intrv_Interval(*args))

    def Bounds(self, *args):
        r"""

        Parameters
        ----------

        Return
        -------
        Start: float
        TolStart: float
        End: float
        TolEnd: float

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Interval_Bounds(self, *args)

    def CutAtEnd(self, *args):
        r"""

        Parameters
        ----------
        End: float
        TolEnd: float

        Return
        -------
        None

        Description
        -----------
        <-----****+****  old one **+**------> tool for cutting <<< <<< <-----****+****  result.

        """
        return _Intrv.Intrv_Interval_CutAtEnd(self, *args)

    def CutAtStart(self, *args):
        r"""

        Parameters
        ----------
        Start: float
        TolStart: float

        Return
        -------
        None

        Description
        -----------
        ****+****-----------> old one <----------**+** tool for cutting >>> >>> ****+****-----------> result.

        """
        return _Intrv.Intrv_Interval_CutAtStart(self, *args)

    def End(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Interval_End(self, *args)

    def FuseAtEnd(self, *args):
        r"""

        Parameters
        ----------
        End: float
        TolEnd: float

        Return
        -------
        None

        Description
        -----------
        <---------------------****+**** old one <-----------------**+**  new one to fuse >>> >>> <---------------------****+**** result.

        """
        return _Intrv.Intrv_Interval_FuseAtEnd(self, *args)

    def FuseAtStart(self, *args):
        r"""

        Parameters
        ----------
        Start: float
        TolStart: float

        Return
        -------
        None

        Description
        -----------
        ****+****--------------------> old one ****+****------------------------> new one to fuse <<< <<< ****+****------------------------> result.

        """
        return _Intrv.Intrv_Interval_FuseAtStart(self, *args)

    def IsAfter(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is after other **-----------**** me ***----------------**  other.

        """
        return _Intrv.Intrv_Interval_IsAfter(self, *args)

    def IsBefore(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is before other ***----------------**  me **-----------**** other.

        """
        return _Intrv.Intrv_Interval_IsBefore(self, *args)

    def IsEnclosing(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is enclosing other ***----------------------------**** me ***------------------** other.

        """
        return _Intrv.Intrv_Interval_IsEnclosing(self, *args)

    def IsInside(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is inside other **-----------****  me ***--------------------------**  other.

        """
        return _Intrv.Intrv_Interval_IsInside(self, *args)

    def IsJustAfter(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is just after other ****-------****  me ***-----------**  other.

        """
        return _Intrv.Intrv_Interval_IsJustAfter(self, *args)

    def IsJustBefore(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is just before other ***--------****   me ***-----------** other.

        """
        return _Intrv.Intrv_Interval_IsJustBefore(self, *args)

    def IsJustEnclosingAtEnd(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is just enclosing other at end ***----------------------------**** me ***-----------------****  other.

        """
        return _Intrv.Intrv_Interval_IsJustEnclosingAtEnd(self, *args)

    def IsJustEnclosingAtStart(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is just enclosing other at start ***---------------------------**** me ***------------------** other.

        """
        return _Intrv.Intrv_Interval_IsJustEnclosingAtStart(self, *args)

    def IsJustOverlappingAtEnd(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is just overlapping other at end ***-----------*  me ***------------------------** other.

        """
        return _Intrv.Intrv_Interval_IsJustOverlappingAtEnd(self, *args)

    def IsJustOverlappingAtStart(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is just overlapping other at start ***-----------***  me ***------------------------** other.

        """
        return _Intrv.Intrv_Interval_IsJustOverlappingAtStart(self, *args)

    def IsOverlappingAtEnd(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is overlapping other at end ***-----------** me ***---------------***  other.

        """
        return _Intrv.Intrv_Interval_IsOverlappingAtEnd(self, *args)

    def IsOverlappingAtStart(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me is overlapping other at start ***---------------***  me ***-----------** other.

        """
        return _Intrv.Intrv_Interval_IsOverlappingAtStart(self, *args)

    def IsProbablyEmpty(self, *args):
        r"""
        Return
        -------
        bool

        Description
        -----------
        True if mystart+mytolstart > myend-mytolend or if myend+mytolend > mystart-mytolstart.

        """
        return _Intrv.Intrv_Interval_IsProbablyEmpty(self, *args)

    def IsSimilar(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        bool

        Description
        -----------
        True if me and other have the same bounds *----------------***  me ***-----------------**  other.

        """
        return _Intrv.Intrv_Interval_IsSimilar(self, *args)

    def Position(self, *args):
        r"""

        Parameters
        ----------
        Other: Intrv_Interval

        Return
        -------
        Intrv_Position

        Description
        -----------
        True if me is before other **-----------**** other ***-----*   before ***------------*  justbefore ***-----------------*  overlappingatstart ***--------------------------*  justenclosingatend ***-------------------------------------* enclosing ***----*  justoverlappingatstart ***-------------*  similar ***------------------------* justenclosingatstart ***-*  inside ***------*  justoverlappingatend ***-----------------* overlappingatend ***--------* justafter ***---* after.

        """
        return _Intrv.Intrv_Interval_Position(self, *args)

    def SetEnd(self, *args):
        r"""

        Parameters
        ----------
        End: float
        TolEnd: float

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Interval_SetEnd(self, *args)

    def SetStart(self, *args):
        r"""

        Parameters
        ----------
        Start: float
        TolStart: float

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Interval_SetStart(self, *args)

    def Start(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Interval_Start(self, *args)

    def TolEnd(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Interval_TolEnd(self, *args)

    def TolStart(self, *args):
        r"""
        Return
        -------
        float

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Interval_TolStart(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _Intrv.delete_Intrv_Interval

# Register Intrv_Interval in _Intrv:
_Intrv.Intrv_Interval_swigregister(Intrv_Interval)
class Intrv_Intervals(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        Return
        -------
        None

        Description
        -----------
        Creates a void sequence of intervals.

        Parameters
        ----------
        Int: Intrv_Interval

        Return
        -------
        None

        Description
        -----------
        Creates a sequence of one interval.

        """
        _Intrv.Intrv_Intervals_swiginit(self, _Intrv.new_Intrv_Intervals(*args))

    def Intersect(self, *args):
        r"""

        Parameters
        ----------
        Tool: Intrv_Interval

        Return
        -------
        None

        Description
        -----------
        Intersects the intervals with the interval <tool>.

        Parameters
        ----------
        Tool: Intrv_Intervals

        Return
        -------
        None

        Description
        -----------
        Intersects the intervals with the intervals in the sequence <tool>.

        """
        return _Intrv.Intrv_Intervals_Intersect(self, *args)

    def NbIntervals(self, *args):
        r"""
        Return
        -------
        int

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Intervals_NbIntervals(self, *args)

    def Subtract(self, *args):
        r"""

        Parameters
        ----------
        Tool: Intrv_Interval

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        Parameters
        ----------
        Tool: Intrv_Intervals

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Intervals_Subtract(self, *args)

    def Unite(self, *args):
        r"""

        Parameters
        ----------
        Tool: Intrv_Interval

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        Parameters
        ----------
        Tool: Intrv_Intervals

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Intervals_Unite(self, *args)

    def Value(self, *args):
        r"""

        Parameters
        ----------
        Index: int

        Return
        -------
        Intrv_Interval

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Intervals_Value(self, *args)

    def XUnite(self, *args):
        r"""

        Parameters
        ----------
        Tool: Intrv_Interval

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        Parameters
        ----------
        Tool: Intrv_Intervals

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        return _Intrv.Intrv_Intervals_XUnite(self, *args)

    __repr__ = _dumps_object

    __swig_destroy__ = _Intrv.delete_Intrv_Intervals

# Register Intrv_Intervals in _Intrv:
_Intrv.Intrv_Intervals_swigregister(Intrv_Intervals)



