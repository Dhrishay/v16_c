from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TDF import *
from OCC.Core.TCollection import *
from OCC.Core.TDocStd import *
from OCC.Core.gp import *
from OCC.Core.TColStd import *
from OCC.Core.Message import *
from OCC.Core.TopoDS import *
from OCC.Core.Graphic3d import *
from OCC.Core.TopLoc import *
from OCC.Core.XCAFPrs import *
from OCC.Core.Quantity import *
from OCC.Core.Poly import *
from OCC.Core.Image import *
from OCC.Core.OSD import *


class RWMesh_CafReaderStatusEx(IntEnum):
    RWMesh_CafReaderStatusEx_NONE: int = ...
    RWMesh_CafReaderStatusEx_Partial: int = ...

RWMesh_CafReaderStatusEx_NONE = RWMesh_CafReaderStatusEx.RWMesh_CafReaderStatusEx_NONE
RWMesh_CafReaderStatusEx_Partial = RWMesh_CafReaderStatusEx.RWMesh_CafReaderStatusEx_Partial

class RWMesh_CoordinateSystem(IntEnum):
    RWMesh_CoordinateSystem_Undefined: int = ...
    RWMesh_CoordinateSystem_posYfwd_posZup: int = ...
    RWMesh_CoordinateSystem_negZfwd_posYup: int = ...
    RWMesh_CoordinateSystem_Blender: int = ...
    RWMesh_CoordinateSystem_glTF: int = ...
    RWMesh_CoordinateSystem_Zup: int = ...
    RWMesh_CoordinateSystem_Yup: int = ...

RWMesh_CoordinateSystem_Undefined = RWMesh_CoordinateSystem.RWMesh_CoordinateSystem_Undefined
RWMesh_CoordinateSystem_posYfwd_posZup = RWMesh_CoordinateSystem.RWMesh_CoordinateSystem_posYfwd_posZup
RWMesh_CoordinateSystem_negZfwd_posYup = RWMesh_CoordinateSystem.RWMesh_CoordinateSystem_negZfwd_posYup
RWMesh_CoordinateSystem_Blender = RWMesh_CoordinateSystem.RWMesh_CoordinateSystem_Blender
RWMesh_CoordinateSystem_glTF = RWMesh_CoordinateSystem.RWMesh_CoordinateSystem_glTF
RWMesh_CoordinateSystem_Zup = RWMesh_CoordinateSystem.RWMesh_CoordinateSystem_Zup
RWMesh_CoordinateSystem_Yup = RWMesh_CoordinateSystem.RWMesh_CoordinateSystem_Yup

class RWMesh_NameFormat(IntEnum):
    RWMesh_NameFormat_Empty: int = ...
    RWMesh_NameFormat_Product: int = ...
    RWMesh_NameFormat_Instance: int = ...
    RWMesh_NameFormat_InstanceOrProduct: int = ...
    RWMesh_NameFormat_ProductOrInstance: int = ...
    RWMesh_NameFormat_ProductAndInstance: int = ...
    RWMesh_NameFormat_ProductAndInstanceAndOcaf: int = ...

RWMesh_NameFormat_Empty = RWMesh_NameFormat.RWMesh_NameFormat_Empty
RWMesh_NameFormat_Product = RWMesh_NameFormat.RWMesh_NameFormat_Product
RWMesh_NameFormat_Instance = RWMesh_NameFormat.RWMesh_NameFormat_Instance
RWMesh_NameFormat_InstanceOrProduct = RWMesh_NameFormat.RWMesh_NameFormat_InstanceOrProduct
RWMesh_NameFormat_ProductOrInstance = RWMesh_NameFormat.RWMesh_NameFormat_ProductOrInstance
RWMesh_NameFormat_ProductAndInstance = RWMesh_NameFormat.RWMesh_NameFormat_ProductAndInstance
RWMesh_NameFormat_ProductAndInstanceAndOcaf = RWMesh_NameFormat.RWMesh_NameFormat_ProductAndInstanceAndOcaf

class rwmesh:
    @staticmethod
    def FormatName(theFormat: RWMesh_NameFormat, theLabel: TDF_Label, theRefLabel: TDF_Label) -> str: ...
    @staticmethod
    def ReadNameAttribute(theLabel: TDF_Label) -> str: ...

class RWMesh_CafReader(Standard_Transient):
    def CoordinateSystemConverter(self) -> RWMesh_CoordinateSystemConverter: ...
    def Document(self) -> TDocStd_Document: ...
    def ExternalFiles(self) -> False: ...
    def ExtraStatus(self) -> int: ...
    def FileCoordinateSystem(self) -> gp_Ax3: ...
    def FileLengthUnit(self) -> float: ...
    def HasFileCoordinateSystem(self) -> bool: ...
    def HasSystemCoordinateSystem(self) -> bool: ...
    def MemoryLimitMiB(self) -> int: ...
    def Metadata(self) -> TColStd_IndexedDataMapOfStringString: ...
    @overload
    def Perform(self, theFile: str, theProgress: Message_ProgressRange) -> bool: ...
    @overload
    def Perform(self, theStream: str, theProgress: Message_ProgressRange, theFile: Optional[str] = "") -> bool: ...
    @overload
    def ProbeHeader(self, theFile: str, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    @overload
    def ProbeHeader(self, theStream: str, theFile: Optional[str] = "", theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    def RootPrefix(self) -> str: ...
    def SetCoordinateSystemConverter(self, theConverter: RWMesh_CoordinateSystemConverter) -> None: ...
    def SetDocument(self, theDoc: TDocStd_Document) -> None: ...
    @overload
    def SetFileCoordinateSystem(self, theCS: gp_Ax3) -> None: ...
    @overload
    def SetFileCoordinateSystem(self, theCS: RWMesh_CoordinateSystem) -> None: ...
    def SetFileLengthUnit(self, theUnits: float) -> None: ...
    def SetFillIncompleteDocument(self, theToFillIncomplete: bool) -> None: ...
    def SetMemoryLimitMiB(self, theLimitMiB: int) -> None: ...
    def SetRootPrefix(self, theRootPrefix: str) -> None: ...
    @overload
    def SetSystemCoordinateSystem(self, theCS: gp_Ax3) -> None: ...
    @overload
    def SetSystemCoordinateSystem(self, theCS: RWMesh_CoordinateSystem) -> None: ...
    def SetSystemLengthUnit(self, theUnits: float) -> None: ...
    def SingleShape(self) -> TopoDS_Shape: ...
    def SystemCoordinateSystem(self) -> gp_Ax3: ...
    def SystemLengthUnit(self) -> float: ...
    def ToFillIncompleteDocument(self) -> bool: ...

class RWMesh_CoordinateSystemConverter:
    def __init__(self) -> None: ...
    def HasInputCoordinateSystem(self) -> bool: ...
    def HasOutputCoordinateSystem(self) -> bool: ...
    def Init(self, theInputSystem: gp_Ax3, theInputLengthUnit: float, theOutputSystem: gp_Ax3, theOutputLengthUnit: float) -> None: ...
    def InputCoordinateSystem(self) -> gp_Ax3: ...
    def InputLengthUnit(self) -> float: ...
    def IsEmpty(self) -> bool: ...
    def OutputCoordinateSystem(self) -> gp_Ax3: ...
    def OutputLengthUnit(self) -> float: ...
    @overload
    def SetInputCoordinateSystem(self, theSysFrom: gp_Ax3) -> None: ...
    @overload
    def SetInputCoordinateSystem(self, theSysFrom: RWMesh_CoordinateSystem) -> None: ...
    def SetInputLengthUnit(self, theInputScale: float) -> None: ...
    @overload
    def SetOutputCoordinateSystem(self, theSysTo: gp_Ax3) -> None: ...
    @overload
    def SetOutputCoordinateSystem(self, theSysTo: RWMesh_CoordinateSystem) -> None: ...
    def SetOutputLengthUnit(self, theOutputScale: float) -> None: ...
    @staticmethod
    def StandardCoordinateSystem(theSys: RWMesh_CoordinateSystem) -> gp_Ax3: ...
    def TransformNormal(self, theNorm: Graphic3d_Vec3) -> None: ...
    def TransformPosition(self, thePos: gp_XYZ) -> None: ...
    def TransformTransformation(self, theTrsf: gp_Trsf) -> None: ...

class RWMesh_FaceIterator:
    @overload
    def __init__(self, theLabel: TDF_Label, theLocation: TopLoc_Location, theToMapColors: Optional[bool] = false, theStyle: Optional[XCAFPrs_Style] = XCAFPrs_Style()) -> None: ...
    @overload
    def __init__(self, theShape: TopoDS_Shape, theStyle: Optional[XCAFPrs_Style] = XCAFPrs_Style()) -> None: ...
    def ElemLower(self) -> int: ...
    def ElemUpper(self) -> int: ...
    def ExploredShape(self) -> TopoDS_Shape: ...
    def Face(self) -> TopoDS_Face: ...
    def FaceColor(self) -> Quantity_ColorRGBA: ...
    def FaceStyle(self) -> XCAFPrs_Style: ...
    def HasFaceColor(self) -> bool: ...
    def HasNormals(self) -> bool: ...
    def HasTexCoords(self) -> bool: ...
    def IsEmptyMesh(self) -> bool: ...
    def More(self) -> bool: ...
    def NbNodes(self) -> int: ...
    def NbTriangles(self) -> int: ...
    def Next(self) -> None: ...
    def NodeLower(self) -> int: ...
    def NodeTexCoord(self, theNode: int) -> gp_Pnt2d: ...
    def NodeTransformed(self, theNode: int) -> gp_Pnt: ...
    def NodeUpper(self) -> int: ...
    def NormalTransformed(self, theNode: int) -> gp_Dir: ...
    def TriangleOriented(self, theElemIndex: int) -> Poly_Triangle: ...
    def Triangulation(self) -> Poly_Triangulation: ...
    def node(self, theNode: int) -> gp_Pnt: ...
    def normal(self, theNode: int) -> gp_Dir: ...
    def triangle(self, theElemIndex: int) -> Poly_Triangle: ...

class RWMesh_MaterialMap(Standard_Transient):
    def AddMaterial(self, theStyle: XCAFPrs_Style) -> str: ...
    def CopyTexture(self, theResTexture: str, theTexture: Image_Texture, theKey: str) -> bool: ...
    def CreateTextureFolder(self) -> bool: ...
    def DefaultStyle(self) -> XCAFPrs_Style: ...
    def DefineMaterial(self, theStyle: XCAFPrs_Style, theKey: str, theName: str) -> None: ...
    def FindMaterial(self, theStyle: XCAFPrs_Style) -> str: ...
    def IsFailed(self) -> bool: ...
    def SetDefaultStyle(self, theStyle: XCAFPrs_Style) -> None: ...

class RWMesh_NodeAttributes:
    pass

class RWMesh_TriangulationReader(Standard_Transient):
    def CoordinateSystemConverter(self) -> RWMesh_CoordinateSystemConverter: ...
    def FileName(self) -> str: ...
    def IsDoublePrecision(self) -> bool: ...
    def Load(self, theSourceMesh: RWMesh_TriangulationSource, theDestMesh: Poly_Triangulation, theFileSystem: OSD_FileSystem) -> bool: ...
    def PrintStatistic(self) -> None: ...
    def SetCoordinateSystemConverter(self, theConverter: RWMesh_CoordinateSystemConverter) -> None: ...
    def SetDoublePrecision(self, theIsDouble: bool) -> None: ...
    def SetFileName(self, theFileName: str) -> None: ...
    def SetToPrintDebugMessages(self, theToPrint: bool) -> None: ...
    def SetToSkipDegenerates(self, theToSkip: bool) -> None: ...
    def StartStatistic(self) -> None: ...
    def StopStatistic(self) -> None: ...
    def ToPrintDebugMessages(self) -> bool: ...
    def ToSkipDegenerates(self) -> bool: ...

class RWMesh_TriangulationSource(Poly_Triangulation):
    def __init__(self) -> None: ...
    def GetChangeDegeneratedTriNb(self) -> int: ...
    def SetChangeDegeneratedTriNb(self, value: int) -> None: ...
    def DegeneratedTriNb(self) -> int: ...
    def NbDeferredNodes(self) -> int: ...
    def NbDeferredTriangles(self) -> int: ...
    def Reader(self) -> RWMesh_TriangulationReader: ...
    def SetNbDeferredNodes(self, theNbNodes: int) -> None: ...
    def SetNbDeferredTriangles(self, theNbTris: int) -> None: ...
    def SetReader(self, theReader: RWMesh_TriangulationReader) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

