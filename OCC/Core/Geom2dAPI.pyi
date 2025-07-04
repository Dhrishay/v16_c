from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Geom2d import *
from OCC.Core.Extrema import *
from OCC.Core.gp import *
from OCC.Core.Geom2dInt import *
from OCC.Core.TColgp import *
from OCC.Core.TColStd import *
from OCC.Core.GeomAbs import *
from OCC.Core.Approx import *


class Geom2dAPI_ExtremaCurveCurve:
    @overload
    def __init__(self, C1: Geom2d_Curve, C2: Geom2d_Curve, U1min: float, U1max: float, U2min: float, U2max: float) -> None: ...
    def Distance(self, Index: int) -> float: ...
    def Extrema(self) -> Extrema_ExtCC2d: ...
    def LowerDistance(self) -> float: ...
    def LowerDistanceParameters(self) -> Tuple[float, float]: ...
    def NbExtrema(self) -> int: ...
    def NearestPoints(self, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    def Parameters(self, Index: int) -> Tuple[float, float]: ...
    def Points(self, Index: int, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...

class Geom2dAPI_InterCurveCurve:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, C1: Geom2d_Curve, C2: Geom2d_Curve, Tol: Optional[float] = 1.0e-6) -> None: ...
    @overload
    def __init__(self, C1: Geom2d_Curve, Tol: Optional[float] = 1.0e-6) -> None: ...
    @overload
    def Init(self, C1: Geom2d_Curve, C2: Geom2d_Curve, Tol: Optional[float] = 1.0e-6) -> None: ...
    @overload
    def Init(self, C1: Geom2d_Curve, Tol: Optional[float] = 1.0e-6) -> None: ...
    def Intersector(self) -> Geom2dInt_GInter: ...
    def NbPoints(self) -> int: ...
    def NbSegments(self) -> int: ...
    def Point(self, Index: int) -> gp_Pnt2d: ...
    def Segment(self, Index: int, Curve1: Geom2d_Curve, Curve2: Geom2d_Curve) -> None: ...

class Geom2dAPI_Interpolate:
    @overload
    def __init__(self, Points: TColgp_HArray1OfPnt2d, PeriodicFlag: bool, Tolerance: float) -> None: ...
    @overload
    def __init__(self, Points: TColgp_HArray1OfPnt2d, Parameters: TColStd_HArray1OfReal, PeriodicFlag: bool, Tolerance: float) -> None: ...
    def Curve(self) -> Geom2d_BSplineCurve: ...
    def IsDone(self) -> bool: ...
    @overload
    def Load(self, InitialTangent: gp_Vec2d, FinalTangent: gp_Vec2d, Scale: Optional[bool] = True) -> None: ...
    @overload
    def Load(self, Tangents: TColgp_Array1OfVec2d, TangentFlags: TColStd_HArray1OfBoolean, Scale: Optional[bool] = True) -> None: ...
    def Perform(self) -> None: ...

class Geom2dAPI_PointsToBSpline:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Points: TColgp_Array1OfPnt2d, DegMin: Optional[int] = 3, DegMax: Optional[int] = 8, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Tol2D: Optional[float] = 1.0e-6) -> None: ...
    @overload
    def __init__(self, YValues: TColStd_Array1OfReal, X0: float, DX: float, DegMin: Optional[int] = 3, DegMax: Optional[int] = 8, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Tol2D: Optional[float] = 1.0e-6) -> None: ...
    @overload
    def __init__(self, Points: TColgp_Array1OfPnt2d, ParType: Approx_ParametrizationType, DegMin: Optional[int] = 3, DegMax: Optional[int] = 8, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Tol2D: Optional[float] = 1.0e-3) -> None: ...
    @overload
    def __init__(self, Points: TColgp_Array1OfPnt2d, Parameters: TColStd_Array1OfReal, DegMin: Optional[int] = 3, DegMax: Optional[int] = 8, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Tol2D: Optional[float] = 1.0e-3) -> None: ...
    @overload
    def __init__(self, Points: TColgp_Array1OfPnt2d, Weight1: float, Weight2: float, Weight3: float, DegMax: Optional[int] = 8, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Tol3D: Optional[float] = 1.0e-3) -> None: ...
    def Curve(self) -> Geom2d_BSplineCurve: ...
    @overload
    def Init(self, Points: TColgp_Array1OfPnt2d, DegMin: Optional[int] = 3, DegMax: Optional[int] = 8, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Tol2D: Optional[float] = 1.0e-6) -> None: ...
    @overload
    def Init(self, YValues: TColStd_Array1OfReal, X0: float, DX: float, DegMin: Optional[int] = 3, DegMax: Optional[int] = 8, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Tol2D: Optional[float] = 1.0e-6) -> None: ...
    @overload
    def Init(self, Points: TColgp_Array1OfPnt2d, ParType: Approx_ParametrizationType, DegMin: Optional[int] = 3, DegMax: Optional[int] = 8, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Tol2D: Optional[float] = 1.0e-3) -> None: ...
    @overload
    def Init(self, Points: TColgp_Array1OfPnt2d, Parameters: TColStd_Array1OfReal, DegMin: Optional[int] = 3, DegMax: Optional[int] = 8, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Tol2D: Optional[float] = 1.0e-3) -> None: ...
    @overload
    def Init(self, Points: TColgp_Array1OfPnt2d, Weight1: float, Weight2: float, Weight3: float, DegMax: Optional[int] = 8, Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2, Tol2D: Optional[float] = 1.0e-3) -> None: ...
    def IsDone(self) -> bool: ...

class Geom2dAPI_ProjectPointOnCurve:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, P: gp_Pnt2d, Curve: Geom2d_Curve) -> None: ...
    @overload
    def __init__(self, P: gp_Pnt2d, Curve: Geom2d_Curve, Umin: float, Usup: float) -> None: ...
    def Distance(self, Index: int) -> float: ...
    def Extrema(self) -> Extrema_ExtPC2d: ...
    @overload
    def Init(self, P: gp_Pnt2d, Curve: Geom2d_Curve) -> None: ...
    @overload
    def Init(self, P: gp_Pnt2d, Curve: Geom2d_Curve, Umin: float, Usup: float) -> None: ...
    def LowerDistance(self) -> float: ...
    def LowerDistanceParameter(self) -> float: ...
    def NbPoints(self) -> int: ...
    def NearestPoint(self) -> gp_Pnt2d: ...
    @overload
    def Parameter(self, Index: int) -> float: ...
    @overload
    def Parameter(self, Index: int) -> float: ...
    def Point(self, Index: int) -> gp_Pnt2d: ...

# harray1 classes
# harray2 classes
# hsequence classes

