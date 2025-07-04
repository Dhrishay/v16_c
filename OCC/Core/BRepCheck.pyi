from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Adaptor3d import *
from OCC.Core.TopoDS import *
from OCC.Core.TopTools import *

# the following typedef cannot be wrapped as is
BRepCheck_HListOfStatus = NewType("BRepCheck_HListOfStatus", Any)
# the following typedef cannot be wrapped as is
BRepCheck_IndexedDataMapOfShapeResult = NewType("BRepCheck_IndexedDataMapOfShapeResult", Any)

class BRepCheck_ListOfStatus:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> BRepCheck_Status: ...
    def Last(self) -> BRepCheck_Status: ...
    def Append(self, theItem: BRepCheck_Status) -> BRepCheck_Status: ...
    def Prepend(self, theItem: BRepCheck_Status) -> BRepCheck_Status: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> BRepCheck_Status: ...
    def SetValue(self, theIndex: int, theValue: BRepCheck_Status) -> None: ...

class BRepCheck_Status(IntEnum):
    BRepCheck_NoError: int = ...
    BRepCheck_InvalidPointOnCurve: int = ...
    BRepCheck_InvalidPointOnCurveOnSurface: int = ...
    BRepCheck_InvalidPointOnSurface: int = ...
    BRepCheck_No3DCurve: int = ...
    BRepCheck_Multiple3DCurve: int = ...
    BRepCheck_Invalid3DCurve: int = ...
    BRepCheck_NoCurveOnSurface: int = ...
    BRepCheck_InvalidCurveOnSurface: int = ...
    BRepCheck_InvalidCurveOnClosedSurface: int = ...
    BRepCheck_InvalidSameRangeFlag: int = ...
    BRepCheck_InvalidSameParameterFlag: int = ...
    BRepCheck_InvalidDegeneratedFlag: int = ...
    BRepCheck_FreeEdge: int = ...
    BRepCheck_InvalidMultiConnexity: int = ...
    BRepCheck_InvalidRange: int = ...
    BRepCheck_EmptyWire: int = ...
    BRepCheck_RedundantEdge: int = ...
    BRepCheck_SelfIntersectingWire: int = ...
    BRepCheck_NoSurface: int = ...
    BRepCheck_InvalidWire: int = ...
    BRepCheck_RedundantWire: int = ...
    BRepCheck_IntersectingWires: int = ...
    BRepCheck_InvalidImbricationOfWires: int = ...
    BRepCheck_EmptyShell: int = ...
    BRepCheck_RedundantFace: int = ...
    BRepCheck_InvalidImbricationOfShells: int = ...
    BRepCheck_UnorientableShape: int = ...
    BRepCheck_NotClosed: int = ...
    BRepCheck_NotConnected: int = ...
    BRepCheck_SubshapeNotInShape: int = ...
    BRepCheck_BadOrientation: int = ...
    BRepCheck_BadOrientationOfSubshape: int = ...
    BRepCheck_InvalidPolygonOnTriangulation: int = ...
    BRepCheck_InvalidToleranceValue: int = ...
    BRepCheck_EnclosedRegion: int = ...
    BRepCheck_CheckFail: int = ...

BRepCheck_NoError = BRepCheck_Status.BRepCheck_NoError
BRepCheck_InvalidPointOnCurve = BRepCheck_Status.BRepCheck_InvalidPointOnCurve
BRepCheck_InvalidPointOnCurveOnSurface = BRepCheck_Status.BRepCheck_InvalidPointOnCurveOnSurface
BRepCheck_InvalidPointOnSurface = BRepCheck_Status.BRepCheck_InvalidPointOnSurface
BRepCheck_No3DCurve = BRepCheck_Status.BRepCheck_No3DCurve
BRepCheck_Multiple3DCurve = BRepCheck_Status.BRepCheck_Multiple3DCurve
BRepCheck_Invalid3DCurve = BRepCheck_Status.BRepCheck_Invalid3DCurve
BRepCheck_NoCurveOnSurface = BRepCheck_Status.BRepCheck_NoCurveOnSurface
BRepCheck_InvalidCurveOnSurface = BRepCheck_Status.BRepCheck_InvalidCurveOnSurface
BRepCheck_InvalidCurveOnClosedSurface = BRepCheck_Status.BRepCheck_InvalidCurveOnClosedSurface
BRepCheck_InvalidSameRangeFlag = BRepCheck_Status.BRepCheck_InvalidSameRangeFlag
BRepCheck_InvalidSameParameterFlag = BRepCheck_Status.BRepCheck_InvalidSameParameterFlag
BRepCheck_InvalidDegeneratedFlag = BRepCheck_Status.BRepCheck_InvalidDegeneratedFlag
BRepCheck_FreeEdge = BRepCheck_Status.BRepCheck_FreeEdge
BRepCheck_InvalidMultiConnexity = BRepCheck_Status.BRepCheck_InvalidMultiConnexity
BRepCheck_InvalidRange = BRepCheck_Status.BRepCheck_InvalidRange
BRepCheck_EmptyWire = BRepCheck_Status.BRepCheck_EmptyWire
BRepCheck_RedundantEdge = BRepCheck_Status.BRepCheck_RedundantEdge
BRepCheck_SelfIntersectingWire = BRepCheck_Status.BRepCheck_SelfIntersectingWire
BRepCheck_NoSurface = BRepCheck_Status.BRepCheck_NoSurface
BRepCheck_InvalidWire = BRepCheck_Status.BRepCheck_InvalidWire
BRepCheck_RedundantWire = BRepCheck_Status.BRepCheck_RedundantWire
BRepCheck_IntersectingWires = BRepCheck_Status.BRepCheck_IntersectingWires
BRepCheck_InvalidImbricationOfWires = BRepCheck_Status.BRepCheck_InvalidImbricationOfWires
BRepCheck_EmptyShell = BRepCheck_Status.BRepCheck_EmptyShell
BRepCheck_RedundantFace = BRepCheck_Status.BRepCheck_RedundantFace
BRepCheck_InvalidImbricationOfShells = BRepCheck_Status.BRepCheck_InvalidImbricationOfShells
BRepCheck_UnorientableShape = BRepCheck_Status.BRepCheck_UnorientableShape
BRepCheck_NotClosed = BRepCheck_Status.BRepCheck_NotClosed
BRepCheck_NotConnected = BRepCheck_Status.BRepCheck_NotConnected
BRepCheck_SubshapeNotInShape = BRepCheck_Status.BRepCheck_SubshapeNotInShape
BRepCheck_BadOrientation = BRepCheck_Status.BRepCheck_BadOrientation
BRepCheck_BadOrientationOfSubshape = BRepCheck_Status.BRepCheck_BadOrientationOfSubshape
BRepCheck_InvalidPolygonOnTriangulation = BRepCheck_Status.BRepCheck_InvalidPolygonOnTriangulation
BRepCheck_InvalidToleranceValue = BRepCheck_Status.BRepCheck_InvalidToleranceValue
BRepCheck_EnclosedRegion = BRepCheck_Status.BRepCheck_EnclosedRegion
BRepCheck_CheckFail = BRepCheck_Status.BRepCheck_CheckFail

class brepcheck:
    @staticmethod
    def Add(List: BRepCheck_ListOfStatus, Stat: BRepCheck_Status) -> None: ...
    @staticmethod
    def PrecCurve(aAC3D: Adaptor3d_Curve) -> float: ...
    @staticmethod
    def PrecSurface(aAHSurf: Adaptor3d_Surface) -> float: ...
    @staticmethod
    def Print(Stat: BRepCheck_Status) -> str: ...
    @staticmethod
    def SelfIntersection(W: TopoDS_Wire, F: TopoDS_Face, E1: TopoDS_Edge, E2: TopoDS_Edge) -> bool: ...

class BRepCheck_Analyzer:
    def __init__(self, S: TopoDS_Shape, GeomControls: Optional[bool] = True, theIsParallel: Optional[bool] = False, theIsExact: Optional[bool] = False) -> None: ...
    def Init(self, S: TopoDS_Shape, GeomControls: Optional[bool] = True) -> None: ...
    def IsExactMethod(self) -> bool: ...
    def IsParallel(self) -> bool: ...
    @overload
    def IsValid(self, S: TopoDS_Shape) -> bool: ...
    @overload
    def IsValid(self) -> bool: ...
    def Result(self, theSubS: TopoDS_Shape) -> BRepCheck_Result: ...
    def SetExactMethod(self, theIsExact: bool) -> None: ...
    def SetParallel(self, theIsParallel: bool) -> None: ...

class BRepCheck_Result(Standard_Transient):
    def Blind(self) -> None: ...
    def ContextualShape(self) -> TopoDS_Shape: ...
    def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
    def Init(self, S: TopoDS_Shape) -> None: ...
    def InitContextIterator(self) -> None: ...
    def IsBlind(self) -> bool: ...
    def IsMinimum(self) -> bool: ...
    def IsStatusOnShape(self, theShape: TopoDS_Shape) -> bool: ...
    def Minimum(self) -> None: ...
    def MoreShapeInContext(self) -> bool: ...
    def NextShapeInContext(self) -> None: ...
    def SetFailStatus(self, S: TopoDS_Shape) -> None: ...
    def SetParallel(self, theIsParallel: bool) -> None: ...
    def Status(self) -> BRepCheck_ListOfStatus: ...
    @overload
    def StatusOnShape(self) -> BRepCheck_ListOfStatus: ...
    @overload
    def StatusOnShape(self, theShape: TopoDS_Shape) -> BRepCheck_ListOfStatus: ...

class BRepCheck_Edge(BRepCheck_Result):
    def __init__(self, E: TopoDS_Edge) -> None: ...
    def Blind(self) -> None: ...
    def CheckPolygonOnTriangulation(self, theEdge: TopoDS_Edge) -> BRepCheck_Status: ...
    @overload
    def GeometricControls(self) -> bool: ...
    @overload
    def GeometricControls(self, B: bool) -> None: ...
    def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
    def IsExactMethod(self) -> bool: ...
    def Minimum(self) -> None: ...
    def SetExactMethod(self, theIsExact: bool) -> None: ...
    def SetStatus(self, theStatus: BRepCheck_Status) -> None: ...
    def Tolerance(self) -> float: ...

class BRepCheck_Face(BRepCheck_Result):
    def __init__(self, F: TopoDS_Face) -> None: ...
    def Blind(self) -> None: ...
    def ClassifyWires(self, Update: Optional[bool] = False) -> BRepCheck_Status: ...
    @overload
    def GeometricControls(self) -> bool: ...
    @overload
    def GeometricControls(self, B: bool) -> None: ...
    def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
    def IntersectWires(self, Update: Optional[bool] = False) -> BRepCheck_Status: ...
    def IsUnorientable(self) -> bool: ...
    def Minimum(self) -> None: ...
    def OrientationOfWires(self, Update: Optional[bool] = False) -> BRepCheck_Status: ...
    def SetStatus(self, theStatus: BRepCheck_Status) -> None: ...
    def SetUnorientable(self) -> None: ...

class BRepCheck_Shell(BRepCheck_Result):
    def __init__(self, S: TopoDS_Shell) -> None: ...
    def Blind(self) -> None: ...
    def Closed(self, Update: Optional[bool] = False) -> BRepCheck_Status: ...
    def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
    def IsUnorientable(self) -> bool: ...
    def Minimum(self) -> None: ...
    def NbConnectedSet(self, theSets: TopTools_ListOfShape) -> int: ...
    def Orientation(self, Update: Optional[bool] = False) -> BRepCheck_Status: ...
    def SetUnorientable(self) -> None: ...

class BRepCheck_Solid(BRepCheck_Result):
    def __init__(self, theS: TopoDS_Solid) -> None: ...
    def Blind(self) -> None: ...
    def InContext(self, theContextShape: TopoDS_Shape) -> None: ...
    def Minimum(self) -> None: ...

class BRepCheck_Vertex(BRepCheck_Result):
    def __init__(self, V: TopoDS_Vertex) -> None: ...
    def Blind(self) -> None: ...
    def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
    def Minimum(self) -> None: ...
    def Tolerance(self) -> float: ...

class BRepCheck_Wire(BRepCheck_Result):
    def __init__(self, W: TopoDS_Wire) -> None: ...
    def Blind(self) -> None: ...
    def Closed(self, Update: Optional[bool] = False) -> BRepCheck_Status: ...
    def Closed2d(self, F: TopoDS_Face, Update: Optional[bool] = False) -> BRepCheck_Status: ...
    @overload
    def GeometricControls(self) -> bool: ...
    @overload
    def GeometricControls(self, B: bool) -> None: ...
    def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
    def Minimum(self) -> None: ...
    def Orientation(self, F: TopoDS_Face, Update: Optional[bool] = False) -> BRepCheck_Status: ...
    def SelfIntersect(self, F: TopoDS_Face, E1: TopoDS_Edge, E2: TopoDS_Edge, Update: Optional[bool] = False) -> BRepCheck_Status: ...
    def SetStatus(self, theStatus: BRepCheck_Status) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

