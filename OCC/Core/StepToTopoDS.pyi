from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.StepRepr import *
from OCC.Core.StepShape import *
from OCC.Core.StepGeom import *
from OCC.Core.TCollection import *
from OCC.Core.Geom import *
from OCC.Core.TopoDS import *
from OCC.Core.Transfer import *
from OCC.Core.Geom2d import *
from OCC.Core.StepData import *
from OCC.Core.gp import *
from OCC.Core.Message import *
from OCC.Core.StepVisual import *


class StepToTopoDS_BuilderError(IntEnum):
    StepToTopoDS_BuilderDone: int = ...
    StepToTopoDS_BuilderOther: int = ...

StepToTopoDS_BuilderDone = StepToTopoDS_BuilderError.StepToTopoDS_BuilderDone
StepToTopoDS_BuilderOther = StepToTopoDS_BuilderError.StepToTopoDS_BuilderOther

class StepToTopoDS_GeometricToolError(IntEnum):
    StepToTopoDS_GeometricToolDone: int = ...
    StepToTopoDS_GeometricToolIsDegenerated: int = ...
    StepToTopoDS_GeometricToolHasNoPCurve: int = ...
    StepToTopoDS_GeometricToolWrong3dParameters: int = ...
    StepToTopoDS_GeometricToolNoProjectiOnCurve: int = ...
    StepToTopoDS_GeometricToolOther: int = ...

StepToTopoDS_GeometricToolDone = StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolDone
StepToTopoDS_GeometricToolIsDegenerated = StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolIsDegenerated
StepToTopoDS_GeometricToolHasNoPCurve = StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolHasNoPCurve
StepToTopoDS_GeometricToolWrong3dParameters = StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolWrong3dParameters
StepToTopoDS_GeometricToolNoProjectiOnCurve = StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolNoProjectiOnCurve
StepToTopoDS_GeometricToolOther = StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolOther

class StepToTopoDS_TranslateEdgeError(IntEnum):
    StepToTopoDS_TranslateEdgeDone: int = ...
    StepToTopoDS_TranslateEdgeOther: int = ...

StepToTopoDS_TranslateEdgeDone = StepToTopoDS_TranslateEdgeError.StepToTopoDS_TranslateEdgeDone
StepToTopoDS_TranslateEdgeOther = StepToTopoDS_TranslateEdgeError.StepToTopoDS_TranslateEdgeOther

class StepToTopoDS_TranslateEdgeLoopError(IntEnum):
    StepToTopoDS_TranslateEdgeLoopDone: int = ...
    StepToTopoDS_TranslateEdgeLoopOther: int = ...

StepToTopoDS_TranslateEdgeLoopDone = StepToTopoDS_TranslateEdgeLoopError.StepToTopoDS_TranslateEdgeLoopDone
StepToTopoDS_TranslateEdgeLoopOther = StepToTopoDS_TranslateEdgeLoopError.StepToTopoDS_TranslateEdgeLoopOther

class StepToTopoDS_TranslateFaceError(IntEnum):
    StepToTopoDS_TranslateFaceDone: int = ...
    StepToTopoDS_TranslateFaceOther: int = ...

StepToTopoDS_TranslateFaceDone = StepToTopoDS_TranslateFaceError.StepToTopoDS_TranslateFaceDone
StepToTopoDS_TranslateFaceOther = StepToTopoDS_TranslateFaceError.StepToTopoDS_TranslateFaceOther

class StepToTopoDS_TranslatePolyLoopError(IntEnum):
    StepToTopoDS_TranslatePolyLoopDone: int = ...
    StepToTopoDS_TranslatePolyLoopOther: int = ...

StepToTopoDS_TranslatePolyLoopDone = StepToTopoDS_TranslatePolyLoopError.StepToTopoDS_TranslatePolyLoopDone
StepToTopoDS_TranslatePolyLoopOther = StepToTopoDS_TranslatePolyLoopError.StepToTopoDS_TranslatePolyLoopOther

class StepToTopoDS_TranslateShellError(IntEnum):
    StepToTopoDS_TranslateShellDone: int = ...
    StepToTopoDS_TranslateShellOther: int = ...

StepToTopoDS_TranslateShellDone = StepToTopoDS_TranslateShellError.StepToTopoDS_TranslateShellDone
StepToTopoDS_TranslateShellOther = StepToTopoDS_TranslateShellError.StepToTopoDS_TranslateShellOther

class StepToTopoDS_TranslateSolidError(IntEnum):
    StepToTopoDS_TranslateSolidDone: int = ...
    StepToTopoDS_TranslateSolidOther: int = ...

StepToTopoDS_TranslateSolidDone = StepToTopoDS_TranslateSolidError.StepToTopoDS_TranslateSolidDone
StepToTopoDS_TranslateSolidOther = StepToTopoDS_TranslateSolidError.StepToTopoDS_TranslateSolidOther

class StepToTopoDS_TranslateVertexError(IntEnum):
    StepToTopoDS_TranslateVertexDone: int = ...
    StepToTopoDS_TranslateVertexOther: int = ...

StepToTopoDS_TranslateVertexDone = StepToTopoDS_TranslateVertexError.StepToTopoDS_TranslateVertexDone
StepToTopoDS_TranslateVertexOther = StepToTopoDS_TranslateVertexError.StepToTopoDS_TranslateVertexOther

class StepToTopoDS_TranslateVertexLoopError(IntEnum):
    StepToTopoDS_TranslateVertexLoopDone: int = ...
    StepToTopoDS_TranslateVertexLoopOther: int = ...

StepToTopoDS_TranslateVertexLoopDone = StepToTopoDS_TranslateVertexLoopError.StepToTopoDS_TranslateVertexLoopDone
StepToTopoDS_TranslateVertexLoopOther = StepToTopoDS_TranslateVertexLoopError.StepToTopoDS_TranslateVertexLoopOther

class steptotopods:
    @staticmethod
    def DecodeBuilderError(Error: StepToTopoDS_BuilderError) -> TCollection_HAsciiString: ...
    @staticmethod
    def DecodeEdgeError(Error: StepToTopoDS_TranslateEdgeError) -> TCollection_HAsciiString: ...
    @staticmethod
    def DecodeFaceError(Error: StepToTopoDS_TranslateFaceError) -> TCollection_HAsciiString: ...
    @staticmethod
    def DecodeGeometricToolError(Error: StepToTopoDS_GeometricToolError) -> str: ...
    @staticmethod
    def DecodePolyLoopError(Error: StepToTopoDS_TranslatePolyLoopError) -> TCollection_HAsciiString: ...
    @staticmethod
    def DecodeShellError(Error: StepToTopoDS_TranslateShellError) -> TCollection_HAsciiString: ...
    @staticmethod
    def DecodeVertexError(Error: StepToTopoDS_TranslateVertexError) -> TCollection_HAsciiString: ...
    @staticmethod
    def DecodeVertexLoopError(Error: StepToTopoDS_TranslateVertexLoopError) -> TCollection_HAsciiString: ...

class StepToTopoDS_GeometricTool:
    @staticmethod
    def IsLikeSeam(SC: StepGeom_SurfaceCurve, S: StepGeom_Surface, E: StepShape_Edge, EL: StepShape_EdgeLoop) -> bool: ...
    @staticmethod
    def IsSeamCurve(SC: StepGeom_SurfaceCurve, S: StepGeom_Surface, E: StepShape_Edge, EL: StepShape_EdgeLoop) -> bool: ...
    @staticmethod
    def PCurve(SC: StepGeom_SurfaceCurve, S: StepGeom_Surface, PC: StepGeom_Pcurve, last: Optional[int] = 0) -> int: ...
    @staticmethod
    def UpdateParam3d(C: Geom_Curve, preci: float) -> Tuple[bool, float, float]: ...

class StepToTopoDS_NMTool:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, MapOfRI: StepToTopoDS_DataMapOfRI, MapOfRINames: StepToTopoDS_DataMapOfRINames) -> None: ...
    @overload
    def Bind(self, RI: StepRepr_RepresentationItem, S: TopoDS_Shape) -> None: ...
    @overload
    def Bind(self, RIName: str, S: TopoDS_Shape) -> None: ...
    def CleanUp(self) -> None: ...
    @overload
    def Find(self, RI: StepRepr_RepresentationItem) -> TopoDS_Shape: ...
    @overload
    def Find(self, RIName: str) -> TopoDS_Shape: ...
    def Init(self, MapOfRI: StepToTopoDS_DataMapOfRI, MapOfRINames: StepToTopoDS_DataMapOfRINames) -> None: ...
    def IsActive(self) -> bool: ...
    @overload
    def IsBound(self, RI: StepRepr_RepresentationItem) -> bool: ...
    @overload
    def IsBound(self, RIName: str) -> bool: ...
    def IsIDEASCase(self) -> bool: ...
    def IsPureNMShell(self, Shell: TopoDS_Shape) -> bool: ...
    def IsSuspectedAsClosing(self, BaseShell: TopoDS_Shape, SuspectedShell: TopoDS_Shape) -> bool: ...
    def RegisterNMEdge(self, Edge: TopoDS_Shape) -> None: ...
    def SetActive(self, isActive: bool) -> None: ...
    def SetIDEASCase(self, IDEASCase: bool) -> None: ...

class StepToTopoDS_PointPair:
    def __init__(self, P1: StepGeom_CartesianPoint, P2: StepGeom_CartesianPoint) -> None: ...
    def GetPoint1(self) -> StepGeom_CartesianPoint: ...
    def GetPoint2(self) -> StepGeom_CartesianPoint: ...

class StepToTopoDS_Root:
    def IsDone(self) -> bool: ...
    def MaxTol(self) -> float: ...
    def Precision(self) -> float: ...
    def SetMaxTol(self, maxpreci: float) -> None: ...
    def SetPrecision(self, preci: float) -> None: ...

class StepToTopoDS_Tool:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Map: StepToTopoDS_DataMapOfTRI, TP: Transfer_TransientProcess) -> None: ...
    @overload
    def AddContinuity(self, GeomSurf: Geom_Surface) -> None: ...
    @overload
    def AddContinuity(self, GeomCurve: Geom_Curve) -> None: ...
    @overload
    def AddContinuity(self, GeomCur2d: Geom2d_Curve) -> None: ...
    def Bind(self, TRI: StepShape_TopologicalRepresentationItem, S: TopoDS_Shape) -> None: ...
    def BindEdge(self, PP: StepToTopoDS_PointPair, E: TopoDS_Edge) -> None: ...
    def BindVertex(self, P: StepGeom_CartesianPoint, V: TopoDS_Vertex) -> None: ...
    def C0Cur2(self) -> int: ...
    def C0Cur3(self) -> int: ...
    def C0Surf(self) -> int: ...
    def C1Cur2(self) -> int: ...
    def C1Cur3(self) -> int: ...
    def C1Surf(self) -> int: ...
    def C2Cur2(self) -> int: ...
    def C2Cur3(self) -> int: ...
    def C2Surf(self) -> int: ...
    def ClearEdgeMap(self) -> None: ...
    def ClearVertexMap(self) -> None: ...
    @overload
    def ComputePCurve(self, B: bool) -> None: ...
    @overload
    def ComputePCurve(self) -> bool: ...
    def Find(self, TRI: StepShape_TopologicalRepresentationItem) -> TopoDS_Shape: ...
    def FindEdge(self, PP: StepToTopoDS_PointPair) -> TopoDS_Edge: ...
    def FindVertex(self, P: StepGeom_CartesianPoint) -> TopoDS_Vertex: ...
    def Init(self, Map: StepToTopoDS_DataMapOfTRI, TP: Transfer_TransientProcess) -> None: ...
    def IsBound(self, TRI: StepShape_TopologicalRepresentationItem) -> bool: ...
    def IsEdgeBound(self, PP: StepToTopoDS_PointPair) -> bool: ...
    def IsVertexBound(self, PG: StepGeom_CartesianPoint) -> bool: ...
    def TransientProcess(self) -> Transfer_TransientProcess: ...

class StepToTopoDS_MakeTransformed(StepToTopoDS_Root):
    def __init__(self) -> None: ...
    @overload
    def Compute(self, Origin: StepGeom_Axis2Placement3d, Target: StepGeom_Axis2Placement3d, theLocalFactors: StepData_Factors) -> bool: ...
    @overload
    def Compute(self, Operator: StepGeom_CartesianTransformationOperator3d, theLocalFactors: StepData_Factors) -> bool: ...
    def Transform(self, shape: TopoDS_Shape) -> bool: ...
    def Transformation(self) -> gp_Trsf: ...
    def TranslateMappedItem(self, mapit: StepRepr_MappedItem, TP: Transfer_TransientProcess, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> TopoDS_Shape: ...

class StepToTopoDS_TranslateCompositeCurve(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, CC: StepGeom_CompositeCurve, TP: Transfer_TransientProcess, theLocalFactors: StepData_Factors) -> None: ...
    @overload
    def __init__(self, CC: StepGeom_CompositeCurve, TP: Transfer_TransientProcess, S: StepGeom_Surface, Surf: Geom_Surface, theLocalFactors: StepData_Factors) -> None: ...
    @overload
    def Init(self, CC: StepGeom_CompositeCurve, TP: Transfer_TransientProcess, theLocalFactors: StepData_Factors) -> bool: ...
    @overload
    def Init(self, CC: StepGeom_CompositeCurve, TP: Transfer_TransientProcess, S: StepGeom_Surface, Surf: Geom_Surface, theLocalFactors: StepData_Factors) -> bool: ...
    def IsInfiniteSegment(self) -> bool: ...
    def Value(self) -> TopoDS_Wire: ...

class StepToTopoDS_TranslateCurveBoundedSurface(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, CBS: StepGeom_CurveBoundedSurface, TP: Transfer_TransientProcess, theLocalFactors: StepData_Factors) -> None: ...
    def Init(self, CBS: StepGeom_CurveBoundedSurface, TP: Transfer_TransientProcess, theLocalFactors: StepData_Factors) -> bool: ...
    def Value(self) -> TopoDS_Face: ...

class StepToTopoDS_TranslateEdge(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, E: StepShape_Edge, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> StepToTopoDS_TranslateEdgeError: ...
    def Init(self, E: StepShape_Edge, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    def MakeFromCurve3D(self, C3D: StepGeom_Curve, EC: StepShape_EdgeCurve, Vend: StepShape_Vertex, preci: float, E: TopoDS_Edge, V1: TopoDS_Vertex, V2: TopoDS_Vertex, T: StepToTopoDS_Tool, theLocalFactors: StepData_Factors) -> None: ...
    def MakePCurve(self, PCU: StepGeom_Pcurve, ConvSurf: Geom_Surface, theLocalFactors: StepData_Factors) -> Geom2d_Curve: ...
    def Value(self) -> TopoDS_Shape: ...

class StepToTopoDS_TranslateEdgeLoop(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, FB: StepShape_FaceBound, F: TopoDS_Face, S: Geom_Surface, SS: StepGeom_Surface, ss: bool, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> StepToTopoDS_TranslateEdgeLoopError: ...
    def Init(self, FB: StepShape_FaceBound, F: TopoDS_Face, S: Geom_Surface, SS: StepGeom_Surface, ss: bool, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> TopoDS_Shape: ...

class StepToTopoDS_TranslateFace(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, FS: StepShape_FaceSurface, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    @overload
    def __init__(self, theTF: StepVisual_TessellatedFace, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theReadTessellatedWhenNoBRepOnly: bool, theLocalFactors: StepData_Factors) -> bool: ...
    @overload
    def __init__(self, theTSS: StepVisual_TessellatedSurfaceSet, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> StepToTopoDS_TranslateFaceError: ...
    @overload
    def Init(self, FS: StepShape_FaceSurface, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    @overload
    def Init(self, theTF: StepVisual_TessellatedFace, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theReadTessellatedWhenNoBRepOnly: bool, theLocalFactors: StepData_Factors) -> bool: ...
    @overload
    def Init(self, theTSS: StepVisual_TessellatedSurfaceSet, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> TopoDS_Shape: ...

class StepToTopoDS_TranslatePolyLoop(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, PL: StepShape_PolyLoop, T: StepToTopoDS_Tool, S: Geom_Surface, F: TopoDS_Face, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> StepToTopoDS_TranslatePolyLoopError: ...
    def Init(self, PL: StepShape_PolyLoop, T: StepToTopoDS_Tool, S: Geom_Surface, F: TopoDS_Face, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> TopoDS_Shape: ...

class StepToTopoDS_TranslateShell(StepToTopoDS_Root):
    def __init__(self) -> None: ...
    def Error(self) -> StepToTopoDS_TranslateShellError: ...
    @overload
    def Init(self, CFS: StepShape_ConnectedFaceSet, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def Init(self, theTSh: StepVisual_TessellatedShell, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theReadTessellatedWhenNoBRepOnly: bool, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    def Value(self) -> TopoDS_Shape: ...

class StepToTopoDS_TranslateSolid(StepToTopoDS_Root):
    def __init__(self) -> None: ...
    def Error(self) -> StepToTopoDS_TranslateSolidError: ...
    def Init(self, theTSo: StepVisual_TessellatedSolid, theTP: Transfer_TransientProcess, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theReadTessellatedWhenNoBRepOnly: bool, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    def Value(self) -> TopoDS_Shape: ...

class StepToTopoDS_TranslateVertex(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, V: StepShape_Vertex, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> StepToTopoDS_TranslateVertexError: ...
    def Init(self, V: StepShape_Vertex, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> TopoDS_Shape: ...

class StepToTopoDS_TranslateVertexLoop(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, VL: StepShape_VertexLoop, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> StepToTopoDS_TranslateVertexLoopError: ...
    def Init(self, VL: StepShape_VertexLoop, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> TopoDS_Shape: ...

#classnotwrapped
class StepToTopoDS_Builder: ...

#classnotwrapped
class StepToTopoDS_PointVertexMap: ...

# harray1 classes
# harray2 classes
# hsequence classes

