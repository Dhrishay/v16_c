from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.IFSelect import *
from OCC.Core.TopoDS import *
from OCC.Core.Transfer import *
from OCC.Core.TopAbs import *
from OCC.Core.TColStd import *
from OCC.Core.Interface import *
from OCC.Core.TCollection import *
from OCC.Core.Message import *
from OCC.Core.TopTools import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *


class xscontrol:
    @staticmethod
    def Session(pilot: IFSelect_SessionPilot) -> XSControl_WorkSession: ...
    @staticmethod
    def Vars(pilot: IFSelect_SessionPilot) -> XSControl_Vars: ...

class XSControl_ConnectedShapes(IFSelect_SelectExplore):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, TR: XSControl_TransferReader) -> None: ...
    @staticmethod
    def AdjacentEntities(ashape: TopoDS_Shape, TP: Transfer_TransientProcess, type: TopAbs_ShapeEnum) -> TColStd_HSequenceOfTransient: ...
    def Explore(self, level: int, ent: Standard_Transient, G: Interface_Graph, explored: Interface_EntityIterator) -> bool: ...
    def ExploreLabel(self) -> str: ...
    def SetReader(self, TR: XSControl_TransferReader) -> None: ...

class XSControl_Controller(Standard_Transient):
    def ActorRead(self, model: Interface_InterfaceModel) -> Transfer_ActorOfTransientProcess: ...
    def ActorWrite(self) -> Transfer_ActorOfFinderProcess: ...
    def AdaptorSession(self) -> False: ...
    def AddSessionItem(self, theItem: Standard_Transient, theName: str, toApply: Optional[bool] = False) -> None: ...
    def AutoRecord(self) -> None: ...
    def Customise(self, WS: XSControl_WorkSession) -> None: ...
    def IsModeWrite(self, modetrans: int, shape: Optional[bool] = True) -> bool: ...
    def ModeWriteBounds(self, shape: Optional[bool] = True) -> Tuple[bool, int, int]: ...
    def ModeWriteHelp(self, modetrans: int, shape: Optional[bool] = True) -> str: ...
    def Name(self, rsc: Optional[bool] = False) -> str: ...
    def NewModel(self) -> Interface_InterfaceModel: ...
    def Protocol(self) -> Interface_Protocol: ...
    def RecognizeWriteShape(self, shape: TopoDS_Shape, modetrans: Optional[int] = 0) -> bool: ...
    def RecognizeWriteTransient(self, obj: Standard_Transient, modetrans: Optional[int] = 0) -> bool: ...
    def Record(self, name: str) -> None: ...
    @staticmethod
    def Recorded(name: str) -> XSControl_Controller: ...
    def SessionItem(self, theName: str) -> Standard_Transient: ...
    def SetModeWrite(self, modemin: int, modemax: int, shape: Optional[bool] = True) -> None: ...
    def SetModeWriteHelp(self, modetrans: int, help: str, shape: Optional[bool] = True) -> None: ...
    def SetNames(self, theLongName: str, theShortName: str) -> None: ...
    def TransferWriteShape(self, shape: TopoDS_Shape, FP: Transfer_FinderProcess, model: Interface_InterfaceModel, modetrans: Optional[int] = 0, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> IFSelect_ReturnStatus: ...
    def TransferWriteTransient(self, obj: Standard_Transient, FP: Transfer_FinderProcess, model: Interface_InterfaceModel, modetrans: Optional[int] = 0, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> IFSelect_ReturnStatus: ...
    def WorkLibrary(self) -> IFSelect_WorkLibrary: ...

class XSControl_FuncShape:
    @staticmethod
    def FileAndVar(session: XSControl_WorkSession, file: str, var: str, def_: str, resfile: str, resvar: str) -> bool: ...
    @staticmethod
    def Init() -> None: ...
    @staticmethod
    def MoreShapes(session: XSControl_WorkSession, list: TopTools_HSequenceOfShape, name: str) -> int: ...

class XSControl_Functions:
    @staticmethod
    def Init() -> None: ...

class XSControl_Reader:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, norm: str) -> None: ...
    @overload
    def __init__(self, WS: XSControl_WorkSession, scratch: Optional[bool] = True) -> None: ...
    def ClearShapes(self) -> None: ...
    def GetStatsTransfer(self, list: TColStd_HSequenceOfTransient) -> Tuple[int, int, int]: ...
    @overload
    def GiveList(self, first: Optional[str] = "", second: Optional[str] = "") -> TColStd_HSequenceOfTransient: ...
    @overload
    def GiveList(self, first: str, ent: Standard_Transient) -> TColStd_HSequenceOfTransient: ...
    def Model(self) -> Interface_InterfaceModel: ...
    def NbRootsForTransfer(self) -> int: ...
    def NbShapes(self) -> int: ...
    def OneShape(self) -> TopoDS_Shape: ...
    @overload
    def PrintCheckLoad(self, failsonly: bool, mode: IFSelect_PrintCount) -> None: ...
    @overload
    def PrintCheckLoad(self, failsonly: bool, mode: IFSelect_PrintCount) -> str: ...
    @overload
    def PrintCheckTransfer(self, failsonly: bool, mode: IFSelect_PrintCount) -> None: ...
    @overload
    def PrintCheckTransfer(self, failsonly: bool, mode: IFSelect_PrintCount) -> str: ...
    @overload
    def PrintStatsTransfer(self, what: int, mode: Optional[int] = 0) -> None: ...
    @overload
    def PrintStatsTransfer(self, what: int, mode: Optional[int] = 0) -> str: ...
    def ReadFile(self, filename: str) -> IFSelect_ReturnStatus: ...
    def ReadStream(self, theName: str, theIStream: str) -> IFSelect_ReturnStatus: ...
    def RootForTransfer(self, num: Optional[int] = 1) -> Standard_Transient: ...
    def SetNorm(self, norm: str) -> bool: ...
    def SetWS(self, WS: XSControl_WorkSession, scratch: Optional[bool] = True) -> None: ...
    def Shape(self, num: Optional[int] = 1) -> TopoDS_Shape: ...
    def TransferEntity(self, start: Standard_Transient, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    def TransferList(self, list: TColStd_HSequenceOfTransient, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> int: ...
    def TransferOne(self, num: int, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    def TransferOneRoot(self, num: Optional[int] = 1, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    def TransferRoots(self, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> int: ...
    def WS(self) -> XSControl_WorkSession: ...

class XSControl_SelectForTransfer(IFSelect_SelectExtract):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, TR: XSControl_TransferReader) -> None: ...
    def Actor(self) -> Transfer_ActorOfTransientProcess: ...
    def ExtractLabel(self) -> str: ...
    def Reader(self) -> XSControl_TransferReader: ...
    def SetActor(self, act: Transfer_ActorOfTransientProcess) -> None: ...
    def SetReader(self, TR: XSControl_TransferReader) -> None: ...
    def Sort(self, rank: int, ent: Standard_Transient, model: Interface_InterfaceModel) -> bool: ...

class XSControl_SignTransferStatus(IFSelect_Signature):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, TR: XSControl_TransferReader) -> None: ...
    def Map(self) -> Transfer_TransientProcess: ...
    def Reader(self) -> XSControl_TransferReader: ...
    def SetMap(self, TP: Transfer_TransientProcess) -> None: ...
    def SetReader(self, TR: XSControl_TransferReader) -> None: ...
    def Value(self, ent: Standard_Transient, model: Interface_InterfaceModel) -> str: ...

class XSControl_TransferReader(Standard_Transient):
    def __init__(self) -> None: ...
    def Actor(self) -> Transfer_ActorOfTransientProcess: ...
    def BeginTransfer(self) -> bool: ...
    def CheckList(self, theEnt: Standard_Transient, theLevel: Optional[int] = 0) -> Interface_CheckIterator: ...
    def CheckedList(self, theEnt: Standard_Transient, WithCheck: Optional[Interface_CheckStatus] = Interface_CheckAny, theResult: Optional[bool] = True) -> TColStd_HSequenceOfTransient: ...
    def Clear(self, theMode: int) -> None: ...
    def ClearResult(self, theEnt: Standard_Transient, theMode: int) -> bool: ...
    def Context(self) -> False: ...
    def EntitiesFromShapeList(self, theRes: TopTools_HSequenceOfShape, theMode: Optional[int] = 0) -> TColStd_HSequenceOfTransient: ...
    def EntityFromResult(self, theRes: Standard_Transient, theMode: Optional[int] = 0) -> Standard_Transient: ...
    def EntityFromShapeResult(self, theRes: TopoDS_Shape, theMode: Optional[int] = 0) -> Standard_Transient: ...
    def FileName(self) -> str: ...
    def FinalEntityLabel(self, theEnt: Standard_Transient) -> str: ...
    def FinalEntityNumber(self, theEnt: Standard_Transient) -> int: ...
    def FinalResult(self, theEnt: Standard_Transient) -> Transfer_ResultFromModel: ...
    def GetContext(self, theName: str, theType: Standard_Type, theCtx: Standard_Transient) -> bool: ...
    def HasChecks(self, theEnt: Standard_Transient, FailsOnly: bool) -> bool: ...
    def HasResult(self, theEnt: Standard_Transient) -> bool: ...
    def IsMarked(self, theEnt: Standard_Transient) -> bool: ...
    def IsRecorded(self, theEnt: Standard_Transient) -> bool: ...
    def IsSkipped(self, theEnt: Standard_Transient) -> bool: ...
    def LastCheckList(self) -> Interface_CheckIterator: ...
    def LastTransferList(self, theRoots: bool) -> TColStd_HSequenceOfTransient: ...
    def Model(self) -> Interface_InterfaceModel: ...
    def PrintStats(self, theWhat: int, theMode: Optional[int] = 0) -> str: ...
    @staticmethod
    def PrintStatsOnList(theTP: Transfer_TransientProcess, theList: TColStd_HSequenceOfTransient, theWhat: int, theMode: Optional[int] = 0) -> None: ...
    @staticmethod
    def PrintStatsProcess(theTP: Transfer_TransientProcess, theWhat: int, theMode: Optional[int] = 0) -> None: ...
    def Recognize(self, theEnt: Standard_Transient) -> bool: ...
    def RecordResult(self, theEnt: Standard_Transient) -> bool: ...
    def RecordedList(self) -> TColStd_HSequenceOfTransient: ...
    def ResultFromNumber(self, theNum: int) -> Transfer_ResultFromModel: ...
    def SetActor(self, theActor: Transfer_ActorOfTransientProcess) -> None: ...
    def SetContext(self, theName: str, theCtx: Standard_Transient) -> None: ...
    def SetController(self, theControl: XSControl_Controller) -> None: ...
    def SetFileName(self, theName: str) -> None: ...
    def SetGraph(self, theGraph: Interface_HGraph) -> None: ...
    def SetModel(self, theModel: Interface_InterfaceModel) -> None: ...
    def SetTransientProcess(self, theTP: Transfer_TransientProcess) -> None: ...
    def ShapeResult(self, theEnt: Standard_Transient) -> TopoDS_Shape: ...
    def ShapeResultList(self, theRec: bool) -> TopTools_HSequenceOfShape: ...
    def Skip(self, theEnt: Standard_Transient) -> bool: ...
    def TransferClear(self, theEnt: Standard_Transient, theLevel: Optional[int] = 0) -> None: ...
    def TransferList(self, theList: TColStd_HSequenceOfTransient, theRec: Optional[bool] = True, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> int: ...
    def TransferOne(self, theEnt: Standard_Transient, theRec: Optional[bool] = True, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> int: ...
    def TransferRoots(self, theGraph: Interface_Graph, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> int: ...
    def TransientProcess(self) -> Transfer_TransientProcess: ...
    def TransientResult(self, theEnt: Standard_Transient) -> Standard_Transient: ...

class XSControl_TransferWriter(Standard_Transient):
    def __init__(self) -> None: ...
    def CheckList(self) -> Interface_CheckIterator: ...
    def Clear(self, theMode: int) -> None: ...
    def Controller(self) -> XSControl_Controller: ...
    def FinderProcess(self) -> Transfer_FinderProcess: ...
    def PrintStats(self, theWhat: int, theMode: Optional[int] = 0) -> None: ...
    def RecognizeShape(self, theShape: TopoDS_Shape) -> bool: ...
    def RecognizeTransient(self, theObj: Standard_Transient) -> bool: ...
    def ResultCheckList(self, theModel: Interface_InterfaceModel) -> Interface_CheckIterator: ...
    def SetController(self, theCtl: XSControl_Controller) -> None: ...
    def SetFinderProcess(self, theFP: Transfer_FinderProcess) -> None: ...
    def SetTransferMode(self, theMode: int) -> None: ...
    def TransferMode(self) -> int: ...
    def TransferWriteShape(self, theModel: Interface_InterfaceModel, theShape: TopoDS_Shape, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> IFSelect_ReturnStatus: ...
    def TransferWriteTransient(self, theModel: Interface_InterfaceModel, theObj: Standard_Transient, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> IFSelect_ReturnStatus: ...

class XSControl_Utils:
    def __init__(self) -> None: ...
    def AppendCStr(self, seqval: TColStd_HSequenceOfHAsciiString, strval: str) -> None: ...
    def AppendEStr(self, seqval: TColStd_HSequenceOfHExtendedString, strval: Standard_ExtString) -> None: ...
    def AppendShape(self, seqv: TopTools_HSequenceOfShape, shape: TopoDS_Shape) -> None: ...
    def AppendTra(self, seqval: TColStd_HSequenceOfTransient, traval: Standard_Transient) -> None: ...
    def ArrToSeq(self, arr: Standard_Transient) -> Standard_Transient: ...
    def AsciiToExtended(self, str: str) -> Standard_ExtString: ...
    def BinderShape(self, tr: Standard_Transient) -> TopoDS_Shape: ...
    def CStrValue(self, list: Standard_Transient, num: int) -> str: ...
    def CompoundFromSeq(self, seqval: TopTools_HSequenceOfShape) -> TopoDS_Shape: ...
    def DateString(self, yy: int, mm: int, dd: int, hh: int, mn: int, ss: int) -> str: ...
    def DateValues(self, text: str) -> Tuple[int, int, int, int, int, int]: ...
    def EStrValue(self, list: Standard_Transient, num: int) -> Standard_ExtString: ...
    def ExtendedToAscii(self, str: Standard_ExtString) -> str: ...
    def IsAscii(self, str: Standard_ExtString) -> bool: ...
    def IsKind(self, item: Standard_Transient, what: Standard_Type) -> bool: ...
    def NewSeqCStr(self) -> TColStd_HSequenceOfHAsciiString: ...
    def NewSeqEStr(self) -> TColStd_HSequenceOfHExtendedString: ...
    def NewSeqShape(self) -> TopTools_HSequenceOfShape: ...
    def NewSeqTra(self) -> TColStd_HSequenceOfTransient: ...
    def SeqIntValue(self, list: TColStd_HSequenceOfInteger, num: int) -> int: ...
    def SeqLength(self, list: Standard_Transient) -> int: ...
    def SeqToArr(self, seq: Standard_Transient, first: Optional[int] = 1) -> Standard_Transient: ...
    def ShapeBinder(self, shape: TopoDS_Shape, hs: Optional[bool] = True) -> Standard_Transient: ...
    def ShapeType(self, shape: TopoDS_Shape, compound: bool) -> TopAbs_ShapeEnum: ...
    def ShapeValue(self, seqv: TopTools_HSequenceOfShape, num: int) -> TopoDS_Shape: ...
    def SortedCompound(self, shape: TopoDS_Shape, type: TopAbs_ShapeEnum, explore: bool, compound: bool) -> TopoDS_Shape: ...
    def ToAString(self, strcon: str) -> str: ...
    @overload
    def ToCString(self, strval: TCollection_HAsciiString) -> str: ...
    @overload
    def ToCString(self, strval: str) -> str: ...
    @overload
    def ToEString(self, strval: TCollection_HExtendedString) -> Standard_ExtString: ...
    @overload
    def ToEString(self, strval: str) -> Standard_ExtString: ...
    @overload
    def ToHString(self, strcon: str) -> TCollection_HAsciiString: ...
    @overload
    def ToHString(self, strcon: Standard_ExtString) -> TCollection_HExtendedString: ...
    def ToXString(self, strcon: Standard_ExtString) -> str: ...
    def TraValue(self, list: Standard_Transient, num: int) -> Standard_Transient: ...
    def TraceLine(self, line: str) -> None: ...
    def TraceLines(self, lines: Standard_Transient) -> None: ...
    def TypeName(self, item: Standard_Transient, nopk: Optional[bool] = False) -> str: ...

class XSControl_Vars(Standard_Transient):
    def __init__(self) -> None: ...
    def Get(self, name: str) -> Standard_Transient: ...
    def GetCurve(self, name: str) -> Geom_Curve: ...
    def GetCurve2d(self, name: str) -> Geom2d_Curve: ...
    def GetGeom(self, name: str) -> Geom_Geometry: ...
    def GetPoint(self, name: str, pnt: gp_Pnt) -> bool: ...
    def GetPoint2d(self, name: str, pnt: gp_Pnt2d) -> bool: ...
    def GetShape(self, name: str) -> TopoDS_Shape: ...
    def GetSurface(self, name: str) -> Geom_Surface: ...
    def Set(self, name: str, val: Standard_Transient) -> None: ...
    def SetPoint(self, name: str, val: gp_Pnt) -> None: ...
    def SetPoint2d(self, name: str, val: gp_Pnt2d) -> None: ...
    def SetShape(self, name: str, val: TopoDS_Shape) -> None: ...

class XSControl_WorkSession(IFSelect_WorkSession):
    def __init__(self) -> None: ...
    def ClearContext(self) -> None: ...
    def ClearData(self, theMode: int) -> None: ...
    def Context(self) -> False: ...
    def InitTransferReader(self, theMode: int) -> None: ...
    def MapReader(self) -> Transfer_TransientProcess: ...
    def NewModel(self) -> Interface_InterfaceModel: ...
    def NormAdaptor(self) -> XSControl_Controller: ...
    def PrintTransferStatus(self, theNum: int, theWri: bool) -> Tuple[bool, str]: ...
    def Result(self, theEnt: Standard_Transient, theMode: int) -> Standard_Transient: ...
    def SelectNorm(self, theNormName: str) -> bool: ...
    def SelectedNorm(self, theRsc: Optional[bool] = False) -> str: ...
    def SetController(self, theCtl: XSControl_Controller) -> None: ...
    def SetMapReader(self, theTP: Transfer_TransientProcess) -> bool: ...
    def SetMapWriter(self, theFP: Transfer_FinderProcess) -> bool: ...
    def SetTransferReader(self, theTR: XSControl_TransferReader) -> None: ...
    def SetVars(self, theVars: XSControl_Vars) -> None: ...
    def TransferReadOne(self, theEnts: Standard_Transient, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> int: ...
    def TransferReadRoots(self, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> int: ...
    def TransferReader(self) -> XSControl_TransferReader: ...
    def TransferWriteCheckList(self) -> Interface_CheckIterator: ...
    def TransferWriteShape(self, theShape: TopoDS_Shape, theCompGraph: Optional[bool] = True, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> IFSelect_ReturnStatus: ...
    def TransferWriter(self) -> XSControl_TransferWriter: ...
    def Vars(self) -> XSControl_Vars: ...

class XSControl_Writer:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, norm: str) -> None: ...
    @overload
    def __init__(self, WS: XSControl_WorkSession, scratch: Optional[bool] = True) -> None: ...
    def Model(self, newone: Optional[bool] = False) -> Interface_InterfaceModel: ...
    def PrintStatsTransfer(self, what: int, mode: Optional[int] = 0) -> None: ...
    def SetNorm(self, norm: str) -> bool: ...
    def SetWS(self, WS: XSControl_WorkSession, scratch: Optional[bool] = True) -> None: ...
    def TransferShape(self, sh: TopoDS_Shape, mode: Optional[int] = 0, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> IFSelect_ReturnStatus: ...
    def WS(self) -> XSControl_WorkSession: ...
    def WriteFile(self, filename: str) -> IFSelect_ReturnStatus: ...

# harray1 classes
# harray2 classes
# hsequence classes

