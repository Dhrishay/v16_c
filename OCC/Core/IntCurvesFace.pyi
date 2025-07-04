from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.Bnd import *
from OCC.Core.gp import *
from OCC.Core.TopAbs import *
from OCC.Core.Adaptor3d import *
from OCC.Core.GeomAbs import *
from OCC.Core.IntCurveSurface import *


class IntCurvesFace_Intersector(Standard_Transient):
    def __init__(self, F: TopoDS_Face, aTol: float, aRestr: Optional[bool] = True, UseBToler: Optional[bool] = True) -> None: ...
    def Bounding(self) -> Bnd_Box: ...
    def ClassifyUVPoint(self, Puv: gp_Pnt2d) -> TopAbs_State: ...
    def Face(self) -> TopoDS_Face: ...
    def GetUseBoundToler(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def IsParallel(self) -> bool: ...
    def NbPnt(self) -> int: ...
    @overload
    def Perform(self, L: gp_Lin, PInf: float, PSup: float) -> None: ...
    @overload
    def Perform(self, HCu: Adaptor3d_Curve, PInf: float, PSup: float) -> None: ...
    def Pnt(self, I: int) -> gp_Pnt: ...
    def SetUseBoundToler(self, UseBToler: bool) -> None: ...
    def State(self, I: int) -> TopAbs_State: ...
    def SurfaceType(self) -> GeomAbs_SurfaceType: ...
    def Transition(self, I: int) -> IntCurveSurface_TransitionOnCurve: ...
    def UParameter(self, I: int) -> float: ...
    def VParameter(self, I: int) -> float: ...
    def WParameter(self, I: int) -> float: ...

class IntCurvesFace_ShapeIntersector:
    def __init__(self) -> None: ...
    def Face(self, I: int) -> TopoDS_Face: ...
    def IsDone(self) -> bool: ...
    def Load(self, Sh: TopoDS_Shape, Tol: float) -> None: ...
    def NbPnt(self) -> int: ...
    @overload
    def Perform(self, L: gp_Lin, PInf: float, PSup: float) -> None: ...
    @overload
    def Perform(self, HCu: Adaptor3d_Curve, PInf: float, PSup: float) -> None: ...
    def PerformNearest(self, L: gp_Lin, PInf: float, PSup: float) -> None: ...
    def Pnt(self, I: int) -> gp_Pnt: ...
    def SortResult(self) -> None: ...
    def State(self, I: int) -> TopAbs_State: ...
    def Transition(self, I: int) -> IntCurveSurface_TransitionOnCurve: ...
    def UParameter(self, I: int) -> float: ...
    def VParameter(self, I: int) -> float: ...
    def WParameter(self, I: int) -> float: ...

# harray1 classes
# harray2 classes
# hsequence classes

