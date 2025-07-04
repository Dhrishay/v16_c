# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

"""
Storage module, see official documentation at
https://dev.opencascade.org/doc/occt-7.8.0/refman/html/package_storage.html
"""

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Storage
else:
    import _Storage

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
    __swig_destroy__ = _Storage.delete_SwigPyIterator

    def value(self):
        return _Storage.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _Storage.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _Storage.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _Storage.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _Storage.SwigPyIterator_equal(self, x)

    def copy(self):
        return _Storage.SwigPyIterator_copy(self)

    def next(self):
        return _Storage.SwigPyIterator_next(self)

    def __next__(self):
        return _Storage.SwigPyIterator___next__(self)

    def previous(self):
        return _Storage.SwigPyIterator_previous(self)

    def advance(self, n):
        return _Storage.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _Storage.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _Storage.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _Storage.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _Storage.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _Storage.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _Storage.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Storage:
_Storage.SwigPyIterator_swigregister(SwigPyIterator)

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
    return _Storage.process_exception(error, method_name, class_name)

import warnings
from odoo.addons.OCC.Wrapper.wrapper_utils import Proxy, deprecated

class ios_base(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    erase_event = _Storage.ios_base_erase_event
    imbue_event = _Storage.ios_base_imbue_event
    copyfmt_event = _Storage.ios_base_copyfmt_event

    def register_callback(self, __fn, __index):
        return _Storage.ios_base_register_callback(self, __fn, __index)

    def flags(self, *args):
        return _Storage.ios_base_flags(self, *args)

    def setf(self, *args):
        return _Storage.ios_base_setf(self, *args)

    def unsetf(self, __mask):
        return _Storage.ios_base_unsetf(self, __mask)

    def precision(self, *args):
        return _Storage.ios_base_precision(self, *args)

    def width(self, *args):
        return _Storage.ios_base_width(self, *args)

    @staticmethod
    def sync_with_stdio(__sync=True):
        return _Storage.ios_base_sync_with_stdio(__sync)

    def imbue(self, __loc):
        return _Storage.ios_base_imbue(self, __loc)

    def getloc(self):
        return _Storage.ios_base_getloc(self)

    @staticmethod
    def xalloc():
        return _Storage.ios_base_xalloc()

    def iword(self, __ix):
        return _Storage.ios_base_iword(self, __ix)

    def pword(self, __ix):
        return _Storage.ios_base_pword(self, __ix)
    __swig_destroy__ = _Storage.delete_ios_base

# Register ios_base in _Storage:
_Storage.ios_base_swigregister(ios_base)
cvar = _Storage.cvar
ios_base.boolalpha = _Storage.cvar.ios_base_boolalpha
ios_base.dec = _Storage.cvar.ios_base_dec
ios_base.fixed = _Storage.cvar.ios_base_fixed
ios_base.hex = _Storage.cvar.ios_base_hex
ios_base.internal = _Storage.cvar.ios_base_internal
ios_base.left = _Storage.cvar.ios_base_left
ios_base.oct = _Storage.cvar.ios_base_oct
ios_base.right = _Storage.cvar.ios_base_right
ios_base.scientific = _Storage.cvar.ios_base_scientific
ios_base.showbase = _Storage.cvar.ios_base_showbase
ios_base.showpoint = _Storage.cvar.ios_base_showpoint
ios_base.showpos = _Storage.cvar.ios_base_showpos
ios_base.skipws = _Storage.cvar.ios_base_skipws
ios_base.unitbuf = _Storage.cvar.ios_base_unitbuf
ios_base.uppercase = _Storage.cvar.ios_base_uppercase
ios_base.adjustfield = _Storage.cvar.ios_base_adjustfield
ios_base.basefield = _Storage.cvar.ios_base_basefield
ios_base.floatfield = _Storage.cvar.ios_base_floatfield
ios_base.badbit = _Storage.cvar.ios_base_badbit
ios_base.eofbit = _Storage.cvar.ios_base_eofbit
ios_base.failbit = _Storage.cvar.ios_base_failbit
ios_base.goodbit = _Storage.cvar.ios_base_goodbit
ios_base.app = _Storage.cvar.ios_base_app
ios_base.ate = _Storage.cvar.ios_base_ate
ios_base.binary = _Storage.cvar.ios_base_binary
ios_base.ios_base_in = _Storage.cvar.ios_base_ios_base_in
ios_base.out = _Storage.cvar.ios_base_out
ios_base.trunc = _Storage.cvar.ios_base_trunc
ios_base.beg = _Storage.cvar.ios_base_beg
ios_base.cur = _Storage.cvar.ios_base_cur
ios_base.end = _Storage.cvar.ios_base_end

class ios(ios_base):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def rdstate(self):
        return _Storage.ios_rdstate(self)

    def clear(self, *args):
        return _Storage.ios_clear(self, *args)

    def setstate(self, __state):
        return _Storage.ios_setstate(self, __state)

    def good(self):
        return _Storage.ios_good(self)

    def eof(self):
        return _Storage.ios_eof(self)

    def fail(self):
        return _Storage.ios_fail(self)

    def bad(self):
        return _Storage.ios_bad(self)

    def exceptions(self, *args):
        return _Storage.ios_exceptions(self, *args)

    def __init__(self, __sb):
        _Storage.ios_swiginit(self, _Storage.new_ios(__sb))
    __swig_destroy__ = _Storage.delete_ios

    def tie(self, *args):
        return _Storage.ios_tie(self, *args)

    def rdbuf(self, *args):
        return _Storage.ios_rdbuf(self, *args)

    def copyfmt(self, __rhs):
        return _Storage.ios_copyfmt(self, __rhs)

    def fill(self, *args):
        return _Storage.ios_fill(self, *args)

    def imbue(self, __loc):
        return _Storage.ios_imbue(self, __loc)

    def narrow(self, __c, __dfault):
        return _Storage.ios_narrow(self, __c, __dfault)

    def widen(self, __c):
        return _Storage.ios_widen(self, __c)

# Register ios in _Storage:
_Storage.ios_swigregister(ios)
class ostream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _Storage.ostream_swiginit(self, _Storage.new_ostream(__sb))
    __swig_destroy__ = _Storage.delete_ostream

    def __lshift__(self, *args):
        return _Storage.ostream___lshift__(self, *args)

    def put(self, __c):
        return _Storage.ostream_put(self, __c)

    def write(self, __s, __n):
        return _Storage.ostream_write(self, __s, __n)

    def flush(self):
        return _Storage.ostream_flush(self)

    def tellp(self):
        return _Storage.ostream_tellp(self)

    def seekp(self, *args):
        return _Storage.ostream_seekp(self, *args)

# Register ostream in _Storage:
_Storage.ostream_swigregister(ostream)
class istream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _Storage.istream_swiginit(self, _Storage.new_istream(__sb))
    __swig_destroy__ = _Storage.delete_istream

    def __rshift__(self, *args):
        return _Storage.istream___rshift__(self, *args)

    def gcount(self):
        return _Storage.istream_gcount(self)

    def get(self, *args):
        return _Storage.istream_get(self, *args)

    def getline(self, *args):
        return _Storage.istream_getline(self, *args)

    def ignore(self, *args):
        return _Storage.istream_ignore(self, *args)

    def peek(self):
        return _Storage.istream_peek(self)

    def read(self, __s, __n):
        return _Storage.istream_read(self, __s, __n)

    def readsome(self, __s, __n):
        return _Storage.istream_readsome(self, __s, __n)

    def putback(self, __c):
        return _Storage.istream_putback(self, __c)

    def unget(self):
        return _Storage.istream_unget(self)

    def sync(self):
        return _Storage.istream_sync(self)

    def tellg(self):
        return _Storage.istream_tellg(self)

    def seekg(self, *args):
        return _Storage.istream_seekg(self, *args)

# Register istream in _Storage:
_Storage.istream_swigregister(istream)
class iostream(istream, ostream):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _Storage.iostream_swiginit(self, _Storage.new_iostream(__sb))
    __swig_destroy__ = _Storage.delete_iostream

# Register iostream in _Storage:
_Storage.iostream_swigregister(iostream)
cin = cvar.cin
cout = cvar.cout
cerr = cvar.cerr
clog = cvar.clog

endl_cb_ptr = _Storage.endl_cb_ptr
endl = _Storage.endl
ends_cb_ptr = _Storage.ends_cb_ptr
ends = _Storage.ends
flush_cb_ptr = _Storage.flush_cb_ptr
flush = _Storage.flush
import odoo.addons.OCC.Core.Standard
import odoo.addons.OCC.Core.NCollection

from enum import IntEnum
from odoo.addons.OCC.Core.Exception import *

Storage_VSOk = _Storage.Storage_VSOk
Storage_VSOpenError = _Storage.Storage_VSOpenError
Storage_VSModeError = _Storage.Storage_VSModeError
Storage_VSCloseError = _Storage.Storage_VSCloseError
Storage_VSAlreadyOpen = _Storage.Storage_VSAlreadyOpen
Storage_VSNotOpen = _Storage.Storage_VSNotOpen
Storage_VSSectionNotFound = _Storage.Storage_VSSectionNotFound
Storage_VSWriteError = _Storage.Storage_VSWriteError
Storage_VSFormatError = _Storage.Storage_VSFormatError
Storage_VSUnknownType = _Storage.Storage_VSUnknownType
Storage_VSTypeMismatch = _Storage.Storage_VSTypeMismatch
Storage_VSInternalError = _Storage.Storage_VSInternalError
Storage_VSExtCharParityError = _Storage.Storage_VSExtCharParityError
Storage_VSWrongFileDriver = _Storage.Storage_VSWrongFileDriver
Storage_VSNone = _Storage.Storage_VSNone
Storage_VSRead = _Storage.Storage_VSRead
Storage_VSWrite = _Storage.Storage_VSWrite
Storage_VSReadWrite = _Storage.Storage_VSReadWrite
Storage_AddSolve = _Storage.Storage_AddSolve
Storage_WriteSolve = _Storage.Storage_WriteSolve
Storage_ReadSolve = _Storage.Storage_ReadSolve


class Storage_Error(IntEnum):
	Storage_VSOk = 0
	Storage_VSOpenError = 1
	Storage_VSModeError = 2
	Storage_VSCloseError = 3
	Storage_VSAlreadyOpen = 4
	Storage_VSNotOpen = 5
	Storage_VSSectionNotFound = 6
	Storage_VSWriteError = 7
	Storage_VSFormatError = 8
	Storage_VSUnknownType = 9
	Storage_VSTypeMismatch = 10
	Storage_VSInternalError = 11
	Storage_VSExtCharParityError = 12
	Storage_VSWrongFileDriver = 13
Storage_VSOk = Storage_Error.Storage_VSOk
Storage_VSOpenError = Storage_Error.Storage_VSOpenError
Storage_VSModeError = Storage_Error.Storage_VSModeError
Storage_VSCloseError = Storage_Error.Storage_VSCloseError
Storage_VSAlreadyOpen = Storage_Error.Storage_VSAlreadyOpen
Storage_VSNotOpen = Storage_Error.Storage_VSNotOpen
Storage_VSSectionNotFound = Storage_Error.Storage_VSSectionNotFound
Storage_VSWriteError = Storage_Error.Storage_VSWriteError
Storage_VSFormatError = Storage_Error.Storage_VSFormatError
Storage_VSUnknownType = Storage_Error.Storage_VSUnknownType
Storage_VSTypeMismatch = Storage_Error.Storage_VSTypeMismatch
Storage_VSInternalError = Storage_Error.Storage_VSInternalError
Storage_VSExtCharParityError = Storage_Error.Storage_VSExtCharParityError
Storage_VSWrongFileDriver = Storage_Error.Storage_VSWrongFileDriver

class Storage_OpenMode(IntEnum):
	Storage_VSNone = 0
	Storage_VSRead = 1
	Storage_VSWrite = 2
	Storage_VSReadWrite = 3
Storage_VSNone = Storage_OpenMode.Storage_VSNone
Storage_VSRead = Storage_OpenMode.Storage_VSRead
Storage_VSWrite = Storage_OpenMode.Storage_VSWrite
Storage_VSReadWrite = Storage_OpenMode.Storage_VSReadWrite

class Storage_SolveMode(IntEnum):
	Storage_AddSolve = 0
	Storage_WriteSolve = 1
	Storage_ReadSolve = 2
Storage_AddSolve = Storage_SolveMode.Storage_AddSolve
Storage_WriteSolve = Storage_SolveMode.Storage_WriteSolve
Storage_ReadSolve = Storage_SolveMode.Storage_ReadSolve

class Storage_ArrayOfCallBack(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def begin(self, *args):
        return _Storage.Storage_ArrayOfCallBack_begin(self, *args)

    def cbegin(self):
        return _Storage.Storage_ArrayOfCallBack_cbegin(self)

    def end(self, *args):
        return _Storage.Storage_ArrayOfCallBack_end(self, *args)

    def cend(self):
        return _Storage.Storage_ArrayOfCallBack_cend(self)

    def __init__(self, *args):
        _Storage.Storage_ArrayOfCallBack_swiginit(self, _Storage.new_Storage_ArrayOfCallBack(*args))
    __swig_destroy__ = _Storage.delete_Storage_ArrayOfCallBack

    def Init(self, theValue):
        return _Storage.Storage_ArrayOfCallBack_Init(self, theValue)

    def Size(self):
        return _Storage.Storage_ArrayOfCallBack_Size(self)

    def Length(self):
        return _Storage.Storage_ArrayOfCallBack_Length(self)

    def IsEmpty(self):
        return _Storage.Storage_ArrayOfCallBack_IsEmpty(self)

    def Lower(self):
        return _Storage.Storage_ArrayOfCallBack_Lower(self)

    def Upper(self):
        return _Storage.Storage_ArrayOfCallBack_Upper(self)

    def Assign(self, theOther):
        return _Storage.Storage_ArrayOfCallBack_Assign(self, theOther)

    def Move(self, *args):
        return _Storage.Storage_ArrayOfCallBack_Move(self, *args)

    def Set(self, *args):
        return _Storage.Storage_ArrayOfCallBack_Set(self, *args)

    def First(self):
        return _Storage.Storage_ArrayOfCallBack_First(self)

    def ChangeFirst(self):
        return _Storage.Storage_ArrayOfCallBack_ChangeFirst(self)

    def Last(self):
        return _Storage.Storage_ArrayOfCallBack_Last(self)

    def ChangeLast(self):
        return _Storage.Storage_ArrayOfCallBack_ChangeLast(self)

    def Value(self, theIndex):
        return _Storage.Storage_ArrayOfCallBack_Value(self, theIndex)

    def ChangeValue(self, theIndex):
        return _Storage.Storage_ArrayOfCallBack_ChangeValue(self, theIndex)

    def __call__(self, *args):
        return _Storage.Storage_ArrayOfCallBack___call__(self, *args)

    def SetValue(self, *args):
        return _Storage.Storage_ArrayOfCallBack_SetValue(self, *args)

    def UpdateLowerBound(self, theLower):
        return _Storage.Storage_ArrayOfCallBack_UpdateLowerBound(self, theLower)

    def UpdateUpperBound(self, theUpper):
        return _Storage.Storage_ArrayOfCallBack_UpdateUpperBound(self, theUpper)

    def Resize(self, theLower, theUpper, theToCopyData):
        return _Storage.Storage_ArrayOfCallBack_Resize(self, theLower, theUpper, theToCopyData)

    def IsDeletable(self):
        return _Storage.Storage_ArrayOfCallBack_IsDeletable(self)

    def __getitem__(self, index):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            return self.Value(index + self.Lower())

    def __setitem__(self, index, value):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            self.SetValue(index + self.Lower(), value)

    def __len__(self):
        return self.Length()

    def __iter__(self):
        self.low = self.Lower()
        self.up = self.Upper()
        self.current = self.Lower() - 1
        return self

    def next(self):
        if self.current >= self.Upper():
            raise StopIteration
        else:
            self.current += 1
        return self.Value(self.current)

    __next__ = next


# Register Storage_ArrayOfCallBack in _Storage:
_Storage.Storage_ArrayOfCallBack_swigregister(Storage_ArrayOfCallBack)
class Storage_ArrayOfSchema(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def begin(self, *args):
        return _Storage.Storage_ArrayOfSchema_begin(self, *args)

    def cbegin(self):
        return _Storage.Storage_ArrayOfSchema_cbegin(self)

    def end(self, *args):
        return _Storage.Storage_ArrayOfSchema_end(self, *args)

    def cend(self):
        return _Storage.Storage_ArrayOfSchema_cend(self)

    def __init__(self, *args):
        _Storage.Storage_ArrayOfSchema_swiginit(self, _Storage.new_Storage_ArrayOfSchema(*args))
    __swig_destroy__ = _Storage.delete_Storage_ArrayOfSchema

    def Init(self, theValue):
        return _Storage.Storage_ArrayOfSchema_Init(self, theValue)

    def Size(self):
        return _Storage.Storage_ArrayOfSchema_Size(self)

    def Length(self):
        return _Storage.Storage_ArrayOfSchema_Length(self)

    def IsEmpty(self):
        return _Storage.Storage_ArrayOfSchema_IsEmpty(self)

    def Lower(self):
        return _Storage.Storage_ArrayOfSchema_Lower(self)

    def Upper(self):
        return _Storage.Storage_ArrayOfSchema_Upper(self)

    def Assign(self, theOther):
        return _Storage.Storage_ArrayOfSchema_Assign(self, theOther)

    def Move(self, *args):
        return _Storage.Storage_ArrayOfSchema_Move(self, *args)

    def Set(self, *args):
        return _Storage.Storage_ArrayOfSchema_Set(self, *args)

    def First(self):
        return _Storage.Storage_ArrayOfSchema_First(self)

    def ChangeFirst(self):
        return _Storage.Storage_ArrayOfSchema_ChangeFirst(self)

    def Last(self):
        return _Storage.Storage_ArrayOfSchema_Last(self)

    def ChangeLast(self):
        return _Storage.Storage_ArrayOfSchema_ChangeLast(self)

    def Value(self, theIndex):
        return _Storage.Storage_ArrayOfSchema_Value(self, theIndex)

    def ChangeValue(self, theIndex):
        return _Storage.Storage_ArrayOfSchema_ChangeValue(self, theIndex)

    def __call__(self, *args):
        return _Storage.Storage_ArrayOfSchema___call__(self, *args)

    def SetValue(self, *args):
        return _Storage.Storage_ArrayOfSchema_SetValue(self, *args)

    def UpdateLowerBound(self, theLower):
        return _Storage.Storage_ArrayOfSchema_UpdateLowerBound(self, theLower)

    def UpdateUpperBound(self, theUpper):
        return _Storage.Storage_ArrayOfSchema_UpdateUpperBound(self, theUpper)

    def Resize(self, theLower, theUpper, theToCopyData):
        return _Storage.Storage_ArrayOfSchema_Resize(self, theLower, theUpper, theToCopyData)

    def IsDeletable(self):
        return _Storage.Storage_ArrayOfSchema_IsDeletable(self)

    def __getitem__(self, index):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            return self.Value(index + self.Lower())

    def __setitem__(self, index, value):
        if index + self.Lower() > self.Upper():
            raise IndexError("index out of range")
        else:
            self.SetValue(index + self.Lower(), value)

    def __len__(self):
        return self.Length()

    def __iter__(self):
        self.low = self.Lower()
        self.up = self.Upper()
        self.current = self.Lower() - 1
        return self

    def next(self):
        if self.current >= self.Upper():
            raise StopIteration
        else:
            self.current += 1
        return self.Value(self.current)

    __next__ = next


# Register Storage_ArrayOfSchema in _Storage:
_Storage.Storage_ArrayOfSchema_swigregister(Storage_ArrayOfSchema)

from odoo.addons.OCC.Core.NCollection import NCollection_BaseMap

class Storage_MapOfCallBack(NCollection_BaseMap):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def begin(self):
        return _Storage.Storage_MapOfCallBack_begin(self)

    def end(self):
        return _Storage.Storage_MapOfCallBack_end(self)

    def cbegin(self):
        return _Storage.Storage_MapOfCallBack_cbegin(self)

    def cend(self):
        return _Storage.Storage_MapOfCallBack_cend(self)

    def __init__(self, *args):
        _Storage.Storage_MapOfCallBack_swiginit(self, _Storage.new_Storage_MapOfCallBack(*args))

    def Exchange(self, theOther):
        return _Storage.Storage_MapOfCallBack_Exchange(self, theOther)

    def Assign(self, theOther):
        return _Storage.Storage_MapOfCallBack_Assign(self, theOther)

    def Set(self, *args):
        return _Storage.Storage_MapOfCallBack_Set(self, *args)

    def ReSize(self, N):
        return _Storage.Storage_MapOfCallBack_ReSize(self, N)

    def Bind(self, *args):
        return _Storage.Storage_MapOfCallBack_Bind(self, *args)

    def Bound(self, *args):
        return _Storage.Storage_MapOfCallBack_Bound(self, *args)

    def IsBound(self, theKey):
        return _Storage.Storage_MapOfCallBack_IsBound(self, theKey)

    def UnBind(self, theKey):
        return _Storage.Storage_MapOfCallBack_UnBind(self, theKey)

    def Seek(self, theKey):
        return _Storage.Storage_MapOfCallBack_Seek(self, theKey)

    def Find(self, *args):
        return _Storage.Storage_MapOfCallBack_Find(self, *args)

    def ChangeSeek(self, theKey):
        return _Storage.Storage_MapOfCallBack_ChangeSeek(self, theKey)

    def ChangeFind(self, theKey):
        return _Storage.Storage_MapOfCallBack_ChangeFind(self, theKey)

    def __call__(self, *args):
        return _Storage.Storage_MapOfCallBack___call__(self, *args)

    def Clear(self, *args):
        return _Storage.Storage_MapOfCallBack_Clear(self, *args)
    __swig_destroy__ = _Storage.delete_Storage_MapOfCallBack

    def Size(self):
        return _Storage.Storage_MapOfCallBack_Size(self)

# Register Storage_MapOfCallBack in _Storage:
_Storage.Storage_MapOfCallBack_swigregister(Storage_MapOfCallBack)

from odoo.addons.OCC.Core.NCollection import NCollection_BaseMap

class Storage_MapOfPers(NCollection_BaseMap):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def begin(self):
        return _Storage.Storage_MapOfPers_begin(self)

    def end(self):
        return _Storage.Storage_MapOfPers_end(self)

    def cbegin(self):
        return _Storage.Storage_MapOfPers_cbegin(self)

    def cend(self):
        return _Storage.Storage_MapOfPers_cend(self)

    def __init__(self, *args):
        _Storage.Storage_MapOfPers_swiginit(self, _Storage.new_Storage_MapOfPers(*args))

    def Exchange(self, theOther):
        return _Storage.Storage_MapOfPers_Exchange(self, theOther)

    def Assign(self, theOther):
        return _Storage.Storage_MapOfPers_Assign(self, theOther)

    def Set(self, *args):
        return _Storage.Storage_MapOfPers_Set(self, *args)

    def ReSize(self, N):
        return _Storage.Storage_MapOfPers_ReSize(self, N)

    def Bind(self, *args):
        return _Storage.Storage_MapOfPers_Bind(self, *args)

    def Bound(self, *args):
        return _Storage.Storage_MapOfPers_Bound(self, *args)

    def IsBound(self, theKey):
        return _Storage.Storage_MapOfPers_IsBound(self, theKey)

    def UnBind(self, theKey):
        return _Storage.Storage_MapOfPers_UnBind(self, theKey)

    def Seek(self, theKey):
        return _Storage.Storage_MapOfPers_Seek(self, theKey)

    def Find(self, *args):
        return _Storage.Storage_MapOfPers_Find(self, *args)

    def ChangeSeek(self, theKey):
        return _Storage.Storage_MapOfPers_ChangeSeek(self, theKey)

    def ChangeFind(self, theKey):
        return _Storage.Storage_MapOfPers_ChangeFind(self, theKey)

    def __call__(self, *args):
        return _Storage.Storage_MapOfPers___call__(self, *args)

    def Clear(self, *args):
        return _Storage.Storage_MapOfPers_Clear(self, *args)
    __swig_destroy__ = _Storage.delete_Storage_MapOfPers

    def Size(self):
        return _Storage.Storage_MapOfPers_Size(self)

# Register Storage_MapOfPers in _Storage:
_Storage.Storage_MapOfPers_swigregister(Storage_MapOfPers)

from odoo.addons.OCC.Core.NCollection import NCollection_BaseMap

class Storage_PType(NCollection_BaseMap):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def begin(self):
        return _Storage.Storage_PType_begin(self)

    def end(self):
        return _Storage.Storage_PType_end(self)

    def cbegin(self):
        return _Storage.Storage_PType_cbegin(self)

    def cend(self):
        return _Storage.Storage_PType_cend(self)

    def __init__(self, *args):
        _Storage.Storage_PType_swiginit(self, _Storage.new_Storage_PType(*args))

    def Exchange(self, theOther):
        return _Storage.Storage_PType_Exchange(self, theOther)

    def Assign(self, theOther):
        return _Storage.Storage_PType_Assign(self, theOther)

    def Set(self, *args):
        return _Storage.Storage_PType_Set(self, *args)

    def ReSize(self, N):
        return _Storage.Storage_PType_ReSize(self, N)

    def Add(self, *args):
        return _Storage.Storage_PType_Add(self, *args)

    def Contains(self, theKey1):
        return _Storage.Storage_PType_Contains(self, theKey1)

    def Substitute(self, theIndex, theKey1, theItem):
        return _Storage.Storage_PType_Substitute(self, theIndex, theKey1, theItem)

    def Swap(self, theIndex1, theIndex2):
        return _Storage.Storage_PType_Swap(self, theIndex1, theIndex2)

    def RemoveLast(self):
        return _Storage.Storage_PType_RemoveLast(self)

    def RemoveFromIndex(self, theIndex):
        return _Storage.Storage_PType_RemoveFromIndex(self, theIndex)

    def RemoveKey(self, theKey1):
        return _Storage.Storage_PType_RemoveKey(self, theKey1)

    def FindKey(self, theIndex):
        return _Storage.Storage_PType_FindKey(self, theIndex)

    def FindFromIndex(self, theIndex):
        return _Storage.Storage_PType_FindFromIndex(self, theIndex)

    def ChangeFromIndex(self, theIndex):
        return _Storage.Storage_PType_ChangeFromIndex(self, theIndex)

    def __call__(self, *args):
        return _Storage.Storage_PType___call__(self, *args)

    def FindIndex(self, theKey1):
        return _Storage.Storage_PType_FindIndex(self, theKey1)

    def ChangeFromKey(self, theKey1):
        return _Storage.Storage_PType_ChangeFromKey(self, theKey1)

    def Seek(self, theKey1):
        return _Storage.Storage_PType_Seek(self, theKey1)

    def ChangeSeek(self, theKey1):
        return _Storage.Storage_PType_ChangeSeek(self, theKey1)

    def FindFromKey(self, *args):
        return _Storage.Storage_PType_FindFromKey(self, *args)

    def Clear(self, *args):
        return _Storage.Storage_PType_Clear(self, *args)
    __swig_destroy__ = _Storage.delete_Storage_PType

    def Size(self):
        return _Storage.Storage_PType_Size(self)

# Register Storage_PType in _Storage:
_Storage.Storage_PType_swigregister(Storage_PType)
class Storage_SeqOfRoot(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def begin(self):
        return _Storage.Storage_SeqOfRoot_begin(self)

    def end(self):
        return _Storage.Storage_SeqOfRoot_end(self)

    def cbegin(self):
        return _Storage.Storage_SeqOfRoot_cbegin(self)

    def cend(self):
        return _Storage.Storage_SeqOfRoot_cend(self)

    def __init__(self, *args):
        _Storage.Storage_SeqOfRoot_swiginit(self, _Storage.new_Storage_SeqOfRoot(*args))

    def Size(self):
        return _Storage.Storage_SeqOfRoot_Size(self)

    def Length(self):
        return _Storage.Storage_SeqOfRoot_Length(self)

    def Lower(self):
        return _Storage.Storage_SeqOfRoot_Lower(self)

    def Upper(self):
        return _Storage.Storage_SeqOfRoot_Upper(self)

    def IsEmpty(self):
        return _Storage.Storage_SeqOfRoot_IsEmpty(self)

    def Reverse(self):
        return _Storage.Storage_SeqOfRoot_Reverse(self)

    def Exchange(self, I, J):
        return _Storage.Storage_SeqOfRoot_Exchange(self, I, J)

    @staticmethod
    def delNode(theNode, theAl):
        return _Storage.Storage_SeqOfRoot_delNode(theNode, theAl)

    def Clear(self, theAllocator=0):
        return _Storage.Storage_SeqOfRoot_Clear(self, theAllocator)

    def Assign(self, theOther):
        return _Storage.Storage_SeqOfRoot_Assign(self, theOther)

    def Set(self, *args):
        return _Storage.Storage_SeqOfRoot_Set(self, *args)

    def Remove(self, *args):
        return _Storage.Storage_SeqOfRoot_Remove(self, *args)

    def Append(self, *args):
        return _Storage.Storage_SeqOfRoot_Append(self, *args)

    def Prepend(self, *args):
        return _Storage.Storage_SeqOfRoot_Prepend(self, *args)

    def InsertBefore(self, *args):
        return _Storage.Storage_SeqOfRoot_InsertBefore(self, *args)

    def InsertAfter(self, *args):
        return _Storage.Storage_SeqOfRoot_InsertAfter(self, *args)

    def Split(self, theIndex, theSeq):
        return _Storage.Storage_SeqOfRoot_Split(self, theIndex, theSeq)

    def First(self):
        return _Storage.Storage_SeqOfRoot_First(self)

    def ChangeFirst(self):
        return _Storage.Storage_SeqOfRoot_ChangeFirst(self)

    def Last(self):
        return _Storage.Storage_SeqOfRoot_Last(self)

    def ChangeLast(self):
        return _Storage.Storage_SeqOfRoot_ChangeLast(self)

    def Value(self, theIndex):
        return _Storage.Storage_SeqOfRoot_Value(self, theIndex)

    def ChangeValue(self, theIndex):
        return _Storage.Storage_SeqOfRoot_ChangeValue(self, theIndex)

    def __call__(self, *args):
        return _Storage.Storage_SeqOfRoot___call__(self, *args)

    def SetValue(self, theIndex, theItem):
        return _Storage.Storage_SeqOfRoot_SetValue(self, theIndex, theItem)
    __swig_destroy__ = _Storage.delete_Storage_SeqOfRoot

    def __len__(self):
        return self.Size()


# Register Storage_SeqOfRoot in _Storage:
_Storage.Storage_SeqOfRoot_swigregister(Storage_SeqOfRoot)

@classnotwrapped
class Storage:
	pass

@classnotwrapped
class Storage_BaseDriver:
	pass

@classnotwrapped
class Storage_Bucket:
	pass

@classnotwrapped
class Storage_BucketOfPersistent:
	pass

@classnotwrapped
class Storage_BucketIterator:
	pass

@classnotwrapped
class Storage_CallBack:
	pass

@classnotwrapped
class Storage_Data:
	pass

@classnotwrapped
class Storage_DefaultCallBack:
	pass

@classnotwrapped
class Storage_HeaderData:
	pass

@classnotwrapped
class Storage_InternalData:
	pass

@classnotwrapped
class Storage_Root:
	pass

@classnotwrapped
class Storage_RootData:
	pass

@classnotwrapped
class Storage_Schema:
	pass

@classnotwrapped
class Storage_TypeData:
	pass

@classnotwrapped
class Storage_TypedCallBack:
	pass


class Storage_HArrayOfCallBack(Storage_ArrayOfCallBack, odoo.addons.OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Storage.Storage_HArrayOfCallBack_swiginit(self, _Storage.new_Storage_HArrayOfCallBack(*args))

    def Array1(self):
        return _Storage.Storage_HArrayOfCallBack_Array1(self)

    def ChangeArray1(self):
        return _Storage.Storage_HArrayOfCallBack_ChangeArray1(self)
    __swig_destroy__ = _Storage.delete_Storage_HArrayOfCallBack

# Register Storage_HArrayOfCallBack in _Storage:
_Storage.Storage_HArrayOfCallBack_swigregister(Storage_HArrayOfCallBack)
class Storage_HArrayOfSchema(Storage_ArrayOfSchema, odoo.addons.OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Storage.Storage_HArrayOfSchema_swiginit(self, _Storage.new_Storage_HArrayOfSchema(*args))

    def Array1(self):
        return _Storage.Storage_HArrayOfSchema_Array1(self)

    def ChangeArray1(self):
        return _Storage.Storage_HArrayOfSchema_ChangeArray1(self)
    __swig_destroy__ = _Storage.delete_Storage_HArrayOfSchema

# Register Storage_HArrayOfSchema in _Storage:
_Storage.Storage_HArrayOfSchema_swigregister(Storage_HArrayOfSchema)
class Storage_HPArray(odoo.addons.OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Storage.Storage_HPArray_swiginit(self, _Storage.new_Storage_HPArray(*args))

    def Array1(self):
        return _Storage.Storage_HPArray_Array1(self)

    def ChangeArray1(self):
        return _Storage.Storage_HPArray_ChangeArray1(self)
    __swig_destroy__ = _Storage.delete_Storage_HPArray

# Register Storage_HPArray in _Storage:
_Storage.Storage_HPArray_swigregister(Storage_HPArray)
class Storage_HSeqOfRoot(Storage_SeqOfRoot, odoo.addons.OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Storage.Storage_HSeqOfRoot_swiginit(self, _Storage.new_Storage_HSeqOfRoot(*args))

    def Sequence(self):
        return _Storage.Storage_HSeqOfRoot_Sequence(self)

    def Append(self, *args):
        return _Storage.Storage_HSeqOfRoot_Append(self, *args)

    def ChangeSequence(self):
        return _Storage.Storage_HSeqOfRoot_ChangeSequence(self)
    __swig_destroy__ = _Storage.delete_Storage_HSeqOfRoot

# Register Storage_HSeqOfRoot in _Storage:
_Storage.Storage_HSeqOfRoot_swigregister(Storage_HSeqOfRoot)



