from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Transfer import *
from OCC.Core.TopoDS import *
from OCC.Core.TCollection import *
from OCC.Core.StepData import *
from OCC.Core.MoniTool import *
from OCC.Core.StepShape import *
from OCC.Core.Message import *
from OCC.Core.StepVisual import *
from OCC.Core.TColStd import *


class TopoDSToStep_BuilderError(IntEnum):
    TopoDSToStep_BuilderDone: int = ...
    TopoDSToStep_NoFaceMapped: int = ...
    TopoDSToStep_BuilderOther: int = ...

TopoDSToStep_BuilderDone = TopoDSToStep_BuilderError.TopoDSToStep_BuilderDone
TopoDSToStep_NoFaceMapped = TopoDSToStep_BuilderError.TopoDSToStep_NoFaceMapped
TopoDSToStep_BuilderOther = TopoDSToStep_BuilderError.TopoDSToStep_BuilderOther

class TopoDSToStep_FacetedError(IntEnum):
    TopoDSToStep_FacetedDone: int = ...
    TopoDSToStep_SurfaceNotPlane: int = ...
    TopoDSToStep_PCurveNotLinear: int = ...

TopoDSToStep_FacetedDone = TopoDSToStep_FacetedError.TopoDSToStep_FacetedDone
TopoDSToStep_SurfaceNotPlane = TopoDSToStep_FacetedError.TopoDSToStep_SurfaceNotPlane
TopoDSToStep_PCurveNotLinear = TopoDSToStep_FacetedError.TopoDSToStep_PCurveNotLinear

class TopoDSToStep_MakeEdgeError(IntEnum):
    TopoDSToStep_EdgeDone: int = ...
    TopoDSToStep_NonManifoldEdge: int = ...
    TopoDSToStep_EdgeOther: int = ...

TopoDSToStep_EdgeDone = TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeDone
TopoDSToStep_NonManifoldEdge = TopoDSToStep_MakeEdgeError.TopoDSToStep_NonManifoldEdge
TopoDSToStep_EdgeOther = TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeOther

class TopoDSToStep_MakeFaceError(IntEnum):
    TopoDSToStep_FaceDone: int = ...
    TopoDSToStep_InfiniteFace: int = ...
    TopoDSToStep_NonManifoldFace: int = ...
    TopoDSToStep_NoWireMapped: int = ...
    TopoDSToStep_FaceOther: int = ...

TopoDSToStep_FaceDone = TopoDSToStep_MakeFaceError.TopoDSToStep_FaceDone
TopoDSToStep_InfiniteFace = TopoDSToStep_MakeFaceError.TopoDSToStep_InfiniteFace
TopoDSToStep_NonManifoldFace = TopoDSToStep_MakeFaceError.TopoDSToStep_NonManifoldFace
TopoDSToStep_NoWireMapped = TopoDSToStep_MakeFaceError.TopoDSToStep_NoWireMapped
TopoDSToStep_FaceOther = TopoDSToStep_MakeFaceError.TopoDSToStep_FaceOther

class TopoDSToStep_MakeVertexError(IntEnum):
    TopoDSToStep_VertexDone: int = ...
    TopoDSToStep_VertexOther: int = ...

TopoDSToStep_VertexDone = TopoDSToStep_MakeVertexError.TopoDSToStep_VertexDone
TopoDSToStep_VertexOther = TopoDSToStep_MakeVertexError.TopoDSToStep_VertexOther

class TopoDSToStep_MakeWireError(IntEnum):
    TopoDSToStep_WireDone: int = ...
    TopoDSToStep_NonManifoldWire: int = ...
    TopoDSToStep_WireOther: int = ...

TopoDSToStep_WireDone = TopoDSToStep_MakeWireError.TopoDSToStep_WireDone
TopoDSToStep_NonManifoldWire = TopoDSToStep_MakeWireError.TopoDSToStep_NonManifoldWire
TopoDSToStep_WireOther = TopoDSToStep_MakeWireError.TopoDSToStep_WireOther

class topodstostep:
    @overload
    @staticmethod
    def AddResult(FP: Transfer_FinderProcess, Shape: TopoDS_Shape, entity: Standard_Transient) -> None: ...
    @overload
    @staticmethod
    def AddResult(FP: Transfer_FinderProcess, Tool: TopoDSToStep_Tool) -> None: ...
    @staticmethod
    def DecodeBuilderError(E: TopoDSToStep_BuilderError) -> TCollection_HAsciiString: ...
    @staticmethod
    def DecodeEdgeError(E: TopoDSToStep_MakeEdgeError) -> TCollection_HAsciiString: ...
    @staticmethod
    def DecodeFaceError(E: TopoDSToStep_MakeFaceError) -> TCollection_HAsciiString: ...
    @staticmethod
    def DecodeVertexError(E: TopoDSToStep_MakeVertexError) -> TCollection_HAsciiString: ...
    @staticmethod
    def DecodeWireError(E: TopoDSToStep_MakeWireError) -> TCollection_HAsciiString: ...

class TopoDSToStep_FacetedTool:
    @staticmethod
    def CheckTopoDSShape(SH: TopoDS_Shape) -> TopoDSToStep_FacetedError: ...

class TopoDSToStep_Root:
    def IsDone(self) -> bool: ...
    def GetTolerance(self) -> float: ...
    def SetTolerance(self, value: float) -> None: ...

class TopoDSToStep_Tool:
    @overload
    def __init__(self, theModel: StepData_StepModel) -> None: ...
    @overload
    def __init__(self, M: MoniTool_DataMapOfShapeTransient, FacetedContext: bool, theSurfCurveMode: int) -> None: ...
    def Bind(self, S: TopoDS_Shape, T: StepShape_TopologicalRepresentationItem) -> None: ...
    def CurrentEdge(self) -> TopoDS_Edge: ...
    def CurrentFace(self) -> TopoDS_Face: ...
    def CurrentShell(self) -> TopoDS_Shell: ...
    def CurrentVertex(self) -> TopoDS_Vertex: ...
    def CurrentWire(self) -> TopoDS_Wire: ...
    def Faceted(self) -> bool: ...
    def Find(self, S: TopoDS_Shape) -> StepShape_TopologicalRepresentationItem: ...
    def Init(self, M: MoniTool_DataMapOfShapeTransient, FacetedContext: bool, theSurfCurveMode: int) -> None: ...
    def IsBound(self, S: TopoDS_Shape) -> bool: ...
    def Lowest3DTolerance(self) -> float: ...
    def Map(self) -> MoniTool_DataMapOfShapeTransient: ...
    def PCurveMode(self) -> int: ...
    def SetCurrentEdge(self, E: TopoDS_Edge) -> None: ...
    def SetCurrentFace(self, F: TopoDS_Face) -> None: ...
    def SetCurrentShell(self, S: TopoDS_Shell) -> None: ...
    def SetCurrentVertex(self, V: TopoDS_Vertex) -> None: ...
    def SetCurrentWire(self, W: TopoDS_Wire) -> None: ...
    def SetSurfaceReversed(self, B: bool) -> None: ...
    def SurfaceReversed(self) -> bool: ...

class TopoDSToStep_Builder(TopoDSToStep_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shape, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess, theTessellatedGeomParam: int, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def Error(self) -> TopoDSToStep_BuilderError: ...
    def Init(self, S: TopoDS_Shape, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess, theTessellatedGeomParam: int, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def TessellatedValue(self) -> StepVisual_TessellatedItem: ...
    def Value(self) -> StepShape_TopologicalRepresentationItem: ...

class TopoDSToStep_MakeBrepWithVoids(TopoDSToStep_Root):
    def __init__(self, S: TopoDS_Solid, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def TessellatedValue(self) -> StepVisual_TessellatedItem: ...
    def Value(self) -> StepShape_BrepWithVoids: ...

class TopoDSToStep_MakeFacetedBrep(TopoDSToStep_Root):
    @overload
    def __init__(self, S: TopoDS_Shell, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Solid, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def TessellatedValue(self) -> StepVisual_TessellatedItem: ...
    def Value(self) -> StepShape_FacetedBrep: ...

class TopoDSToStep_MakeFacetedBrepAndBrepWithVoids(TopoDSToStep_Root):
    def __init__(self, S: TopoDS_Solid, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def TessellatedValue(self) -> StepVisual_TessellatedItem: ...
    def Value(self) -> StepShape_FacetedBrepAndBrepWithVoids: ...

class TopoDSToStep_MakeGeometricCurveSet(TopoDSToStep_Root):
    def __init__(self, SH: TopoDS_Shape, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> StepShape_GeometricCurveSet: ...

class TopoDSToStep_MakeManifoldSolidBrep(TopoDSToStep_Root):
    @overload
    def __init__(self, S: TopoDS_Shell, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Solid, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def TessellatedValue(self) -> StepVisual_TessellatedItem: ...
    def Value(self) -> StepShape_ManifoldSolidBrep: ...

class TopoDSToStep_MakeShellBasedSurfaceModel(TopoDSToStep_Root):
    @overload
    def __init__(self, F: TopoDS_Face, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shell, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Solid, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def TessellatedValue(self) -> StepVisual_TessellatedItem: ...
    def Value(self) -> StepShape_ShellBasedSurfaceModel: ...

class TopoDSToStep_MakeStepEdge(TopoDSToStep_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, E: TopoDS_Edge, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> TopoDSToStep_MakeEdgeError: ...
    def Init(self, E: TopoDS_Edge, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> StepShape_TopologicalRepresentationItem: ...

class TopoDSToStep_MakeStepFace(TopoDSToStep_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, F: TopoDS_Face, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> TopoDSToStep_MakeFaceError: ...
    def Init(self, F: TopoDS_Face, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> StepShape_TopologicalRepresentationItem: ...

class TopoDSToStep_MakeStepVertex(TopoDSToStep_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, V: TopoDS_Vertex, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> TopoDSToStep_MakeVertexError: ...
    def Init(self, V: TopoDS_Vertex, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> StepShape_TopologicalRepresentationItem: ...

class TopoDSToStep_MakeStepWire(TopoDSToStep_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, W: TopoDS_Wire, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> TopoDSToStep_MakeWireError: ...
    def Init(self, W: TopoDS_Wire, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> StepShape_TopologicalRepresentationItem: ...

class TopoDSToStep_MakeTessellatedItem(TopoDSToStep_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theFace: TopoDS_Face, theTool: TopoDSToStep_Tool, theFP: Transfer_FinderProcess, theToPreferSurfaceSet: bool, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def __init__(self, theShell: TopoDS_Shell, theTool: TopoDSToStep_Tool, theFP: Transfer_FinderProcess, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def Init(self, theFace: TopoDS_Face, theTool: TopoDSToStep_Tool, theFP: Transfer_FinderProcess, theToPreferSurfaceSet: bool, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def Init(self, theShell: TopoDS_Shell, theTool: TopoDSToStep_Tool, theFP: Transfer_FinderProcess, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def Value(self) -> StepVisual_TessellatedItem: ...

class TopoDSToStep_WireframeBuilder(TopoDSToStep_Root):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shape, T: TopoDSToStep_Tool, theLocalFactors: StepData_Factors) -> None: ...
    def Error(self) -> TopoDSToStep_BuilderError: ...
    def GetTrimmedCurveFromEdge(self, E: TopoDS_Edge, F: TopoDS_Face, M: MoniTool_DataMapOfShapeTransient, L: TColStd_HSequenceOfTransient, theLocalFactors: StepData_Factors) -> bool: ...
    def GetTrimmedCurveFromFace(self, F: TopoDS_Face, M: MoniTool_DataMapOfShapeTransient, L: TColStd_HSequenceOfTransient, theLocalFactors: StepData_Factors) -> bool: ...
    def GetTrimmedCurveFromShape(self, S: TopoDS_Shape, M: MoniTool_DataMapOfShapeTransient, L: TColStd_HSequenceOfTransient, theLocalFactors: StepData_Factors) -> bool: ...
    def Init(self, S: TopoDS_Shape, T: TopoDSToStep_Tool, theLocalFactors: StepData_Factors) -> None: ...
    def Value(self) -> TColStd_HSequenceOfTransient: ...

# harray1 classes
# harray2 classes
# hsequence classes

