from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.Message import *
from OCC.Core.gp import *


class math_Array1OfValueAndWeight:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> math_ValueAndWeight: ...
    def __setitem__(self, index: int, value: math_ValueAndWeight) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[math_ValueAndWeight]: ...
    def next(self) -> math_ValueAndWeight: ...
    __next__ = next
    def Init(self, theValue: math_ValueAndWeight) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> math_ValueAndWeight: ...
    def Last(self) -> math_ValueAndWeight: ...
    def Value(self, theIndex: int) -> math_ValueAndWeight: ...
    def SetValue(self, theIndex: int, theValue: math_ValueAndWeight) -> None: ...

class math_Status(IntEnum):
    math_OK: int = ...
    math_TooManyIterations: int = ...
    math_FunctionError: int = ...
    math_DirectionSearchError: int = ...
    math_NotBracketed: int = ...

math_OK = math_Status.math_OK
math_TooManyIterations = math_Status.math_TooManyIterations
math_FunctionError = math_Status.math_FunctionError
math_DirectionSearchError = math_Status.math_DirectionSearchError
math_NotBracketed = math_Status.math_NotBracketed

class math:
    @staticmethod
    def GaussPoints(Index: int, Points: math_Vector) -> None: ...
    @staticmethod
    def GaussPointsMax() -> int: ...
    @staticmethod
    def GaussWeights(Index: int, Weights: math_Vector) -> None: ...
    @staticmethod
    def KronrodPointsAndWeights(Index: int, Points: math_Vector, Weights: math_Vector) -> bool: ...
    @staticmethod
    def KronrodPointsMax() -> int: ...
    @staticmethod
    def OrderedGaussPointsAndWeights(Index: int, Points: math_Vector, Weights: math_Vector) -> bool: ...

class math_BFGS:
    def __init__(self, NbVariables: int, Tolerance: Optional[float] = 1.0e-8, NbIterations: Optional[int] = 200, ZEPS: Optional[float] = 1.0e-12) -> None: ...
    def Dump(self) -> str: ...
    @overload
    def Gradient(self) -> math_Vector: ...
    @overload
    def Gradient(self, Grad: math_Vector) -> None: ...
    def IsDone(self) -> bool: ...
    def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool: ...
    @overload
    def Location(self) -> math_Vector: ...
    @overload
    def Location(self, Loc: math_Vector) -> None: ...
    def Minimum(self) -> float: ...
    def NbIterations(self) -> int: ...
    def Perform(self, F: math_MultipleVarFunctionWithGradient, StartingPoint: math_Vector) -> None: ...
    def SetBoundary(self, theLeftBorder: math_Vector, theRightBorder: math_Vector) -> None: ...

class math_BissecNewton:
    def __init__(self, theXTolerance: float) -> None: ...
    def Derivative(self) -> float: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def IsSolutionReached(self, theFunction: math_FunctionWithDerivative) -> bool: ...
    def Perform(self, F: math_FunctionWithDerivative, Bound1: float, Bound2: float, NbIterations: Optional[int] = 100) -> None: ...
    def Root(self) -> float: ...
    def Value(self) -> float: ...

class math_BracketMinimum:
    @overload
    def __init__(self, A: float, B: float) -> None: ...
    @overload
    def __init__(self, F: math_Function, A: float, B: float) -> None: ...
    @overload
    def __init__(self, F: math_Function, A: float, B: float, FA: float) -> None: ...
    @overload
    def __init__(self, F: math_Function, A: float, B: float, FA: float, FB: float) -> None: ...
    def Dump(self) -> str: ...
    def FunctionValues(self) -> Tuple[float, float, float]: ...
    def IsDone(self) -> bool: ...
    def Perform(self, F: math_Function) -> None: ...
    def SetFA(self, theValue: float) -> None: ...
    def SetFB(self, theValue: float) -> None: ...
    def SetLimits(self, theLeft: float, theRight: float) -> None: ...
    def Values(self) -> Tuple[float, float, float]: ...

class math_BracketedRoot:
    def __init__(self, F: math_Function, Bound1: float, Bound2: float, Tolerance: float, NbIterations: Optional[int] = 100, ZEPS: Optional[float] = 1.0e-12) -> None: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def NbIterations(self) -> int: ...
    def Root(self) -> float: ...
    def Value(self) -> float: ...

class math_BrentMinimum:
    @overload
    def __init__(self, TolX: float, NbIterations: Optional[int] = 100, ZEPS: Optional[float] = 1.0e-12) -> None: ...
    @overload
    def __init__(self, TolX: float, Fbx: float, NbIterations: Optional[int] = 100, ZEPS: Optional[float] = 1.0e-12) -> None: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def IsSolutionReached(self, theFunction: math_Function) -> bool: ...
    def Location(self) -> float: ...
    def Minimum(self) -> float: ...
    def NbIterations(self) -> int: ...
    def Perform(self, F: math_Function, Ax: float, Bx: float, Cx: float) -> None: ...

class math_BullardGenerator:
    def __init__(self, theSeed: Optional[int] = 1) -> None: ...
    def NextInt(self) -> int: ...
    def NextReal(self) -> float: ...
    def SetSeed(self, theSeed: Optional[int] = 1) -> None: ...

class math_ComputeGaussPointsAndWeights:
    def __init__(self, Number: int) -> None: ...
    def IsDone(self) -> bool: ...
    def Points(self) -> math_Vector: ...
    def Weights(self) -> math_Vector: ...

class math_ComputeKronrodPointsAndWeights:
    def __init__(self, Number: int) -> None: ...
    def IsDone(self) -> bool: ...
    def Points(self) -> math_Vector: ...
    def Weights(self) -> math_Vector: ...

class math_Crout:
    def __init__(self, A: math_Matrix, MinPivot: Optional[float] = 1.0e-20) -> None: ...
    def Determinant(self) -> float: ...
    def Dump(self) -> str: ...
    def Inverse(self) -> math_Matrix: ...
    def Invert(self, Inv: math_Matrix) -> None: ...
    def IsDone(self) -> bool: ...
    def Solve(self, B: math_Vector, X: math_Vector) -> None: ...

class math_DirectPolynomialRoots:
    @overload
    def __init__(self, A: float, B: float, C: float, D: float, E: float) -> None: ...
    @overload
    def __init__(self, A: float, B: float, C: float, D: float) -> None: ...
    @overload
    def __init__(self, A: float, B: float, C: float) -> None: ...
    @overload
    def __init__(self, A: float, B: float) -> None: ...
    def Dump(self) -> str: ...
    def InfiniteRoots(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def NbSolutions(self) -> int: ...
    def Value(self, Nieme: int) -> float: ...

class math_DoubleTab:
    @overload
    def __init__(self, LowerRow: int, UpperRow: int, LowerCol: int, UpperCol: int) -> None: ...
    @overload
    def __init__(self, Tab: None, LowerRow: int, UpperRow: int, LowerCol: int, UpperCol: int) -> None: ...
    @overload
    def __init__(self, Other: math_DoubleTab) -> None: ...
    def Copy(self, Other: math_DoubleTab) -> None: ...
    def Free(self) -> None: ...
    def Init(self, InitValue: float) -> None: ...
    def SetLowerCol(self, LowerCol: int) -> None: ...
    def SetLowerRow(self, LowerRow: int) -> None: ...
    def GetValue(self, RowIndex: int, ColIndex: int) -> float: ...
    def SetValue(self, RowIndex: int, ColIndex: int, value: float) -> None: ...

class math_EigenValuesSearcher:
    def __init__(self, Diagonal: TColStd_Array1OfReal, Subdiagonal: TColStd_Array1OfReal) -> None: ...
    def Dimension(self) -> int: ...
    def EigenValue(self, Index: int) -> float: ...
    def EigenVector(self, Index: int) -> math_Vector: ...
    def IsDone(self) -> bool: ...

class math_FRPR:
    def __init__(self, theFunction: math_MultipleVarFunctionWithGradient, theTolerance: float, theNbIterations: Optional[int] = 200, theZEPS: Optional[float] = 1.0e-12) -> None: ...
    def Dump(self) -> str: ...
    @overload
    def Gradient(self) -> math_Vector: ...
    @overload
    def Gradient(self, Grad: math_Vector) -> None: ...
    def IsDone(self) -> bool: ...
    def IsSolutionReached(self, theFunction: math_MultipleVarFunctionWithGradient) -> bool: ...
    @overload
    def Location(self) -> math_Vector: ...
    @overload
    def Location(self, Loc: math_Vector) -> None: ...
    def Minimum(self) -> float: ...
    def NbIterations(self) -> int: ...
    def Perform(self, theFunction: math_MultipleVarFunctionWithGradient, theStartingPoint: math_Vector) -> None: ...

class math_Function:
    def GetStateNumber(self) -> int: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...

class math_FunctionAllRoots:
    def __init__(self, F: math_FunctionWithDerivative, S: math_FunctionSample, EpsX: float, EpsF: float, EpsNul: float) -> None: ...
    def Dump(self) -> str: ...
    def GetInterval(self, Index: int) -> Tuple[float, float]: ...
    def GetIntervalState(self, Index: int) -> Tuple[int, int]: ...
    def GetPoint(self, Index: int) -> float: ...
    def GetPointState(self, Index: int) -> int: ...
    def IsDone(self) -> bool: ...
    def NbIntervals(self) -> int: ...
    def NbPoints(self) -> int: ...

class math_FunctionRoot:
    @overload
    def __init__(self, F: math_FunctionWithDerivative, Guess: float, Tolerance: float, NbIterations: Optional[int] = 100) -> None: ...
    @overload
    def __init__(self, F: math_FunctionWithDerivative, Guess: float, Tolerance: float, A: float, B: float, NbIterations: Optional[int] = 100) -> None: ...
    def Derivative(self) -> float: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def NbIterations(self) -> int: ...
    def Root(self) -> float: ...
    def Value(self) -> float: ...

class math_FunctionRoots:
    def __init__(self, F: math_FunctionWithDerivative, A: float, B: float, NbSample: int, EpsX: Optional[float] = 0.0, EpsF: Optional[float] = 0.0, EpsNull: Optional[float] = 0.0, K: Optional[float] = 0.0) -> None: ...
    def Dump(self) -> str: ...
    def IsAllNull(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def NbSolutions(self) -> int: ...
    def StateNumber(self, Nieme: int) -> int: ...
    def Value(self, Nieme: int) -> float: ...

class math_FunctionSample:
    def __init__(self, A: float, B: float, N: int) -> None: ...
    def Bounds(self) -> Tuple[float, float]: ...
    def GetParameter(self, Index: int) -> float: ...
    def NbPoints(self) -> int: ...

class math_FunctionSet:
    def GetStateNumber(self) -> int: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...

class math_FunctionSetRoot:
    @overload
    def __init__(self, F: math_FunctionSetWithDerivatives, Tolerance: math_Vector, NbIterations: Optional[int] = 100) -> None: ...
    @overload
    def __init__(self, F: math_FunctionSetWithDerivatives, NbIterations: Optional[int] = 100) -> None: ...
    @overload
    def Derivative(self) -> math_Matrix: ...
    @overload
    def Derivative(self, Der: math_Matrix) -> None: ...
    def Dump(self) -> str: ...
    @overload
    def FunctionSetErrors(self) -> math_Vector: ...
    @overload
    def FunctionSetErrors(self, Err: math_Vector) -> None: ...
    def IsDivergent(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def NbIterations(self) -> int: ...
    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: math_Vector, theStopOnDivergent: Optional[bool] = False) -> None: ...
    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: math_Vector, theInfBound: math_Vector, theSupBound: math_Vector, theStopOnDivergent: Optional[bool] = False) -> None: ...
    @overload
    def Root(self) -> math_Vector: ...
    @overload
    def Root(self, Root: math_Vector) -> None: ...
    def SetTolerance(self, Tolerance: math_Vector) -> None: ...
    def StateNumber(self) -> int: ...

class math_Gauss:
    def __init__(self, A: math_Matrix, MinPivot: Optional[float] = 1.0e-20, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def Determinant(self) -> float: ...
    def Dump(self) -> str: ...
    def Invert(self, Inv: math_Matrix) -> None: ...
    def IsDone(self) -> bool: ...
    @overload
    def Solve(self, B: math_Vector, X: math_Vector) -> None: ...
    @overload
    def Solve(self, B: math_Vector) -> None: ...

class math_GaussLeastSquare:
    def __init__(self, A: math_Matrix, MinPivot: Optional[float] = 1.0e-20) -> None: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def Solve(self, B: math_Vector, X: math_Vector) -> None: ...

class math_GaussMultipleIntegration:
    def __init__(self, F: math_MultipleVarFunction, Lower: math_Vector, Upper: math_Vector, Order: math_IntegerVector) -> None: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def Value(self) -> float: ...

class math_GaussSetIntegration:
    def __init__(self, F: math_FunctionSet, Lower: math_Vector, Upper: math_Vector, Order: math_IntegerVector) -> None: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def Value(self) -> math_Vector: ...

class math_GaussSingleIntegration:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, F: math_Function, Lower: float, Upper: float, Order: int) -> None: ...
    @overload
    def __init__(self, F: math_Function, Lower: float, Upper: float, Order: int, Tol: float) -> None: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def Value(self) -> float: ...

class math_GlobOptMin:
    def __init__(self, theFunc: math_MultipleVarFunction, theLowerBorder: math_Vector, theUpperBorder: math_Vector, theC: Optional[float] = 9, theDiscretizationTol: Optional[float] = 1.0e-2, theSameTol: Optional[float] = 1.0e-7) -> None: ...
    def GetContinuity(self) -> int: ...
    def GetF(self) -> float: ...
    def GetFunctionalMinimalValue(self) -> float: ...
    def GetLipConstState(self) -> bool: ...
    def GetTol(self) -> Tuple[float, float]: ...
    def NbExtrema(self) -> int: ...
    def Perform(self, isFindSingleSolution: Optional[bool] = False) -> None: ...
    def Points(self, theIndex: int, theSol: math_Vector) -> None: ...
    def SetContinuity(self, theCont: int) -> None: ...
    def SetFunctionalMinimalValue(self, theMinimalValue: float) -> None: ...
    def SetGlobalParams(self, theFunc: math_MultipleVarFunction, theLowerBorder: math_Vector, theUpperBorder: math_Vector, theC: Optional[float] = 9, theDiscretizationTol: Optional[float] = 1.0e-2, theSameTol: Optional[float] = 1.0e-7) -> None: ...
    def SetLipConstState(self, theFlag: bool) -> None: ...
    def SetLocalParams(self, theLocalA: math_Vector, theLocalB: math_Vector) -> None: ...
    def SetTol(self, theDiscretizationTol: float, theSameTol: float) -> None: ...
    def isDone(self) -> bool: ...

class math_Householder:
    @overload
    def __init__(self, A: math_Matrix, B: math_Matrix, EPS: Optional[float] = 1.0e-20) -> None: ...
    @overload
    def __init__(self, A: math_Matrix, B: math_Matrix, lowerArow: int, upperArow: int, lowerAcol: int, upperAcol: int, EPS: Optional[float] = 1.0e-20) -> None: ...
    @overload
    def __init__(self, A: math_Matrix, B: math_Vector, EPS: Optional[float] = 1.0e-20) -> None: ...
    def AllValues(self) -> math_Matrix: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def Value(self, sol: math_Vector, Index: Optional[int] = 1) -> None: ...

class math_Jacobi:
    def __init__(self, A: math_Matrix) -> None: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def Value(self, Num: int) -> float: ...
    def Values(self) -> math_Vector: ...
    def Vector(self, Num: int, V: math_Vector) -> None: ...
    def Vectors(self) -> math_Matrix: ...

class math_KronrodSingleIntegration:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theFunction: math_Function, theLower: float, theUpper: float, theNbPnts: int) -> None: ...
    @overload
    def __init__(self, theFunction: math_Function, theLower: float, theUpper: float, theNbPnts: int, theTolerance: float, theMaxNbIter: int) -> None: ...
    def AbsolutError(self) -> float: ...
    def ErrorReached(self) -> float: ...
    @staticmethod
    def GKRule(theFunction: math_Function, theLower: float, theUpper: float, theGaussP: math_Vector, theGaussW: math_Vector, theKronrodP: math_Vector, theKronrodW: math_Vector) -> Tuple[bool, float, float]: ...
    def IsDone(self) -> bool: ...
    def NbIterReached(self) -> int: ...
    def OrderReached(self) -> int: ...
    @overload
    def Perform(self, theFunction: math_Function, theLower: float, theUpper: float, theNbPnts: int) -> None: ...
    @overload
    def Perform(self, theFunction: math_Function, theLower: float, theUpper: float, theNbPnts: int, theTolerance: float, theMaxNbIter: int) -> None: ...
    def Value(self) -> float: ...

class math_Matrix:
    @overload
    def __init__(self, LowerRow: int, UpperRow: int, LowerCol: int, UpperCol: int) -> None: ...
    @overload
    def __init__(self, LowerRow: int, UpperRow: int, LowerCol: int, UpperCol: int, InitialValue: float) -> None: ...
    @overload
    def __init__(self, Tab: None, LowerRow: int, UpperRow: int, LowerCol: int, UpperCol: int) -> None: ...
    @overload
    def __init__(self, Other: math_Matrix) -> None: ...
    @overload
    def Add(self, Right: math_Matrix) -> None: ...
    @overload
    def Add(self, Left: math_Matrix, Right: math_Matrix) -> None: ...
    def Added(self, Right: math_Matrix) -> math_Matrix: ...
    def Col(self, Col: int) -> False: ...
    def ColNumber(self) -> int: ...
    def Determinant(self) -> float: ...
    def Divide(self, Right: float) -> None: ...
    def Divided(self, Right: float) -> math_Matrix: ...
    def Dump(self) -> str: ...
    def Init(self, InitialValue: float) -> None: ...
    def Initialized(self, Other: math_Matrix) -> math_Matrix: ...
    def Inverse(self) -> math_Matrix: ...
    def Invert(self) -> None: ...
    def LowerCol(self) -> int: ...
    def LowerRow(self) -> int: ...
    @overload
    def Multiplied(self, Right: float) -> math_Matrix: ...
    @overload
    def Multiplied(self, Right: math_Matrix) -> math_Matrix: ...
    @overload
    def Multiply(self, Right: float) -> None: ...
    @overload
    def Multiply(self, Left: math_Matrix, Right: math_Matrix) -> None: ...
    @overload
    def Multiply(self, Right: math_Matrix) -> None: ...
    def Opposite(self) -> math_Matrix: ...
    def Row(self, Row: int) -> False: ...
    def RowNumber(self) -> int: ...
    def Set(self, I1: int, I2: int, J1: int, J2: int, M: math_Matrix) -> None: ...
    def SetDiag(self, Value: float) -> None: ...
    @overload
    def Subtract(self, Right: math_Matrix) -> None: ...
    @overload
    def Subtract(self, Left: math_Matrix, Right: math_Matrix) -> None: ...
    def Subtracted(self, Right: math_Matrix) -> math_Matrix: ...
    def SwapCol(self, Col1: int, Col2: int) -> None: ...
    def SwapRow(self, Row1: int, Row2: int) -> None: ...
    def TMultiplied(self, Right: float) -> math_Matrix: ...
    @overload
    def TMultiply(self, Right: math_Matrix) -> math_Matrix: ...
    @overload
    def TMultiply(self, TLeft: math_Matrix, Right: math_Matrix) -> None: ...
    def Transpose(self) -> None: ...
    def Transposed(self) -> math_Matrix: ...
    def UpperCol(self) -> int: ...
    def UpperRow(self) -> int: ...
    def GetValue(self, Row: int, Col: int) -> float: ...
    def SetValue(self, Row: int, Col: int, value: float) -> None: ...

class math_MultipleVarFunction:
    def GetStateNumber(self) -> int: ...
    def NbVariables(self) -> int: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...

class math_NewtonFunctionRoot:
    @overload
    def __init__(self, F: math_FunctionWithDerivative, Guess: float, EpsX: float, EpsF: float, NbIterations: Optional[int] = 100) -> None: ...
    @overload
    def __init__(self, F: math_FunctionWithDerivative, Guess: float, EpsX: float, EpsF: float, A: float, B: float, NbIterations: Optional[int] = 100) -> None: ...
    @overload
    def __init__(self, A: float, B: float, EpsX: float, EpsF: float, NbIterations: Optional[int] = 100) -> None: ...
    def Derivative(self) -> float: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def NbIterations(self) -> int: ...
    def Perform(self, F: math_FunctionWithDerivative, Guess: float) -> None: ...
    def Root(self) -> float: ...
    def Value(self) -> float: ...

class math_NewtonFunctionSetRoot:
    @overload
    def __init__(self, theFunction: math_FunctionSetWithDerivatives, theXTolerance: math_Vector, theFTolerance: float, tehNbIterations: Optional[int] = 100) -> None: ...
    @overload
    def __init__(self, theFunction: math_FunctionSetWithDerivatives, theFTolerance: float, theNbIterations: Optional[int] = 100) -> None: ...
    @overload
    def Derivative(self) -> math_Matrix: ...
    @overload
    def Derivative(self, Der: math_Matrix) -> None: ...
    def Dump(self) -> str: ...
    @overload
    def FunctionSetErrors(self) -> math_Vector: ...
    @overload
    def FunctionSetErrors(self, Err: math_Vector) -> None: ...
    def IsDone(self) -> bool: ...
    def IsSolutionReached(self, F: math_FunctionSetWithDerivatives) -> bool: ...
    def NbIterations(self) -> int: ...
    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: math_Vector) -> None: ...
    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: math_Vector, theInfBound: math_Vector, theSupBound: math_Vector) -> None: ...
    @overload
    def Root(self) -> math_Vector: ...
    @overload
    def Root(self, Root: math_Vector) -> None: ...
    def SetTolerance(self, XTol: math_Vector) -> None: ...

class math_NewtonMinimum:
    def __init__(self, theFunction: math_MultipleVarFunctionWithHessian, theTolerance: Optional[float] = Precision.Confusion(), theNbIterations: Optional[int] = 40, theConvexity: Optional[float] = 1.0e-6, theWithSingularity: Optional[bool] = True) -> None: ...
    def Dump(self) -> str: ...
    def GetStatus(self) -> math_Status: ...
    @overload
    def Gradient(self) -> math_Vector: ...
    @overload
    def Gradient(self, Grad: math_Vector) -> None: ...
    def IsConverged(self) -> bool: ...
    def IsDone(self) -> bool: ...
    @overload
    def Location(self) -> math_Vector: ...
    @overload
    def Location(self, Loc: math_Vector) -> None: ...
    def Minimum(self) -> float: ...
    def NbIterations(self) -> int: ...
    def Perform(self, theFunction: math_MultipleVarFunctionWithHessian, theStartingPoint: math_Vector) -> None: ...
    def SetBoundary(self, theLeftBorder: math_Vector, theRightBorder: math_Vector) -> None: ...

class math_PSO:
    def __init__(self, theFunc: math_MultipleVarFunction, theLowBorder: math_Vector, theUppBorder: math_Vector, theSteps: math_Vector, theNbParticles: Optional[int] = 32, theNbIter: Optional[int] = 100) -> None: ...
    @overload
    def Perform(self, theSteps: math_Vector, theOutPnt: math_Vector, theNbIter: Optional[int] = 100) -> float: ...
    @overload
    def Perform(self, theParticles: math_PSOParticlesPool, theNbParticles: int, theOutPnt: math_Vector, theNbIter: Optional[int] = 100) -> float: ...

class math_PSOParticlesPool:
    def __init__(self, theParticlesCount: int, theDimensionCount: int) -> None: ...
    def GetBestParticle(self) -> False: ...
    def GetParticle(self, theIdx: int) -> False: ...
    def GetWorstParticle(self) -> False: ...

class math_Powell:
    def __init__(self, theFunction: math_MultipleVarFunction, theTolerance: float, theNbIterations: Optional[int] = 200, theZEPS: Optional[float] = 1.0e-12) -> None: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def IsSolutionReached(self, theFunction: math_MultipleVarFunction) -> bool: ...
    @overload
    def Location(self) -> math_Vector: ...
    @overload
    def Location(self, Loc: math_Vector) -> None: ...
    def Minimum(self) -> float: ...
    def NbIterations(self) -> int: ...
    def Perform(self, theFunction: math_MultipleVarFunction, theStartingPoint: math_Vector, theStartingDirections: math_Matrix) -> None: ...

class math_SVD:
    def __init__(self, A: math_Matrix) -> None: ...
    def Dump(self) -> str: ...
    def IsDone(self) -> bool: ...
    def PseudoInverse(self, Inv: math_Matrix, Eps: Optional[float] = 1.0e-6) -> None: ...
    def Solve(self, B: math_Vector, X: math_Vector, Eps: Optional[float] = 1.0e-6) -> None: ...

class math_TrigonometricFunctionRoots:
    @overload
    def __init__(self, A: float, B: float, C: float, D: float, E: float, InfBound: float, SupBound: float) -> None: ...
    @overload
    def __init__(self, D: float, E: float, InfBound: float, SupBound: float) -> None: ...
    @overload
    def __init__(self, C: float, D: float, E: float, InfBound: float, SupBound: float) -> None: ...
    def Dump(self) -> str: ...
    def InfiniteRoots(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def NbSolutions(self) -> int: ...
    def Value(self, Index: int) -> float: ...

class math_Uzawa:
    @overload
    def __init__(self, Cont: math_Matrix, Secont: math_Vector, StartingPoint: math_Vector, EpsLix: Optional[float] = 1.0e-06, EpsLic: Optional[float] = 1.0e-06, NbIterations: Optional[int] = 500) -> None: ...
    @overload
    def __init__(self, Cont: math_Matrix, Secont: math_Vector, StartingPoint: math_Vector, Nci: int, Nce: int, EpsLix: Optional[float] = 1.0e-06, EpsLic: Optional[float] = 1.0e-06, NbIterations: Optional[int] = 500) -> None: ...
    def Duale(self, V: math_Vector) -> None: ...
    def Dump(self) -> str: ...
    def Error(self) -> math_Vector: ...
    def InitialError(self) -> math_Vector: ...
    def InverseCont(self) -> math_Matrix: ...
    def IsDone(self) -> bool: ...
    def NbIterations(self) -> int: ...
    def Value(self) -> math_Vector: ...

class math_ValueAndWeight:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theValue: float, theWeight: float) -> None: ...
    def Value(self) -> float: ...
    def Weight(self) -> float: ...

class math_VectorBase:
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    @overload
    def __init__(self, Other: gp_XY) -> None: ...
    @overload
    def __init__(self, Other: gp_XYZ) -> None: ...
    @overload
    def __init__(self, theOther: math_VectorBase) -> None: ...
    @overload
    def Add(self, theRight: math_VectorBase) -> None: ...
    @overload
    def Add(self, theLeft: math_VectorBase, theRight: math_VectorBase) -> None: ...
    def Added(self, theRight: math_VectorBase) -> math_VectorBase: ...
    def Dump(self) -> str: ...
    def Initialized(self, theOther: math_VectorBase) -> math_VectorBase: ...
    def Inverse(self) -> math_VectorBase: ...
    def Invert(self) -> None: ...
    def Length(self) -> int: ...
    def Lower(self) -> int: ...
    def Max(self) -> int: ...
    def Min(self) -> int: ...
    @overload
    def Multiplied(self, theRight: math_VectorBase) -> False: ...
    @overload
    def Multiplied(self, theRight: math_Matrix) -> math_VectorBase: ...
    @overload
    def Multiply(self, theLeft: math_VectorBase, theRight: math_Matrix) -> None: ...
    @overload
    def Multiply(self, theLeft: math_Matrix, theRight: math_VectorBase) -> None: ...
    def Norm(self) -> float: ...
    def Norm2(self) -> float: ...
    def Normalize(self) -> None: ...
    def Normalized(self) -> math_VectorBase: ...
    def Opposite(self) -> math_VectorBase: ...
    def Set(self, theI1: int, theI2: int, theV: math_VectorBase) -> None: ...
    def Slice(self, theI1: int, theI2: int) -> math_VectorBase: ...
    @overload
    def Subtract(self, theLeft: math_VectorBase, theRight: math_VectorBase) -> None: ...
    @overload
    def Subtract(self, theRight: math_VectorBase) -> None: ...
    def Subtracted(self, theRight: math_VectorBase) -> math_VectorBase: ...
    @overload
    def TMultiply(self, theTLeft: math_Matrix, theRight: math_VectorBase) -> None: ...
    @overload
    def TMultiply(self, theLeft: math_VectorBase, theTRight: math_Matrix) -> None: ...
    def Upper(self) -> int: ...
    @overload
    def Value(self, theNum: int) -> False: ...
    @overload
    def Value(self, theNum: int) -> False: ...

class math_FunctionSetWithDerivatives(math_FunctionSet):
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class math_FunctionWithDerivative(math_Function):
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

class math_MultipleVarFunctionWithGradient(math_MultipleVarFunction):
    def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
    def NbVariables(self) -> int: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...
    def Values(self, X: math_Vector, G: math_Vector) -> Tuple[bool, float]: ...

class math_MultipleVarFunctionWithHessian(math_MultipleVarFunctionWithGradient):
    def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
    def NbVariables(self) -> int: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...
    @overload
    def Values(self, X: math_Vector, G: math_Vector) -> Tuple[bool, float]: ...
    @overload
    def Values(self, X: math_Vector, G: math_Vector, H: math_Matrix) -> Tuple[bool, float]: ...

class math_TrigonometricEquationFunction(math_FunctionWithDerivative):
    def __init__(self, A: float, B: float, C: float, D: float, E: float) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

# harray1 classes
# harray2 classes
# hsequence classes

