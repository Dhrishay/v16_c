from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Message import *
from OCC.Core.TDF import *
from OCC.Core.XmlObjMgt import *
from OCC.Core.TCollection import *


class xmlmdf:
    @staticmethod
    def AddDrivers(aDriverTable: XmlMDF_ADriverTable, theMessageDriver: Message_Messenger) -> None: ...
    @overload
    @staticmethod
    def FromTo(aSource: TDF_Data, aTarget: XmlObjMgt_Element, aReloc: XmlObjMgt_SRelocationTable, aDrivers: XmlMDF_ADriverTable, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    @staticmethod
    def FromTo(aSource: XmlObjMgt_Element, aTarget: TDF_Data, aReloc: XmlObjMgt_RRelocationTable, aDrivers: XmlMDF_ADriverTable, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...

class XmlMDF_ADriver(Standard_Transient):
    def MessageDriver(self) -> Message_Messenger: ...
    def Namespace(self) -> str: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(self, aSource: XmlObjMgt_Persistent, aTarget: TDF_Attribute, aRelocTable: XmlObjMgt_RRelocationTable) -> bool: ...
    @overload
    def Paste(self, aSource: TDF_Attribute, aTarget: XmlObjMgt_Persistent, aRelocTable: XmlObjMgt_SRelocationTable) -> None: ...
    def SourceType(self) -> Standard_Type: ...
    def TypeName(self) -> str: ...
    def VersionNumber(self) -> int: ...

class XmlMDF_ADriverTable(Standard_Transient):
    def __init__(self) -> None: ...
    @overload
    def AddDerivedDriver(self, theInstance: TDF_Attribute) -> None: ...
    @overload
    def AddDerivedDriver(self, theDerivedType: str) -> Standard_Type: ...
    def AddDriver(self, anHDriver: XmlMDF_ADriver) -> None: ...
    def CreateDrvMap(self, theDriverMap: XmlMDF_MapOfDriver) -> None: ...
    def GetDriver(self, theType: Standard_Type, theDriver: XmlMDF_ADriver) -> bool: ...

class XmlMDF_DerivedDriver(XmlMDF_ADriver):
    def __init__(self, theDerivative: TDF_Attribute, theBaseDriver: XmlMDF_ADriver) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(self, theSource: XmlObjMgt_Persistent, theTarget: TDF_Attribute, theRelocTable: XmlObjMgt_RRelocationTable) -> bool: ...
    @overload
    def Paste(self, theSource: TDF_Attribute, theTarget: XmlObjMgt_Persistent, theRelocTable: XmlObjMgt_SRelocationTable) -> None: ...
    def TypeName(self) -> str: ...

class XmlMDF_ReferenceDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(self, Source: XmlObjMgt_Persistent, Target: TDF_Attribute, RelocTable: XmlObjMgt_RRelocationTable) -> bool: ...
    @overload
    def Paste(self, Source: TDF_Attribute, Target: XmlObjMgt_Persistent, RelocTable: XmlObjMgt_SRelocationTable) -> None: ...

class XmlMDF_TagSourceDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(self, Source: XmlObjMgt_Persistent, Target: TDF_Attribute, RelocTable: XmlObjMgt_RRelocationTable) -> bool: ...
    @overload
    def Paste(self, Source: TDF_Attribute, Target: XmlObjMgt_Persistent, RelocTable: XmlObjMgt_SRelocationTable) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

