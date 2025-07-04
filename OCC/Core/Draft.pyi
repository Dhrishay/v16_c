from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.Geom2d import *
from OCC.Core.Geom import *
from OCC.Core.BRepTools import *
from OCC.Core.TopTools import *
from OCC.Core.GeomAbs import *
from OCC.Core.TopLoc import *

# the following typedef cannot be wrapped as is
Draft_IndexedDataMapOfEdgeEdgeInfo = NewType("Draft_IndexedDataMapOfEdgeEdgeInfo", Any)
# the following typedef cannot be wrapped as is
Draft_IndexedDataMapOfFaceFaceInfo = NewType("Draft_IndexedDataMapOfFaceFaceInfo", Any)
# the following typedef cannot be wrapped as is
Draft_IndexedDataMapOfVertexVertexInfo = NewType("Draft_IndexedDataMapOfVertexVertexInfo", Any)

class Draft_ErrorStatus(IntEnum):
    Draft_NoError: int = ...
    Draft_FaceRecomputation: int = ...
    Draft_EdgeRecomputation: int = ...
    Draft_VertexRecomputation: int = ...

Draft_NoError = Draft_ErrorStatus.Draft_NoError
Draft_FaceRecomputation = Draft_ErrorStatus.Draft_FaceRecomputation
Draft_EdgeRecomputation = Draft_ErrorStatus.Draft_EdgeRecomputation
Draft_VertexRecomputation = Draft_ErrorStatus.Draft_VertexRecomputation

class draft:
    @staticmethod
    def Angle(F: TopoDS_Face, Direction: gp_Dir) -> float: ...

class Draft_EdgeInfo:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, HasNewGeometry: bool) -> None: ...
    def Add(self, F: TopoDS_Face) -> None: ...
    def ChangeFirstPC(self) -> Geom2d_Curve: ...
    def ChangeGeometry(self) -> Geom_Curve: ...
    def ChangeSecondPC(self) -> Geom2d_Curve: ...
    def FirstFace(self) -> TopoDS_Face: ...
    def FirstPC(self) -> Geom2d_Curve: ...
    def Geometry(self) -> Geom_Curve: ...
    def IsTangent(self, P: gp_Pnt) -> bool: ...
    def NewGeometry(self) -> bool: ...
    @overload
    def RootFace(self, F: TopoDS_Face) -> None: ...
    @overload
    def RootFace(self) -> TopoDS_Face: ...
    def SecondFace(self) -> TopoDS_Face: ...
    def SecondPC(self) -> Geom2d_Curve: ...
    def SetNewGeometry(self, NewGeom: bool) -> None: ...
    def Tangent(self, P: gp_Pnt) -> None: ...
    @overload
    def Tolerance(self, tol: float) -> None: ...
    @overload
    def Tolerance(self) -> float: ...

class Draft_FaceInfo:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: Geom_Surface, HasNewGeometry: bool) -> None: ...
    def Add(self, F: TopoDS_Face) -> None: ...
    def ChangeCurve(self) -> Geom_Curve: ...
    def ChangeGeometry(self) -> Geom_Surface: ...
    def Curve(self) -> Geom_Curve: ...
    def FirstFace(self) -> TopoDS_Face: ...
    def Geometry(self) -> Geom_Surface: ...
    def NewGeometry(self) -> bool: ...
    @overload
    def RootFace(self, F: TopoDS_Face) -> None: ...
    @overload
    def RootFace(self) -> TopoDS_Face: ...
    def SecondFace(self) -> TopoDS_Face: ...

class Draft_Modification(BRepTools_Modification):
    def __init__(self, S: TopoDS_Shape) -> None: ...
    def Add(self, F: TopoDS_Face, Direction: gp_Dir, Angle: float, NeutralPlane: gp_Pln, Flag: Optional[bool] = True) -> bool: ...
    def Clear(self) -> None: ...
    def ConnectedFaces(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
    def Continuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, NewE: TopoDS_Edge, NewF1: TopoDS_Face, NewF2: TopoDS_Face) -> GeomAbs_Shape: ...
    def Error(self) -> Draft_ErrorStatus: ...
    def Init(self, S: TopoDS_Shape) -> None: ...
    def IsDone(self) -> bool: ...
    def ModifiedFaces(self) -> TopTools_ListOfShape: ...
    def NewCurve(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location) -> Tuple[bool, float]: ...
    def NewCurve2d(self, E: TopoDS_Edge, F: TopoDS_Face, NewE: TopoDS_Edge, NewF: TopoDS_Face, C: Geom2d_Curve) -> Tuple[bool, float]: ...
    def NewParameter(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
    def NewPoint(self, V: TopoDS_Vertex, P: gp_Pnt) -> Tuple[bool, float]: ...
    def NewSurface(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location) -> Tuple[bool, float, bool, bool]: ...
    def Perform(self) -> None: ...
    def ProblematicShape(self) -> TopoDS_Shape: ...
    def Remove(self, F: TopoDS_Face) -> None: ...

class Draft_VertexInfo:
    def __init__(self) -> None: ...
    def Add(self, E: TopoDS_Edge) -> None: ...
    def ChangeGeometry(self) -> gp_Pnt: ...
    def GetChangeParameter(self, E: TopoDS_Edge) -> float: ...
    def SetChangeParameter(self, E: TopoDS_Edge, value: float) -> None: ...
    def Edge(self) -> TopoDS_Edge: ...
    def Geometry(self) -> gp_Pnt: ...
    def InitEdgeIterator(self) -> None: ...
    def MoreEdge(self) -> bool: ...
    def NextEdge(self) -> None: ...
    def Parameter(self, E: TopoDS_Edge) -> float: ...

# harray1 classes
# harray2 classes
# hsequence classes

