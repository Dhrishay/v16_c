from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.IntRes2d import *
from OCC.Core.TopAbs import *
from OCC.Core.Geom2dAdaptor import *
from OCC.Core.Geom2d import *
from OCC.Core.HatchGen import *
from OCC.Core.Geom2dInt import *


class Geom2dHatch_Classifier:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, F: Geom2dHatch_Elements, P: gp_Pnt2d, Tol: float) -> None: ...
    def Edge(self) -> Geom2dAdaptor_Curve: ...
    def EdgeParameter(self) -> float: ...
    def NoWires(self) -> bool: ...
    def Perform(self, F: Geom2dHatch_Elements, P: gp_Pnt2d, Tol: float) -> None: ...
    def Position(self) -> IntRes2d_Position: ...
    def Rejected(self) -> bool: ...
    def State(self) -> TopAbs_State: ...

class Geom2dHatch_Element:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Curve: Geom2dAdaptor_Curve, Orientation: Optional[TopAbs_Orientation] = TopAbs_FORWARD) -> None: ...
    def ChangeCurve(self) -> Geom2dAdaptor_Curve: ...
    def Curve(self) -> Geom2dAdaptor_Curve: ...
    @overload
    def Orientation(self, Orientation: TopAbs_Orientation) -> None: ...
    @overload
    def Orientation(self) -> TopAbs_Orientation: ...

class Geom2dHatch_Elements:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Other: Geom2dHatch_Elements) -> None: ...
    def Bind(self, K: int, I: Geom2dHatch_Element) -> bool: ...
    def ChangeFind(self, K: int) -> Geom2dHatch_Element: ...
    def CheckPoint(self, P: gp_Pnt2d) -> bool: ...
    def Clear(self) -> None: ...
    def CurrentEdge(self, E: Geom2dAdaptor_Curve) -> TopAbs_Orientation: ...
    def Find(self, K: int) -> Geom2dHatch_Element: ...
    def InitEdges(self) -> None: ...
    def InitWires(self) -> None: ...
    def IsBound(self, K: int) -> bool: ...
    def MoreEdges(self) -> bool: ...
    def MoreWires(self) -> bool: ...
    def NextEdge(self) -> None: ...
    def NextWire(self) -> None: ...
    def OtherSegment(self, P: gp_Pnt2d, L: gp_Lin2d) -> Tuple[bool, float]: ...
    def Reject(self, P: gp_Pnt2d) -> bool: ...
    def RejectEdge(self, L: gp_Lin2d, Par: float) -> bool: ...
    def RejectWire(self, L: gp_Lin2d, Par: float) -> bool: ...
    def Segment(self, P: gp_Pnt2d, L: gp_Lin2d) -> Tuple[bool, float]: ...
    def UnBind(self, K: int) -> bool: ...

class Geom2dHatch_FClass2dOfClassifier:
    def __init__(self) -> None: ...
    def ClosestIntersection(self) -> int: ...
    def Compare(self, E: Geom2dAdaptor_Curve, Or: TopAbs_Orientation) -> None: ...
    def Intersector(self) -> Geom2dHatch_Intersector: ...
    def IsHeadOrEnd(self) -> bool: ...
    def Parameter(self) -> float: ...
    def Reset(self, L: gp_Lin2d, P: float, Tol: float) -> None: ...
    def State(self) -> TopAbs_State: ...

class Geom2dHatch_Hatcher:
    def __init__(self, Intersector: Geom2dHatch_Intersector, Confusion2d: float, Confusion3d: float, KeepPnt: Optional[bool] = False, KeepSeg: Optional[bool] = False) -> None: ...
    @overload
    def AddElement(self, Curve: Geom2dAdaptor_Curve, Orientation: Optional[TopAbs_Orientation] = TopAbs_FORWARD) -> int: ...
    @overload
    def AddElement(self, Curve: Geom2d_Curve, Orientation: Optional[TopAbs_Orientation] = TopAbs_FORWARD) -> int: ...
    def AddHatching(self, Curve: Geom2dAdaptor_Curve) -> int: ...
    def ChangeIntersector(self) -> Geom2dHatch_Intersector: ...
    def Clear(self) -> None: ...
    def ClrElements(self) -> None: ...
    def ClrHatchings(self) -> None: ...
    @overload
    def ComputeDomains(self) -> None: ...
    @overload
    def ComputeDomains(self, IndH: int) -> None: ...
    @overload
    def Confusion2d(self, Confusion: float) -> None: ...
    @overload
    def Confusion2d(self) -> float: ...
    @overload
    def Confusion3d(self, Confusion: float) -> None: ...
    @overload
    def Confusion3d(self) -> float: ...
    def Domain(self, IndH: int, IDom: int) -> HatchGen_Domain: ...
    def Dump(self) -> None: ...
    def ElementCurve(self, IndE: int) -> Geom2dAdaptor_Curve: ...
    def HatchingCurve(self, IndH: int) -> Geom2dAdaptor_Curve: ...
    @overload
    def Intersector(self, Intersector: Geom2dHatch_Intersector) -> None: ...
    @overload
    def Intersector(self) -> Geom2dHatch_Intersector: ...
    @overload
    def KeepPoints(self, Keep: bool) -> None: ...
    @overload
    def KeepPoints(self) -> bool: ...
    @overload
    def KeepSegments(self, Keep: bool) -> None: ...
    @overload
    def KeepSegments(self) -> bool: ...
    def NbDomains(self, IndH: int) -> int: ...
    def NbPoints(self, IndH: int) -> int: ...
    def Point(self, IndH: int, IndP: int) -> HatchGen_PointOnHatching: ...
    def RemElement(self, IndE: int) -> None: ...
    def RemHatching(self, IndH: int) -> None: ...
    def Status(self, IndH: int) -> HatchGen_ErrorStatus: ...
    @overload
    def Trim(self) -> None: ...
    @overload
    def Trim(self, Curve: Geom2dAdaptor_Curve) -> int: ...
    @overload
    def Trim(self, IndH: int) -> None: ...
    def TrimDone(self, IndH: int) -> bool: ...
    def TrimFailed(self, IndH: int) -> bool: ...

class Geom2dHatch_Hatching:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Curve: Geom2dAdaptor_Curve) -> None: ...
    def AddDomain(self, Domain: HatchGen_Domain) -> None: ...
    def AddPoint(self, Point: HatchGen_PointOnHatching, Confusion: float) -> None: ...
    def ChangeCurve(self) -> Geom2dAdaptor_Curve: ...
    def ChangePoint(self, Index: int) -> HatchGen_PointOnHatching: ...
    def ClassificationPoint(self) -> gp_Pnt2d: ...
    def ClrDomains(self) -> None: ...
    def ClrPoints(self) -> None: ...
    def Curve(self) -> Geom2dAdaptor_Curve: ...
    def Domain(self, Index: int) -> HatchGen_Domain: ...
    @overload
    def IsDone(self, Flag: bool) -> None: ...
    @overload
    def IsDone(self) -> bool: ...
    def NbDomains(self) -> int: ...
    def NbPoints(self) -> int: ...
    def Point(self, Index: int) -> HatchGen_PointOnHatching: ...
    def RemDomain(self, Index: int) -> None: ...
    def RemPoint(self, Index: int) -> None: ...
    @overload
    def Status(self, theStatus: HatchGen_ErrorStatus) -> None: ...
    @overload
    def Status(self) -> HatchGen_ErrorStatus: ...
    @overload
    def TrimDone(self, Flag: bool) -> None: ...
    @overload
    def TrimDone(self) -> bool: ...
    @overload
    def TrimFailed(self, Flag: bool) -> None: ...
    @overload
    def TrimFailed(self) -> bool: ...

class Geom2dHatch_Intersector(Geom2dInt_GInter):
    @overload
    def __init__(self, Confusion: float, Tangency: float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ConfusionTolerance(self) -> float: ...
    def Intersect(self, C1: Geom2dAdaptor_Curve, C2: Geom2dAdaptor_Curve) -> None: ...
    def LocalGeometry(self, E: Geom2dAdaptor_Curve, U: float, T: gp_Dir2d, N: gp_Dir2d) -> float: ...
    def Perform(self, L: gp_Lin2d, P: float, Tol: float, E: Geom2dAdaptor_Curve) -> None: ...
    def SetConfusionTolerance(self, Confusion: float) -> None: ...
    def SetTangencyTolerance(self, Tangency: float) -> None: ...
    def TangencyTolerance(self) -> float: ...

# harray1 classes
# harray2 classes
# hsequence classes

