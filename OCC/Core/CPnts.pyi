from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Adaptor2d import *
from OCC.Core.math import *
from OCC.Core.gp import *


class CPnts_AbscissaPoint:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, C: Adaptor3d_Curve, Abscissa: float, U0: float, Resolution: float) -> None: ...
    @overload
    def __init__(self, C: Adaptor2d_Curve2d, Abscissa: float, U0: float, Resolution: float) -> None: ...
    @overload
    def __init__(self, C: Adaptor3d_Curve, Abscissa: float, U0: float, Ui: float, Resolution: float) -> None: ...
    @overload
    def __init__(self, C: Adaptor2d_Curve2d, Abscissa: float, U0: float, Ui: float, Resolution: float) -> None: ...
    def AdvPerform(self, Abscissa: float, U0: float, Ui: float, Resolution: float) -> None: ...
    @overload
    def Init(self, C: Adaptor3d_Curve) -> None: ...
    @overload
    def Init(self, C: Adaptor2d_Curve2d) -> None: ...
    @overload
    def Init(self, C: Adaptor3d_Curve, Tol: float) -> None: ...
    @overload
    def Init(self, C: Adaptor2d_Curve2d, Tol: float) -> None: ...
    @overload
    def Init(self, C: Adaptor3d_Curve, U1: float, U2: float) -> None: ...
    @overload
    def Init(self, C: Adaptor2d_Curve2d, U1: float, U2: float) -> None: ...
    @overload
    def Init(self, C: Adaptor3d_Curve, U1: float, U2: float, Tol: float) -> None: ...
    @overload
    def Init(self, C: Adaptor2d_Curve2d, U1: float, U2: float, Tol: float) -> None: ...
    def IsDone(self) -> bool: ...
    @overload
    @staticmethod
    def Length(C: Adaptor3d_Curve) -> float: ...
    @overload
    @staticmethod
    def Length(C: Adaptor2d_Curve2d) -> float: ...
    @overload
    @staticmethod
    def Length(C: Adaptor3d_Curve, Tol: float) -> float: ...
    @overload
    @staticmethod
    def Length(C: Adaptor2d_Curve2d, Tol: float) -> float: ...
    @overload
    @staticmethod
    def Length(C: Adaptor3d_Curve, U1: float, U2: float) -> float: ...
    @overload
    @staticmethod
    def Length(C: Adaptor2d_Curve2d, U1: float, U2: float) -> float: ...
    @overload
    @staticmethod
    def Length(C: Adaptor3d_Curve, U1: float, U2: float, Tol: float) -> float: ...
    @overload
    @staticmethod
    def Length(C: Adaptor2d_Curve2d, U1: float, U2: float, Tol: float) -> float: ...
    def Parameter(self) -> float: ...
    @overload
    def Perform(self, Abscissa: float, U0: float, Resolution: float) -> None: ...
    @overload
    def Perform(self, Abscissa: float, U0: float, Ui: float, Resolution: float) -> None: ...
    def SetParameter(self, P: float) -> None: ...

class CPnts_MyGaussFunction(math_Function):
    def __init__(self) -> None: ...
    def Init(self, F: CPnts_RealFunction, D: None) -> None: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...

class CPnts_MyRootFunction(math_FunctionWithDerivative):
    def __init__(self) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    @overload
    def Init(self, F: CPnts_RealFunction, D: None, Order: int) -> None: ...
    @overload
    def Init(self, X0: float, L: float) -> None: ...
    @overload
    def Init(self, X0: float, L: float, Tol: float) -> None: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

class CPnts_UniformDeflection:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, C: Adaptor3d_Curve, Deflection: float, Resolution: float, WithControl: bool) -> None: ...
    @overload
    def __init__(self, C: Adaptor2d_Curve2d, Deflection: float, Resolution: float, WithControl: bool) -> None: ...
    @overload
    def __init__(self, C: Adaptor3d_Curve, Deflection: float, U1: float, U2: float, Resolution: float, WithControl: bool) -> None: ...
    @overload
    def __init__(self, C: Adaptor2d_Curve2d, Deflection: float, U1: float, U2: float, Resolution: float, WithControl: bool) -> None: ...
    @overload
    def Initialize(self, C: Adaptor3d_Curve, Deflection: float, Resolution: float, WithControl: bool) -> None: ...
    @overload
    def Initialize(self, C: Adaptor2d_Curve2d, Deflection: float, Resolution: float, WithControl: bool) -> None: ...
    @overload
    def Initialize(self, C: Adaptor3d_Curve, Deflection: float, U1: float, U2: float, Resolution: float, WithControl: bool) -> None: ...
    @overload
    def Initialize(self, C: Adaptor2d_Curve2d, Deflection: float, U1: float, U2: float, Resolution: float, WithControl: bool) -> None: ...
    def IsAllDone(self) -> bool: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def Point(self) -> gp_Pnt: ...
    def Value(self) -> float: ...

# harray1 classes
# harray2 classes
# hsequence classes

