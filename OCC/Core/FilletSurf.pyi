from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.TopTools import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.ChFi3d import *


class FilletSurf_ErrorTypeStatus(IntEnum):
    FilletSurf_EmptyList: int = ...
    FilletSurf_EdgeNotG1: int = ...
    FilletSurf_FacesNotG1: int = ...
    FilletSurf_EdgeNotOnShape: int = ...
    FilletSurf_NotSharpEdge: int = ...
    FilletSurf_PbFilletCompute: int = ...

FilletSurf_EmptyList = FilletSurf_ErrorTypeStatus.FilletSurf_EmptyList
FilletSurf_EdgeNotG1 = FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotG1
FilletSurf_FacesNotG1 = FilletSurf_ErrorTypeStatus.FilletSurf_FacesNotG1
FilletSurf_EdgeNotOnShape = FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotOnShape
FilletSurf_NotSharpEdge = FilletSurf_ErrorTypeStatus.FilletSurf_NotSharpEdge
FilletSurf_PbFilletCompute = FilletSurf_ErrorTypeStatus.FilletSurf_PbFilletCompute

class FilletSurf_StatusDone(IntEnum):
    FilletSurf_IsOk: int = ...
    FilletSurf_IsNotOk: int = ...
    FilletSurf_IsPartial: int = ...

FilletSurf_IsOk = FilletSurf_StatusDone.FilletSurf_IsOk
FilletSurf_IsNotOk = FilletSurf_StatusDone.FilletSurf_IsNotOk
FilletSurf_IsPartial = FilletSurf_StatusDone.FilletSurf_IsPartial

class FilletSurf_StatusType(IntEnum):
    FilletSurf_TwoExtremityOnEdge: int = ...
    FilletSurf_OneExtremityOnEdge: int = ...
    FilletSurf_NoExtremityOnEdge: int = ...

FilletSurf_TwoExtremityOnEdge = FilletSurf_StatusType.FilletSurf_TwoExtremityOnEdge
FilletSurf_OneExtremityOnEdge = FilletSurf_StatusType.FilletSurf_OneExtremityOnEdge
FilletSurf_NoExtremityOnEdge = FilletSurf_StatusType.FilletSurf_NoExtremityOnEdge

class FilletSurf_Builder:
    def __init__(self, S: TopoDS_Shape, E: TopTools_ListOfShape, R: float, Ta: Optional[float] = 1.0e-2, Tapp3d: Optional[float] = 1.0e-4, Tapp2d: Optional[float] = 1.0e-5) -> None: ...
    def CurveOnFace1(self, Index: int) -> Geom_Curve: ...
    def CurveOnFace2(self, Index: int) -> Geom_Curve: ...
    def EndSectionStatus(self) -> FilletSurf_StatusType: ...
    def FirstParameter(self) -> float: ...
    def IsDone(self) -> FilletSurf_StatusDone: ...
    def LastParameter(self) -> float: ...
    def NbSection(self, IndexSurf: int) -> int: ...
    def NbSurface(self) -> int: ...
    def PCurve1OnFillet(self, Index: int) -> Geom2d_Curve: ...
    def PCurve2OnFillet(self, Index: int) -> Geom2d_Curve: ...
    def PCurveOnFace1(self, Index: int) -> Geom2d_Curve: ...
    def PCurveOnFace2(self, Index: int) -> Geom2d_Curve: ...
    def Perform(self) -> None: ...
    def Section(self, IndexSurf: int, IndexSec: int, Circ: Geom_TrimmedCurve) -> None: ...
    def Simulate(self) -> None: ...
    def StartSectionStatus(self) -> FilletSurf_StatusType: ...
    def StatusError(self) -> FilletSurf_ErrorTypeStatus: ...
    def SupportFace1(self, Index: int) -> TopoDS_Face: ...
    def SupportFace2(self, Index: int) -> TopoDS_Face: ...
    def SurfaceFillet(self, Index: int) -> Geom_Surface: ...
    def TolApp3d(self, Index: int) -> float: ...

class FilletSurf_InternalBuilder(ChFi3d_FilBuilder):
    def __init__(self, S: TopoDS_Shape, FShape: Optional[ChFi3d_FilletShape] = ChFi3d_Polynomial, Ta: Optional[float] = 1.0e-2, Tapp3d: Optional[float] = 1.0e-4, Tapp2d: Optional[float] = 1.0e-5) -> None: ...
    def Add(self, E: TopTools_ListOfShape, R: float) -> int: ...
    def CurveOnFace1(self, Index: int) -> Geom_Curve: ...
    def CurveOnFace2(self, Index: int) -> Geom_Curve: ...
    def Done(self) -> bool: ...
    def EndSectionStatus(self) -> FilletSurf_StatusType: ...
    def FirstParameter(self) -> float: ...
    def LastParameter(self) -> float: ...
    def NbSection(self, IndexSurf: int) -> int: ...
    def NbSurface(self) -> int: ...
    def PCurve1OnFillet(self, Index: int) -> Geom2d_Curve: ...
    def PCurve2OnFillet(self, Index: int) -> Geom2d_Curve: ...
    def PCurveOnFace1(self, Index: int) -> Geom2d_Curve: ...
    def PCurveOnFace2(self, Index: int) -> Geom2d_Curve: ...
    def Perform(self) -> None: ...
    def Section(self, IndexSurf: int, IndexSec: int, Circ: Geom_TrimmedCurve) -> None: ...
    def Simulate(self) -> None: ...
    def StartSectionStatus(self) -> FilletSurf_StatusType: ...
    def SupportFace1(self, Index: int) -> TopoDS_Face: ...
    def SupportFace2(self, Index: int) -> TopoDS_Face: ...
    def SurfaceFillet(self, Index: int) -> Geom_Surface: ...
    def TolApp3d(self, Index: int) -> float: ...

# harray1 classes
# harray2 classes
# hsequence classes

