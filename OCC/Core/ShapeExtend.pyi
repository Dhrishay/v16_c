from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Message import *
from OCC.Core.TopoDS import *
from OCC.Core.Geom import *
from OCC.Core.GeomAbs import *
from OCC.Core.gp import *
from OCC.Core.TColGeom import *
from OCC.Core.TColStd import *
from OCC.Core.TopTools import *
from OCC.Core.TopAbs import *


class ShapeExtend_Parametrisation(IntEnum):
    ShapeExtend_Natural: int = ...
    ShapeExtend_Uniform: int = ...
    ShapeExtend_Unitary: int = ...

ShapeExtend_Natural = ShapeExtend_Parametrisation.ShapeExtend_Natural
ShapeExtend_Uniform = ShapeExtend_Parametrisation.ShapeExtend_Uniform
ShapeExtend_Unitary = ShapeExtend_Parametrisation.ShapeExtend_Unitary

class ShapeExtend_Status(IntEnum):
    ShapeExtend_OK: int = ...
    ShapeExtend_DONE1: int = ...
    ShapeExtend_DONE2: int = ...
    ShapeExtend_DONE3: int = ...
    ShapeExtend_DONE4: int = ...
    ShapeExtend_DONE5: int = ...
    ShapeExtend_DONE6: int = ...
    ShapeExtend_DONE7: int = ...
    ShapeExtend_DONE8: int = ...
    ShapeExtend_DONE: int = ...
    ShapeExtend_FAIL1: int = ...
    ShapeExtend_FAIL2: int = ...
    ShapeExtend_FAIL3: int = ...
    ShapeExtend_FAIL4: int = ...
    ShapeExtend_FAIL5: int = ...
    ShapeExtend_FAIL6: int = ...
    ShapeExtend_FAIL7: int = ...
    ShapeExtend_FAIL8: int = ...
    ShapeExtend_FAIL: int = ...

ShapeExtend_OK = ShapeExtend_Status.ShapeExtend_OK
ShapeExtend_DONE1 = ShapeExtend_Status.ShapeExtend_DONE1
ShapeExtend_DONE2 = ShapeExtend_Status.ShapeExtend_DONE2
ShapeExtend_DONE3 = ShapeExtend_Status.ShapeExtend_DONE3
ShapeExtend_DONE4 = ShapeExtend_Status.ShapeExtend_DONE4
ShapeExtend_DONE5 = ShapeExtend_Status.ShapeExtend_DONE5
ShapeExtend_DONE6 = ShapeExtend_Status.ShapeExtend_DONE6
ShapeExtend_DONE7 = ShapeExtend_Status.ShapeExtend_DONE7
ShapeExtend_DONE8 = ShapeExtend_Status.ShapeExtend_DONE8
ShapeExtend_DONE = ShapeExtend_Status.ShapeExtend_DONE
ShapeExtend_FAIL1 = ShapeExtend_Status.ShapeExtend_FAIL1
ShapeExtend_FAIL2 = ShapeExtend_Status.ShapeExtend_FAIL2
ShapeExtend_FAIL3 = ShapeExtend_Status.ShapeExtend_FAIL3
ShapeExtend_FAIL4 = ShapeExtend_Status.ShapeExtend_FAIL4
ShapeExtend_FAIL5 = ShapeExtend_Status.ShapeExtend_FAIL5
ShapeExtend_FAIL6 = ShapeExtend_Status.ShapeExtend_FAIL6
ShapeExtend_FAIL7 = ShapeExtend_Status.ShapeExtend_FAIL7
ShapeExtend_FAIL8 = ShapeExtend_Status.ShapeExtend_FAIL8
ShapeExtend_FAIL = ShapeExtend_Status.ShapeExtend_FAIL

class shapeextend:
    @staticmethod
    def DecodeStatus(flag: int, status: ShapeExtend_Status) -> bool: ...
    @staticmethod
    def EncodeStatus(status: ShapeExtend_Status) -> int: ...
    @staticmethod
    def Init() -> None: ...

class ShapeExtend_BasicMsgRegistrator(Standard_Transient):
    def __init__(self) -> None: ...
    @overload
    def Send(self, object: Standard_Transient, message: Message_Msg, gravity: Message_Gravity) -> None: ...
    @overload
    def Send(self, shape: TopoDS_Shape, message: Message_Msg, gravity: Message_Gravity) -> None: ...
    @overload
    def Send(self, message: Message_Msg, gravity: Message_Gravity) -> None: ...

class ShapeExtend_ComplexCurve(Geom_Curve):
    def CheckConnectivity(self, Preci: float) -> bool: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def Curve(self, index: int) -> Geom_Curve: ...
    def D0(self, U: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, P: gp_Pnt, V1: gp_Vec) -> None: ...
    def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
    def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
    def DN(self, U: float, N: int) -> gp_Vec: ...
    def FirstParameter(self) -> float: ...
    def GetScaleFactor(self, ind: int) -> float: ...
    def IsCN(self, N: int) -> bool: ...
    def IsClosed(self) -> bool: ...
    def IsPeriodic(self) -> bool: ...
    def LastParameter(self) -> float: ...
    def LocalToGlobal(self, index: int, Ulocal: float) -> float: ...
    def LocateParameter(self, U: float) -> Tuple[int, float]: ...
    def NbCurves(self) -> int: ...
    def ReversedParameter(self, U: float) -> float: ...
    def Transform(self, T: gp_Trsf) -> None: ...

class ShapeExtend_CompositeSurface(Geom_Surface):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, GridSurf: TColGeom_HArray2OfSurface, param: Optional[ShapeExtend_Parametrisation] = ShapeExtend_Natural) -> None: ...
    @overload
    def __init__(self, GridSurf: TColGeom_HArray2OfSurface, UJoints: TColStd_Array1OfReal, VJoints: TColStd_Array1OfReal) -> None: ...
    def Bounds(self) -> Tuple[float, float, float, float]: ...
    def CheckConnectivity(self, prec: float) -> bool: ...
    def ComputeJointValues(self, param: Optional[ShapeExtend_Parametrisation] = ShapeExtend_Natural) -> None: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def Copy(self) -> Geom_Geometry: ...
    def D0(self, U: float, V: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec) -> None: ...
    def D2(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec) -> None: ...
    def D3(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec, D3U: gp_Vec, D3V: gp_Vec, D3UUV: gp_Vec, D3UVV: gp_Vec) -> None: ...
    def DN(self, U: float, V: float, Nu: int, Nv: int) -> gp_Vec: ...
    def GlobalToLocal(self, i: int, j: int, UV: gp_Pnt2d) -> gp_Pnt2d: ...
    def GlobalToLocalTransformation(self, i: int, j: int, Trsf: gp_Trsf2d) -> Tuple[bool, float]: ...
    @overload
    def Init(self, GridSurf: TColGeom_HArray2OfSurface, param: Optional[ShapeExtend_Parametrisation] = ShapeExtend_Natural) -> bool: ...
    @overload
    def Init(self, GridSurf: TColGeom_HArray2OfSurface, UJoints: TColStd_Array1OfReal, VJoints: TColStd_Array1OfReal) -> bool: ...
    def IsCNu(self, N: int) -> bool: ...
    def IsCNv(self, N: int) -> bool: ...
    def IsUClosed(self) -> bool: ...
    def IsUPeriodic(self) -> bool: ...
    def IsVClosed(self) -> bool: ...
    def IsVPeriodic(self) -> bool: ...
    def LocalToGlobal(self, i: int, j: int, uv: gp_Pnt2d) -> gp_Pnt2d: ...
    def LocateUParameter(self, U: float) -> int: ...
    def LocateUVPoint(self, pnt: gp_Pnt2d) -> Tuple[int, int]: ...
    def LocateVParameter(self, V: float) -> int: ...
    def NbUPatches(self) -> int: ...
    def NbVPatches(self) -> int: ...
    @overload
    def Patch(self, i: int, j: int) -> Geom_Surface: ...
    @overload
    def Patch(self, U: float, V: float) -> Geom_Surface: ...
    @overload
    def Patch(self, pnt: gp_Pnt2d) -> Geom_Surface: ...
    def Patches(self) -> TColGeom_HArray2OfSurface: ...
    def SetUFirstValue(self, UFirst: float) -> None: ...
    def SetUJointValues(self, UJoints: TColStd_Array1OfReal) -> bool: ...
    def SetVFirstValue(self, VFirst: float) -> None: ...
    def SetVJointValues(self, VJoints: TColStd_Array1OfReal) -> bool: ...
    def Transform(self, T: gp_Trsf) -> None: ...
    def UGlobalToLocal(self, i: int, j: int, U: float) -> float: ...
    def UIso(self, U: float) -> Geom_Curve: ...
    def UJointValue(self, i: int) -> float: ...
    def UJointValues(self) -> TColStd_HArray1OfReal: ...
    def ULocalToGlobal(self, i: int, j: int, u: float) -> float: ...
    def UReverse(self) -> None: ...
    def UReversedParameter(self, U: float) -> float: ...
    def VGlobalToLocal(self, i: int, j: int, V: float) -> float: ...
    def VIso(self, V: float) -> Geom_Curve: ...
    def VJointValue(self, j: int) -> float: ...
    def VJointValues(self) -> TColStd_HArray1OfReal: ...
    def VLocalToGlobal(self, i: int, j: int, v: float) -> float: ...
    def VReverse(self) -> None: ...
    def VReversedParameter(self, V: float) -> float: ...
    def Value(self, pnt: gp_Pnt2d) -> gp_Pnt: ...

class ShapeExtend_Explorer:
    def __init__(self) -> None: ...
    def CompoundFromSeq(self, seqval: TopTools_HSequenceOfShape) -> TopoDS_Shape: ...
    def DispatchList(self, list: TopTools_HSequenceOfShape, vertices: TopTools_HSequenceOfShape, edges: TopTools_HSequenceOfShape, wires: TopTools_HSequenceOfShape, faces: TopTools_HSequenceOfShape, shells: TopTools_HSequenceOfShape, solids: TopTools_HSequenceOfShape, compsols: TopTools_HSequenceOfShape, compounds: TopTools_HSequenceOfShape) -> None: ...
    def ListFromSeq(self, seqval: TopTools_HSequenceOfShape, lisval: TopTools_ListOfShape, clear: Optional[bool] = True) -> None: ...
    def SeqFromCompound(self, comp: TopoDS_Shape, expcomp: bool) -> TopTools_HSequenceOfShape: ...
    def SeqFromList(self, lisval: TopTools_ListOfShape) -> TopTools_HSequenceOfShape: ...
    def ShapeType(self, shape: TopoDS_Shape, compound: bool) -> TopAbs_ShapeEnum: ...
    def SortedCompound(self, shape: TopoDS_Shape, type: TopAbs_ShapeEnum, explore: bool, compound: bool) -> TopoDS_Shape: ...

class ShapeExtend_WireData(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, wire: TopoDS_Wire, chained: Optional[bool] = True, theManifoldMode: Optional[bool] = True) -> None: ...
    @overload
    def Add(self, edge: TopoDS_Edge, atnum: Optional[int] = 0) -> None: ...
    @overload
    def Add(self, wire: TopoDS_Wire, atnum: Optional[int] = 0) -> None: ...
    @overload
    def Add(self, wire: ShapeExtend_WireData, atnum: Optional[int] = 0) -> None: ...
    @overload
    def Add(self, shape: TopoDS_Shape, atnum: Optional[int] = 0) -> None: ...
    @overload
    def AddOriented(self, edge: TopoDS_Edge, mode: int) -> None: ...
    @overload
    def AddOriented(self, wire: TopoDS_Wire, mode: int) -> None: ...
    @overload
    def AddOriented(self, shape: TopoDS_Shape, mode: int) -> None: ...
    def Clear(self) -> None: ...
    def ComputeSeams(self, enforce: Optional[bool] = True) -> None: ...
    def Edge(self, num: int) -> TopoDS_Edge: ...
    def Index(self, edge: TopoDS_Edge) -> int: ...
    @overload
    def Init(self, other: ShapeExtend_WireData) -> None: ...
    @overload
    def Init(self, wire: TopoDS_Wire, chained: Optional[bool] = True, theManifoldMode: Optional[bool] = True) -> bool: ...
    def IsSeam(self, num: int) -> bool: ...
    def GetManifoldMode(self) -> bool: ...
    def SetManifoldMode(self, value: bool) -> None: ...
    def NbEdges(self) -> int: ...
    def NbNonManifoldEdges(self) -> int: ...
    def NonmanifoldEdge(self, num: int) -> TopoDS_Edge: ...
    def NonmanifoldEdges(self) -> TopTools_HSequenceOfShape: ...
    def Remove(self, num: Optional[int] = 0) -> None: ...
    @overload
    def Reverse(self) -> None: ...
    @overload
    def Reverse(self, face: TopoDS_Face) -> None: ...
    def Set(self, edge: TopoDS_Edge, num: Optional[int] = 0) -> None: ...
    def SetDegeneratedLast(self) -> None: ...
    def SetLast(self, num: int) -> None: ...
    def Wire(self) -> TopoDS_Wire: ...
    def WireAPIMake(self) -> TopoDS_Wire: ...

class ShapeExtend_MsgRegistrator(ShapeExtend_BasicMsgRegistrator):
    def __init__(self) -> None: ...
    def MapShape(self) -> ShapeExtend_DataMapOfShapeListOfMsg: ...
    def MapTransient(self) -> ShapeExtend_DataMapOfTransientListOfMsg: ...
    @overload
    def Send(self, object: Standard_Transient, message: Message_Msg, gravity: Message_Gravity) -> None: ...
    @overload
    def Send(self, shape: TopoDS_Shape, message: Message_Msg, gravity: Message_Gravity) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

