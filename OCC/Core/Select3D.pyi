from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.BVH import *
from OCC.Core.Graphic3d import *
from OCC.Core.gp import *
from OCC.Core.SelectMgr import *
from OCC.Core.Bnd import *
from OCC.Core.SelectBasics import *
from OCC.Core.TColgp import *
from OCC.Core.TopLoc import *
from OCC.Core.TColStd import *
from OCC.Core.Geom import *

# the following typedef cannot be wrapped as is
Select3D_BVHBuilder3d = NewType("Select3D_BVHBuilder3d", Any)
# the following typedef cannot be wrapped as is
Select3D_BndBox3d = NewType("Select3D_BndBox3d", Any)
# the following typedef cannot be wrapped as is
Select3D_IndexedMapOfEntity = NewType("Select3D_IndexedMapOfEntity", Any)
# the following typedef cannot be wrapped as is
Select3D_Vec3 = NewType("Select3D_Vec3", Any)
# the following typedef cannot be wrapped as is
Select3D_VectorOfHPoly = NewType("Select3D_VectorOfHPoly", Any)
SelectBasics_SensitiveEntity = NewType("SelectBasics_SensitiveEntity", Select3D_SensitiveEntity)

class Select3D_EntitySequence:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Length(self) -> int: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class Select3D_TypeOfSensitivity(IntEnum):
    Select3D_TOS_INTERIOR: int = ...
    Select3D_TOS_BOUNDARY: int = ...

Select3D_TOS_INTERIOR = Select3D_TypeOfSensitivity.Select3D_TOS_INTERIOR
Select3D_TOS_BOUNDARY = Select3D_TypeOfSensitivity.Select3D_TOS_BOUNDARY

class Select3D_BVHIndexBuffer(Graphic3d_Buffer):
    def __init__(self, theAlloc: NCollection_BaseAllocator) -> None: ...
    def HasPatches(self) -> bool: ...
    def Index(self, theIndex: int) -> int: ...
    def Init(self, theNbElems: int, theHasPatches: bool) -> bool: ...
    def PatchSize(self, theIndex: int) -> int: ...
    @overload
    def SetIndex(self, theIndex: int, theValue: int) -> None: ...
    @overload
    def SetIndex(self, theIndex: int, theValue: int, thePatchSize: int) -> None: ...

class Select3D_Pnt:
    pass

class Select3D_PointData:
    def __init__(self, theNbPoints: int) -> None: ...
    def Pnt(self, theIndex: int) -> Select3D_Pnt: ...
    def Pnt3d(self, theIndex: int) -> gp_Pnt: ...
    @overload
    def SetPnt(self, theIndex: int, theValue: Select3D_Pnt) -> None: ...
    @overload
    def SetPnt(self, theIndex: int, theValue: gp_Pnt) -> None: ...
    def Size(self) -> int: ...

class Select3D_SensitiveBox(Select3D_SensitiveEntity):
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, theBox: Bnd_Box) -> None: ...
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, theXMin: float, theYMin: float, theZMin: float, theXMax: float, theYMax: float, theZMax: float) -> None: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetConnected(self) -> Select3D_SensitiveEntity: ...
    def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
    def NbSubElements(self) -> int: ...
    def ToBuildBVH(self) -> bool: ...

class Select3D_SensitiveCylinder(Select3D_SensitiveEntity):
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: gp_Trsf, theIsHollow: Optional[bool] = False) -> None: ...
    def BottomRadius(self) -> float: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def Height(self) -> float: ...
    def IsHollow(self) -> bool: ...
    def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
    def NbSubElements(self) -> int: ...
    def ToBuildBVH(self) -> bool: ...
    def TopRadius(self) -> float: ...
    def Transformation(self) -> gp_Trsf: ...

class Select3D_SensitiveFace(Select3D_SensitiveEntity):
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, thePoints: TColgp_Array1OfPnt, theType: Select3D_TypeOfSensitivity) -> None: ...
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, thePoints: TColgp_HArray1OfPnt, theType: Select3D_TypeOfSensitivity) -> None: ...
    def BVH(self) -> None: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetConnected(self) -> Select3D_SensitiveEntity: ...
    def GetPoints(self, theHArrayOfPnt: TColgp_HArray1OfPnt) -> None: ...
    def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
    def NbSubElements(self) -> int: ...
    def ToBuildBVH(self) -> bool: ...

class Select3D_SensitivePoint(Select3D_SensitiveEntity):
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, thePoint: gp_Pnt) -> None: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetConnected(self) -> Select3D_SensitiveEntity: ...
    def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
    def NbSubElements(self) -> int: ...
    def Point(self) -> gp_Pnt: ...
    def ToBuildBVH(self) -> bool: ...

class Select3D_SensitiveSegment(Select3D_SensitiveEntity):
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, theFirstPnt: gp_Pnt, theLastPnt: gp_Pnt) -> None: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    @overload
    def EndPoint(self) -> gp_Pnt: ...
    @overload
    def EndPoint(self, thePnt: gp_Pnt) -> None: ...
    def GetConnected(self) -> Select3D_SensitiveEntity: ...
    def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
    def NbSubElements(self) -> int: ...
    def SetEndPoint(self, thePnt: gp_Pnt) -> None: ...
    def SetStartPoint(self, thePnt: gp_Pnt) -> None: ...
    @overload
    def StartPoint(self) -> gp_Pnt: ...
    @overload
    def StartPoint(self, thePnt: gp_Pnt) -> None: ...
    def ToBuildBVH(self) -> bool: ...

class Select3D_SensitiveSphere(Select3D_SensitiveEntity):
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, theCenter: gp_Pnt, theRadius: float) -> None: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def GetConnected(self) -> Select3D_SensitiveEntity: ...
    def LastDetectedPoint(self) -> gp_Pnt: ...
    def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
    def NbSubElements(self) -> int: ...
    def Radius(self) -> float: ...
    def ResetLastDetectedPoint(self) -> None: ...
    def ToBuildBVH(self) -> bool: ...

class Select3D_SensitiveTriangle(Select3D_SensitiveEntity):
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, thePnt0: gp_Pnt, thePnt1: gp_Pnt, thePnt2: gp_Pnt, theType: Optional[Select3D_TypeOfSensitivity] = Select3D_TOS_INTERIOR) -> None: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def Center3D(self) -> gp_Pnt: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetConnected(self) -> Select3D_SensitiveEntity: ...
    def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
    def NbSubElements(self) -> int: ...
    def Points3D(self, thePnt0: gp_Pnt, thePnt1: gp_Pnt, thePnt2: gp_Pnt) -> None: ...
    def ToBuildBVH(self) -> bool: ...

class Select3D_InteriorSensitivePointSet(Select3D_SensitiveSet):
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, thePoints: TColgp_Array1OfPnt) -> None: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def Box(self, theIdx: int) -> Select3D_BndBox3d: ...
    def Center(self, theIdx: int, theAxis: int) -> float: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetPoints(self, theHArrayOfPnt: TColgp_HArray1OfPnt) -> None: ...
    def NbSubElements(self) -> int: ...
    def Size(self) -> int: ...
    def Swap(self, theIdx1: int, theIdx2: int) -> None: ...

class Select3D_SensitiveGroup(Select3D_SensitiveSet):
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, theIsMustMatchAll: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, theEntities: Select3D_EntitySequence, theIsMustMatchAll: Optional[bool] = True) -> None: ...
    @overload
    def Add(self, theEntities: Select3D_EntitySequence) -> None: ...
    @overload
    def Add(self, theSensitive: Select3D_SensitiveEntity) -> None: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def Box(self, theIdx: int) -> Select3D_BndBox3d: ...
    def Center(self, theIdx: int, theAxis: int) -> float: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def Clear(self) -> None: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Entities(self) -> Select3D_IndexedMapOfEntity: ...
    def GetConnected(self) -> Select3D_SensitiveEntity: ...
    def IsIn(self, theSensitive: Select3D_SensitiveEntity) -> bool: ...
    def LastDetectedEntity(self) -> Select3D_SensitiveEntity: ...
    def LastDetectedEntityIndex(self) -> int: ...
    def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
    def MustMatchAll(self) -> bool: ...
    def NbSubElements(self) -> int: ...
    def Remove(self, theSensitive: Select3D_SensitiveEntity) -> None: ...
    def Set(self, theOwnerId: SelectMgr_EntityOwner) -> None: ...
    def SetCheckOverlapAll(self, theToCheckAll: bool) -> None: ...
    def SetMatchType(self, theIsMustMatchAll: bool) -> None: ...
    def Size(self) -> int: ...
    def SubEntity(self, theIndex: int) -> Select3D_SensitiveEntity: ...
    def Swap(self, theIdx1: int, theIdx2: int) -> None: ...
    def ToCheckOverlapAll(self) -> bool: ...

class Select3D_SensitivePoly(Select3D_SensitiveSet):
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, thePoints: TColgp_Array1OfPnt, theIsBVHEnabled: bool) -> None: ...
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, thePoints: TColgp_HArray1OfPnt, theIsBVHEnabled: bool) -> None: ...
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, theCircle: gp_Circ, theU1: float, theU2: float, theIsFilled: Optional[bool] = False, theNbPnts: Optional[int] = 12) -> None: ...
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, theIsBVHEnabled: bool, theNbPnts: Optional[int] = 6) -> None: ...
    def ArrayBounds(self) -> Tuple[int, int]: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def Box(self, theIdx: int) -> Select3D_BndBox3d: ...
    def Center(self, theIdx: int, theAxis: int) -> float: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetPoint3d(self, thePntIdx: int) -> gp_Pnt: ...
    def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
    def NbSubElements(self) -> int: ...
    def Points3D(self, theHArrayOfPnt: TColgp_HArray1OfPnt) -> None: ...
    def Size(self) -> int: ...
    def Swap(self, theIdx1: int, theIdx2: int) -> None: ...

class Select3D_SensitivePrimitiveArray(Select3D_SensitiveSet):
    def __init__(self, theOwnerId: SelectMgr_EntityOwner) -> None: ...
    def BVH(self) -> None: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def Box(self, theIdx: int) -> Select3D_BndBox3d: ...
    def Center(self, theIdx: int, theAxis: int) -> float: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetConnected(self) -> Select3D_SensitiveEntity: ...
    def HasInitLocation(self) -> bool: ...
    @overload
    def InitPoints(self, theVerts: Graphic3d_Buffer, theIndices: Graphic3d_IndexBuffer, theInitLoc: TopLoc_Location, theIndexLower: int, theIndexUpper: int, theToEvalMinMax: Optional[bool] = true, theNbGroups: Optional[int] = 1) -> bool: ...
    @overload
    def InitPoints(self, theVerts: Graphic3d_Buffer, theIndices: Graphic3d_IndexBuffer, theInitLoc: TopLoc_Location, theToEvalMinMax: Optional[bool] = true, theNbGroups: Optional[int] = 1) -> bool: ...
    @overload
    def InitPoints(self, theVerts: Graphic3d_Buffer, theInitLoc: TopLoc_Location, theToEvalMinMax: Optional[bool] = true, theNbGroups: Optional[int] = 1) -> bool: ...
    @overload
    def InitTriangulation(self, theVerts: Graphic3d_Buffer, theIndices: Graphic3d_IndexBuffer, theInitLoc: TopLoc_Location, theIndexLower: int, theIndexUpper: int, theToEvalMinMax: Optional[bool] = true, theNbGroups: Optional[int] = 1) -> bool: ...
    @overload
    def InitTriangulation(self, theVerts: Graphic3d_Buffer, theIndices: Graphic3d_IndexBuffer, theInitLoc: TopLoc_Location, theToEvalMinMax: Optional[bool] = true, theNbGroups: Optional[int] = 1) -> bool: ...
    def InvInitLocation(self) -> gp_GTrsf: ...
    def LastDetectedEdgeNode1(self) -> int: ...
    def LastDetectedEdgeNode2(self) -> int: ...
    def LastDetectedElement(self) -> int: ...
    def LastDetectedElementMap(self) -> TColStd_HPackedMapOfInteger: ...
    def LastDetectedNode(self) -> int: ...
    def LastDetectedNodeMap(self) -> TColStd_HPackedMapOfInteger: ...
    def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
    def NbSubElements(self) -> int: ...
    def PatchDistance(self) -> float: ...
    def PatchSizeMax(self) -> int: ...
    def Set(self, theOwnerId: SelectMgr_EntityOwner) -> None: ...
    def SetDetectEdges(self, theToDetect: bool) -> None: ...
    def SetDetectElementMap(self, theToDetect: bool) -> None: ...
    def SetDetectElements(self, theToDetect: bool) -> None: ...
    def SetDetectNodeMap(self, theToDetect: bool) -> None: ...
    def SetDetectNodes(self, theToDetect: bool) -> None: ...
    def SetMinMax(self, theMinX: float, theMinY: float, theMinZ: float, theMaxX: float, theMaxY: float, theMaxZ: float) -> None: ...
    def SetPatchDistance(self, thePatchDistMax: float) -> None: ...
    def SetPatchSizeMax(self, thePatchSizeMax: int) -> None: ...
    def Size(self) -> int: ...
    def Swap(self, theIdx1: int, theIdx2: int) -> None: ...
    def ToDetectEdges(self) -> bool: ...
    def ToDetectElementMap(self) -> bool: ...
    def ToDetectElements(self) -> bool: ...
    def ToDetectNodeMap(self) -> bool: ...
    def ToDetectNodes(self) -> bool: ...

class Select3D_SensitiveWire(Select3D_SensitiveSet):
    def __init__(self, theOwnerId: SelectMgr_EntityOwner) -> None: ...
    def Add(self, theSensitive: Select3D_SensitiveEntity) -> None: ...
    def BoundingBox(self) -> Select3D_BndBox3d: ...
    def Box(self, theIdx: int) -> Select3D_BndBox3d: ...
    def Center(self, theIdx: int, theAxis: int) -> float: ...
    def CenterOfGeometry(self) -> gp_Pnt: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def GetConnected(self) -> Select3D_SensitiveEntity: ...
    def GetEdges(self) -> False: ...
    def GetLastDetected(self) -> Select3D_SensitiveEntity: ...
    def NbSubElements(self) -> int: ...
    def Set(self, theOwnerId: SelectMgr_EntityOwner) -> None: ...
    def Size(self) -> int: ...
    def Swap(self, theIdx1: int, theIdx2: int) -> None: ...

class Select3D_SensitiveCurve(Select3D_SensitivePoly):
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, theCurve: Geom_Curve, theNbPnts: Optional[int] = 17) -> None: ...
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, thePoints: TColgp_HArray1OfPnt) -> None: ...
    @overload
    def __init__(self, theOwnerId: SelectMgr_EntityOwner, thePoints: TColgp_Array1OfPnt) -> None: ...
    def GetConnected(self) -> Select3D_SensitiveEntity: ...

#classnotwrapped
class Select3D_SensitiveTriangulation: ...

#classnotwrapped
class Select3D_SensitiveEntity: ...

#classnotwrapped
class Handle_Select3D_SensitiveEntity: ...

#classnotwrapped
class Select3D_SensitiveSet: ...

#classnotwrapped
class Select3D_SensitiveCircle: ...

# harray1 classes
# harray2 classes
# hsequence classes

