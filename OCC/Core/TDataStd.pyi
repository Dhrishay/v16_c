from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.TDF import *
from OCC.Core.TCollection import *

TDataStd_PtrTreeNode = NewType("TDataStd_PtrTreeNode", TDataStd_TreeNode)

class TDataStd_LabelArray1:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> TDF_Label: ...
    def __setitem__(self, index: int, value: TDF_Label) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TDF_Label]: ...
    def next(self) -> TDF_Label: ...
    __next__ = next
    def Init(self, theValue: TDF_Label) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> TDF_Label: ...
    def Last(self) -> TDF_Label: ...
    def Value(self, theIndex: int) -> TDF_Label: ...
    def SetValue(self, theIndex: int, theValue: TDF_Label) -> None: ...

class TDataStd_ListOfByte:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> str: ...
    def Last(self) -> str: ...
    def Append(self, theItem: str) -> str: ...
    def Prepend(self, theItem: str) -> str: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> str: ...
    def SetValue(self, theIndex: int, theValue: str) -> None: ...

class TDataStd_ListOfExtendedString:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> str: ...
    def Last(self) -> str: ...
    def Append(self, theItem: str) -> str: ...
    def Prepend(self, theItem: str) -> str: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> str: ...
    def SetValue(self, theIndex: int, theValue: str) -> None: ...

class TDataStd_RealEnum(IntEnum):
    TDataStd_SCALAR: int = ...
    TDataStd_LENGTH: int = ...
    TDataStd_ANGULAR: int = ...

TDataStd_SCALAR = TDataStd_RealEnum.TDataStd_SCALAR
TDataStd_LENGTH = TDataStd_RealEnum.TDataStd_LENGTH
TDataStd_ANGULAR = TDataStd_RealEnum.TDataStd_ANGULAR

class tdatastd:
    @staticmethod
    def IDList(anIDList: TDF_IDList) -> None: ...
    @staticmethod
    def Print(DIM: TDataStd_RealEnum) -> Tuple[Standard_OStream, str]: ...

class TDataStd_AsciiString(TDF_Attribute):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Get(self) -> str: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def IsEmpty(self) -> bool: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, with_: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, string: str) -> TDataStd_AsciiString: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, guid: Standard_GUID, string: str) -> TDataStd_AsciiString: ...
    @overload
    def Set(self, S: str) -> None: ...
    @overload
    def SetID(self, guid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...

class TDataStd_BooleanArray(TDF_Attribute):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def Init(self, lower: int, upper: int) -> None: ...
    def InternalArray(self) -> TColStd_HArray1OfByte: ...
    def Length(self) -> int: ...
    def Lower(self) -> int: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, with_: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, lower: int, upper: int) -> TDataStd_BooleanArray: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID, lower: int, upper: int) -> TDataStd_BooleanArray: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...
    def SetInternalArray(self, values: TColStd_HArray1OfByte) -> None: ...
    def SetValue(self, index: int, value: bool) -> None: ...
    def Upper(self) -> int: ...
    def Value(self, Index: int) -> bool: ...

class TDataStd_BooleanList(TDF_Attribute):
    def __init__(self) -> None: ...
    def Append(self, value: bool) -> None: ...
    def Clear(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Extent(self) -> int: ...
    def First(self) -> bool: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def InsertAfter(self, index: int, after_value: bool) -> bool: ...
    def InsertBefore(self, index: int, before_value: bool) -> bool: ...
    def IsEmpty(self) -> bool: ...
    def Last(self) -> bool: ...
    def List(self) -> TDataStd_ListOfByte: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Prepend(self, value: bool) -> None: ...
    def Remove(self, index: int) -> bool: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_BooleanList: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID) -> TDataStd_BooleanList: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...

class TDataStd_ByteArray(TDF_Attribute):
    def __init__(self) -> None: ...
    def ChangeArray(self, newArray: TColStd_HArray1OfByte, isCheckItems: Optional[bool] = True) -> None: ...
    def DeltaOnModification(self, anOldAttribute: TDF_Attribute) -> TDF_DeltaOnModification: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetDelta(self) -> bool: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def Init(self, lower: int, upper: int) -> None: ...
    def InternalArray(self) -> TColStd_HArray1OfByte: ...
    def Length(self) -> int: ...
    def Lower(self) -> int: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, with_: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, lower: int, upper: int, isDelta: Optional[bool] = False) -> TDataStd_ByteArray: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID, lower: int, upper: int, isDelta: Optional[bool] = False) -> TDataStd_ByteArray: ...
    def SetDelta(self, isDelta: bool) -> None: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...
    def SetValue(self, index: int, value: str) -> None: ...
    def Upper(self) -> int: ...
    def Value(self, Index: int) -> str: ...

class TDataStd_ChildNodeIterator:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, aTreeNode: TDataStd_TreeNode, allLevels: Optional[bool] = False) -> None: ...
    def Initialize(self, aTreeNode: TDataStd_TreeNode, allLevels: Optional[bool] = False) -> None: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def NextBrother(self) -> None: ...
    def Value(self) -> TDataStd_TreeNode: ...

class TDataStd_Current(TDF_Attribute):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    @staticmethod
    def Get(acces: TDF_Label) -> TDF_Label: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def GetLabel(self) -> TDF_Label: ...
    @staticmethod
    def Has(acces: TDF_Label) -> bool: ...
    def ID(self) -> Standard_GUID: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @staticmethod
    def Set(L: TDF_Label) -> None: ...
    def SetLabel(self, current: TDF_Label) -> None: ...

class TDataStd_DeltaOnModificationOfByteArray(TDF_DeltaOnModification):
    def __init__(self, Arr: TDataStd_ByteArray) -> None: ...
    def Apply(self) -> None: ...

class TDataStd_DeltaOnModificationOfExtStringArray(TDF_DeltaOnModification):
    def __init__(self, Arr: TDataStd_ExtStringArray) -> None: ...
    def Apply(self) -> None: ...

class TDataStd_DeltaOnModificationOfIntArray(TDF_DeltaOnModification):
    def __init__(self, Arr: TDataStd_IntegerArray) -> None: ...
    def Apply(self) -> None: ...

class TDataStd_DeltaOnModificationOfIntPackedMap(TDF_DeltaOnModification):
    def __init__(self, Arr: TDataStd_IntPackedMap) -> None: ...
    def Apply(self) -> None: ...

class TDataStd_DeltaOnModificationOfRealArray(TDF_DeltaOnModification):
    def __init__(self, Arr: TDataStd_RealArray) -> None: ...
    def Apply(self) -> None: ...

class TDataStd_Expression(TDF_Attribute):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetExpression(self) -> str: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def GetVariables(self) -> TDF_AttributeList: ...
    def ID(self) -> Standard_GUID: ...
    def Name(self) -> str: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_Expression: ...
    def SetExpression(self, E: str) -> None: ...

class TDataStd_ExtStringArray(TDF_Attribute):
    def __init__(self) -> None: ...
    def Array(self) -> TColStd_HArray1OfExtendedString: ...
    def ChangeArray(self, newArray: TColStd_HArray1OfExtendedString, isCheckItems: Optional[bool] = True) -> None: ...
    def DeltaOnModification(self, anOldAttribute: TDF_Attribute) -> TDF_DeltaOnModification: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetDelta(self) -> bool: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def Init(self, lower: int, upper: int) -> None: ...
    def Length(self) -> int: ...
    def Lower(self) -> int: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, lower: int, upper: int, isDelta: Optional[bool] = False) -> TDataStd_ExtStringArray: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID, lower: int, upper: int, isDelta: Optional[bool] = False) -> TDataStd_ExtStringArray: ...
    def SetDelta(self, isDelta: bool) -> None: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...
    def SetValue(self, Index: int, Value: str) -> None: ...
    def Upper(self) -> int: ...
    def Value(self, Index: int) -> str: ...

class TDataStd_ExtStringList(TDF_Attribute):
    def __init__(self) -> None: ...
    def Append(self, value: str) -> None: ...
    def Clear(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Extent(self) -> int: ...
    def First(self) -> str: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    @overload
    def InsertAfter(self, value: str, after_value: str) -> bool: ...
    @overload
    def InsertAfter(self, index: int, after_value: str) -> bool: ...
    @overload
    def InsertBefore(self, value: str, before_value: str) -> bool: ...
    @overload
    def InsertBefore(self, index: int, before_value: str) -> bool: ...
    def IsEmpty(self) -> bool: ...
    def Last(self) -> str: ...
    def List(self) -> TDataStd_ListOfExtendedString: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Prepend(self, value: str) -> None: ...
    @overload
    def Remove(self, value: str) -> bool: ...
    @overload
    def Remove(self, index: int) -> bool: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_ExtStringList: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID) -> TDataStd_ExtStringList: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...

class TDataStd_HDataMapOfStringByte(Standard_Transient):
    @overload
    def __init__(self, NbBuckets: Optional[int] = 1) -> None: ...
    @overload
    def __init__(self, theOther: TDataStd_DataMapOfStringByte) -> None: ...
    def ChangeMap(self) -> TDataStd_DataMapOfStringByte: ...
    def Map(self) -> TDataStd_DataMapOfStringByte: ...

class TDataStd_HDataMapOfStringHArray1OfInteger(Standard_Transient):
    @overload
    def __init__(self, NbBuckets: Optional[int] = 1) -> None: ...
    @overload
    def __init__(self, theOther: TDataStd_DataMapOfStringHArray1OfInteger) -> None: ...
    def ChangeMap(self) -> TDataStd_DataMapOfStringHArray1OfInteger: ...
    def Map(self) -> TDataStd_DataMapOfStringHArray1OfInteger: ...

class TDataStd_HDataMapOfStringHArray1OfReal(Standard_Transient):
    @overload
    def __init__(self, NbBuckets: Optional[int] = 1) -> None: ...
    @overload
    def __init__(self, theOther: TDataStd_DataMapOfStringHArray1OfReal) -> None: ...
    def ChangeMap(self) -> TDataStd_DataMapOfStringHArray1OfReal: ...
    def Map(self) -> TDataStd_DataMapOfStringHArray1OfReal: ...

class TDataStd_HDataMapOfStringInteger(Standard_Transient):
    @overload
    def __init__(self, NbBuckets: Optional[int] = 1) -> None: ...
    @overload
    def __init__(self, theOther: TColStd_DataMapOfStringInteger) -> None: ...
    def ChangeMap(self) -> TColStd_DataMapOfStringInteger: ...
    def Map(self) -> TColStd_DataMapOfStringInteger: ...

class TDataStd_HDataMapOfStringReal(Standard_Transient):
    @overload
    def __init__(self, NbBuckets: Optional[int] = 1) -> None: ...
    @overload
    def __init__(self, theOther: TDataStd_DataMapOfStringReal) -> None: ...
    def ChangeMap(self) -> TDataStd_DataMapOfStringReal: ...
    def Map(self) -> TDataStd_DataMapOfStringReal: ...

class TDataStd_HDataMapOfStringString(Standard_Transient):
    @overload
    def __init__(self, NbBuckets: Optional[int] = 1) -> None: ...
    @overload
    def __init__(self, theOther: TDataStd_DataMapOfStringString) -> None: ...
    def ChangeMap(self) -> TDataStd_DataMapOfStringString: ...
    def Map(self) -> TDataStd_DataMapOfStringString: ...

class TDataStd_IntPackedMap(TDF_Attribute):
    def __init__(self) -> None: ...
    def Add(self, theKey: int) -> bool: ...
    @overload
    def ChangeMap(self, theMap: TColStd_HPackedMapOfInteger) -> bool: ...
    @overload
    def ChangeMap(self, theMap: TColStd_PackedMapOfInteger) -> bool: ...
    def Clear(self) -> bool: ...
    def Contains(self, theKey: int) -> bool: ...
    def DeltaOnModification(self, anOldAttribute: TDF_Attribute) -> TDF_DeltaOnModification: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Extent(self) -> int: ...
    def GetDelta(self) -> bool: ...
    def GetHMap(self) -> TColStd_HPackedMapOfInteger: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def GetMap(self) -> TColStd_PackedMapOfInteger: ...
    def ID(self) -> Standard_GUID: ...
    def IsEmpty(self) -> bool: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Remove(self, theKey: int) -> bool: ...
    def Restore(self, with_: TDF_Attribute) -> None: ...
    @staticmethod
    def Set(label: TDF_Label, isDelta: Optional[bool] = False) -> TDataStd_IntPackedMap: ...
    def SetDelta(self, isDelta: bool) -> None: ...

class TDataStd_Integer(TDF_Attribute):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Get(self) -> int: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def IsCaptured(self) -> bool: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, value: int) -> TDataStd_Integer: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, guid: Standard_GUID, value: int) -> TDataStd_Integer: ...
    @overload
    def Set(self, V: int) -> None: ...
    @overload
    def SetID(self, guid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...

class TDataStd_IntegerArray(TDF_Attribute):
    def __init__(self) -> None: ...
    def Array(self) -> TColStd_HArray1OfInteger: ...
    def ChangeArray(self, newArray: TColStd_HArray1OfInteger, isCheckItems: Optional[bool] = True) -> None: ...
    def DeltaOnModification(self, anOldAttribute: TDF_Attribute) -> TDF_DeltaOnModification: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetDelta(self) -> bool: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def Init(self, lower: int, upper: int) -> None: ...
    def Length(self) -> int: ...
    def Lower(self) -> int: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, lower: int, upper: int, isDelta: Optional[bool] = False) -> TDataStd_IntegerArray: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID, lower: int, upper: int, isDelta: Optional[bool] = False) -> TDataStd_IntegerArray: ...
    def SetDelta(self, isDelta: bool) -> None: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...
    def SetValue(self, Index: int, Value: int) -> None: ...
    def Upper(self) -> int: ...
    def Value(self, Index: int) -> int: ...

class TDataStd_IntegerList(TDF_Attribute):
    def __init__(self) -> None: ...
    def Append(self, value: int) -> None: ...
    def Clear(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Extent(self) -> int: ...
    def First(self) -> int: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def InsertAfter(self, value: int, after_value: int) -> bool: ...
    def InsertAfterByIndex(self, index: int, after_value: int) -> bool: ...
    def InsertBefore(self, value: int, before_value: int) -> bool: ...
    def InsertBeforeByIndex(self, index: int, before_value: int) -> bool: ...
    def IsEmpty(self) -> bool: ...
    def Last(self) -> int: ...
    def List(self) -> TColStd_ListOfInteger: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Prepend(self, value: int) -> None: ...
    def Remove(self, value: int) -> bool: ...
    def RemoveByIndex(self, index: int) -> bool: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_IntegerList: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID) -> TDataStd_IntegerList: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...

class TDataStd_NamedData(TDF_Attribute):
    def __init__(self) -> None: ...
    def ChangeArraysOfIntegers(self, theArraysOfIntegers: TDataStd_DataMapOfStringHArray1OfInteger) -> None: ...
    def ChangeArraysOfReals(self, theArraysOfReals: TDataStd_DataMapOfStringHArray1OfReal) -> None: ...
    def ChangeBytes(self, theBytes: TDataStd_DataMapOfStringByte) -> None: ...
    def ChangeIntegers(self, theIntegers: TColStd_DataMapOfStringInteger) -> None: ...
    def ChangeReals(self, theReals: TDataStd_DataMapOfStringReal) -> None: ...
    def ChangeStrings(self, theStrings: TDataStd_DataMapOfStringString) -> None: ...
    def Clear(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetArrayOfIntegers(self, theName: str) -> TColStd_HArray1OfInteger: ...
    def GetArrayOfReals(self, theName: str) -> TColStd_HArray1OfReal: ...
    def GetArraysOfIntegersContainer(self) -> TDataStd_DataMapOfStringHArray1OfInteger: ...
    def GetArraysOfRealsContainer(self) -> TDataStd_DataMapOfStringHArray1OfReal: ...
    def GetByte(self, theName: str) -> str: ...
    def GetBytesContainer(self) -> TDataStd_DataMapOfStringByte: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def GetInteger(self, theName: str) -> int: ...
    def GetIntegersContainer(self) -> TColStd_DataMapOfStringInteger: ...
    def GetReal(self, theName: str) -> float: ...
    def GetRealsContainer(self) -> TDataStd_DataMapOfStringReal: ...
    def GetString(self, theName: str) -> str: ...
    def GetStringsContainer(self) -> TDataStd_DataMapOfStringString: ...
    def HasArrayOfIntegers(self, theName: str) -> bool: ...
    def HasArrayOfReals(self, theName: str) -> bool: ...
    def HasArraysOfIntegers(self) -> bool: ...
    def HasArraysOfReals(self) -> bool: ...
    def HasByte(self, theName: str) -> bool: ...
    def HasBytes(self) -> bool: ...
    def HasDeferredData(self) -> bool: ...
    def HasInteger(self, theName: str) -> bool: ...
    def HasIntegers(self) -> bool: ...
    def HasReal(self, theName: str) -> bool: ...
    def HasReals(self) -> bool: ...
    def HasString(self, theName: str) -> bool: ...
    def HasStrings(self) -> bool: ...
    def ID(self) -> Standard_GUID: ...
    def LoadDeferredData(self, theToKeepDeferred: Optional[bool] = false) -> bool: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_NamedData: ...
    def SetArrayOfIntegers(self, theName: str, theArrayOfIntegers: TColStd_HArray1OfInteger) -> None: ...
    def SetArrayOfReals(self, theName: str, theArrayOfReals: TColStd_HArray1OfReal) -> None: ...
    def SetByte(self, theName: str, theByte: str) -> None: ...
    def SetInteger(self, theName: str, theInteger: int) -> None: ...
    def SetReal(self, theName: str, theReal: float) -> None: ...
    def SetString(self, theName: str, theString: str) -> None: ...
    def UnloadDeferredData(self) -> bool: ...
    def clear(self) -> None: ...
    def setArrayOfIntegers(self, theName: str, theArrayOfIntegers: TColStd_HArray1OfInteger) -> None: ...
    def setArrayOfReals(self, theName: str, theArrayOfReals: TColStd_HArray1OfReal) -> None: ...
    def setByte(self, theName: str, theByte: str) -> None: ...
    def setInteger(self, theName: str, theInteger: int) -> None: ...
    def setReal(self, theName: str, theReal: float) -> None: ...
    def setString(self, theName: str, theString: str) -> None: ...

class TDataStd_Real(TDF_Attribute):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Get(self) -> float: ...
    def GetDimension(self) -> TDataStd_RealEnum: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def IsCaptured(self) -> bool: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, value: float) -> TDataStd_Real: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, guid: Standard_GUID, value: float) -> TDataStd_Real: ...
    @overload
    def Set(self, V: float) -> None: ...
    def SetDimension(self, DIM: TDataStd_RealEnum) -> None: ...
    @overload
    def SetID(self, guid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...

class TDataStd_RealArray(TDF_Attribute):
    def __init__(self) -> None: ...
    def Array(self) -> TColStd_HArray1OfReal: ...
    def ChangeArray(self, newArray: TColStd_HArray1OfReal, isCheckItems: Optional[bool] = True) -> None: ...
    def DeltaOnModification(self, anOldAttribute: TDF_Attribute) -> TDF_DeltaOnModification: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetDelta(self) -> bool: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def Init(self, lower: int, upper: int) -> None: ...
    def Length(self) -> int: ...
    def Lower(self) -> int: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, lower: int, upper: int, isDelta: Optional[bool] = False) -> TDataStd_RealArray: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID, lower: int, upper: int, isDelta: Optional[bool] = False) -> TDataStd_RealArray: ...
    def SetDelta(self, isDelta: bool) -> None: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...
    def SetValue(self, Index: int, Value: float) -> None: ...
    def Upper(self) -> int: ...
    def Value(self, Index: int) -> float: ...

class TDataStd_RealList(TDF_Attribute):
    def __init__(self) -> None: ...
    def Append(self, value: float) -> None: ...
    def Clear(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Extent(self) -> int: ...
    def First(self) -> float: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def InsertAfter(self, value: float, after_value: float) -> bool: ...
    def InsertAfterByIndex(self, index: int, after_value: float) -> bool: ...
    def InsertBefore(self, value: float, before_value: float) -> bool: ...
    def InsertBeforeByIndex(self, index: int, before_value: float) -> bool: ...
    def IsEmpty(self) -> bool: ...
    def Last(self) -> float: ...
    def List(self) -> TColStd_ListOfReal: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Prepend(self, value: float) -> None: ...
    def Remove(self, value: float) -> bool: ...
    def RemoveByIndex(self, index: int) -> bool: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_RealList: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID) -> TDataStd_RealList: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...

class TDataStd_ReferenceArray(TDF_Attribute):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def Init(self, lower: int, upper: int) -> None: ...
    def InternalArray(self) -> TDataStd_HLabelArray1: ...
    def Length(self) -> int: ...
    def Lower(self) -> int: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def References(self, DS: TDF_DataSet) -> None: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, lower: int, upper: int) -> TDataStd_ReferenceArray: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID, lower: int, upper: int) -> TDataStd_ReferenceArray: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...
    def SetInternalArray(self, values: TDataStd_HLabelArray1, isCheckItems: Optional[bool] = True) -> None: ...
    def SetValue(self, index: int, value: TDF_Label) -> None: ...
    def Upper(self) -> int: ...
    def Value(self, Index: int) -> TDF_Label: ...

class TDataStd_ReferenceList(TDF_Attribute):
    def __init__(self) -> None: ...
    def Append(self, value: TDF_Label) -> None: ...
    def Clear(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Extent(self) -> int: ...
    def First(self) -> TDF_Label: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    @overload
    def InsertAfter(self, value: TDF_Label, after_value: TDF_Label) -> bool: ...
    @overload
    def InsertAfter(self, index: int, after_value: TDF_Label) -> bool: ...
    @overload
    def InsertBefore(self, value: TDF_Label, before_value: TDF_Label) -> bool: ...
    @overload
    def InsertBefore(self, index: int, before_value: TDF_Label) -> bool: ...
    def IsEmpty(self) -> bool: ...
    def Last(self) -> TDF_Label: ...
    def List(self) -> TDF_LabelList: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Prepend(self, value: TDF_Label) -> None: ...
    def References(self, DS: TDF_DataSet) -> None: ...
    @overload
    def Remove(self, value: TDF_Label) -> bool: ...
    @overload
    def Remove(self, index: int) -> bool: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_ReferenceList: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, theGuid: Standard_GUID) -> TDataStd_ReferenceList: ...
    @overload
    def SetID(self, theGuid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...

class TDataStd_TreeNode(TDF_Attribute):
    def __init__(self) -> None: ...
    def AfterAddition(self) -> None: ...
    def AfterResume(self) -> None: ...
    def AfterUndo(self, anAttDelta: TDF_AttributeDelta, forceIt: Optional[bool] = False) -> bool: ...
    def Append(self, Child: TDataStd_TreeNode) -> bool: ...
    def BeforeForget(self) -> None: ...
    def BeforeUndo(self, anAttDelta: TDF_AttributeDelta, forceIt: Optional[bool] = False) -> bool: ...
    def Depth(self) -> int: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Father(self) -> TDataStd_TreeNode: ...
    @staticmethod
    def Find(L: TDF_Label, T: TDataStd_TreeNode) -> bool: ...
    def FindLast(self) -> TDataStd_TreeNode: ...
    def First(self) -> TDataStd_TreeNode: ...
    @staticmethod
    def GetDefaultTreeID() -> Standard_GUID: ...
    def HasFather(self) -> bool: ...
    def HasFirst(self) -> bool: ...
    def HasLast(self) -> bool: ...
    def HasNext(self) -> bool: ...
    def HasPrevious(self) -> bool: ...
    def ID(self) -> Standard_GUID: ...
    def InsertAfter(self, Node: TDataStd_TreeNode) -> bool: ...
    def InsertBefore(self, Node: TDataStd_TreeNode) -> bool: ...
    def IsAscendant(self, of: TDataStd_TreeNode) -> bool: ...
    def IsChild(self, of: TDataStd_TreeNode) -> bool: ...
    def IsDescendant(self, of: TDataStd_TreeNode) -> bool: ...
    def IsFather(self, of: TDataStd_TreeNode) -> bool: ...
    def IsRoot(self) -> bool: ...
    def Last(self) -> TDataStd_TreeNode: ...
    def NbChildren(self, allLevels: Optional[bool] = False) -> int: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Next(self) -> TDataStd_TreeNode: ...
    def Paste(self, into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Prepend(self, Child: TDataStd_TreeNode) -> bool: ...
    def Previous(self) -> TDataStd_TreeNode: ...
    def References(self, aDataSet: TDF_DataSet) -> None: ...
    def Remove(self) -> bool: ...
    def Restore(self, with_: TDF_Attribute) -> None: ...
    def Root(self) -> TDataStd_TreeNode: ...
    @overload
    @staticmethod
    def Set(L: TDF_Label) -> TDataStd_TreeNode: ...
    @overload
    @staticmethod
    def Set(L: TDF_Label, ExplicitTreeID: Standard_GUID) -> TDataStd_TreeNode: ...
    def SetFather(self, F: TDataStd_TreeNode) -> None: ...
    def SetFirst(self, F: TDataStd_TreeNode) -> None: ...
    def SetLast(self, F: TDataStd_TreeNode) -> None: ...
    def SetNext(self, F: TDataStd_TreeNode) -> None: ...
    def SetPrevious(self, F: TDataStd_TreeNode) -> None: ...
    def SetTreeID(self, explicitID: Standard_GUID) -> None: ...

class TDataStd_UAttribute(TDF_Attribute):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def ID(self) -> Standard_GUID: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def References(self, DS: TDF_DataSet) -> None: ...
    def Restore(self, with_: TDF_Attribute) -> None: ...
    @staticmethod
    def Set(label: TDF_Label, LocalID: Standard_GUID) -> TDataStd_UAttribute: ...
    def SetID(self, LocalID: Standard_GUID) -> None: ...

class TDataStd_Variable(TDF_Attribute):
    def __init__(self) -> None: ...
    def Assign(self) -> TDataStd_Expression: ...
    def Constant(self, status: bool) -> None: ...
    def Desassign(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Expression(self) -> TDataStd_Expression: ...
    def Get(self) -> float: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def IsAssigned(self) -> bool: ...
    def IsCaptured(self) -> bool: ...
    def IsConstant(self) -> bool: ...
    def IsValued(self) -> bool: ...
    @overload
    def Name(self, string: str) -> None: ...
    @overload
    def Name(self) -> str: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def Real(self) -> TDataStd_Real: ...
    def References(self, DS: TDF_DataSet) -> None: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_Variable: ...
    @overload
    def Set(self, value: float) -> None: ...
    @overload
    def Set(self, value: float, dimension: TDataStd_RealEnum) -> None: ...
    @overload
    def Unit(self, unit: str) -> None: ...
    @overload
    def Unit(self) -> str: ...

class TDataStd_Comment(TDataStd_GenericExtString):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_Comment: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, string: str) -> TDataStd_Comment: ...
    @overload
    def Set(self, S: str) -> None: ...
    @overload
    def SetID(self, guid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...

class TDataStd_Directory(TDataStd_GenericEmpty):
    def __init__(self) -> None: ...
    @staticmethod
    def AddDirectory(dir: TDataStd_Directory) -> TDataStd_Directory: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    @staticmethod
    def Find(current: TDF_Label, D: TDataStd_Directory) -> bool: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    @staticmethod
    def MakeObjectLabel(dir: TDataStd_Directory) -> TDF_Label: ...
    @staticmethod
    def New(label: TDF_Label) -> TDataStd_Directory: ...

class TDataStd_Name(TDataStd_GenericExtString):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, string: str) -> TDataStd_Name: ...
    @overload
    @staticmethod
    def Set(label: TDF_Label, guid: Standard_GUID, string: str) -> TDataStd_Name: ...
    @overload
    def Set(self, S: str) -> None: ...
    @overload
    def SetID(self, guid: Standard_GUID) -> None: ...
    @overload
    def SetID(self) -> None: ...

class TDataStd_NoteBook(TDataStd_GenericEmpty):
    def __init__(self) -> None: ...
    @overload
    def Append(self, value: float, isExported: Optional[bool] = False) -> TDataStd_Real: ...
    @overload
    def Append(self, value: int, isExported: Optional[bool] = False) -> TDataStd_Integer: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    @staticmethod
    def Find(current: TDF_Label, N: TDataStd_NoteBook) -> bool: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    @staticmethod
    def New(label: TDF_Label) -> TDataStd_NoteBook: ...

class TDataStd_Relation(TDataStd_Expression):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def GetRelation(self) -> str: ...
    def ID(self) -> Standard_GUID: ...
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_Relation: ...
    def SetRelation(self, E: str) -> None: ...

class TDataStd_Tick(TDataStd_GenericEmpty):
    def __init__(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    @staticmethod
    def Set(label: TDF_Label) -> TDataStd_Tick: ...

#classnotwrapped
class TDataStd_GenericEmpty: ...

#classnotwrapped
class TDataStd_GenericExtString: ...

# harray1 classes

class TDataStd_HLabelArray1(TDataStd_LabelArray1, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> TDataStd_LabelArray1: ...

# harray2 classes
# hsequence classes

