from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.Message import *
from OCC.Core.Geom2d import *
from OCC.Core.Geom import *
from OCC.Core.TopLoc import *
from OCC.Core.TopAbs import *

BinTools_LocationSetPtr = NewType("BinTools_LocationSetPtr", BinTools_LocationSet)

class BinTools_FormatVersion(IntEnum):
    BinTools_FormatVersion_VERSION_1: int = ...
    BinTools_FormatVersion_VERSION_2: int = ...
    BinTools_FormatVersion_VERSION_3: int = ...
    BinTools_FormatVersion_VERSION_4: int = ...
    BinTools_FormatVersion_CURRENT: int = ...

BinTools_FormatVersion_VERSION_1 = BinTools_FormatVersion.BinTools_FormatVersion_VERSION_1
BinTools_FormatVersion_VERSION_2 = BinTools_FormatVersion.BinTools_FormatVersion_VERSION_2
BinTools_FormatVersion_VERSION_3 = BinTools_FormatVersion.BinTools_FormatVersion_VERSION_3
BinTools_FormatVersion_VERSION_4 = BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4
BinTools_FormatVersion_CURRENT = BinTools_FormatVersion.BinTools_FormatVersion_CURRENT


class BinTools_ObjectType(IntEnum):
    BinTools_ObjectType_Unknown: int = ...
    BinTools_ObjectType_Reference8: int = ...
    BinTools_ObjectType_Reference16: int = ...
    BinTools_ObjectType_Reference32: int = ...
    BinTools_ObjectType_Reference64: int = ...
    BinTools_ObjectType_Location: int = ...
    BinTools_ObjectType_SimpleLocation: int = ...
    BinTools_ObjectType_EmptyLocation: int = ...
    BinTools_ObjectType_LocationEnd: int = ...
    BinTools_ObjectType_Curve: int = ...
    BinTools_ObjectType_EmptyCurve: int = ...
    BinTools_ObjectType_Curve2d: int = ...
    BinTools_ObjectType_EmptyCurve2d: int = ...
    BinTools_ObjectType_Surface: int = ...
    BinTools_ObjectType_EmptySurface: int = ...
    BinTools_ObjectType_Polygon3d: int = ...
    BinTools_ObjectType_EmptyPolygon3d: int = ...
    BinTools_ObjectType_PolygonOnTriangulation: int = ...
    BinTools_ObjectType_EmptyPolygonOnTriangulation: int = ...
    BinTools_ObjectType_Triangulation: int = ...
    BinTools_ObjectType_EmptyTriangulation: int = ...
    BinTools_ObjectType_EmptyShape: int = ...
    BinTools_ObjectType_EndShape: int = ...

BinTools_ObjectType_Unknown = BinTools_ObjectType.BinTools_ObjectType_Unknown
BinTools_ObjectType_Reference8 = BinTools_ObjectType.BinTools_ObjectType_Reference8
BinTools_ObjectType_Reference16 = BinTools_ObjectType.BinTools_ObjectType_Reference16
BinTools_ObjectType_Reference32 = BinTools_ObjectType.BinTools_ObjectType_Reference32
BinTools_ObjectType_Reference64 = BinTools_ObjectType.BinTools_ObjectType_Reference64
BinTools_ObjectType_Location = BinTools_ObjectType.BinTools_ObjectType_Location
BinTools_ObjectType_SimpleLocation = BinTools_ObjectType.BinTools_ObjectType_SimpleLocation
BinTools_ObjectType_EmptyLocation = BinTools_ObjectType.BinTools_ObjectType_EmptyLocation
BinTools_ObjectType_LocationEnd = BinTools_ObjectType.BinTools_ObjectType_LocationEnd
BinTools_ObjectType_Curve = BinTools_ObjectType.BinTools_ObjectType_Curve
BinTools_ObjectType_EmptyCurve = BinTools_ObjectType.BinTools_ObjectType_EmptyCurve
BinTools_ObjectType_Curve2d = BinTools_ObjectType.BinTools_ObjectType_Curve2d
BinTools_ObjectType_EmptyCurve2d = BinTools_ObjectType.BinTools_ObjectType_EmptyCurve2d
BinTools_ObjectType_Surface = BinTools_ObjectType.BinTools_ObjectType_Surface
BinTools_ObjectType_EmptySurface = BinTools_ObjectType.BinTools_ObjectType_EmptySurface
BinTools_ObjectType_Polygon3d = BinTools_ObjectType.BinTools_ObjectType_Polygon3d
BinTools_ObjectType_EmptyPolygon3d = BinTools_ObjectType.BinTools_ObjectType_EmptyPolygon3d
BinTools_ObjectType_PolygonOnTriangulation = BinTools_ObjectType.BinTools_ObjectType_PolygonOnTriangulation
BinTools_ObjectType_EmptyPolygonOnTriangulation = BinTools_ObjectType.BinTools_ObjectType_EmptyPolygonOnTriangulation
BinTools_ObjectType_Triangulation = BinTools_ObjectType.BinTools_ObjectType_Triangulation
BinTools_ObjectType_EmptyTriangulation = BinTools_ObjectType.BinTools_ObjectType_EmptyTriangulation
BinTools_ObjectType_EmptyShape = BinTools_ObjectType.BinTools_ObjectType_EmptyShape
BinTools_ObjectType_EndShape = BinTools_ObjectType.BinTools_ObjectType_EndShape

class bintools:
    @staticmethod
    def GetBool(IS: str) -> Tuple[Standard_IStream, bool]: ...
    @staticmethod
    def GetExtChar(IS: str, theValue: Standard_ExtCharacter) -> Standard_IStream: ...
    @staticmethod
    def GetInteger(IS: str) -> Tuple[Standard_IStream, int]: ...
    @staticmethod
    def GetReal(IS: str) -> Tuple[Standard_IStream, float]: ...
    @staticmethod
    def GetShortReal(IS: str) -> Tuple[Standard_IStream, float]: ...
    @staticmethod
    def PutBool(theValue: bool) -> Tuple[Standard_OStream, str]: ...
    @staticmethod
    def PutExtChar(theValue: Standard_ExtCharacter) -> Tuple[Standard_OStream, str]: ...
    @staticmethod
    def PutInteger(theValue: int) -> Tuple[Standard_OStream, str]: ...
    @staticmethod
    def PutReal(theValue: float) -> Tuple[Standard_OStream, str]: ...
    @staticmethod
    def PutShortReal(theValue: float) -> Tuple[Standard_OStream, str]: ...
    @overload
    @staticmethod
    def Read(theShape: TopoDS_Shape, theStream: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    @staticmethod
    def Read(theShape: TopoDS_Shape, theFile: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    @overload
    @staticmethod
    def Write(theShape: TopoDS_Shape, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    @overload
    @staticmethod
    def Write(theShape: TopoDS_Shape, theWithTriangles: bool, theWithNormals: bool, theVersion: BinTools_FormatVersion, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    @overload
    @staticmethod
    def Write(theShape: TopoDS_Shape, theFile: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    @overload
    @staticmethod
    def Write(theShape: TopoDS_Shape, theFile: str, theWithTriangles: bool, theWithNormals: bool, theVersion: BinTools_FormatVersion, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...

class BinTools_Curve2dSet:
    def __init__(self) -> None: ...
    def Add(self, C: Geom2d_Curve) -> int: ...
    def Clear(self) -> None: ...
    def Curve2d(self, I: int) -> Geom2d_Curve: ...
    def Index(self, C: Geom2d_Curve) -> int: ...
    def Read(self, IS: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @staticmethod
    def ReadCurve2d(IS: str, C: Geom2d_Curve) -> Standard_IStream: ...
    def Write(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    @staticmethod
    def WriteCurve2d(C: Geom2d_Curve, OS: BinTools_OStream) -> None: ...

class BinTools_CurveSet:
    def __init__(self) -> None: ...
    def Add(self, C: Geom_Curve) -> int: ...
    def Clear(self) -> None: ...
    def Curve(self, I: int) -> Geom_Curve: ...
    def Index(self, C: Geom_Curve) -> int: ...
    def Read(self, IS: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @staticmethod
    def ReadCurve(IS: str, C: Geom_Curve) -> Standard_IStream: ...
    def Write(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    @staticmethod
    def WriteCurve(C: Geom_Curve, OS: BinTools_OStream) -> None: ...

class BinTools_LocationSet:
    def __init__(self) -> None: ...
    def Add(self, L: TopLoc_Location) -> int: ...
    def Clear(self) -> None: ...
    def Index(self, L: TopLoc_Location) -> int: ...
    def Location(self, I: int) -> TopLoc_Location: ...
    def NbLocations(self) -> int: ...
    def Read(self, IS: str) -> None: ...
    def Write(self) -> str: ...

class BinTools_ShapeSetBase:
    def __init__(self) -> None: ...
    def Clear(self) -> None: ...
    def FormatNb(self) -> int: ...
    def IsWithNormals(self) -> bool: ...
    def IsWithTriangles(self) -> bool: ...
    def SetFormatNb(self, theFormatNb: int) -> None: ...
    def SetWithNormals(self, theWithNormals: bool) -> None: ...
    def SetWithTriangles(self, theWithTriangles: bool) -> None: ...

class BinTools_SurfaceSet:
    def __init__(self) -> None: ...
    def Add(self, S: Geom_Surface) -> int: ...
    def Clear(self) -> None: ...
    def Index(self, S: Geom_Surface) -> int: ...
    def Read(self, IS: str, therange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @staticmethod
    def ReadSurface(IS: str, S: Geom_Surface) -> Standard_IStream: ...
    def Surface(self, I: int) -> Geom_Surface: ...
    def Write(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    @staticmethod
    def WriteSurface(S: Geom_Surface, OS: BinTools_OStream) -> None: ...

class BinTools_ShapeReader(BinTools_ShapeSetBase):
    def __init__(self) -> None: ...
    def Clear(self) -> None: ...
    def Read(self, theStream: str, theShape: TopoDS_Shape) -> None: ...
    def ReadLocation(self, theStream: BinTools_IStream) -> TopLoc_Location: ...

class BinTools_ShapeSet(BinTools_ShapeSetBase):
    def __init__(self) -> None: ...
    def Add(self, S: TopoDS_Shape) -> int: ...
    def AddShape(self, S: TopoDS_Shape) -> None: ...
    def AddShapes(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
    def ChangeLocations(self) -> BinTools_LocationSet: ...
    def Clear(self) -> None: ...
    def Index(self, S: TopoDS_Shape) -> int: ...
    def Locations(self) -> BinTools_LocationSet: ...
    def NbShapes(self) -> int: ...
    @overload
    def Read(self, IS: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def ReadFlagsAndSubs(self, S: TopoDS_Shape, T: TopAbs_ShapeEnum, IS: str, NbShapes: int) -> None: ...
    def ReadGeometry(self, IS: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def ReadPolygon3D(self, IS: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def ReadPolygonOnTriangulation(self, IS: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def ReadShape(self, T: TopAbs_ShapeEnum, IS: str, S: TopoDS_Shape) -> None: ...
    def ReadSubs(self, S: TopoDS_Shape, IS: str, NbShapes: int) -> None: ...
    def ReadTriangulation(self, IS: str, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def Shape(self, I: int) -> TopoDS_Shape: ...
    @overload
    def Write(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    @overload
    def Write(self, S: TopoDS_Shape) -> str: ...
    def WriteGeometry(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    def WritePolygon3D(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    def WritePolygonOnTriangulation(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...
    def WriteShape(self, S: TopoDS_Shape) -> str: ...
    def WriteTriangulation(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> str: ...

class BinTools_ShapeWriter(BinTools_ShapeSetBase):
    def __init__(self) -> None: ...
    def Clear(self) -> None: ...
    def Write(self, theShape: TopoDS_Shape) -> str: ...
    def WriteLocation(self, theStream: BinTools_OStream, theLocation: TopLoc_Location) -> None: ...

#classnotwrapped
class BinTools_IStream: ...

#classnotwrapped
class BinTools_OStream: ...

# harray1 classes
# harray2 classes
# hsequence classes

