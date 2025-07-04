from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Message import *
from OCC.Core.TCollection import *
from OCC.Core.TopAbs import *
from OCC.Core.TopLoc import *


class topods:
    @overload
    @staticmethod
    def CompSolid(S: TopoDS_Shape) -> TopoDS_CompSolid: ...
    @overload
    @staticmethod
    def Compound(S: TopoDS_Shape) -> TopoDS_Compound: ...
    @overload
    @staticmethod
    def Edge(S: TopoDS_Shape) -> TopoDS_Edge: ...
    @overload
    @staticmethod
    def Face(S: TopoDS_Shape) -> TopoDS_Face: ...
    @overload
    @staticmethod
    def Shell(S: TopoDS_Shape) -> TopoDS_Shell: ...
    @overload
    @staticmethod
    def Solid(S: TopoDS_Shape) -> TopoDS_Solid: ...
    @overload
    @staticmethod
    def Vertex(S: TopoDS_Shape) -> TopoDS_Vertex: ...
    @overload
    @staticmethod
    def Wire(S: TopoDS_Shape) -> TopoDS_Wire: ...

class TopoDS_AlertAttribute(Message_AttributeStream):
    def __init__(self, theShape: TopoDS_Shape, theName: Optional[str] = TCollection_AsciiString()) -> None: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetShape(self) -> TopoDS_Shape: ...
    @staticmethod
    def Send(theMessenger: Message_Messenger, theShape: TopoDS_Shape) -> None: ...

class TopoDS_AlertWithShape(Message_Alert):
    def __init__(self, theShape: TopoDS_Shape) -> None: ...
    def GetShape(self) -> TopoDS_Shape: ...
    def Merge(self, theTarget: Message_Alert) -> bool: ...
    def SetShape(self, theShape: TopoDS_Shape) -> None: ...
    def SupportsMerge(self) -> bool: ...

class TopoDS_Builder:
    def Add(self, S: TopoDS_Shape, C: TopoDS_Shape) -> None: ...
    def MakeCompSolid(self, C: TopoDS_CompSolid) -> None: ...
    def MakeCompound(self, C: TopoDS_Compound) -> None: ...
    def MakeShell(self, S: TopoDS_Shell) -> None: ...
    def MakeSolid(self, S: TopoDS_Solid) -> None: ...
    def MakeWire(self, W: TopoDS_Wire) -> None: ...
    def Remove(self, S: TopoDS_Shape, C: TopoDS_Shape) -> None: ...

class TopoDS_HShape(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, aShape: TopoDS_Shape) -> None: ...
    def ChangeShape(self) -> TopoDS_Shape: ...
    @overload
    def Shape(self, aShape: TopoDS_Shape) -> None: ...
    @overload
    def Shape(self) -> TopoDS_Shape: ...

class TopoDS_Iterator:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shape, cumOri: Optional[bool] = True, cumLoc: Optional[bool] = True) -> None: ...
    def Initialize(self, S: TopoDS_Shape, cumOri: Optional[bool] = True, cumLoc: Optional[bool] = True) -> None: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def Value(self) -> TopoDS_Shape: ...

class TopoDS_Shape:
    @overload
    def __init__(self) -> None: ...
    @overload
    def Checked(self) -> bool: ...
    @overload
    def Checked(self, theIsChecked: bool) -> None: ...
    @overload
    def Closed(self) -> bool: ...
    @overload
    def Closed(self, theIsClosed: bool) -> None: ...
    def Complement(self) -> None: ...
    def Complemented(self) -> TopoDS_Shape: ...
    def Compose(self, theOrient: TopAbs_Orientation) -> None: ...
    def Composed(self, theOrient: TopAbs_Orientation) -> TopoDS_Shape: ...
    @overload
    def Convex(self) -> bool: ...
    @overload
    def Convex(self, theIsConvex: bool) -> None: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def EmptyCopied(self) -> TopoDS_Shape: ...
    def EmptyCopy(self) -> None: ...
    @overload
    def Free(self) -> bool: ...
    @overload
    def Free(self, theIsFree: bool) -> None: ...
    @overload
    def Infinite(self) -> bool: ...
    @overload
    def Infinite(self, theIsInfinite: bool) -> None: ...
    def IsEqual(self, theOther: TopoDS_Shape) -> bool: ...
    def IsNotEqual(self, theOther: TopoDS_Shape) -> bool: ...
    def IsNull(self) -> bool: ...
    def IsPartner(self, theOther: TopoDS_Shape) -> bool: ...
    def IsSame(self, theOther: TopoDS_Shape) -> bool: ...
    def Located(self, theLoc: TopLoc_Location, theRaiseExc: Optional[bool] = True) -> TopoDS_Shape: ...
    @overload
    def Location(self) -> TopLoc_Location: ...
    @overload
    def Location(self, theLoc: TopLoc_Location, theRaiseExc: Optional[bool] = True) -> None: ...
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Locked(self, theIsLocked: bool) -> None: ...
    @overload
    def Modified(self) -> bool: ...
    @overload
    def Modified(self, theIsModified: bool) -> None: ...
    def Move(self, thePosition: TopLoc_Location, theRaiseExc: Optional[bool] = True) -> None: ...
    def Moved(self, thePosition: TopLoc_Location, theRaiseExc: Optional[bool] = True) -> TopoDS_Shape: ...
    def NbChildren(self) -> int: ...
    def Nullify(self) -> None: ...
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientable(self, theIsOrientable: bool) -> None: ...
    @overload
    def Orientation(self) -> TopAbs_Orientation: ...
    @overload
    def Orientation(self, theOrient: TopAbs_Orientation) -> None: ...
    def Oriented(self, theOrient: TopAbs_Orientation) -> TopoDS_Shape: ...
    def Reverse(self) -> None: ...
    def Reversed(self) -> TopoDS_Shape: ...
    def ShapeType(self) -> TopAbs_ShapeEnum: ...
    @overload
    def TShape(self) -> TopoDS_TShape: ...
    @overload
    def TShape(self, theTShape: TopoDS_TShape) -> None: ...

class TopoDS_TShape(Standard_Transient):
    @overload
    def Checked(self) -> bool: ...
    @overload
    def Checked(self, theIsChecked: bool) -> None: ...
    @overload
    def Closed(self) -> bool: ...
    @overload
    def Closed(self, theIsClosed: bool) -> None: ...
    @overload
    def Convex(self) -> bool: ...
    @overload
    def Convex(self, theIsConvex: bool) -> None: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def EmptyCopy(self) -> TopoDS_TShape: ...
    @overload
    def Free(self) -> bool: ...
    @overload
    def Free(self, theIsFree: bool) -> None: ...
    @overload
    def Infinite(self) -> bool: ...
    @overload
    def Infinite(self, theIsInfinite: bool) -> None: ...
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Locked(self, theIsLocked: bool) -> None: ...
    @overload
    def Modified(self) -> bool: ...
    @overload
    def Modified(self, theIsModified: bool) -> None: ...
    def NbChildren(self) -> int: ...
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientable(self, theIsOrientable: bool) -> None: ...
    def ShapeType(self) -> TopAbs_ShapeEnum: ...

class TopoDS_CompSolid(TopoDS_Shape):
    def __init__(self) -> None: ...

class TopoDS_Compound(TopoDS_Shape):
    def __init__(self) -> None: ...

class TopoDS_Edge(TopoDS_Shape):
    def __init__(self) -> None: ...

class TopoDS_Face(TopoDS_Shape):
    def __init__(self) -> None: ...

class TopoDS_Shell(TopoDS_Shape):
    def __init__(self) -> None: ...

class TopoDS_Solid(TopoDS_Shape):
    def __init__(self) -> None: ...

class TopoDS_TCompSolid(TopoDS_TShape):
    def __init__(self) -> None: ...
    def EmptyCopy(self) -> TopoDS_TShape: ...
    def ShapeType(self) -> TopAbs_ShapeEnum: ...

class TopoDS_TCompound(TopoDS_TShape):
    def __init__(self) -> None: ...
    def EmptyCopy(self) -> TopoDS_TShape: ...
    def ShapeType(self) -> TopAbs_ShapeEnum: ...

class TopoDS_TEdge(TopoDS_TShape):
    def ShapeType(self) -> TopAbs_ShapeEnum: ...

class TopoDS_TFace(TopoDS_TShape):
    def __init__(self) -> None: ...
    def EmptyCopy(self) -> TopoDS_TShape: ...
    def ShapeType(self) -> TopAbs_ShapeEnum: ...

class TopoDS_TShell(TopoDS_TShape):
    def __init__(self) -> None: ...
    def EmptyCopy(self) -> TopoDS_TShape: ...
    def ShapeType(self) -> TopAbs_ShapeEnum: ...

class TopoDS_TSolid(TopoDS_TShape):
    def __init__(self) -> None: ...
    def EmptyCopy(self) -> TopoDS_TShape: ...
    def ShapeType(self) -> TopAbs_ShapeEnum: ...

class TopoDS_TVertex(TopoDS_TShape):
    def ShapeType(self) -> TopAbs_ShapeEnum: ...

class TopoDS_TWire(TopoDS_TShape):
    def __init__(self) -> None: ...
    def EmptyCopy(self) -> TopoDS_TShape: ...
    def ShapeType(self) -> TopAbs_ShapeEnum: ...

class TopoDS_Vertex(TopoDS_Shape):
    def __init__(self) -> None: ...

class TopoDS_Wire(TopoDS_Shape):
    def __init__(self) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

