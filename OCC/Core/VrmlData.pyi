from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.gp import *
from OCC.Core.TopoDS import *
from OCC.Core.TDocStd import *
from OCC.Core.Bnd import *
from OCC.Core.Quantity import *

# the following typedef cannot be wrapped as is
VrmlData_MapOfNode = NewType("VrmlData_MapOfNode", Any)

class VrmlData_ListOfNode:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class VrmlData_ErrorStatus(IntEnum):
    VrmlData_StatusOK: int = ...
    VrmlData_EmptyData: int = ...
    VrmlData_UnrecoverableError: int = ...
    VrmlData_GeneralError: int = ...
    VrmlData_EndOfFile: int = ...
    VrmlData_NotVrmlFile: int = ...
    VrmlData_CannotOpenFile: int = ...
    VrmlData_VrmlFormatError: int = ...
    VrmlData_NumericInputError: int = ...
    VrmlData_IrrelevantNumber: int = ...
    VrmlData_BooleanInputError: int = ...
    VrmlData_StringInputError: int = ...
    VrmlData_NodeNameUnknown: int = ...
    VrmlData_NonPositiveSize: int = ...
    VrmlData_ReadUnknownNode: int = ...
    VrmlData_NonSupportedFeature: int = ...
    VrmlData_OutputStreamUndefined: int = ...
    VrmlData_NotImplemented: int = ...

VrmlData_StatusOK = VrmlData_ErrorStatus.VrmlData_StatusOK
VrmlData_EmptyData = VrmlData_ErrorStatus.VrmlData_EmptyData
VrmlData_UnrecoverableError = VrmlData_ErrorStatus.VrmlData_UnrecoverableError
VrmlData_GeneralError = VrmlData_ErrorStatus.VrmlData_GeneralError
VrmlData_EndOfFile = VrmlData_ErrorStatus.VrmlData_EndOfFile
VrmlData_NotVrmlFile = VrmlData_ErrorStatus.VrmlData_NotVrmlFile
VrmlData_CannotOpenFile = VrmlData_ErrorStatus.VrmlData_CannotOpenFile
VrmlData_VrmlFormatError = VrmlData_ErrorStatus.VrmlData_VrmlFormatError
VrmlData_NumericInputError = VrmlData_ErrorStatus.VrmlData_NumericInputError
VrmlData_IrrelevantNumber = VrmlData_ErrorStatus.VrmlData_IrrelevantNumber
VrmlData_BooleanInputError = VrmlData_ErrorStatus.VrmlData_BooleanInputError
VrmlData_StringInputError = VrmlData_ErrorStatus.VrmlData_StringInputError
VrmlData_NodeNameUnknown = VrmlData_ErrorStatus.VrmlData_NodeNameUnknown
VrmlData_NonPositiveSize = VrmlData_ErrorStatus.VrmlData_NonPositiveSize
VrmlData_ReadUnknownNode = VrmlData_ErrorStatus.VrmlData_ReadUnknownNode
VrmlData_NonSupportedFeature = VrmlData_ErrorStatus.VrmlData_NonSupportedFeature
VrmlData_OutputStreamUndefined = VrmlData_ErrorStatus.VrmlData_OutputStreamUndefined
VrmlData_NotImplemented = VrmlData_ErrorStatus.VrmlData_NotImplemented

class VrmlData_Node(Standard_Transient):
    @staticmethod
    def GlobalIndent() -> int: ...
    def IsDefault(self) -> bool: ...
    def Name(self) -> str: ...
    @overload
    @staticmethod
    def OK(theStat: VrmlData_ErrorStatus) -> bool: ...
    @overload
    @staticmethod
    def OK(theStat: VrmlData_ErrorStatus) -> Tuple[bool, VrmlData_ErrorStatus]: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    @staticmethod
    def ReadBoolean(theBuffer: VrmlData_InBuffer) -> Tuple[VrmlData_ErrorStatus, bool]: ...
    def ReadNode(self, theBuffer: VrmlData_InBuffer, theNode: VrmlData_Node, Type: Optional[Standard_Type] = None) -> VrmlData_ErrorStatus: ...
    @staticmethod
    def ReadString(theBuffer: VrmlData_InBuffer, theRes: str) -> VrmlData_ErrorStatus: ...
    def Scene(self) -> VrmlData_Scene: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...
    def WriteClosing(self) -> VrmlData_ErrorStatus: ...

class VrmlData_Scene:
    def AddNode(self, theN: VrmlData_Node, isTopLevel: Optional[bool] = True) -> VrmlData_Node: ...
    def Allocator(self) -> NCollection_IncAllocator: ...
    def Dump(self) -> str: ...
    @overload
    def FindNode(self, theName: str, theType: Optional[Standard_Type] = 0) -> VrmlData_Node: ...
    @overload
    def FindNode(self, theName: str, theLocation: gp_Trsf) -> VrmlData_Node: ...
    def GetIterator(self) -> False: ...
    def GetLineError(self) -> int: ...
    def GetShape(self, M: VrmlData_DataMapOfShapeAppearance) -> TopoDS_Shape: ...
    def IsDummyWrite(self) -> bool: ...
    def NamedNodesIterator(self) -> False: ...
    def ReadArrIndex(self, theBuffer: VrmlData_InBuffer, theArr: int, theNBl: int) -> VrmlData_ErrorStatus: ...
    @staticmethod
    def ReadLine(theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def ReadReal(self, theBuffer: VrmlData_InBuffer, isApplyScale: bool, isOnlyPositive: bool) -> Tuple[VrmlData_ErrorStatus, float]: ...
    @staticmethod
    def ReadWord(theBuffer: VrmlData_InBuffer, theStr: str) -> VrmlData_ErrorStatus: ...
    def ReadXY(self, theBuffer: VrmlData_InBuffer, theXYZ: gp_XY, isApplyScale: bool, isOnlyPositive: bool) -> VrmlData_ErrorStatus: ...
    def ReadXYZ(self, theBuffer: VrmlData_InBuffer, theXYZ: gp_XYZ, isApplyScale: bool, isOnlyPositive: bool) -> VrmlData_ErrorStatus: ...
    def SetIndent(self, nSpc: int) -> None: ...
    def SetLinearScale(self, theScale: float) -> None: ...
    def Status(self) -> VrmlData_ErrorStatus: ...
    def VrmlDirIterator(self) -> False: ...
    def WorldInfo(self) -> VrmlData_WorldInfo: ...
    def WriteArrIndex(self, thePrefix: str, theArr: int, theNbBl: int) -> VrmlData_ErrorStatus: ...
    def WriteLine(self, theLine0: str, theLine1: Optional[str] = 0, theIndent: Optional[int] = 0) -> VrmlData_ErrorStatus: ...
    def WriteXYZ(self, theXYZ: gp_XYZ, isScale: bool, thePostfix: Optional[str] = 0) -> VrmlData_ErrorStatus: ...

class VrmlData_ShapeConvert:
    def __init__(self, theScene: VrmlData_Scene, theScale: Optional[float] = 1) -> None: ...
    def AddShape(self, theShape: TopoDS_Shape, theName: Optional[str] = 0) -> None: ...
    def Convert(self, theExtractFaces: bool, theExtractEdges: bool, theDeflection: Optional[float] = 0.01, theDeflAngle: Optional[float] = 20*M_PI/180) -> None: ...
    def ConvertDocument(self, theDoc: TDocStd_Document) -> None: ...

class VrmlData_Appearance(VrmlData_Node):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str) -> None: ...
    def IsDefault(self) -> bool: ...
    def Material(self) -> VrmlData_Material: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def SetMaterial(self, theMat: VrmlData_Material) -> None: ...
    def SetTexture(self, theTexture: VrmlData_Texture) -> None: ...
    def SetTextureTransform(self, theTT: VrmlData_TextureTransform) -> None: ...
    def Texture(self) -> VrmlData_Texture: ...
    def TextureTransform(self) -> VrmlData_TextureTransform: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_Geometry(VrmlData_Node):
    def TShape(self) -> TopoDS_TShape: ...

class VrmlData_Group(VrmlData_Node):
    @overload
    def __init__(self, isTransform: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, isTransform: Optional[bool] = False) -> None: ...
    def AddNode(self, theNode: VrmlData_Node) -> VrmlData_Node: ...
    def Box(self) -> Bnd_B3f: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def FindNode(self, theName: str, theLocation: gp_Trsf) -> VrmlData_Node: ...
    def GetTransform(self) -> gp_Trsf: ...
    def IsTransform(self) -> bool: ...
    def NodeIterator(self) -> False: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def RemoveNode(self, theNode: VrmlData_Node) -> bool: ...
    def SetBox(self, theBox: Bnd_B3f) -> None: ...
    def SetTransform(self, theTrsf: gp_Trsf) -> bool: ...
    def Shape(self, theShape: TopoDS_Shape, pMapApp: VrmlData_DataMapOfShapeAppearance) -> None: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_Material(VrmlData_Node):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, theAmbientIntensity: Optional[float] = -1, theShininess: Optional[float] = -1, theTransparency: Optional[float] = -1) -> None: ...
    def AmbientColor(self) -> Quantity_Color: ...
    def AmbientIntensity(self) -> float: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def DiffuseColor(self) -> Quantity_Color: ...
    def EmissiveColor(self) -> Quantity_Color: ...
    def IsDefault(self) -> bool: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def SetAmbientColor(self, theColor: Quantity_Color) -> None: ...
    def SetAmbientIntensity(self, theAmbientIntensity: float) -> None: ...
    def SetDiffuseColor(self, theColor: Quantity_Color) -> None: ...
    def SetEmissiveColor(self, theColor: Quantity_Color) -> None: ...
    def SetShininess(self, theShininess: float) -> None: ...
    def SetSpecularColor(self, theColor: Quantity_Color) -> None: ...
    def SetTransparency(self, theTransparency: float) -> None: ...
    def Shininess(self) -> float: ...
    def SpecularColor(self) -> Quantity_Color: ...
    def Transparency(self) -> float: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_ShapeNode(VrmlData_Node):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str) -> None: ...
    def Appearance(self) -> VrmlData_Appearance: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def Geometry(self) -> VrmlData_Geometry: ...
    def IsDefault(self) -> bool: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def SetAppearance(self, theAppear: VrmlData_Appearance) -> None: ...
    def SetGeometry(self, theGeometry: VrmlData_Geometry) -> None: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_TextureCoordinate(VrmlData_Node):
    @overload
    def __init__(self) -> None: ...
    def AllocateValues(self, theLength: int) -> bool: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def Length(self) -> False: ...
    def Points(self) -> gp_XY: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...

class VrmlData_UnknownNode(VrmlData_Node):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: Optional[str] = 0, theTitle: Optional[str] = 0) -> None: ...
    def GetTitle(self) -> str: ...
    def IsDefault(self) -> bool: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...

class VrmlData_WorldInfo(VrmlData_Node):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: Optional[str] = 0, theTitle: Optional[str] = 0) -> None: ...
    def AddInfo(self, theString: str) -> None: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def InfoIterator(self) -> str: ...
    def IsDefault(self) -> bool: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def SetTitle(self, theString: str) -> None: ...
    def Title(self) -> str: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_Box(VrmlData_Geometry):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, sizeX: Optional[float] = 2, sizeY: Optional[float] = 2, sizeZ: Optional[float] = 2) -> None: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def SetSize(self, theSize: gp_XYZ) -> None: ...
    def Size(self) -> gp_XYZ: ...
    def TShape(self) -> TopoDS_TShape: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_Color(VrmlData_ArrayVec3d):
    @overload
    def __init__(self) -> None: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def Color(self, i: int) -> Quantity_Color: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_Cone(VrmlData_Geometry):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, theBottomRadius: Optional[float] = 1, theHeight: Optional[float] = 2) -> None: ...
    def BottomRadius(self) -> float: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def HasBottom(self) -> bool: ...
    def HasSide(self) -> bool: ...
    def Height(self) -> float: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def SetBottomRadius(self, theRadius: float) -> None: ...
    def SetFaces(self, hasBottom: bool, hasSide: bool) -> None: ...
    def SetHeight(self, theHeight: float) -> None: ...
    def TShape(self) -> TopoDS_TShape: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_Coordinate(VrmlData_ArrayVec3d):
    @overload
    def __init__(self) -> None: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def Coordinate(self, i: int) -> gp_XYZ: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_Cylinder(VrmlData_Geometry):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, theRadius: Optional[float] = 1, theHeight: Optional[float] = 2) -> None: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def HasBottom(self) -> bool: ...
    def HasSide(self) -> bool: ...
    def HasTop(self) -> bool: ...
    def Height(self) -> float: ...
    def Radius(self) -> float: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def SetFaces(self, hasBottom: bool, hasSide: bool, hasTop: bool) -> None: ...
    def SetHeight(self, theHeight: float) -> None: ...
    def SetRadius(self, theRadius: float) -> None: ...
    def TShape(self) -> TopoDS_TShape: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_ImageTexture(VrmlData_Texture):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, theURL: Optional[str] = 0, theRepS: Optional[bool] = False, theRepT: Optional[bool] = False) -> None: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def URL(self) -> False: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_IndexedLineSet(VrmlData_Geometry):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, isColorPerVertex: Optional[bool] = True) -> None: ...
    def ArrayColorInd(self, arrColorInd: int) -> False: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def Colors(self) -> VrmlData_Color: ...
    def Coordinates(self) -> VrmlData_Coordinate: ...
    def GetColor(self, iFace: int, iVertex: int) -> Quantity_Color: ...
    def IsDefault(self) -> bool: ...
    def Polygon(self, iPolygon: int, outIndice: int) -> int: ...
    def Polygons(self, arrPolygons: int) -> False: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def SetColorInd(self, nIndice: int, theIndice: int) -> None: ...
    def SetColorPerVertex(self, isColorPerVertex: bool) -> None: ...
    def SetColors(self, theColors: VrmlData_Color) -> None: ...
    def SetCoordinates(self, theCoord: VrmlData_Coordinate) -> None: ...
    def SetPolygons(self, nPolygons: int, thePolygons: int) -> None: ...
    def TShape(self) -> TopoDS_TShape: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_Normal(VrmlData_ArrayVec3d):
    @overload
    def __init__(self) -> None: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def Normal(self, i: int) -> gp_XYZ: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_Sphere(VrmlData_Geometry):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, theRadius: Optional[float] = 1) -> None: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def Radius(self) -> float: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def SetRadius(self, theRadius: float) -> None: ...
    def TShape(self) -> TopoDS_TShape: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

class VrmlData_IndexedFaceSet(VrmlData_Faceted):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, isCCW: Optional[bool] = True, isSolid: Optional[bool] = True, isConvex: Optional[bool] = True, theCreaseAngle: Optional[float] = 0) -> None: ...
    def ArrayColorInd(self, arrColorInd: int) -> False: ...
    def ArrayNormalInd(self, arrNormalInd: int) -> False: ...
    def ArrayTextureCoordInd(self, arrTextureCoordInd: int) -> False: ...
    def Clone(self, theOther: VrmlData_Node) -> VrmlData_Node: ...
    def Colors(self) -> VrmlData_Color: ...
    def Coordinates(self) -> VrmlData_Coordinate: ...
    def GetColor(self, iFace: int, iVertex: int) -> Quantity_Color: ...
    def IndiceNormals(self, iFace: int, outIndice: int) -> int: ...
    def IsDefault(self) -> bool: ...
    def Normals(self) -> VrmlData_Normal: ...
    def Polygon(self, iFace: int, outIndice: int) -> int: ...
    def Polygons(self, arrPolygons: int) -> False: ...
    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus: ...
    def SetColorInd(self, nIndice: int, theIndice: int) -> None: ...
    def SetColorPerVertex(self, isColorPerVertex: bool) -> None: ...
    def SetColors(self, theColors: VrmlData_Color) -> None: ...
    def SetCoordinates(self, theCoord: VrmlData_Coordinate) -> None: ...
    def SetNormalInd(self, nIndice: int, theIndice: int) -> None: ...
    def SetNormalPerVertex(self, isNormalPerVertex: bool) -> None: ...
    def SetNormals(self, theNormals: VrmlData_Normal) -> None: ...
    def SetPolygons(self, nPolygons: int, thePolygons: int) -> None: ...
    def SetTextureCoordInd(self, nIndice: int, theIndice: int) -> None: ...
    def SetTextureCoords(self, tc: VrmlData_TextureCoordinate) -> None: ...
    def TShape(self) -> TopoDS_TShape: ...
    def TextureCoords(self) -> VrmlData_TextureCoordinate: ...
    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus: ...

#classnotwrapped
class VrmlData_InBuffer: ...

#classnotwrapped
class VrmlData_ArrayVec3d: ...

#classnotwrapped
class VrmlData_Texture: ...

#classnotwrapped
class VrmlData_TextureTransform: ...

#classnotwrapped
class VrmlData_Faceted: ...

# harray1 classes
# harray2 classes
# hsequence classes

