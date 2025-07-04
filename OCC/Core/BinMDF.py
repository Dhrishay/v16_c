# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

"""
BinMDF module, see official documentation at
https://dev.opencascade.org/doc/occt-7.8.0/refman/html/package_binmdf.html
"""

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _BinMDF
else:
    import _BinMDF

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
    __swig_destroy__ = _BinMDF.delete_SwigPyIterator

    def value(self):
        return _BinMDF.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _BinMDF.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _BinMDF.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _BinMDF.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _BinMDF.SwigPyIterator_equal(self, x)

    def copy(self):
        return _BinMDF.SwigPyIterator_copy(self)

    def next(self):
        return _BinMDF.SwigPyIterator_next(self)

    def __next__(self):
        return _BinMDF.SwigPyIterator___next__(self)

    def previous(self):
        return _BinMDF.SwigPyIterator_previous(self)

    def advance(self, n):
        return _BinMDF.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _BinMDF.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _BinMDF.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _BinMDF.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _BinMDF.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _BinMDF.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _BinMDF.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _BinMDF:
_BinMDF.SwigPyIterator_swigregister(SwigPyIterator)

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
    return _BinMDF.process_exception(error, method_name, class_name)

import warnings
from odoo.addons.OCC.Wrapper.wrapper_utils import Proxy, deprecated

class ios_base(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    erase_event = _BinMDF.ios_base_erase_event
    imbue_event = _BinMDF.ios_base_imbue_event
    copyfmt_event = _BinMDF.ios_base_copyfmt_event

    def register_callback(self, __fn, __index):
        return _BinMDF.ios_base_register_callback(self, __fn, __index)

    def flags(self, *args):
        return _BinMDF.ios_base_flags(self, *args)

    def setf(self, *args):
        return _BinMDF.ios_base_setf(self, *args)

    def unsetf(self, __mask):
        return _BinMDF.ios_base_unsetf(self, __mask)

    def precision(self, *args):
        return _BinMDF.ios_base_precision(self, *args)

    def width(self, *args):
        return _BinMDF.ios_base_width(self, *args)

    @staticmethod
    def sync_with_stdio(__sync=True):
        return _BinMDF.ios_base_sync_with_stdio(__sync)

    def imbue(self, __loc):
        return _BinMDF.ios_base_imbue(self, __loc)

    def getloc(self):
        return _BinMDF.ios_base_getloc(self)

    @staticmethod
    def xalloc():
        return _BinMDF.ios_base_xalloc()

    def iword(self, __ix):
        return _BinMDF.ios_base_iword(self, __ix)

    def pword(self, __ix):
        return _BinMDF.ios_base_pword(self, __ix)
    __swig_destroy__ = _BinMDF.delete_ios_base

# Register ios_base in _BinMDF:
_BinMDF.ios_base_swigregister(ios_base)
cvar = _BinMDF.cvar
ios_base.boolalpha = _BinMDF.cvar.ios_base_boolalpha
ios_base.dec = _BinMDF.cvar.ios_base_dec
ios_base.fixed = _BinMDF.cvar.ios_base_fixed
ios_base.hex = _BinMDF.cvar.ios_base_hex
ios_base.internal = _BinMDF.cvar.ios_base_internal
ios_base.left = _BinMDF.cvar.ios_base_left
ios_base.oct = _BinMDF.cvar.ios_base_oct
ios_base.right = _BinMDF.cvar.ios_base_right
ios_base.scientific = _BinMDF.cvar.ios_base_scientific
ios_base.showbase = _BinMDF.cvar.ios_base_showbase
ios_base.showpoint = _BinMDF.cvar.ios_base_showpoint
ios_base.showpos = _BinMDF.cvar.ios_base_showpos
ios_base.skipws = _BinMDF.cvar.ios_base_skipws
ios_base.unitbuf = _BinMDF.cvar.ios_base_unitbuf
ios_base.uppercase = _BinMDF.cvar.ios_base_uppercase
ios_base.adjustfield = _BinMDF.cvar.ios_base_adjustfield
ios_base.basefield = _BinMDF.cvar.ios_base_basefield
ios_base.floatfield = _BinMDF.cvar.ios_base_floatfield
ios_base.badbit = _BinMDF.cvar.ios_base_badbit
ios_base.eofbit = _BinMDF.cvar.ios_base_eofbit
ios_base.failbit = _BinMDF.cvar.ios_base_failbit
ios_base.goodbit = _BinMDF.cvar.ios_base_goodbit
ios_base.app = _BinMDF.cvar.ios_base_app
ios_base.ate = _BinMDF.cvar.ios_base_ate
ios_base.binary = _BinMDF.cvar.ios_base_binary
ios_base.ios_base_in = _BinMDF.cvar.ios_base_ios_base_in
ios_base.out = _BinMDF.cvar.ios_base_out
ios_base.trunc = _BinMDF.cvar.ios_base_trunc
ios_base.beg = _BinMDF.cvar.ios_base_beg
ios_base.cur = _BinMDF.cvar.ios_base_cur
ios_base.end = _BinMDF.cvar.ios_base_end

class ios(ios_base):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def rdstate(self):
        return _BinMDF.ios_rdstate(self)

    def clear(self, *args):
        return _BinMDF.ios_clear(self, *args)

    def setstate(self, __state):
        return _BinMDF.ios_setstate(self, __state)

    def good(self):
        return _BinMDF.ios_good(self)

    def eof(self):
        return _BinMDF.ios_eof(self)

    def fail(self):
        return _BinMDF.ios_fail(self)

    def bad(self):
        return _BinMDF.ios_bad(self)

    def exceptions(self, *args):
        return _BinMDF.ios_exceptions(self, *args)

    def __init__(self, __sb):
        _BinMDF.ios_swiginit(self, _BinMDF.new_ios(__sb))
    __swig_destroy__ = _BinMDF.delete_ios

    def tie(self, *args):
        return _BinMDF.ios_tie(self, *args)

    def rdbuf(self, *args):
        return _BinMDF.ios_rdbuf(self, *args)

    def copyfmt(self, __rhs):
        return _BinMDF.ios_copyfmt(self, __rhs)

    def fill(self, *args):
        return _BinMDF.ios_fill(self, *args)

    def imbue(self, __loc):
        return _BinMDF.ios_imbue(self, __loc)

    def narrow(self, __c, __dfault):
        return _BinMDF.ios_narrow(self, __c, __dfault)

    def widen(self, __c):
        return _BinMDF.ios_widen(self, __c)

# Register ios in _BinMDF:
_BinMDF.ios_swigregister(ios)
class ostream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _BinMDF.ostream_swiginit(self, _BinMDF.new_ostream(__sb))
    __swig_destroy__ = _BinMDF.delete_ostream

    def __lshift__(self, *args):
        return _BinMDF.ostream___lshift__(self, *args)

    def put(self, __c):
        return _BinMDF.ostream_put(self, __c)

    def write(self, __s, __n):
        return _BinMDF.ostream_write(self, __s, __n)

    def flush(self):
        return _BinMDF.ostream_flush(self)

    def tellp(self):
        return _BinMDF.ostream_tellp(self)

    def seekp(self, *args):
        return _BinMDF.ostream_seekp(self, *args)

# Register ostream in _BinMDF:
_BinMDF.ostream_swigregister(ostream)
class istream(ios):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _BinMDF.istream_swiginit(self, _BinMDF.new_istream(__sb))
    __swig_destroy__ = _BinMDF.delete_istream

    def __rshift__(self, *args):
        return _BinMDF.istream___rshift__(self, *args)

    def gcount(self):
        return _BinMDF.istream_gcount(self)

    def get(self, *args):
        return _BinMDF.istream_get(self, *args)

    def getline(self, *args):
        return _BinMDF.istream_getline(self, *args)

    def ignore(self, *args):
        return _BinMDF.istream_ignore(self, *args)

    def peek(self):
        return _BinMDF.istream_peek(self)

    def read(self, __s, __n):
        return _BinMDF.istream_read(self, __s, __n)

    def readsome(self, __s, __n):
        return _BinMDF.istream_readsome(self, __s, __n)

    def putback(self, __c):
        return _BinMDF.istream_putback(self, __c)

    def unget(self):
        return _BinMDF.istream_unget(self)

    def sync(self):
        return _BinMDF.istream_sync(self)

    def tellg(self):
        return _BinMDF.istream_tellg(self)

    def seekg(self, *args):
        return _BinMDF.istream_seekg(self, *args)

# Register istream in _BinMDF:
_BinMDF.istream_swigregister(istream)
class iostream(istream, ostream):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, __sb):
        _BinMDF.iostream_swiginit(self, _BinMDF.new_iostream(__sb))
    __swig_destroy__ = _BinMDF.delete_iostream

# Register iostream in _BinMDF:
_BinMDF.iostream_swigregister(iostream)
cin = cvar.cin
cout = cvar.cout
cerr = cvar.cerr
clog = cvar.clog

endl_cb_ptr = _BinMDF.endl_cb_ptr
endl = _BinMDF.endl
ends_cb_ptr = _BinMDF.ends_cb_ptr
ends = _BinMDF.ends
flush_cb_ptr = _BinMDF.flush_cb_ptr
flush = _BinMDF.flush
import odoo.addons.OCC.Core.Standard
import odoo.addons.OCC.Core.NCollection
import odoo.addons.OCC.Core.TColStd
import odoo.addons.OCC.Core.TCollection
import odoo.addons.OCC.Core.Message
import odoo.addons.OCC.Core.OSD
import odoo.addons.OCC.Core.TDF
import odoo.addons.OCC.Core.BinObjMgt
import odoo.addons.OCC.Core.Storage

from enum import IntEnum
from odoo.addons.OCC.Core.Exception import *




def Handle_BinMDF_ADriver_Create():
    return _BinMDF.Handle_BinMDF_ADriver_Create()

def Handle_BinMDF_ADriver_DownCast(t):
    return _BinMDF.Handle_BinMDF_ADriver_DownCast(t)

def Handle_BinMDF_ADriver_IsNull(t):
    return _BinMDF.Handle_BinMDF_ADriver_IsNull(t)

def Handle_BinMDF_ADriverTable_Create():
    return _BinMDF.Handle_BinMDF_ADriverTable_Create()

def Handle_BinMDF_ADriverTable_DownCast(t):
    return _BinMDF.Handle_BinMDF_ADriverTable_DownCast(t)

def Handle_BinMDF_ADriverTable_IsNull(t):
    return _BinMDF.Handle_BinMDF_ADriverTable_IsNull(t)

def Handle_BinMDF_DerivedDriver_Create():
    return _BinMDF.Handle_BinMDF_DerivedDriver_Create()

def Handle_BinMDF_DerivedDriver_DownCast(t):
    return _BinMDF.Handle_BinMDF_DerivedDriver_DownCast(t)

def Handle_BinMDF_DerivedDriver_IsNull(t):
    return _BinMDF.Handle_BinMDF_DerivedDriver_IsNull(t)

def Handle_BinMDF_ReferenceDriver_Create():
    return _BinMDF.Handle_BinMDF_ReferenceDriver_Create()

def Handle_BinMDF_ReferenceDriver_DownCast(t):
    return _BinMDF.Handle_BinMDF_ReferenceDriver_DownCast(t)

def Handle_BinMDF_ReferenceDriver_IsNull(t):
    return _BinMDF.Handle_BinMDF_ReferenceDriver_IsNull(t)

def Handle_BinMDF_TagSourceDriver_Create():
    return _BinMDF.Handle_BinMDF_TagSourceDriver_Create()

def Handle_BinMDF_TagSourceDriver_DownCast(t):
    return _BinMDF.Handle_BinMDF_TagSourceDriver_DownCast(t)

def Handle_BinMDF_TagSourceDriver_IsNull(t):
    return _BinMDF.Handle_BinMDF_TagSourceDriver_IsNull(t)

from odoo.addons.OCC.Core.NCollection import NCollection_BaseMap

class BinMDF_TypeADriverMap(NCollection_BaseMap):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def begin(self):
        return _BinMDF.BinMDF_TypeADriverMap_begin(self)

    def end(self):
        return _BinMDF.BinMDF_TypeADriverMap_end(self)

    def cbegin(self):
        return _BinMDF.BinMDF_TypeADriverMap_cbegin(self)

    def cend(self):
        return _BinMDF.BinMDF_TypeADriverMap_cend(self)

    def __init__(self, *args):
        _BinMDF.BinMDF_TypeADriverMap_swiginit(self, _BinMDF.new_BinMDF_TypeADriverMap(*args))

    def Exchange(self, theOther):
        return _BinMDF.BinMDF_TypeADriverMap_Exchange(self, theOther)

    def Assign(self, theOther):
        return _BinMDF.BinMDF_TypeADriverMap_Assign(self, theOther)

    def Set(self, *args):
        return _BinMDF.BinMDF_TypeADriverMap_Set(self, *args)

    def ReSize(self, N):
        return _BinMDF.BinMDF_TypeADriverMap_ReSize(self, N)

    def Bind(self, *args):
        return _BinMDF.BinMDF_TypeADriverMap_Bind(self, *args)

    def Bound(self, *args):
        return _BinMDF.BinMDF_TypeADriverMap_Bound(self, *args)

    def IsBound(self, theKey):
        return _BinMDF.BinMDF_TypeADriverMap_IsBound(self, theKey)

    def UnBind(self, theKey):
        return _BinMDF.BinMDF_TypeADriverMap_UnBind(self, theKey)

    def Seek(self, theKey):
        return _BinMDF.BinMDF_TypeADriverMap_Seek(self, theKey)

    def Find(self, *args):
        return _BinMDF.BinMDF_TypeADriverMap_Find(self, *args)

    def ChangeSeek(self, theKey):
        return _BinMDF.BinMDF_TypeADriverMap_ChangeSeek(self, theKey)

    def ChangeFind(self, theKey):
        return _BinMDF.BinMDF_TypeADriverMap_ChangeFind(self, theKey)

    def __call__(self, *args):
        return _BinMDF.BinMDF_TypeADriverMap___call__(self, *args)

    def Clear(self, *args):
        return _BinMDF.BinMDF_TypeADriverMap_Clear(self, *args)
    __swig_destroy__ = _BinMDF.delete_BinMDF_TypeADriverMap

    def Size(self):
        return _BinMDF.BinMDF_TypeADriverMap_Size(self)

# Register BinMDF_TypeADriverMap in _BinMDF:
_BinMDF.BinMDF_TypeADriverMap_swigregister(BinMDF_TypeADriverMap)

from odoo.addons.OCC.Core.NCollection import NCollection_BaseMap

class BinMDF_TypeIdMap(NCollection_BaseMap):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _BinMDF.BinMDF_TypeIdMap_swiginit(self, _BinMDF.new_BinMDF_TypeIdMap(*args))

    def Exchange(self, theOther):
        return _BinMDF.BinMDF_TypeIdMap_Exchange(self, theOther)

    def Assign(self, theOther):
        return _BinMDF.BinMDF_TypeIdMap_Assign(self, theOther)

    def Set(self, theOther):
        return _BinMDF.BinMDF_TypeIdMap_Set(self, theOther)

    def ReSize(self, N):
        return _BinMDF.BinMDF_TypeIdMap_ReSize(self, N)

    def Bind(self, theKey1, theKey2):
        return _BinMDF.BinMDF_TypeIdMap_Bind(self, theKey1, theKey2)

    def AreBound(self, theKey1, theKey2):
        return _BinMDF.BinMDF_TypeIdMap_AreBound(self, theKey1, theKey2)

    def IsBound1(self, theKey1):
        return _BinMDF.BinMDF_TypeIdMap_IsBound1(self, theKey1)

    def IsBound2(self, theKey2):
        return _BinMDF.BinMDF_TypeIdMap_IsBound2(self, theKey2)

    def UnBind1(self, theKey1):
        return _BinMDF.BinMDF_TypeIdMap_UnBind1(self, theKey1)

    def UnBind2(self, theKey2):
        return _BinMDF.BinMDF_TypeIdMap_UnBind2(self, theKey2)

    def Find1(self, *args):
        return _BinMDF.BinMDF_TypeIdMap_Find1(self, *args)

    def Seek1(self, theKey1):
        return _BinMDF.BinMDF_TypeIdMap_Seek1(self, theKey1)

    def Find2(self, *args):
        return _BinMDF.BinMDF_TypeIdMap_Find2(self, *args)

    def Seek2(self, theKey2):
        return _BinMDF.BinMDF_TypeIdMap_Seek2(self, theKey2)

    def Clear(self, *args):
        return _BinMDF.BinMDF_TypeIdMap_Clear(self, *args)
    __swig_destroy__ = _BinMDF.delete_BinMDF_TypeIdMap

    def Size(self):
        return _BinMDF.BinMDF_TypeIdMap_Size(self)

# Register BinMDF_TypeIdMap in _BinMDF:
_BinMDF.BinMDF_TypeIdMap_swigregister(BinMDF_TypeIdMap)
class binmdf(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def AddDrivers(*args):
        r"""

        Parameters
        ----------
        aDriverTable: BinMDF_ADriverTable
        aMsgDrv: Message_Messenger

        Return
        -------
        None

        Description
        -----------
        Adds the attribute storage drivers to <adrivertable>.

        """
        return _BinMDF.binmdf_AddDrivers(*args)

    __repr__ = _dumps_object


    def __init__(self):
        _BinMDF.binmdf_swiginit(self, _BinMDF.new_binmdf())
    __swig_destroy__ = _BinMDF.delete_binmdf

# Register binmdf in _BinMDF:
_BinMDF.binmdf_swigregister(binmdf)
class BinMDF_ADriver(odoo.addons.OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def MessageDriver(self, *args):
        r"""
        Return
        -------
        opencascade::handle<Message_Messenger>

        Description
        -----------
        Returns the current message driver of this driver.

        """
        return _BinMDF.BinMDF_ADriver_MessageDriver(self, *args)

    def NewEmpty(self, *args):
        r"""
        Return
        -------
        opencascade::handle<TDF_Attribute>

        Description
        -----------
        Creates a new attribute from tdf.

        """
        return _BinMDF.BinMDF_ADriver_NewEmpty(self, *args)

    def Paste(self, *args):
        r"""

        Parameters
        ----------
        aSource: BinObjMgt_Persistent
        aTarget: TDF_Attribute
        aRelocTable: BinObjMgt_RRelocationTable

        Return
        -------
        bool

        Description
        -----------
        Translate the contents of <asource> and put it into <atarget>, using the relocation table <areloctable> to keep the sharings.

        Parameters
        ----------
        aSource: TDF_Attribute
        aTarget: BinObjMgt_Persistent
        aRelocTable: BinObjMgt_SRelocationTable

        Return
        -------
        None

        Description
        -----------
        Translate the contents of <asource> and put it into <atarget>, using the relocation table <areloctable> to keep the sharings.

        """
        return _BinMDF.BinMDF_ADriver_Paste(self, *args)

    def SourceType(self, *args):
        r"""
        Return
        -------
        opencascade::handle<Standard_Type>

        Description
        -----------
        Returns the type of source object, inheriting from attribute from tdf.

        """
        return _BinMDF.BinMDF_ADriver_SourceType(self, *args)

    def TypeName(self, *args):
        r"""
        Return
        -------
        TCollection_AsciiString

        Description
        -----------
        Returns the type name of the attribute object.

        """
        return _BinMDF.BinMDF_ADriver_TypeName(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDF_ADriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDF.delete_BinMDF_ADriver

# Register BinMDF_ADriver in _BinMDF:
_BinMDF.BinMDF_ADriver_swigregister(BinMDF_ADriver)
class BinMDF_ADriverTable(odoo.addons.OCC.Core.Standard.Standard_Transient):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        Return
        -------
        None

        Description
        -----------
        Constructor.

        """
        _BinMDF.BinMDF_ADriverTable_swiginit(self, _BinMDF.new_BinMDF_ADriverTable(*args))

    def AddDerivedDriver(self, *args):
        r"""

        Parameters
        ----------
        theInstance: TDF_Attribute

        Return
        -------
        None

        Description
        -----------
        Adds a translation driver for the derived attribute. the base driver must be already added. @param theinstance is newly created attribute, detached from any label.

        Parameters
        ----------
        theDerivedType: str

        Return
        -------
        opencascade::handle<Standard_Type>

        Description
        -----------
        Adds a translation driver for the derived attribute. the base driver must be already added. @param thederivedtype is registered attribute type using implement_derived_attribute macro.

        """
        return _BinMDF.BinMDF_ADriverTable_AddDerivedDriver(self, *args)

    def AddDriver(self, *args):
        r"""

        Parameters
        ----------
        theDriver: BinMDF_ADriver

        Return
        -------
        None

        Description
        -----------
        Adds a translation driver <thedriver>.

        """
        return _BinMDF.BinMDF_ADriverTable_AddDriver(self, *args)

    def AssignIds(self, *args):
        r"""

        Parameters
        ----------
        theTypes: TColStd_IndexedMapOfTransient

        Return
        -------
        None

        Description
        -----------
        Assigns the ids to the drivers of the given types. it uses indices in the map as ids. useful in storage procedure.

        Parameters
        ----------
        theTypeNames: TColStd_SequenceOfAsciiString

        Return
        -------
        None

        Description
        -----------
        Assigns the ids to the drivers of the given type names; it uses indices in the sequence as ids. useful in retrieval procedure.

        """
        return _BinMDF.BinMDF_ADriverTable_AssignIds(self, *args)

    def GetDriver(self, *args):
        r"""

        Parameters
        ----------
        theType: Standard_Type
        theDriver: BinMDF_ADriver

        Return
        -------
        int

        Description
        -----------
        Gets a driver <thedriver> according to <thetype>. returns type id if the driver was assigned an id; 0 otherwise.

        Parameters
        ----------
        theTypeId: int

        Return
        -------
        opencascade::handle<BinMDF_ADriver>

        Description
        -----------
        Returns a driver according to <thetypeid>. returns null handle if a driver is not found.

        """
        return _BinMDF.BinMDF_ADriverTable_GetDriver(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDF_ADriverTable_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDF.delete_BinMDF_ADriverTable

# Register BinMDF_ADriverTable in _BinMDF:
_BinMDF.BinMDF_ADriverTable_swigregister(BinMDF_ADriverTable)
class BinMDF_DerivedDriver(BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        theDerivative: TDF_Attribute
        theBaseDriver: BinMDF_ADriver

        Return
        -------
        None

        Description
        -----------
        Creates a derivative persistence driver for thederivative attribute by reusage of thebasedriver @param thederivative an instance of the attribute, just created, detached from any label @param thebasedriver a driver of the base attribute, called by paste methods.

        """
        _BinMDF.BinMDF_DerivedDriver_swiginit(self, _BinMDF.new_BinMDF_DerivedDriver(*args))

    def Paste(self, *args):
        r"""

        Parameters
        ----------
        theSource: BinObjMgt_Persistent
        theTarget: TDF_Attribute
        theRelocTable: BinObjMgt_RRelocationTable

        Return
        -------
        bool

        Description
        -----------
        Reuses the base driver to read the base fields.

        Parameters
        ----------
        theSource: TDF_Attribute
        theTarget: BinObjMgt_Persistent
        theRelocTable: BinObjMgt_SRelocationTable

        Return
        -------
        None

        Description
        -----------
        Reuses the base driver to store the base fields.

        """
        return _BinMDF.BinMDF_DerivedDriver_Paste(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDF_DerivedDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDF.delete_BinMDF_DerivedDriver

# Register BinMDF_DerivedDriver in _BinMDF:
_BinMDF.BinMDF_DerivedDriver_swigregister(BinMDF_DerivedDriver)
class BinMDF_ReferenceDriver(BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        theMessageDriver: Message_Messenger

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        _BinMDF.BinMDF_ReferenceDriver_swiginit(self, _BinMDF.new_BinMDF_ReferenceDriver(*args))

    def Paste(self, *args):
        r"""

        Parameters
        ----------
        Source: BinObjMgt_Persistent
        Target: TDF_Attribute
        RelocTable: BinObjMgt_RRelocationTable

        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        Parameters
        ----------
        Source: TDF_Attribute
        Target: BinObjMgt_Persistent
        RelocTable: BinObjMgt_SRelocationTable

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        return _BinMDF.BinMDF_ReferenceDriver_Paste(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDF_ReferenceDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDF.delete_BinMDF_ReferenceDriver

# Register BinMDF_ReferenceDriver in _BinMDF:
_BinMDF.BinMDF_ReferenceDriver_swigregister(BinMDF_ReferenceDriver)
class BinMDF_TagSourceDriver(BinMDF_ADriver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""

        Parameters
        ----------
        theMessageDriver: Message_Messenger

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        _BinMDF.BinMDF_TagSourceDriver_swiginit(self, _BinMDF.new_BinMDF_TagSourceDriver(*args))

    def Paste(self, *args):
        r"""

        Parameters
        ----------
        Source: BinObjMgt_Persistent
        Target: TDF_Attribute
        RelocTable: BinObjMgt_RRelocationTable

        Return
        -------
        bool

        Description
        -----------
        No available documentation.

        Parameters
        ----------
        Source: TDF_Attribute
        Target: BinObjMgt_Persistent
        RelocTable: BinObjMgt_SRelocationTable

        Return
        -------
        None

        Description
        -----------
        No available documentation.

        """
        return _BinMDF.BinMDF_TagSourceDriver_Paste(self, *args)


    @staticmethod
    def DownCast(t):
      return Handle_BinMDF_TagSourceDriver_DownCast(t)


    __repr__ = _dumps_object

    __swig_destroy__ = _BinMDF.delete_BinMDF_TagSourceDriver

# Register BinMDF_TagSourceDriver in _BinMDF:
_BinMDF.BinMDF_TagSourceDriver_swigregister(BinMDF_TagSourceDriver)

BinMDF_StringIdMap=OCC.Core.TColStd.TColStd_DataMapOfAsciiStringInteger


@deprecated
def binmdf_AddDrivers(*args):
	return binmdf.AddDrivers(*args)



