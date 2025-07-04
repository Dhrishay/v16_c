from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.TopTools import *
from OCC.Core.TopAbs import *
from OCC.Core.gp import *
from OCC.Core.IntRes2d import *
from OCC.Core.Geom2dInt import *


class BRepClass_Edge:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
    @overload
    def Edge(self) -> TopoDS_Edge: ...
    @overload
    def Edge(self) -> TopoDS_Edge: ...
    @overload
    def Face(self) -> TopoDS_Face: ...
    @overload
    def Face(self) -> TopoDS_Face: ...
    def MaxTolerance(self) -> float: ...
    def NextEdge(self) -> TopoDS_Edge: ...
    def SetMaxTolerance(self, theValue: float) -> None: ...
    def SetNextEdge(self, theMapVE: TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...
    def SetUseBndBox(self, theValue: bool) -> None: ...
    def UseBndBox(self) -> bool: ...

class BRepClass_FClass2dOfFClassifier:
    def __init__(self) -> None: ...
    def ClosestIntersection(self) -> int: ...
    def Compare(self, E: BRepClass_Edge, Or: TopAbs_Orientation) -> None: ...
    def Intersector(self) -> BRepClass_Intersector: ...
    def IsHeadOrEnd(self) -> bool: ...
    def Parameter(self) -> float: ...
    def Reset(self, L: gp_Lin2d, P: float, Tol: float) -> None: ...
    def State(self) -> TopAbs_State: ...

class BRepClass_FClassifier:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, F: BRepClass_FaceExplorer, P: gp_Pnt2d, Tol: float) -> None: ...
    def Edge(self) -> BRepClass_Edge: ...
    def EdgeParameter(self) -> float: ...
    def NoWires(self) -> bool: ...
    def Perform(self, F: BRepClass_FaceExplorer, P: gp_Pnt2d, Tol: float) -> None: ...
    def Position(self) -> IntRes2d_Position: ...
    def Rejected(self) -> bool: ...
    def State(self) -> TopAbs_State: ...

class BRepClass_FaceExplorer:
    def __init__(self, F: TopoDS_Face) -> None: ...
    def CheckPoint(self, thePoint: gp_Pnt2d) -> bool: ...
    def CurrentEdge(self, E: BRepClass_Edge) -> TopAbs_Orientation: ...
    def InitEdges(self) -> None: ...
    def InitWires(self) -> None: ...
    def MaxTolerance(self) -> float: ...
    def MoreEdges(self) -> bool: ...
    def MoreWires(self) -> bool: ...
    def NextEdge(self) -> None: ...
    def NextWire(self) -> None: ...
    def OtherSegment(self, P: gp_Pnt2d, L: gp_Lin2d) -> Tuple[bool, float]: ...
    def Reject(self, P: gp_Pnt2d) -> bool: ...
    def RejectEdge(self, L: gp_Lin2d, Par: float) -> bool: ...
    def RejectWire(self, L: gp_Lin2d, Par: float) -> bool: ...
    def Segment(self, P: gp_Pnt2d, L: gp_Lin2d) -> Tuple[bool, float]: ...
    def SetMaxTolerance(self, theValue: float) -> None: ...
    def SetUseBndBox(self, theValue: bool) -> None: ...
    def UseBndBox(self) -> bool: ...

class BRepClass_FacePassiveClassifier:
    def __init__(self) -> None: ...
    def ClosestIntersection(self) -> int: ...
    def Compare(self, E: BRepClass_Edge, Or: TopAbs_Orientation) -> None: ...
    def Intersector(self) -> BRepClass_Intersector: ...
    def IsHeadOrEnd(self) -> bool: ...
    def Parameter(self) -> float: ...
    def Reset(self, L: gp_Lin2d, P: float, Tol: float) -> None: ...
    def State(self) -> TopAbs_State: ...

class BRepClass_Intersector(Geom2dInt_IntConicCurveOfGInter):
    def __init__(self) -> None: ...
    def LocalGeometry(self, E: BRepClass_Edge, U: float, T: gp_Dir2d, N: gp_Dir2d) -> float: ...
    def Perform(self, L: gp_Lin2d, P: float, Tol: float, E: BRepClass_Edge) -> None: ...

class BRepClass_FaceClassifier(BRepClass_FClassifier):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, F: BRepClass_FaceExplorer, P: gp_Pnt2d, Tol: float) -> None: ...
    @overload
    def __init__(self, theF: TopoDS_Face, theP: gp_Pnt2d, theTol: float, theUseBndBox: Optional[bool] = False, theGapCheckTol: Optional[float] = 0.1) -> None: ...
    @overload
    def __init__(self, theF: TopoDS_Face, theP: gp_Pnt, theTol: float, theUseBndBox: Optional[bool] = False, theGapCheckTol: Optional[float] = 0.1) -> None: ...
    @overload
    def Perform(self, theF: TopoDS_Face, theP: gp_Pnt2d, theTol: float, theUseBndBox: Optional[bool] = False, theGapCheckTol: Optional[float] = 0.1) -> None: ...
    @overload
    def Perform(self, theF: TopoDS_Face, theP: gp_Pnt, theTol: float, theUseBndBox: Optional[bool] = False, theGapCheckTol: Optional[float] = 0.1) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

