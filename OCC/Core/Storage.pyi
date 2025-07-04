from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *

# the following typedef cannot be wrapped as is
Storage_PType = NewType("Storage_PType", Any)
Storage_Position = NewType("Storage_Position", long)

class Storage_ArrayOfCallBack:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]: ...
    def next(self) -> False: ...
    __next__ = next
    def Init(self, theValue: False) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class Storage_ArrayOfSchema:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]: ...
    def next(self) -> False: ...
    __next__ = next
    def Init(self, theValue: False) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class Storage_SeqOfRoot:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Length(self) -> int: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class Storage_Error(IntEnum):
    Storage_VSOk: int = ...
    Storage_VSOpenError: int = ...
    Storage_VSModeError: int = ...
    Storage_VSCloseError: int = ...
    Storage_VSAlreadyOpen: int = ...
    Storage_VSNotOpen: int = ...
    Storage_VSSectionNotFound: int = ...
    Storage_VSWriteError: int = ...
    Storage_VSFormatError: int = ...
    Storage_VSUnknownType: int = ...
    Storage_VSTypeMismatch: int = ...
    Storage_VSInternalError: int = ...
    Storage_VSExtCharParityError: int = ...
    Storage_VSWrongFileDriver: int = ...

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
    Storage_VSNone: int = ...
    Storage_VSRead: int = ...
    Storage_VSWrite: int = ...
    Storage_VSReadWrite: int = ...

Storage_VSNone = Storage_OpenMode.Storage_VSNone
Storage_VSRead = Storage_OpenMode.Storage_VSRead
Storage_VSWrite = Storage_OpenMode.Storage_VSWrite
Storage_VSReadWrite = Storage_OpenMode.Storage_VSReadWrite

class Storage_SolveMode(IntEnum):
    Storage_AddSolve: int = ...
    Storage_WriteSolve: int = ...
    Storage_ReadSolve: int = ...

Storage_AddSolve = Storage_SolveMode.Storage_AddSolve
Storage_WriteSolve = Storage_SolveMode.Storage_WriteSolve
Storage_ReadSolve = Storage_SolveMode.Storage_ReadSolve

#classnotwrapped
class Storage: ...

#classnotwrapped
class Storage_BaseDriver: ...

#classnotwrapped
class Storage_Bucket: ...

#classnotwrapped
class Storage_BucketOfPersistent: ...

#classnotwrapped
class Storage_BucketIterator: ...

#classnotwrapped
class Storage_CallBack: ...

#classnotwrapped
class Storage_Data: ...

#classnotwrapped
class Storage_DefaultCallBack: ...

#classnotwrapped
class Storage_HeaderData: ...

#classnotwrapped
class Storage_InternalData: ...

#classnotwrapped
class Storage_Root: ...

#classnotwrapped
class Storage_RootData: ...

#classnotwrapped
class Storage_Schema: ...

#classnotwrapped
class Storage_TypeData: ...

#classnotwrapped
class Storage_TypedCallBack: ...

# harray1 classes

class Storage_HArrayOfCallBack(Storage_ArrayOfCallBack, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> Storage_ArrayOfCallBack: ...


class Storage_HArrayOfSchema(Storage_ArrayOfSchema, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> Storage_ArrayOfSchema: ...


class Storage_HPArray(Storage_PArray, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> Storage_PArray: ...

# harray2 classes
# hsequence classes

class Storage_HSeqOfRoot(Storage_SeqOfRoot, Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: Storage_SeqOfRoot) -> None: ...
    def Sequence(self) -> Storage_SeqOfRoot: ...
    def Append(self, theSequence: Storage_SeqOfRoot) -> None: ...


