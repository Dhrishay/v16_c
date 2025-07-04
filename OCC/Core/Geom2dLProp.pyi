from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *
from OCC.Core.LProp import *
from OCC.Core.math import *


class Geom2dLProp_CLProps2d:
    @overload
    def __init__(self, C: Geom2d_Curve, N: int, Resolution: float) -> None: ...
    @overload
    def __init__(self, C: Geom2d_Curve, U: float, N: int, Resolution: float) -> None: ...
    @overload
    def __init__(self, N: int, Resolution: float) -> None: ...
    def CentreOfCurvature(self, P: gp_Pnt2d) -> None: ...
    def Curvature(self) -> float: ...
    def D1(self) -> gp_Vec2d: ...
    def D2(self) -> gp_Vec2d: ...
    def D3(self) -> gp_Vec2d: ...
    def IsTangentDefined(self) -> bool: ...
    def Normal(self, N: gp_Dir2d) -> None: ...
    def SetCurve(self, C: Geom2d_Curve) -> None: ...
    def SetParameter(self, U: float) -> None: ...
    def Tangent(self, D: gp_Dir2d) -> None: ...
    def Value(self) -> gp_Pnt2d: ...

class Geom2dLProp_CurAndInf2d(LProp_CurAndInf):
    def __init__(self) -> None: ...
    def IsDone(self) -> bool: ...
    def Perform(self, C: Geom2d_Curve) -> None: ...
    def PerformCurExt(self, C: Geom2d_Curve) -> None: ...
    def PerformInf(self, C: Geom2d_Curve) -> None: ...

class Geom2dLProp_Curve2dTool:
    @staticmethod
    def Continuity(C: Geom2d_Curve) -> int: ...
    @staticmethod
    def D1(C: Geom2d_Curve, U: float, P: gp_Pnt2d, V1: gp_Vec2d) -> None: ...
    @staticmethod
    def D2(C: Geom2d_Curve, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
    @staticmethod
    def D3(C: Geom2d_Curve, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
    @staticmethod
    def FirstParameter(C: Geom2d_Curve) -> float: ...
    @staticmethod
    def LastParameter(C: Geom2d_Curve) -> float: ...
    @staticmethod
    def Value(C: Geom2d_Curve, U: float, P: gp_Pnt2d) -> None: ...

class Geom2dLProp_FuncCurExt(math_FunctionWithDerivative):
    def __init__(self, C: Geom2d_Curve, Tol: float) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def IsMinKC(self, Param: float) -> bool: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

class Geom2dLProp_FuncCurNul(math_FunctionWithDerivative):
    def __init__(self, C: Geom2d_Curve) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

class Geom2dLProp_NumericCurInf2d:
    def __init__(self) -> None: ...
    def IsDone(self) -> bool: ...
    @overload
    def PerformCurExt(self, C: Geom2d_Curve, Result: LProp_CurAndInf) -> None: ...
    @overload
    def PerformCurExt(self, C: Geom2d_Curve, UMin: float, UMax: float, Result: LProp_CurAndInf) -> None: ...
    @overload
    def PerformInf(self, C: Geom2d_Curve, Result: LProp_CurAndInf) -> None: ...
    @overload
    def PerformInf(self, C: Geom2d_Curve, UMin: float, UMax: float, Result: LProp_CurAndInf) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

