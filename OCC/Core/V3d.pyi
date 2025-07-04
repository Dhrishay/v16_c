from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Graphic3d import *
from OCC.Core.gp import *
from OCC.Core.Quantity import *
from OCC.Core.Aspect import *
from OCC.Core.Prs3d import *
from OCC.Core.TCollection import *
from OCC.Core.TColStd import *
from OCC.Core.Bnd import *
from OCC.Core.Image import *

Handle_V3d_Light = NewType("Handle_V3d_Light", Handle_Graphic3d_CLight)
V3d_Light = NewType("V3d_Light", Graphic3d_CLight)
# the following typedef cannot be wrapped as is
V3d_ListOfLightIterator = NewType("V3d_ListOfLightIterator", Any)
# the following typedef cannot be wrapped as is
V3d_ListOfViewIterator = NewType("V3d_ListOfViewIterator", Any)
V3d_TypeOfBackfacingModel = NewType("V3d_TypeOfBackfacingModel", Graphic3d_TypeOfBackfacingModel)
V3d_TypeOfLight = NewType("V3d_TypeOfLight", Graphic3d_TypeOfLightSource)
V3d_TypeOfShadingModel = NewType("V3d_TypeOfShadingModel", Graphic3d_TypeOfShadingModel)
V3d_ViewerPointer = NewType("V3d_ViewerPointer", V3d_Viewer)

class V3d_ListOfLight:
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

class V3d_ListOfView:
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

class V3d_StereoDumpOptions(IntEnum):
    V3d_SDO_MONO: int = ...
    V3d_SDO_LEFT_EYE: int = ...
    V3d_SDO_RIGHT_EYE: int = ...
    V3d_SDO_BLENDED: int = ...

V3d_SDO_MONO = V3d_StereoDumpOptions.V3d_SDO_MONO
V3d_SDO_LEFT_EYE = V3d_StereoDumpOptions.V3d_SDO_LEFT_EYE
V3d_SDO_RIGHT_EYE = V3d_StereoDumpOptions.V3d_SDO_RIGHT_EYE
V3d_SDO_BLENDED = V3d_StereoDumpOptions.V3d_SDO_BLENDED

class V3d_TypeOfAxe(IntEnum):
    V3d_X: int = ...
    V3d_Y: int = ...
    V3d_Z: int = ...

V3d_X = V3d_TypeOfAxe.V3d_X
V3d_Y = V3d_TypeOfAxe.V3d_Y
V3d_Z = V3d_TypeOfAxe.V3d_Z

class V3d_TypeOfOrientation(IntEnum):
    V3d_Xpos: int = ...
    V3d_Ypos: int = ...
    V3d_Zpos: int = ...
    V3d_Xneg: int = ...
    V3d_Yneg: int = ...
    V3d_Zneg: int = ...
    V3d_XposYpos: int = ...
    V3d_XposZpos: int = ...
    V3d_YposZpos: int = ...
    V3d_XnegYneg: int = ...
    V3d_XnegYpos: int = ...
    V3d_XnegZneg: int = ...
    V3d_XnegZpos: int = ...
    V3d_YnegZneg: int = ...
    V3d_YnegZpos: int = ...
    V3d_XposYneg: int = ...
    V3d_XposZneg: int = ...
    V3d_YposZneg: int = ...
    V3d_XposYposZpos: int = ...
    V3d_XposYnegZpos: int = ...
    V3d_XposYposZneg: int = ...
    V3d_XnegYposZpos: int = ...
    V3d_XposYnegZneg: int = ...
    V3d_XnegYposZneg: int = ...
    V3d_XnegYnegZpos: int = ...
    V3d_XnegYnegZneg: int = ...
    V3d_TypeOfOrientation_Zup_AxoLeft: int = ...
    V3d_TypeOfOrientation_Zup_AxoRight: int = ...
    V3d_TypeOfOrientation_Zup_Front: int = ...
    V3d_TypeOfOrientation_Zup_Back: int = ...
    V3d_TypeOfOrientation_Zup_Top: int = ...
    V3d_TypeOfOrientation_Zup_Bottom: int = ...
    V3d_TypeOfOrientation_Zup_Left: int = ...
    V3d_TypeOfOrientation_Zup_Right: int = ...
    V3d_TypeOfOrientation_Yup_AxoLeft: int = ...
    V3d_TypeOfOrientation_Yup_AxoRight: int = ...
    V3d_TypeOfOrientation_Yup_Front: int = ...
    V3d_TypeOfOrientation_Yup_Back: int = ...
    V3d_TypeOfOrientation_Yup_Top: int = ...
    V3d_TypeOfOrientation_Yup_Bottom: int = ...
    V3d_TypeOfOrientation_Yup_Left: int = ...
    V3d_TypeOfOrientation_Yup_Right: int = ...

V3d_Xpos = V3d_TypeOfOrientation.V3d_Xpos
V3d_Ypos = V3d_TypeOfOrientation.V3d_Ypos
V3d_Zpos = V3d_TypeOfOrientation.V3d_Zpos
V3d_Xneg = V3d_TypeOfOrientation.V3d_Xneg
V3d_Yneg = V3d_TypeOfOrientation.V3d_Yneg
V3d_Zneg = V3d_TypeOfOrientation.V3d_Zneg
V3d_XposYpos = V3d_TypeOfOrientation.V3d_XposYpos
V3d_XposZpos = V3d_TypeOfOrientation.V3d_XposZpos
V3d_YposZpos = V3d_TypeOfOrientation.V3d_YposZpos
V3d_XnegYneg = V3d_TypeOfOrientation.V3d_XnegYneg
V3d_XnegYpos = V3d_TypeOfOrientation.V3d_XnegYpos
V3d_XnegZneg = V3d_TypeOfOrientation.V3d_XnegZneg
V3d_XnegZpos = V3d_TypeOfOrientation.V3d_XnegZpos
V3d_YnegZneg = V3d_TypeOfOrientation.V3d_YnegZneg
V3d_YnegZpos = V3d_TypeOfOrientation.V3d_YnegZpos
V3d_XposYneg = V3d_TypeOfOrientation.V3d_XposYneg
V3d_XposZneg = V3d_TypeOfOrientation.V3d_XposZneg
V3d_YposZneg = V3d_TypeOfOrientation.V3d_YposZneg
V3d_XposYposZpos = V3d_TypeOfOrientation.V3d_XposYposZpos
V3d_XposYnegZpos = V3d_TypeOfOrientation.V3d_XposYnegZpos
V3d_XposYposZneg = V3d_TypeOfOrientation.V3d_XposYposZneg
V3d_XnegYposZpos = V3d_TypeOfOrientation.V3d_XnegYposZpos
V3d_XposYnegZneg = V3d_TypeOfOrientation.V3d_XposYnegZneg
V3d_XnegYposZneg = V3d_TypeOfOrientation.V3d_XnegYposZneg
V3d_XnegYnegZpos = V3d_TypeOfOrientation.V3d_XnegYnegZpos
V3d_XnegYnegZneg = V3d_TypeOfOrientation.V3d_XnegYnegZneg
V3d_TypeOfOrientation_Zup_AxoLeft = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_AxoLeft
V3d_TypeOfOrientation_Zup_AxoRight = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_AxoRight
V3d_TypeOfOrientation_Zup_Front = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Front
V3d_TypeOfOrientation_Zup_Back = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Back
V3d_TypeOfOrientation_Zup_Top = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Top
V3d_TypeOfOrientation_Zup_Bottom = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Bottom
V3d_TypeOfOrientation_Zup_Left = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Left
V3d_TypeOfOrientation_Zup_Right = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Right
V3d_TypeOfOrientation_Yup_AxoLeft = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_AxoLeft
V3d_TypeOfOrientation_Yup_AxoRight = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_AxoRight
V3d_TypeOfOrientation_Yup_Front = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Front
V3d_TypeOfOrientation_Yup_Back = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Back
V3d_TypeOfOrientation_Yup_Top = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Top
V3d_TypeOfOrientation_Yup_Bottom = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Bottom
V3d_TypeOfOrientation_Yup_Left = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Left
V3d_TypeOfOrientation_Yup_Right = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Right

class V3d_TypeOfView(IntEnum):
    V3d_ORTHOGRAPHIC: int = ...
    V3d_PERSPECTIVE: int = ...

V3d_ORTHOGRAPHIC = V3d_TypeOfView.V3d_ORTHOGRAPHIC
V3d_PERSPECTIVE = V3d_TypeOfView.V3d_PERSPECTIVE

class V3d_TypeOfVisualization(IntEnum):
    V3d_WIREFRAME: int = ...
    V3d_ZBUFFER: int = ...

V3d_WIREFRAME = V3d_TypeOfVisualization.V3d_WIREFRAME
V3d_ZBUFFER = V3d_TypeOfVisualization.V3d_ZBUFFER

class v3d:
    @staticmethod
    def ArrowOfRadius(garrow: Graphic3d_Group, X0: float, Y0: float, Z0: float, DX: float, DY: float, DZ: float, Alpha: float, Lng: float) -> None: ...
    @staticmethod
    def CircleInPlane(gcircle: Graphic3d_Group, X0: float, Y0: float, Z0: float, VX: float, VY: float, VZ: float, Radius: float) -> None: ...
    @staticmethod
    def GetProjAxis(theOrientation: V3d_TypeOfOrientation) -> gp_Dir: ...
    @staticmethod
    def SwitchViewsinWindow(aPreviousView: V3d_View, aNextView: V3d_View) -> None: ...
    @overload
    @staticmethod
    def TypeOfOrientationFromString(theTypeString: str) -> V3d_TypeOfOrientation: ...
    @overload
    @staticmethod
    def TypeOfOrientationFromString(theTypeString: str) -> Tuple[bool, V3d_TypeOfOrientation]: ...
    @staticmethod
    def TypeOfOrientationToString(theType: V3d_TypeOfOrientation) -> str: ...

class V3d_AmbientLight(Graphic3d_CLight):
    def __init__(self, theColor: Optional[Quantity_Color] = Quantity_NOC_WHITE) -> None: ...

class V3d_CircularGrid(Aspect_CircularGrid):
    def __init__(self, aViewer: V3d_ViewerPointer, aColor: Quantity_Color, aTenthColor: Quantity_Color) -> None: ...
    def Display(self) -> None: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Erase(self) -> None: ...
    def GraphicValues(self) -> Tuple[float, float]: ...
    def IsDisplayed(self) -> bool: ...
    def SetColors(self, aColor: Quantity_Color, aTenthColor: Quantity_Color) -> None: ...
    def SetGraphicValues(self, Radius: float, OffSet: float) -> None: ...

class V3d_ImageDumpOptions:
    def __init__(self) -> None: ...

class V3d_Plane(Standard_Transient):
    def __init__(self, theA: Optional[float] = 0.0, theB: Optional[float] = 0.0, theC: Optional[float] = 1.0, theD: Optional[float] = 0.0) -> None: ...
    def ClipPlane(self) -> Graphic3d_ClipPlane: ...
    def Display(self, theView: V3d_View, theColor: Optional[Quantity_Color] = Quantity_NOC_GRAY) -> None: ...
    def Erase(self) -> None: ...
    def IsDisplayed(self) -> bool: ...
    def Plane(self) -> Tuple[float, float, float, float]: ...
    def SetPlane(self, theA: float, theB: float, theC: float, theD: float) -> None: ...

class V3d_PositionLight(Graphic3d_CLight):
    pass

class V3d_RectangularGrid(Aspect_RectangularGrid):
    def __init__(self, aViewer: V3d_ViewerPointer, aColor: Quantity_Color, aTenthColor: Quantity_Color) -> None: ...
    def Display(self) -> None: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Erase(self) -> None: ...
    def GraphicValues(self) -> Tuple[float, float, float]: ...
    def IsDisplayed(self) -> bool: ...
    def SetColors(self, aColor: Quantity_Color, aTenthColor: Quantity_Color) -> None: ...
    def SetGraphicValues(self, XSize: float, YSize: float, OffSet: float) -> None: ...

class V3d_Trihedron(Standard_Transient):
    def __init__(self) -> None: ...
    def ArrowAspect(self, theAxis: V3d_TypeOfAxe) -> Prs3d_ShadingAspect: ...
    def ArrowDiameter(self) -> float: ...
    @overload
    def Display(self, theView: V3d_View) -> None: ...
    @overload
    def Display(self, theView: V3d_View) -> None: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Erase(self) -> None: ...
    def IsWireframe(self) -> bool: ...
    def Label(self, theAxis: V3d_TypeOfAxe) -> str: ...
    def LabelAspect(self, theAxis: V3d_TypeOfAxe) -> Prs3d_TextAspect: ...
    def NbFacets(self) -> int: ...
    def OriginAspect(self) -> Prs3d_ShadingAspect: ...
    def Scale(self) -> float: ...
    def SetArrowDiameter(self, theDiam: float) -> None: ...
    def SetArrowsColor(self, theXColor: Quantity_Color, theYColor: Quantity_Color, theZColor: Quantity_Color) -> None: ...
    def SetLabels(self, theX: str, theY: str, theZ: str) -> None: ...
    @overload
    def SetLabelsColor(self, theXColor: Quantity_Color, theYColor: Quantity_Color, theZColor: Quantity_Color) -> None: ...
    @overload
    def SetLabelsColor(self, theColor: Quantity_Color) -> None: ...
    def SetNbFacets(self, theNbFacets: int) -> None: ...
    def SetPosition(self, thePosition: Aspect_TypeOfTriedronPosition) -> None: ...
    def SetScale(self, theScale: float) -> None: ...
    def SetSizeRatio(self, theRatio: float) -> None: ...
    def SetWireframe(self, theAsWireframe: bool) -> None: ...
    def SizeRatio(self) -> float: ...
    def TransformPersistence(self) -> Graphic3d_TransformPers: ...

class V3d_View(Standard_Transient):
    @overload
    def __init__(self, theViewer: V3d_Viewer, theType: Optional[V3d_TypeOfView] = V3d_ORTHOGRAPHIC) -> None: ...
    @overload
    def __init__(self, theViewer: V3d_Viewer, theView: V3d_View) -> None: ...
    def ActiveLight(self) -> V3d_Light: ...
    def ActiveLightIterator(self) -> V3d_ListOfLightIterator: ...
    def ActiveLights(self) -> V3d_ListOfLight: ...
    def AddClipPlane(self, thePlane: Graphic3d_ClipPlane) -> None: ...
    def AddSubview(self, theView: V3d_View) -> None: ...
    def At(self) -> Tuple[float, float, float]: ...
    def AutoZFit(self) -> None: ...
    def AutoZFitMode(self) -> bool: ...
    def AutoZFitScaleFactor(self) -> float: ...
    @overload
    def AxialScale(self) -> Tuple[float, float, float]: ...
    @overload
    def AxialScale(self, Dx: int, Dy: int, Axis: V3d_TypeOfAxe) -> None: ...
    def BackFacingModel(self) -> Graphic3d_TypeOfBackfacingModel: ...
    @overload
    def BackgroundColor(self, Type: Quantity_TypeOfColor) -> Tuple[float, float, float]: ...
    @overload
    def BackgroundColor(self) -> Quantity_Color: ...
    def BackgroundSkydome(self) -> Aspect_SkydomeBackground: ...
    def Camera(self) -> Graphic3d_Camera: ...
    def ChangeRenderingParams(self) -> Graphic3d_RenderingParams: ...
    def ClearPBREnvironment(self, theToUpdate: Optional[bool] = False) -> None: ...
    def ClipPlanes(self) -> Graphic3d_SequenceOfHClipPlane: ...
    def ComputedMode(self) -> bool: ...
    @overload
    def Convert(self, Vp: int) -> float: ...
    @overload
    def Convert(self, Xp: int, Yp: int) -> Tuple[float, float]: ...
    @overload
    def Convert(self, Vv: float) -> int: ...
    @overload
    def Convert(self, Xv: float, Yv: float) -> Tuple[int, int]: ...
    @overload
    def Convert(self, Xp: int, Yp: int) -> Tuple[float, float, float]: ...
    @overload
    def Convert(self, X: float, Y: float, Z: float) -> Tuple[int, int]: ...
    @overload
    def ConvertToGrid(self, Xp: int, Yp: int) -> Tuple[float, float, float]: ...
    @overload
    def ConvertToGrid(self, X: float, Y: float, Z: float) -> Tuple[float, float, float]: ...
    def ConvertWithProj(self, Xp: int, Yp: int) -> Tuple[float, float, float, float, float, float]: ...
    def DefaultCamera(self) -> Graphic3d_Camera: ...
    def Depth(self) -> float: ...
    def DepthFitAll(self, Aspect: Optional[float] = 0.01, Margin: Optional[float] = 0.01) -> None: ...
    def DiagnosticInformation(self, theDict: TColStd_IndexedDataMapOfStringString, theFlags: Graphic3d_DiagnosticInfo) -> None: ...
    def DoMapping(self) -> None: ...
    def Dump(self, theFile: str, theBufferType: Optional[Graphic3d_BufferType] = Graphic3d_BT_RGB) -> bool: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Eye(self) -> Tuple[float, float, float]: ...
    @overload
    def FitAll(self, theMargin: Optional[float] = 0.01, theToUpdate: Optional[bool] = True) -> None: ...
    @overload
    def FitAll(self, theBox: Bnd_Box, theMargin: Optional[float] = 0.01, theToUpdate: Optional[bool] = True) -> None: ...
    @overload
    def FitAll(self, theMinXv: float, theMinYv: float, theMaxXv: float, theMaxYv: float) -> None: ...
    def FitMinMax(self, theCamera: Graphic3d_Camera, theBox: Bnd_Box, theMargin: float, theResolution: Optional[float] = 0.0, theToEnlargeIfLine: Optional[bool] = True) -> bool: ...
    def FocalReferencePoint(self) -> Tuple[float, float, float]: ...
    def Focale(self) -> float: ...
    def GeneratePBREnvironment(self, theToUpdate: Optional[bool] = False) -> None: ...
    def GetGraduatedTrihedron(self) -> Graphic3d_GraduatedTrihedron: ...
    def GradientBackground(self) -> Aspect_GradientBackground: ...
    def GradientBackgroundColors(self, theColor1: Quantity_Color, theColor2: Quantity_Color) -> None: ...
    def GraduatedTrihedronDisplay(self, theTrihedronData: Graphic3d_GraduatedTrihedron) -> None: ...
    def GraduatedTrihedronErase(self) -> None: ...
    def GravityPoint(self) -> gp_Pnt: ...
    def IfMoreLights(self) -> bool: ...
    def IfWindow(self) -> bool: ...
    def InitActiveLights(self) -> None: ...
    def Invalidate(self) -> None: ...
    def InvalidateImmediate(self) -> None: ...
    def IsActiveLight(self, theLight: V3d_Light) -> bool: ...
    def IsCullingEnabled(self) -> bool: ...
    def IsEmpty(self) -> bool: ...
    def IsImageBasedLighting(self) -> bool: ...
    def IsInvalidated(self) -> bool: ...
    def IsInvalidatedImmediate(self) -> bool: ...
    def IsSubview(self) -> bool: ...
    def LightLimit(self) -> int: ...
    def MoreActiveLights(self) -> bool: ...
    @overload
    def Move(self, Dx: float, Dy: float, Dz: float, Start: Optional[bool] = True) -> None: ...
    @overload
    def Move(self, Axe: V3d_TypeOfAxe, Length: float, Start: Optional[bool] = True) -> None: ...
    @overload
    def Move(self, Length: float, Start: Optional[bool] = True) -> None: ...
    def MustBeResized(self) -> None: ...
    def NextActiveLights(self) -> None: ...
    def Pan(self, theDXp: int, theDYp: int, theZoomFactor: Optional[float] = 1, theToStart: Optional[bool] = True) -> None: ...
    def Panning(self, theDXv: float, theDYv: float, theZoomFactor: Optional[float] = 1, theToStart: Optional[bool] = True) -> None: ...
    def ParentView(self) -> V3d_View: ...
    def PickSubview(self, thePnt: Graphic3d_Vec2i) -> V3d_View: ...
    def Place(self, theXp: int, theYp: int, theZoomFactor: Optional[float] = 1) -> None: ...
    def PlaneLimit(self) -> int: ...
    def Proj(self) -> Tuple[float, float, float]: ...
    def ProjReferenceAxe(self, Xpix: int, Ypix: int) -> Tuple[float, float, float, float, float, float]: ...
    @overload
    def Project(self, theX: float, theY: float, theZ: float) -> Tuple[float, float]: ...
    @overload
    def Project(self, theX: float, theY: float, theZ: float) -> Tuple[float, float, float]: ...
    def Redraw(self) -> None: ...
    def RedrawImmediate(self) -> None: ...
    def Remove(self) -> None: ...
    def RemoveClipPlane(self, thePlane: Graphic3d_ClipPlane) -> None: ...
    def RemoveSubview(self, theView: V3d_View) -> bool: ...
    def RenderingParams(self) -> Graphic3d_RenderingParams: ...
    def Reset(self, theToUpdate: Optional[bool] = True) -> None: ...
    def ResetViewMapping(self) -> None: ...
    def ResetViewOrientation(self) -> None: ...
    @overload
    def Rotate(self, Ax: float, Ay: float, Az: float, Start: Optional[bool] = True) -> None: ...
    @overload
    def Rotate(self, Ax: float, Ay: float, Az: float, X: float, Y: float, Z: float, Start: Optional[bool] = True) -> None: ...
    @overload
    def Rotate(self, Axe: V3d_TypeOfAxe, Angle: float, X: float, Y: float, Z: float, Start: Optional[bool] = True) -> None: ...
    @overload
    def Rotate(self, Axe: V3d_TypeOfAxe, Angle: float, Start: Optional[bool] = True) -> None: ...
    @overload
    def Rotate(self, Angle: float, Start: Optional[bool] = True) -> None: ...
    def Rotation(self, X: int, Y: int) -> None: ...
    def Scale(self) -> float: ...
    def SetAt(self, X: float, Y: float, Z: float) -> None: ...
    def SetAutoZFitMode(self, theIsOn: bool, theScaleFactor: Optional[float] = 1.0) -> None: ...
    def SetAxialScale(self, Sx: float, Sy: float, Sz: float) -> None: ...
    def SetAxis(self, X: float, Y: float, Z: float, Vx: float, Vy: float, Vz: float) -> None: ...
    def SetBackFacingModel(self, theModel: Optional[Graphic3d_TypeOfBackfacingModel] = Graphic3d_TypeOfBackfacingModel_Auto) -> None: ...
    @overload
    def SetBackgroundColor(self, theType: Quantity_TypeOfColor, theV1: float, theV2: float, theV3: float) -> None: ...
    @overload
    def SetBackgroundColor(self, theColor: Quantity_Color) -> None: ...
    def SetBackgroundCubeMap(self, theCubeMap: Graphic3d_CubeMap, theToUpdatePBREnv: Optional[bool] = True, theToUpdate: Optional[bool] = False) -> None: ...
    @overload
    def SetBackgroundImage(self, theFileName: str, theFillStyle: Optional[Aspect_FillMethod] = Aspect_FM_CENTERED, theToUpdate: Optional[bool] = False) -> None: ...
    @overload
    def SetBackgroundImage(self, theTexture: Graphic3d_Texture2D, theFillStyle: Optional[Aspect_FillMethod] = Aspect_FM_CENTERED, theToUpdate: Optional[bool] = False) -> None: ...
    def SetBackgroundSkydome(self, theAspect: Aspect_SkydomeBackground, theToUpdatePBREnv: Optional[bool] = True) -> None: ...
    def SetBgGradientColors(self, theColor1: Quantity_Color, theColor2: Quantity_Color, theFillStyle: Optional[Aspect_GradientFillMethod] = Aspect_GradientFillMethod_Horizontal, theToUpdate: Optional[bool] = False) -> None: ...
    def SetBgGradientStyle(self, theMethod: Optional[Aspect_GradientFillMethod] = Aspect_GradientFillMethod_Horizontal, theToUpdate: Optional[bool] = False) -> None: ...
    def SetBgImageStyle(self, theFillStyle: Aspect_FillMethod, theToUpdate: Optional[bool] = False) -> None: ...
    def SetCamera(self, theCamera: Graphic3d_Camera) -> None: ...
    def SetCenter(self, theXp: int, theYp: int) -> None: ...
    def SetClipPlanes(self, thePlanes: Graphic3d_SequenceOfHClipPlane) -> None: ...
    def SetComputedMode(self, theMode: bool) -> None: ...
    def SetDepth(self, Depth: float) -> None: ...
    def SetEye(self, X: float, Y: float, Z: float) -> None: ...
    def SetFocale(self, Focale: float) -> None: ...
    def SetFront(self) -> None: ...
    def SetFrustumCulling(self, theMode: bool) -> None: ...
    def SetGrid(self, aPlane: gp_Ax3, aGrid: Aspect_Grid) -> None: ...
    def SetGridActivity(self, aFlag: bool) -> None: ...
    def SetImageBasedLighting(self, theToEnableIBL: bool, theToUpdate: Optional[bool] = False) -> None: ...
    def SetImmediateUpdate(self, theImmediateUpdate: bool) -> bool: ...
    @overload
    def SetLightOff(self, theLight: V3d_Light) -> None: ...
    @overload
    def SetLightOff(self) -> None: ...
    @overload
    def SetLightOn(self, theLight: V3d_Light) -> None: ...
    @overload
    def SetLightOn(self) -> None: ...
    def SetMagnify(self, theWindow: Aspect_Window, thePreviousView: V3d_View, theX1: int, theY1: int, theX2: int, theY2: int) -> None: ...
    @overload
    def SetProj(self, Vx: float, Vy: float, Vz: float) -> None: ...
    @overload
    def SetProj(self, theOrientation: V3d_TypeOfOrientation, theIsYup: Optional[bool] = False) -> None: ...
    def SetScale(self, Coef: float) -> None: ...
    def SetShadingModel(self, theShadingModel: Graphic3d_TypeOfShadingModel) -> None: ...
    def SetSize(self, theSize: float) -> None: ...
    def SetTextureEnv(self, theTexture: Graphic3d_TextureEnv) -> None: ...
    def SetTwist(self, Angle: float) -> None: ...
    @overload
    def SetUp(self, Vx: float, Vy: float, Vz: float) -> None: ...
    @overload
    def SetUp(self, Orientation: V3d_TypeOfOrientation) -> None: ...
    def SetViewMappingDefault(self) -> None: ...
    def SetViewOrientationDefault(self) -> None: ...
    def SetVisualization(self, theType: V3d_TypeOfVisualization) -> None: ...
    @overload
    def SetWindow(self, theWindow: Aspect_Window, theContext: Optional[Aspect_RenderingContext] = None) -> None: ...
    @overload
    def SetWindow(self, theParentView: V3d_View, theSize: Graphic3d_Vec2d, theCorner: Optional[Aspect_TypeOfTriedronPosition] = Aspect_TOTP_LEFT_UPPER, theOffset: Optional[Graphic3d_Vec2d] = Graphic3d_Vec2d(), theMargins: Optional[Graphic3d_Vec2i] = Graphic3d_Vec2i()) -> None: ...
    def SetZSize(self, SetZSize: float) -> None: ...
    def SetZoom(self, Coef: float, Start: Optional[bool] = True) -> None: ...
    def ShadingModel(self) -> Graphic3d_TypeOfShadingModel: ...
    def Size(self) -> Tuple[float, float]: ...
    def StartRotation(self, X: int, Y: int, zRotationThreshold: Optional[float] = 0.0) -> None: ...
    def StartZoomAtPoint(self, theXp: int, theYp: int) -> None: ...
    @overload
    def StatisticInformation(self) -> str: ...
    @overload
    def StatisticInformation(self, theDict: TColStd_IndexedDataMapOfStringString) -> None: ...
    def Subviews(self) -> False: ...
    def TextureEnv(self) -> Graphic3d_TextureEnv: ...
    @overload
    def ToPixMap(self, theImage: Image_PixMap, theParams: V3d_ImageDumpOptions) -> bool: ...
    @overload
    def ToPixMap(self, theImage: Image_PixMap, theWidth: int, theHeight: int, theBufferType: Optional[Graphic3d_BufferType] = Graphic3d_BT_RGB, theToAdjustAspect: Optional[bool] = True, theStereoOptions: Optional[V3d_StereoDumpOptions] = V3d_SDO_MONO) -> bool: ...
    @overload
    def Translate(self, Dx: float, Dy: float, Dz: float, Start: Optional[bool] = True) -> None: ...
    @overload
    def Translate(self, Axe: V3d_TypeOfAxe, Length: float, Start: Optional[bool] = True) -> None: ...
    @overload
    def Translate(self, Length: float, Start: Optional[bool] = True) -> None: ...
    def TriedronDisplay(self, thePosition: Optional[Aspect_TypeOfTriedronPosition] = Aspect_TOTP_CENTER, theColor: Optional[Quantity_Color] = Quantity_NOC_WHITE, theScale: Optional[float] = 0.02, theMode: Optional[V3d_TypeOfVisualization] = V3d_WIREFRAME) -> None: ...
    def TriedronErase(self) -> None: ...
    def Trihedron(self, theToCreate: Optional[bool] = true) -> V3d_Trihedron: ...
    @overload
    def Turn(self, Ax: float, Ay: float, Az: float, Start: Optional[bool] = True) -> None: ...
    @overload
    def Turn(self, Axe: V3d_TypeOfAxe, Angle: float, Start: Optional[bool] = True) -> None: ...
    @overload
    def Turn(self, Angle: float, Start: Optional[bool] = True) -> None: ...
    def Twist(self) -> float: ...
    def Type(self) -> V3d_TypeOfView: ...
    def Up(self) -> Tuple[float, float, float]: ...
    def Update(self) -> None: ...
    def UpdateLights(self) -> None: ...
    def View(self) -> Graphic3d_CView: ...
    def Viewer(self) -> V3d_Viewer: ...
    def Visualization(self) -> V3d_TypeOfVisualization: ...
    def Window(self) -> Aspect_Window: ...
    def WindowFit(self, theMinXp: int, theMinYp: int, theMaxXp: int, theMaxYp: int) -> None: ...
    def WindowFitAll(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int) -> None: ...
    def ZBufferTriedronSetup(self, theXColor: Optional[Quantity_Color] = Quantity_NOC_RED, theYColor: Optional[Quantity_Color] = Quantity_NOC_GREEN, theZColor: Optional[Quantity_Color] = Quantity_NOC_BLUE1, theSizeRatio: Optional[float] = 0.8, theAxisDiametr: Optional[float] = 0.05, theNbFacettes: Optional[int] = 12) -> None: ...
    def ZFitAll(self, theScaleFactor: Optional[float] = 1.0) -> None: ...
    def ZSize(self) -> float: ...
    def Zoom(self, theXp1: int, theYp1: int, theXp2: int, theYp2: int) -> None: ...
    def ZoomAtPoint(self, theMouseStartX: int, theMouseStartY: int, theMouseEndX: int, theMouseEndY: int) -> None: ...

class V3d_Viewer(Standard_Transient):
    def __init__(self, theDriver: Graphic3d_GraphicDriver) -> None: ...
    def ActivateGrid(self, aGridType: Aspect_GridType, aGridDrawMode: Aspect_GridDrawMode) -> None: ...
    def ActiveLight(self) -> V3d_Light: ...
    def ActiveLightIterator(self) -> V3d_ListOfLightIterator: ...
    def ActiveLights(self) -> V3d_ListOfLight: ...
    def ActiveView(self) -> V3d_View: ...
    def ActiveViewIterator(self) -> V3d_ListOfViewIterator: ...
    def ActiveViews(self) -> V3d_ListOfView: ...
    def AddLight(self, theLight: V3d_Light) -> None: ...
    def AddZLayer(self, theSettings: Optional[Graphic3d_ZLayerSettings] = Graphic3d_ZLayerSettings()) -> Tuple[bool, int]: ...
    def CircularGridGraphicValues(self) -> Tuple[float, float]: ...
    def CircularGridValues(self) -> Tuple[float, float, float, int, float]: ...
    def ComputedMode(self) -> bool: ...
    def CreateView(self) -> V3d_View: ...
    def DeactivateGrid(self) -> None: ...
    def DefaultBackgroundColor(self) -> Quantity_Color: ...
    def DefaultBgGradientColors(self, theColor1: Quantity_Color, theColor2: Quantity_Color) -> None: ...
    def DefaultComputedMode(self) -> bool: ...
    def DefaultRenderingParams(self) -> Graphic3d_RenderingParams: ...
    def DefaultShadingModel(self) -> Graphic3d_TypeOfShadingModel: ...
    def DefaultTypeOfView(self) -> V3d_TypeOfView: ...
    def DefaultViewProj(self) -> V3d_TypeOfOrientation: ...
    def DefaultViewSize(self) -> float: ...
    def DefaultVisualization(self) -> V3d_TypeOfVisualization: ...
    def DefinedLight(self) -> V3d_Light: ...
    def DefinedLightIterator(self) -> V3d_ListOfLightIterator: ...
    def DefinedLights(self) -> V3d_ListOfLight: ...
    def DefinedView(self) -> V3d_View: ...
    def DefinedViewIterator(self) -> V3d_ListOfViewIterator: ...
    def DefinedViews(self) -> V3d_ListOfView: ...
    def DelLight(self, theLight: V3d_Light) -> None: ...
    def DisplayPrivilegedPlane(self, theOnOff: bool, theSize: Optional[float] = 1) -> None: ...
    def Driver(self) -> Graphic3d_GraphicDriver: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Erase(self) -> None: ...
    def GetAllZLayers(self, theLayerSeq: TColStd_SequenceOfInteger) -> None: ...
    def GetGradientBackground(self) -> Aspect_GradientBackground: ...
    @overload
    def Grid(self, theToCreate: Optional[bool] = true) -> Aspect_Grid: ...
    @overload
    def Grid(self, theGridType: Aspect_GridType, theToCreate: Optional[bool] = true) -> Aspect_Grid: ...
    def GridDrawMode(self) -> Aspect_GridDrawMode: ...
    def GridEcho(self) -> bool: ...
    def GridType(self) -> Aspect_GridType: ...
    def HideGridEcho(self, theView: V3d_View) -> None: ...
    def IfMoreViews(self) -> bool: ...
    def InitActiveLights(self) -> None: ...
    def InitActiveViews(self) -> None: ...
    def InitDefinedLights(self) -> None: ...
    def InitDefinedViews(self) -> None: ...
    def InsertLayerAfter(self, theSettings: Graphic3d_ZLayerSettings, theLayerBefore: int) -> Tuple[bool, int]: ...
    def InsertLayerBefore(self, theSettings: Graphic3d_ZLayerSettings, theLayerAfter: int) -> Tuple[bool, int]: ...
    def Invalidate(self) -> None: ...
    def IsActive(self) -> bool: ...
    def IsGlobalLight(self, TheLight: V3d_Light) -> bool: ...
    def IsGridActive(self) -> bool: ...
    def LastActiveView(self) -> bool: ...
    def MoreActiveLights(self) -> bool: ...
    def MoreActiveViews(self) -> bool: ...
    def MoreDefinedLights(self) -> bool: ...
    def MoreDefinedViews(self) -> bool: ...
    def NextActiveLights(self) -> None: ...
    def NextActiveViews(self) -> None: ...
    def NextDefinedLights(self) -> None: ...
    def NextDefinedViews(self) -> None: ...
    def PrivilegedPlane(self) -> gp_Ax3: ...
    def RectangularGridGraphicValues(self) -> Tuple[float, float, float]: ...
    def RectangularGridValues(self) -> Tuple[float, float, float, float, float]: ...
    def Redraw(self) -> None: ...
    def RedrawImmediate(self) -> None: ...
    def Remove(self) -> None: ...
    def RemoveZLayer(self, theLayerId: int) -> bool: ...
    def SetCircularGridGraphicValues(self, Radius: float, OffSet: float) -> None: ...
    def SetCircularGridValues(self, XOrigin: float, YOrigin: float, RadiusStep: float, DivisionNumber: int, RotationAngle: float) -> None: ...
    def SetComputedMode(self, theMode: bool) -> None: ...
    def SetDefaultBackgroundColor(self, theColor: Quantity_Color) -> None: ...
    def SetDefaultBgGradientColors(self, theColor1: Quantity_Color, theColor2: Quantity_Color, theFillStyle: Optional[Aspect_GradientFillMethod] = Aspect_GradientFillMethod_Horizontal) -> None: ...
    def SetDefaultComputedMode(self, theMode: bool) -> None: ...
    def SetDefaultLights(self) -> None: ...
    def SetDefaultRenderingParams(self, theParams: Graphic3d_RenderingParams) -> None: ...
    def SetDefaultShadingModel(self, theType: Graphic3d_TypeOfShadingModel) -> None: ...
    def SetDefaultTypeOfView(self, theType: V3d_TypeOfView) -> None: ...
    def SetDefaultViewProj(self, theOrientation: V3d_TypeOfOrientation) -> None: ...
    def SetDefaultViewSize(self, theSize: float) -> None: ...
    def SetDefaultVisualization(self, theType: V3d_TypeOfVisualization) -> None: ...
    @overload
    def SetGridEcho(self, showGrid: Optional[bool] = True) -> None: ...
    @overload
    def SetGridEcho(self, aMarker: Graphic3d_AspectMarker3d) -> None: ...
    @overload
    def SetLightOff(self, theLight: V3d_Light) -> None: ...
    @overload
    def SetLightOff(self) -> None: ...
    @overload
    def SetLightOn(self, theLight: V3d_Light) -> None: ...
    @overload
    def SetLightOn(self) -> None: ...
    def SetPrivilegedPlane(self, thePlane: gp_Ax3) -> None: ...
    def SetRectangularGridGraphicValues(self, XSize: float, YSize: float, OffSet: float) -> None: ...
    def SetRectangularGridValues(self, XOrigin: float, YOrigin: float, XStep: float, YStep: float, RotationAngle: float) -> None: ...
    @overload
    def SetViewOff(self) -> None: ...
    @overload
    def SetViewOff(self, theView: V3d_View) -> None: ...
    @overload
    def SetViewOn(self) -> None: ...
    @overload
    def SetViewOn(self, theView: V3d_View) -> None: ...
    def SetZLayerSettings(self, theLayerId: int, theSettings: Graphic3d_ZLayerSettings) -> None: ...
    def ShowGridEcho(self, theView: V3d_View, thePoint: Graphic3d_Vertex) -> None: ...
    def StructureManager(self) -> Graphic3d_StructureManager: ...
    def UnHighlight(self) -> None: ...
    def Update(self) -> None: ...
    def UpdateLights(self) -> None: ...
    def ZLayerSettings(self, theLayerId: int) -> Graphic3d_ZLayerSettings: ...

class V3d_DirectionalLight(V3d_PositionLight):
    @overload
    def __init__(self, theDirection: Optional[V3d_TypeOfOrientation] = V3d_XposYposZpos, theColor: Optional[Quantity_Color] = Quantity_NOC_WHITE, theIsHeadlight: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, theDirection: gp_Dir, theColor: Optional[Quantity_Color] = Quantity_NOC_WHITE, theIsHeadlight: Optional[bool] = False) -> None: ...
    def SetDirection(self, theDirection: V3d_TypeOfOrientation) -> None: ...

class V3d_PositionalLight(V3d_PositionLight):
    def __init__(self, thePos: gp_Pnt, theColor: Optional[Quantity_Color] = Quantity_NOC_WHITE) -> None: ...

class V3d_SpotLight(V3d_PositionLight):
    @overload
    def __init__(self, thePos: gp_Pnt, theDirection: Optional[V3d_TypeOfOrientation] = V3d_XnegYnegZpos, theColor: Optional[Quantity_Color] = Quantity_NOC_WHITE) -> None: ...
    @overload
    def __init__(self, thePos: gp_Pnt, theDirection: gp_Dir, theColor: Optional[Quantity_Color] = Quantity_NOC_WHITE) -> None: ...
    def SetDirection(self, theOrientation: V3d_TypeOfOrientation) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

