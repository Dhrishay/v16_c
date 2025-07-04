from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.Message import *
from OCC.Core.Interface import *
from OCC.Core.TColStd import *

# the following typedef cannot be wrapped as is
Transfer_TransferMapOfProcessForFinder = NewType("Transfer_TransferMapOfProcessForFinder", Any)
# the following typedef cannot be wrapped as is
Transfer_TransferMapOfProcessForTransient = NewType("Transfer_TransferMapOfProcessForTransient", Any)

class Transfer_SequenceOfBinder:
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

class Transfer_SequenceOfFinder:
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

class Transfer_StatusExec(IntEnum):
    Transfer_StatusInitial: int = ...
    Transfer_StatusRun: int = ...
    Transfer_StatusDone: int = ...
    Transfer_StatusError: int = ...
    Transfer_StatusLoop: int = ...

Transfer_StatusInitial = Transfer_StatusExec.Transfer_StatusInitial
Transfer_StatusRun = Transfer_StatusExec.Transfer_StatusRun
Transfer_StatusDone = Transfer_StatusExec.Transfer_StatusDone
Transfer_StatusError = Transfer_StatusExec.Transfer_StatusError
Transfer_StatusLoop = Transfer_StatusExec.Transfer_StatusLoop

class Transfer_StatusResult(IntEnum):
    Transfer_StatusVoid: int = ...
    Transfer_StatusDefined: int = ...
    Transfer_StatusUsed: int = ...

Transfer_StatusVoid = Transfer_StatusResult.Transfer_StatusVoid
Transfer_StatusDefined = Transfer_StatusResult.Transfer_StatusDefined
Transfer_StatusUsed = Transfer_StatusResult.Transfer_StatusUsed

class Transfer_UndefMode(IntEnum):
    Transfer_UndefIgnore: int = ...
    Transfer_UndefFailure: int = ...
    Transfer_UndefContent: int = ...
    Transfer_UndefUser: int = ...

Transfer_UndefIgnore = Transfer_UndefMode.Transfer_UndefIgnore
Transfer_UndefFailure = Transfer_UndefMode.Transfer_UndefFailure
Transfer_UndefContent = Transfer_UndefMode.Transfer_UndefContent
Transfer_UndefUser = Transfer_UndefMode.Transfer_UndefUser

class Transfer_ActorOfProcessForFinder(Standard_Transient):
    def __init__(self) -> None: ...
    def IsLast(self) -> bool: ...
    def Next(self) -> Transfer_ActorOfProcessForFinder: ...
    def NullResult(self) -> Transfer_Binder: ...
    def Recognize(self, start: Transfer_Finder) -> bool: ...
    def SetLast(self, mode: Optional[bool] = True) -> None: ...
    def SetNext(self, next: Transfer_ActorOfProcessForFinder) -> None: ...
    def Transferring(self, start: Transfer_Finder, TP: Transfer_ProcessForFinder, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> Transfer_Binder: ...
    def TransientResult(self, res: Standard_Transient) -> Transfer_SimpleBinderOfTransient: ...

class Transfer_ActorOfProcessForTransient(Standard_Transient):
    def __init__(self) -> None: ...
    def IsLast(self) -> bool: ...
    def Next(self) -> Transfer_ActorOfProcessForTransient: ...
    def NullResult(self) -> Transfer_Binder: ...
    def Recognize(self, start: Standard_Transient) -> bool: ...
    def SetLast(self, mode: Optional[bool] = True) -> None: ...
    def SetNext(self, next: Transfer_ActorOfProcessForTransient) -> None: ...
    def Transferring(self, start: Standard_Transient, TP: Transfer_ProcessForTransient, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> Transfer_Binder: ...
    def TransientResult(self, res: Standard_Transient) -> Transfer_SimpleBinderOfTransient: ...

class Transfer_Binder(Standard_Transient):
    def AddFail(self, mess: str, orig: Optional[str] = "") -> None: ...
    def AddResult(self, next: Transfer_Binder) -> None: ...
    def AddWarning(self, mess: str, orig: Optional[str] = "") -> None: ...
    def CCheck(self) -> Interface_Check: ...
    def Check(self) -> Interface_Check: ...
    def HasResult(self) -> bool: ...
    def IsMultiple(self) -> bool: ...
    def Merge(self, other: Transfer_Binder) -> None: ...
    def NextResult(self) -> Transfer_Binder: ...
    def ResultType(self) -> Standard_Type: ...
    def ResultTypeName(self) -> str: ...
    def SetAlreadyUsed(self) -> None: ...
    def SetStatusExec(self, stat: Transfer_StatusExec) -> None: ...
    def Status(self) -> Transfer_StatusResult: ...
    def StatusExec(self) -> Transfer_StatusExec: ...

class Transfer_DataInfo:
    @staticmethod
    def Type(ent: Standard_Transient) -> Standard_Type: ...
    @staticmethod
    def TypeName(ent: Standard_Transient) -> str: ...

class Transfer_DispatchControl(Interface_CopyControl):
    def __init__(self, model: Interface_InterfaceModel, TP: Transfer_TransientProcess) -> None: ...
    def Bind(self, ent: Standard_Transient, res: Standard_Transient) -> None: ...
    def Clear(self) -> None: ...
    def Search(self, ent: Standard_Transient, res: Standard_Transient) -> bool: ...
    def StartingModel(self) -> Interface_InterfaceModel: ...
    def TransientProcess(self) -> Transfer_TransientProcess: ...

class Transfer_FindHasher:
    pass

class Transfer_Finder(Standard_Transient):
    def AttrList(self) -> False: ...
    def Attribute(self, name: str) -> Standard_Transient: ...
    def AttributeType(self, name: str) -> Interface_ParamType: ...
    def Equates(self, other: Transfer_Finder) -> bool: ...
    def GetAttribute(self, name: str, type: Standard_Type, val: Standard_Transient) -> bool: ...
    def GetAttributes(self, other: Transfer_Finder, fromname: Optional[str] = "", copied: Optional[bool] = True) -> None: ...
    def GetHashCode(self) -> False: ...
    def GetIntegerAttribute(self, name: str) -> Tuple[bool, int]: ...
    def GetRealAttribute(self, name: str) -> Tuple[bool, float]: ...
    def GetStringAttribute(self, name: str, val: str) -> bool: ...
    def IntegerAttribute(self, name: str) -> int: ...
    def RealAttribute(self, name: str) -> float: ...
    def RemoveAttribute(self, name: str) -> bool: ...
    def SameAttributes(self, other: Transfer_Finder) -> None: ...
    def SetAttribute(self, name: str, val: Standard_Transient) -> None: ...
    def SetIntegerAttribute(self, name: str, val: int) -> None: ...
    def SetRealAttribute(self, name: str, val: float) -> None: ...
    def SetStringAttribute(self, name: str, val: str) -> None: ...
    def StringAttribute(self, name: str) -> str: ...
    def ValueType(self) -> Standard_Type: ...
    def ValueTypeName(self) -> str: ...

class Transfer_MapContainer(Standard_Transient):
    def __init__(self) -> None: ...
    def GetMapObjects(self) -> TColStd_DataMapOfTransientTransient: ...
    def SetMapObjects(self, theMapObjects: TColStd_DataMapOfTransientTransient) -> None: ...

class Transfer_ProcessForTransient(Standard_Transient):
    @overload
    def __init__(self, nb: Optional[int] = 10000) -> None: ...
    @overload
    def __init__(self, printer: Message_Messenger, nb: Optional[int] = 10000) -> None: ...
    def AbnormalResult(self) -> Transfer_IteratorOfProcessForTransient: ...
    def Actor(self) -> Transfer_ActorOfProcessForTransient: ...
    def AddError(self, start: Standard_Transient, mess: str, orig: Optional[str] = "") -> None: ...
    @overload
    def AddFail(self, start: Standard_Transient, mess: str, orig: Optional[str] = "") -> None: ...
    @overload
    def AddFail(self, start: Standard_Transient, amsg: Message_Msg) -> None: ...
    def AddMultiple(self, start: Standard_Transient, res: Standard_Transient) -> None: ...
    @overload
    def AddWarning(self, start: Standard_Transient, mess: str, orig: Optional[str] = "") -> None: ...
    @overload
    def AddWarning(self, start: Standard_Transient, amsg: Message_Msg) -> None: ...
    def Bind(self, start: Standard_Transient, binder: Transfer_Binder) -> None: ...
    def BindMultiple(self, start: Standard_Transient) -> None: ...
    def BindTransient(self, start: Standard_Transient, res: Standard_Transient) -> None: ...
    def Check(self, start: Standard_Transient) -> Interface_Check: ...
    def CheckList(self, erronly: bool) -> Interface_CheckIterator: ...
    def CheckListOne(self, start: Standard_Transient, level: int, erronly: bool) -> Interface_CheckIterator: ...
    def CheckNum(self, start: Standard_Transient) -> int: ...
    def Clean(self) -> None: ...
    def Clear(self) -> None: ...
    def CompleteResult(self, withstart: Optional[bool] = False) -> Transfer_IteratorOfProcessForTransient: ...
    def ErrorHandle(self) -> bool: ...
    def Find(self, start: Standard_Transient) -> Transfer_Binder: ...
    def FindElseBind(self, start: Standard_Transient) -> Transfer_Binder: ...
    def FindTransient(self, start: Standard_Transient) -> Standard_Transient: ...
    def FindTypedTransient(self, start: Standard_Transient, atype: Standard_Type, val: Standard_Transient) -> bool: ...
    def GetTypedTransient(self, binder: Transfer_Binder, atype: Standard_Type, val: Standard_Transient) -> bool: ...
    def IsAlreadyUsed(self, start: Standard_Transient) -> bool: ...
    def IsBound(self, start: Standard_Transient) -> bool: ...
    def IsCheckListEmpty(self, start: Standard_Transient, level: int, erronly: bool) -> bool: ...
    def IsLooping(self, alevel: int) -> bool: ...
    def MapIndex(self, start: Standard_Transient) -> int: ...
    def MapItem(self, num: int) -> Transfer_Binder: ...
    def Mapped(self, num: int) -> Standard_Transient: ...
    def Mend(self, start: Standard_Transient, pref: Optional[str] = "") -> None: ...
    def Messenger(self) -> Message_Messenger: ...
    def NbMapped(self) -> int: ...
    def NbRoots(self) -> int: ...
    def NestingLevel(self) -> int: ...
    def PrintTrace(self, start: Standard_Transient) -> str: ...
    def Rebind(self, start: Standard_Transient, binder: Transfer_Binder) -> None: ...
    def Recognize(self, start: Standard_Transient) -> bool: ...
    def RemoveResult(self, start: Standard_Transient, level: int, compute: Optional[bool] = True) -> None: ...
    def ResetNestingLevel(self) -> None: ...
    def Resize(self, nb: int) -> None: ...
    def ResultOne(self, start: Standard_Transient, level: int, withstart: Optional[bool] = False) -> Transfer_IteratorOfProcessForTransient: ...
    def Root(self, num: int) -> Standard_Transient: ...
    def RootIndex(self, start: Standard_Transient) -> int: ...
    def RootItem(self, num: int) -> Transfer_Binder: ...
    def RootResult(self, withstart: Optional[bool] = False) -> Transfer_IteratorOfProcessForTransient: ...
    def SendFail(self, start: Standard_Transient, amsg: Message_Msg) -> None: ...
    def SendMsg(self, start: Standard_Transient, amsg: Message_Msg) -> None: ...
    def SendWarning(self, start: Standard_Transient, amsg: Message_Msg) -> None: ...
    def SetActor(self, actor: Transfer_ActorOfProcessForTransient) -> None: ...
    def SetErrorHandle(self, err: bool) -> None: ...
    def SetMessenger(self, messenger: Message_Messenger) -> None: ...
    def SetRoot(self, start: Standard_Transient) -> None: ...
    def SetRootManagement(self, stat: bool) -> None: ...
    def SetTraceLevel(self, tracelev: int) -> None: ...
    def StartTrace(self, binder: Transfer_Binder, start: Standard_Transient, level: int, mode: int) -> None: ...
    def TraceLevel(self) -> int: ...
    def Transfer(self, start: Standard_Transient, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    def Transferring(self, start: Standard_Transient, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> Transfer_Binder: ...
    def Unbind(self, start: Standard_Transient) -> bool: ...

class Transfer_ResultFromModel(Standard_Transient):
    def __init__(self) -> None: ...
    def CheckList(self, erronly: bool, level: Optional[int] = 2) -> Interface_CheckIterator: ...
    def CheckStatus(self) -> Interface_CheckStatus: ...
    def CheckedList(self, check: Interface_CheckStatus, result: bool) -> TColStd_HSequenceOfTransient: ...
    def ComputeCheckStatus(self, enforce: bool) -> Interface_CheckStatus: ...
    def FileName(self) -> str: ...
    def Fill(self, TP: Transfer_TransientProcess, ent: Standard_Transient) -> bool: ...
    def FillBack(self, TP: Transfer_TransientProcess) -> None: ...
    def HasResult(self) -> bool: ...
    def MainLabel(self) -> str: ...
    def MainNumber(self) -> int: ...
    def MainResult(self) -> Transfer_ResultFromTransient: ...
    def Model(self) -> Interface_InterfaceModel: ...
    def ResultFromKey(self, start: Standard_Transient) -> Transfer_ResultFromTransient: ...
    def Results(self, level: int) -> TColStd_HSequenceOfTransient: ...
    def SetFileName(self, filename: str) -> None: ...
    def SetMainResult(self, amain: Transfer_ResultFromTransient) -> None: ...
    def SetModel(self, model: Interface_InterfaceModel) -> None: ...
    def Strip(self, mode: int) -> None: ...
    def TransferredList(self, level: Optional[int] = 2) -> TColStd_HSequenceOfTransient: ...

class Transfer_ResultFromTransient(Standard_Transient):
    def __init__(self) -> None: ...
    def AddSubResult(self, sub: Transfer_ResultFromTransient) -> None: ...
    def Binder(self) -> Transfer_Binder: ...
    def Check(self) -> Interface_Check: ...
    def CheckStatus(self) -> Interface_CheckStatus: ...
    def ClearSubs(self) -> None: ...
    def Fill(self, TP: Transfer_TransientProcess) -> None: ...
    def FillBack(self, TP: Transfer_TransientProcess) -> None: ...
    def FillMap(self, map: TColStd_IndexedMapOfTransient) -> None: ...
    def HasResult(self) -> bool: ...
    def NbSubResults(self) -> int: ...
    def ResultFromKey(self, key: Standard_Transient) -> Transfer_ResultFromTransient: ...
    def SetBinder(self, binder: Transfer_Binder) -> None: ...
    def SetStart(self, start: Standard_Transient) -> None: ...
    def Start(self) -> Standard_Transient: ...
    def Strip(self) -> None: ...
    def SubResult(self, num: int) -> Transfer_ResultFromTransient: ...

class Transfer_TransferDispatch(Interface_CopyTool):
    @overload
    def __init__(self, amodel: Interface_InterfaceModel, lib: Interface_GeneralLib) -> None: ...
    @overload
    def __init__(self, amodel: Interface_InterfaceModel, protocol: Interface_Protocol) -> None: ...
    @overload
    def __init__(self, amodel: Interface_InterfaceModel) -> None: ...
    def Copy(self, entfrom: Standard_Transient, entto: Standard_Transient, mapped: bool, errstat: bool) -> bool: ...
    def TransientProcess(self) -> Transfer_TransientProcess: ...

class Transfer_TransferInput:
    def __init__(self) -> None: ...
    def Entities(self, list: Transfer_TransferIterator) -> Interface_EntityIterator: ...
    @overload
    def FillModel(self, proc: Transfer_TransientProcess, amodel: Interface_InterfaceModel) -> None: ...
    @overload
    def FillModel(self, proc: Transfer_TransientProcess, amodel: Interface_InterfaceModel, proto: Interface_Protocol, roots: Optional[bool] = True) -> None: ...
    @overload
    def FillModel(self, proc: Transfer_FinderProcess, amodel: Interface_InterfaceModel) -> None: ...
    @overload
    def FillModel(self, proc: Transfer_FinderProcess, amodel: Interface_InterfaceModel, proto: Interface_Protocol, roots: Optional[bool] = True) -> None: ...

class Transfer_TransferIterator:
    def __init__(self) -> None: ...
    def AddItem(self, atr: Transfer_Binder) -> None: ...
    def Check(self) -> Interface_Check: ...
    def HasFails(self) -> bool: ...
    def HasResult(self) -> bool: ...
    def HasTransientResult(self) -> bool: ...
    def HasUniqueResult(self) -> bool: ...
    def HasWarnings(self) -> bool: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def Number(self) -> int: ...
    def ResultType(self) -> Standard_Type: ...
    def SelectBinder(self, atype: Standard_Type, keep: bool) -> None: ...
    def SelectItem(self, num: int, keep: bool) -> None: ...
    def SelectResult(self, atype: Standard_Type, keep: bool) -> None: ...
    def SelectUnique(self, keep: bool) -> None: ...
    def Start(self) -> None: ...
    def Status(self) -> Transfer_StatusExec: ...
    def TransientResult(self) -> Standard_Transient: ...
    def Value(self) -> Transfer_Binder: ...

class Transfer_TransferOutput:
    @overload
    def __init__(self, actor: Transfer_ActorOfTransientProcess, amodel: Interface_InterfaceModel) -> None: ...
    @overload
    def __init__(self, proc: Transfer_TransientProcess, amodel: Interface_InterfaceModel) -> None: ...
    def ListForStatus(self, normal: bool, roots: Optional[bool] = True) -> Interface_EntityIterator: ...
    def Model(self) -> Interface_InterfaceModel: ...
    def ModelForStatus(self, protocol: Interface_Protocol, normal: bool, roots: Optional[bool] = True) -> Interface_InterfaceModel: ...
    def Transfer(self, obj: Standard_Transient, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def TransferRoots(self, protocol: Interface_Protocol, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def TransferRoots(self, G: Interface_Graph, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def TransferRoots(self, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def TransientProcess(self) -> Transfer_TransientProcess: ...

class Transfer_ActorOfFinderProcess(Transfer_ActorOfProcessForFinder):
    def __init__(self) -> None: ...
    def GetModeTrans(self) -> int: ...
    def SetModeTrans(self, value: int) -> None: ...
    def Transfer(self, start: Transfer_Finder, TP: Transfer_FinderProcess, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> Transfer_Binder: ...
    def TransferTransient(self, start: Standard_Transient, TP: Transfer_FinderProcess, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> Standard_Transient: ...
    def Transferring(self, start: Transfer_Finder, TP: Transfer_ProcessForFinder, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> Transfer_Binder: ...

class Transfer_ActorOfTransientProcess(Transfer_ActorOfProcessForTransient):
    def __init__(self) -> None: ...
    def Transfer(self, start: Standard_Transient, TP: Transfer_TransientProcess, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> Transfer_Binder: ...
    def TransferTransient(self, start: Standard_Transient, TP: Transfer_TransientProcess, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> Standard_Transient: ...
    def Transferring(self, start: Standard_Transient, TP: Transfer_ProcessForTransient, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> Transfer_Binder: ...

class Transfer_FinderProcess(Transfer_ProcessForFinder):
    def __init__(self, nb: Optional[int] = 10000) -> None: ...
    def Model(self) -> Interface_InterfaceModel: ...
    def NextMappedWithAttribute(self, name: str, num0: int) -> int: ...
    def PrintStats(self, mode: int) -> str: ...
    def PrintTrace(self, start: Transfer_Finder) -> str: ...
    def SetModel(self, model: Interface_InterfaceModel) -> None: ...
    def TransientMapper(self, obj: Standard_Transient) -> Transfer_TransientMapper: ...

class Transfer_IteratorOfProcessForFinder(Transfer_TransferIterator):
    def __init__(self, withstarts: bool) -> None: ...
    @overload
    def Add(self, binder: Transfer_Binder) -> None: ...
    @overload
    def Add(self, binder: Transfer_Binder, start: Transfer_Finder) -> None: ...
    def Filter(self, list: Transfer_HSequenceOfFinder, keep: Optional[bool] = True) -> None: ...
    def HasStarting(self) -> bool: ...
    def Starting(self) -> Transfer_Finder: ...

class Transfer_IteratorOfProcessForTransient(Transfer_TransferIterator):
    def __init__(self, withstarts: bool) -> None: ...
    @overload
    def Add(self, binder: Transfer_Binder) -> None: ...
    @overload
    def Add(self, binder: Transfer_Binder, start: Standard_Transient) -> None: ...
    def Filter(self, list: TColStd_HSequenceOfTransient, keep: Optional[bool] = True) -> None: ...
    def HasStarting(self) -> bool: ...
    def Starting(self) -> Standard_Transient: ...

class Transfer_MultipleBinder(Transfer_Binder):
    def __init__(self) -> None: ...
    def AddResult(self, res: Standard_Transient) -> None: ...
    def IsMultiple(self) -> bool: ...
    def MultipleResult(self) -> TColStd_HSequenceOfTransient: ...
    def NbResults(self) -> int: ...
    def ResultType(self) -> Standard_Type: ...
    def ResultTypeName(self) -> str: ...
    def ResultValue(self, num: int) -> Standard_Transient: ...
    def SetMultipleResult(self, mulres: TColStd_HSequenceOfTransient) -> None: ...

class Transfer_SimpleBinderOfTransient(Transfer_Binder):
    def __init__(self) -> None: ...
    @staticmethod
    def GetTypedResult(bnd: Transfer_Binder, atype: Standard_Type, res: Standard_Transient) -> bool: ...
    def Result(self) -> Standard_Transient: ...
    def ResultType(self) -> Standard_Type: ...
    def ResultTypeName(self) -> str: ...
    def SetResult(self, res: Standard_Transient) -> None: ...

class Transfer_TransientListBinder(Transfer_Binder):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, list: TColStd_HSequenceOfTransient) -> None: ...
    def AddResult(self, res: Standard_Transient) -> None: ...
    def IsMultiple(self) -> bool: ...
    def NbTransients(self) -> int: ...
    def Result(self) -> TColStd_HSequenceOfTransient: ...
    def ResultType(self) -> Standard_Type: ...
    def ResultTypeName(self) -> str: ...
    def SetResult(self, num: int, res: Standard_Transient) -> None: ...
    def Transient(self, num: int) -> Standard_Transient: ...

class Transfer_TransientMapper(Transfer_Finder):
    def __init__(self, akey: Standard_Transient) -> None: ...
    def Equates(self, other: Transfer_Finder) -> bool: ...
    def Value(self) -> Standard_Transient: ...
    def ValueType(self) -> Standard_Type: ...
    def ValueTypeName(self) -> str: ...

class Transfer_TransientProcess(Transfer_ProcessForTransient):
    def __init__(self, nb: Optional[int] = 10000) -> None: ...
    def CheckNum(self, ent: Standard_Transient) -> int: ...
    def Context(self) -> False: ...
    def GetContext(self, name: str, type: Standard_Type, ctx: Standard_Transient) -> bool: ...
    def Graph(self) -> Interface_Graph: ...
    def HGraph(self) -> Interface_HGraph: ...
    def HasGraph(self) -> bool: ...
    def IsDataFail(self, ent: Standard_Transient) -> bool: ...
    def IsDataLoaded(self, ent: Standard_Transient) -> bool: ...
    def Model(self) -> Interface_InterfaceModel: ...
    def PrintStats(self, mode: int) -> str: ...
    def PrintTrace(self, start: Standard_Transient) -> str: ...
    def RootsForTransfer(self) -> TColStd_HSequenceOfTransient: ...
    def SetContext(self, name: str, ctx: Standard_Transient) -> None: ...
    def SetGraph(self, HG: Interface_HGraph) -> None: ...
    def SetModel(self, model: Interface_InterfaceModel) -> None: ...
    def TypedSharings(self, start: Standard_Transient, type: Standard_Type) -> Interface_EntityIterator: ...

class Transfer_VoidBinder(Transfer_Binder):
    def __init__(self) -> None: ...
    def ResultType(self) -> Standard_Type: ...
    def ResultTypeName(self) -> str: ...

class Transfer_ActorDispatch(Transfer_ActorOfTransientProcess):
    @overload
    def __init__(self, amodel: Interface_InterfaceModel, lib: Interface_GeneralLib) -> None: ...
    @overload
    def __init__(self, amodel: Interface_InterfaceModel, protocol: Interface_Protocol) -> None: ...
    @overload
    def __init__(self, amodel: Interface_InterfaceModel) -> None: ...
    def AddActor(self, actor: Transfer_ActorOfTransientProcess) -> None: ...
    def Transfer(self, start: Standard_Transient, TP: Transfer_TransientProcess, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()) -> Transfer_Binder: ...
    def TransferDispatch(self) -> Transfer_TransferDispatch: ...

class Transfer_BinderOfTransientInteger(Transfer_SimpleBinderOfTransient):
    def __init__(self) -> None: ...
    def Integer(self) -> int: ...
    def SetInteger(self, value: int) -> None: ...

#classnotwrapped
class Transfer_ProcessForFinder: ...

# harray1 classes
# harray2 classes
# hsequence classes

class Transfer_HSequenceOfBinder(Transfer_SequenceOfBinder, Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: Transfer_SequenceOfBinder) -> None: ...
    def Sequence(self) -> Transfer_SequenceOfBinder: ...
    def Append(self, theSequence: Transfer_SequenceOfBinder) -> None: ...


class Transfer_HSequenceOfFinder(Transfer_SequenceOfFinder, Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: Transfer_SequenceOfFinder) -> None: ...
    def Sequence(self) -> Transfer_SequenceOfFinder: ...
    def Append(self, theSequence: Transfer_SequenceOfFinder) -> None: ...


