from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.GeomAbs import *
from OCC.Core.gp import *


class geomlprop:
    @overload
    @staticmethod
    def Continuity(C1: Geom_Curve, C2: Geom_Curve, u1: float, u2: float, r1: bool, r2: bool, tl: float, ta: float) -> GeomAbs_Shape: ...
    @overload
    @staticmethod
    def Continuity(C1: Geom_Curve, C2: Geom_Curve, u1: float, u2: float, r1: bool, r2: bool) -> GeomAbs_Shape: ...

class GeomLProp_CLProps:
    @overload
    def __init__(self, C: Geom_Curve, N: int, Resolution: float) -> None: ...
    @overload
    def __init__(self, C: Geom_Curve, U: float, N: int, Resolution: float) -> None: ...
    @overload
    def __init__(self, N: int, Resolution: float) -> None: ...
    def CentreOfCurvature(self, P: gp_Pnt) -> None: ...
    def Curvature(self) -> float: ...
    def D1(self) -> gp_Vec: ...
    def D2(self) -> gp_Vec: ...
    def D3(self) -> gp_Vec: ...
    def IsTangentDefined(self) -> bool: ...
    def Normal(self, N: gp_Dir) -> None: ...
    def SetCurve(self, C: Geom_Curve) -> None: ...
    def SetParameter(self, U: float) -> None: ...
    def Tangent(self, D: gp_Dir) -> None: ...
    def Value(self) -> gp_Pnt: ...

class GeomLProp_CurveTool:
    @staticmethod
    def Continuity(C: Geom_Curve) -> int: ...
    @staticmethod
    def D1(C: Geom_Curve, U: float, P: gp_Pnt, V1: gp_Vec) -> None: ...
    @staticmethod
    def D2(C: Geom_Curve, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
    @staticmethod
    def D3(C: Geom_Curve, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
    @staticmethod
    def FirstParameter(C: Geom_Curve) -> float: ...
    @staticmethod
    def LastParameter(C: Geom_Curve) -> float: ...
    @staticmethod
    def Value(C: Geom_Curve, U: float, P: gp_Pnt) -> None: ...

class GeomLProp_SLProps:
    @overload
    def __init__(self, S: Geom_Surface, U: float, V: float, N: int, Resolution: float) -> None: ...
    @overload
    def __init__(self, S: Geom_Surface, N: int, Resolution: float) -> None: ...
    @overload
    def __init__(self, N: int, Resolution: float) -> None: ...
    def CurvatureDirections(self, MaxD: gp_Dir, MinD: gp_Dir) -> None: ...
    def D1U(self) -> gp_Vec: ...
    def D1V(self) -> gp_Vec: ...
    def D2U(self) -> gp_Vec: ...
    def D2V(self) -> gp_Vec: ...
    def DUV(self) -> gp_Vec: ...
    def GaussianCurvature(self) -> float: ...
    def IsCurvatureDefined(self) -> bool: ...
    def IsNormalDefined(self) -> bool: ...
    def IsTangentUDefined(self) -> bool: ...
    def IsTangentVDefined(self) -> bool: ...
    def IsUmbilic(self) -> bool: ...
    def MaxCurvature(self) -> float: ...
    def MeanCurvature(self) -> float: ...
    def MinCurvature(self) -> float: ...
    def Normal(self) -> gp_Dir: ...
    def SetParameters(self, U: float, V: float) -> None: ...
    def SetSurface(self, S: Geom_Surface) -> None: ...
    def TangentU(self, D: gp_Dir) -> None: ...
    def TangentV(self, D: gp_Dir) -> None: ...
    def Value(self) -> gp_Pnt: ...

class GeomLProp_SurfaceTool:
    @staticmethod
    def Bounds(S: Geom_Surface) -> Tuple[float, float, float, float]: ...
    @staticmethod
    def Continuity(S: Geom_Surface) -> int: ...
    @staticmethod
    def D1(S: Geom_Surface, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec) -> None: ...
    @staticmethod
    def D2(S: Geom_Surface, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, DUV: gp_Vec) -> None: ...
    @staticmethod
    def DN(S: Geom_Surface, U: float, V: float, IU: int, IV: int) -> gp_Vec: ...
    @staticmethod
    def Value(S: Geom_Surface, U: float, V: float, P: gp_Pnt) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

