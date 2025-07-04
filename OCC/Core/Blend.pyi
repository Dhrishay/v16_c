from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.math import *
from OCC.Core.TColStd import *
from OCC.Core.GeomAbs import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *
from OCC.Core.Adaptor2d import *


class Blend_SequenceOfPoint:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> Blend_Point: ...
    def Last(self) -> Blend_Point: ...
    def Length(self) -> int: ...
    def Append(self, theItem: Blend_Point) -> Blend_Point: ...
    def Prepend(self, theItem: Blend_Point) -> Blend_Point: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> Blend_Point: ...
    def SetValue(self, theIndex: int, theValue: Blend_Point) -> None: ...

class Blend_DecrochStatus(IntEnum):
    Blend_NoDecroch: int = ...
    Blend_DecrochRst1: int = ...
    Blend_DecrochRst2: int = ...
    Blend_DecrochBoth: int = ...

Blend_NoDecroch = Blend_DecrochStatus.Blend_NoDecroch
Blend_DecrochRst1 = Blend_DecrochStatus.Blend_DecrochRst1
Blend_DecrochRst2 = Blend_DecrochStatus.Blend_DecrochRst2
Blend_DecrochBoth = Blend_DecrochStatus.Blend_DecrochBoth

class Blend_Status(IntEnum):
    Blend_StepTooLarge: int = ...
    Blend_StepTooSmall: int = ...
    Blend_Backward: int = ...
    Blend_SamePoints: int = ...
    Blend_OnRst1: int = ...
    Blend_OnRst2: int = ...
    Blend_OnRst12: int = ...
    Blend_OK: int = ...

Blend_StepTooLarge = Blend_Status.Blend_StepTooLarge
Blend_StepTooSmall = Blend_Status.Blend_StepTooSmall
Blend_Backward = Blend_Status.Blend_Backward
Blend_SamePoints = Blend_Status.Blend_SamePoints
Blend_OnRst1 = Blend_Status.Blend_OnRst1
Blend_OnRst2 = Blend_Status.Blend_OnRst2
Blend_OnRst12 = Blend_Status.Blend_OnRst12
Blend_OK = Blend_Status.Blend_OK

class Blend_AppFunction(math_FunctionSetWithDerivatives):
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
    def GetMinimalDistance(self) -> float: ...
    def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
    def GetSectionSize(self) -> float: ...
    def GetShape(self) -> Tuple[int, int, int, int]: ...
    @overload
    def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsRational(self) -> bool: ...
    def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
    def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
    def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
    def NbEquations(self) -> int: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbVariables(self) -> int: ...
    def Parameter(self, P: Blend_Point) -> float: ...
    def Pnt1(self) -> gp_Pnt: ...
    def Pnt2(self) -> gp_Pnt: ...
    def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self, Param: float) -> None: ...
    @overload
    def Set(self, First: float, Last: float) -> None: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class Blend_CurvPointFuncInv(math_FunctionSetWithDerivatives):
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
    def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
    def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def Set(self, P: gp_Pnt) -> None: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class Blend_FuncInv(math_FunctionSetWithDerivatives):
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
    def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
    def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def Set(self, OnFirst: bool, COnSurf: Adaptor2d_Curve2d) -> None: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class Blend_Point:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, Tg1: gp_Vec, Tg2: gp_Vec, Tg12d: gp_Vec2d, Tg22d: gp_Vec2d) -> None: ...
    @overload
    def __init__(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float) -> None: ...
    @overload
    def __init__(self, Pts: gp_Pnt, Ptc: gp_Pnt, Param: float, U: float, V: float, W: float, Tgs: gp_Vec, Tgc: gp_Vec, Tg2d: gp_Vec2d) -> None: ...
    @overload
    def __init__(self, Pts: gp_Pnt, Ptc: gp_Pnt, Param: float, U: float, V: float, W: float) -> None: ...
    @overload
    def __init__(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC: float, Tg1: gp_Vec, Tg2: gp_Vec, Tg12d: gp_Vec2d, Tg22d: gp_Vec2d) -> None: ...
    @overload
    def __init__(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC: float) -> None: ...
    @overload
    def __init__(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC1: float, PC2: float, Tg1: gp_Vec, Tg2: gp_Vec, Tg12d: gp_Vec2d, Tg22d: gp_Vec2d) -> None: ...
    @overload
    def __init__(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC1: float, PC2: float) -> None: ...
    def IsTangencyPoint(self) -> bool: ...
    def Parameter(self) -> float: ...
    def ParameterOnC(self) -> float: ...
    def ParameterOnC1(self) -> float: ...
    def ParameterOnC2(self) -> float: ...
    def ParametersOnS(self) -> Tuple[float, float]: ...
    def ParametersOnS1(self) -> Tuple[float, float]: ...
    def ParametersOnS2(self) -> Tuple[float, float]: ...
    def PointOnC(self) -> gp_Pnt: ...
    def PointOnC1(self) -> gp_Pnt: ...
    def PointOnC2(self) -> gp_Pnt: ...
    def PointOnS(self) -> gp_Pnt: ...
    def PointOnS1(self) -> gp_Pnt: ...
    def PointOnS2(self) -> gp_Pnt: ...
    def SetParameter(self, Param: float) -> None: ...
    @overload
    def SetValue(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, Tg1: gp_Vec, Tg2: gp_Vec, Tg12d: gp_Vec2d, Tg22d: gp_Vec2d) -> None: ...
    @overload
    def SetValue(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float) -> None: ...
    @overload
    def SetValue(self, Pts: gp_Pnt, Ptc: gp_Pnt, Param: float, U: float, V: float, W: float, Tgs: gp_Vec, Tgc: gp_Vec, Tg2d: gp_Vec2d) -> None: ...
    @overload
    def SetValue(self, Pts: gp_Pnt, Ptc: gp_Pnt, Param: float, U: float, V: float, W: float) -> None: ...
    @overload
    def SetValue(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC: float, Tg1: gp_Vec, Tg2: gp_Vec, Tg12d: gp_Vec2d, Tg22d: gp_Vec2d) -> None: ...
    @overload
    def SetValue(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC: float) -> None: ...
    @overload
    def SetValue(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC1: float, PC2: float, Tg1: gp_Vec, Tg2: gp_Vec, Tg12d: gp_Vec2d, Tg22d: gp_Vec2d) -> None: ...
    @overload
    def SetValue(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, U1: float, V1: float, U2: float, V2: float, PC1: float, PC2: float) -> None: ...
    @overload
    def SetValue(self, Pt1: gp_Pnt, Pt2: gp_Pnt, Param: float, PC1: float, PC2: float) -> None: ...
    def Tangent2d(self) -> gp_Vec2d: ...
    def Tangent2dOnS1(self) -> gp_Vec2d: ...
    def Tangent2dOnS2(self) -> gp_Vec2d: ...
    def TangentOnC(self) -> gp_Vec: ...
    def TangentOnC1(self) -> gp_Vec: ...
    def TangentOnC2(self) -> gp_Vec: ...
    def TangentOnS(self) -> gp_Vec: ...
    def TangentOnS1(self) -> gp_Vec: ...
    def TangentOnS2(self) -> gp_Vec: ...

class Blend_SurfCurvFuncInv(math_FunctionSetWithDerivatives):
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
    def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
    def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def Set(self, Rst: Adaptor2d_Curve2d) -> None: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class Blend_SurfPointFuncInv(math_FunctionSetWithDerivatives):
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
    def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
    def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def Set(self, P: gp_Pnt) -> None: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class Blend_CSFunction(Blend_AppFunction):
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
    def GetMinimalDistance(self) -> float: ...
    def GetShape(self) -> Tuple[int, int, int, int]: ...
    @overload
    def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
    def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
    def IsTangencyPoint(self) -> bool: ...
    def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
    def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def ParameterOnC(self) -> float: ...
    def Pnt1(self) -> gp_Pnt: ...
    def Pnt2(self) -> gp_Pnt: ...
    def Pnt2d(self) -> gp_Pnt2d: ...
    def PointOnC(self) -> gp_Pnt: ...
    def PointOnS(self) -> gp_Pnt: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self, Param: float) -> None: ...
    @overload
    def Set(self, First: float, Last: float) -> None: ...
    def Tangent(self, U: float, V: float, TgS: gp_Vec, NormS: gp_Vec) -> None: ...
    def Tangent2d(self) -> gp_Vec2d: ...
    def TangentOnC(self) -> gp_Vec: ...
    def TangentOnS(self) -> gp_Vec: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class Blend_Function(Blend_AppFunction):
    def IsTangencyPoint(self) -> bool: ...
    def NbVariables(self) -> int: ...
    def Pnt1(self) -> gp_Pnt: ...
    def Pnt2(self) -> gp_Pnt: ...
    def PointOnS1(self) -> gp_Pnt: ...
    def PointOnS2(self) -> gp_Pnt: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
    def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: gp_Vec, TgLast: gp_Vec, NormFirst: gp_Vec, NormLast: gp_Vec) -> None: ...
    def Tangent2dOnS1(self) -> gp_Vec2d: ...
    def Tangent2dOnS2(self) -> gp_Vec2d: ...
    def TangentOnS1(self) -> gp_Vec: ...
    def TangentOnS2(self) -> gp_Vec: ...
    def TwistOnS1(self) -> bool: ...
    def TwistOnS2(self) -> bool: ...

class Blend_RstRstFunction(Blend_AppFunction):
    def Decroch(self, Sol: math_Vector, NRst1: gp_Vec, TgRst1: gp_Vec, NRst2: gp_Vec, TgRst2: gp_Vec) -> Blend_DecrochStatus: ...
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
    def GetMinimalDistance(self) -> float: ...
    def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
    def GetSectionSize(self) -> float: ...
    def GetShape(self) -> Tuple[int, int, int, int]: ...
    @overload
    def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsRational(self) -> bool: ...
    def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
    def IsTangencyPoint(self) -> bool: ...
    def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
    def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
    def NbEquations(self) -> int: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbVariables(self) -> int: ...
    def ParameterOnRst1(self) -> float: ...
    def ParameterOnRst2(self) -> float: ...
    def Pnt1(self) -> gp_Pnt: ...
    def Pnt2(self) -> gp_Pnt: ...
    def Pnt2dOnRst1(self) -> gp_Pnt2d: ...
    def Pnt2dOnRst2(self) -> gp_Pnt2d: ...
    def PointOnRst1(self) -> gp_Pnt: ...
    def PointOnRst2(self) -> gp_Pnt: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self, Param: float) -> None: ...
    @overload
    def Set(self, First: float, Last: float) -> None: ...
    def Tangent2dOnRst1(self) -> gp_Vec2d: ...
    def Tangent2dOnRst2(self) -> gp_Vec2d: ...
    def TangentOnRst1(self) -> gp_Vec: ...
    def TangentOnRst2(self) -> gp_Vec: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class Blend_SurfRstFunction(Blend_AppFunction):
    def Decroch(self, Sol: math_Vector, NS: gp_Vec, TgS: gp_Vec) -> bool: ...
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
    def GetMinimalDistance(self) -> float: ...
    def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
    def GetSectionSize(self) -> float: ...
    def GetShape(self) -> Tuple[int, int, int, int]: ...
    @overload
    def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
    @overload
    def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsRational(self) -> bool: ...
    def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
    def IsTangencyPoint(self) -> bool: ...
    def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
    def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
    def NbEquations(self) -> int: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbVariables(self) -> int: ...
    def ParameterOnRst(self) -> float: ...
    def Pnt1(self) -> gp_Pnt: ...
    def Pnt2(self) -> gp_Pnt: ...
    def Pnt2dOnRst(self) -> gp_Pnt2d: ...
    def Pnt2dOnS(self) -> gp_Pnt2d: ...
    def PointOnRst(self) -> gp_Pnt: ...
    def PointOnS(self) -> gp_Pnt: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
    @overload
    def Set(self, Param: float) -> None: ...
    @overload
    def Set(self, First: float, Last: float) -> None: ...
    def Tangent2dOnRst(self) -> gp_Vec2d: ...
    def Tangent2dOnS(self) -> gp_Vec2d: ...
    def TangentOnRst(self) -> gp_Vec: ...
    def TangentOnS(self) -> gp_Vec: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes

