from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.TDF import *
from OCC.Core.TopTools import *
from OCC.Core.TopLoc import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.TColStd import *
from OCC.Core.TopAbs import *

# the following typedef cannot be wrapped as is
TNaming_DataMapIteratorOfDataMapOfShapeMapOfShape = NewType("TNaming_DataMapIteratorOfDataMapOfShapeMapOfShape", Any)
# the following typedef cannot be wrapped as is
TNaming_MapIteratorOfMapOfNamedShape = NewType("TNaming_MapIteratorOfMapOfNamedShape", Any)
# the following typedef cannot be wrapped as is
TNaming_MapIteratorOfMapOfShape = NewType("TNaming_MapIteratorOfMapOfShape", Any)
# the following typedef cannot be wrapped as is
TNaming_MapOfNamedShape = NewType("TNaming_MapOfNamedShape", Any)
# the following typedef cannot be wrapped as is
TNaming_MapOfShape = NewType("TNaming_MapOfShape", Any)
TNaming_PtrAttribute = NewType("TNaming_PtrAttribute", TNaming_NamedShape)
TNaming_PtrNode = NewType("TNaming_PtrNode", TNaming_Node)
TNaming_PtrRefShape = NewType("TNaming_PtrRefShape", TNaming_RefShape)

class TNaming_ListOfIndexedDataMapOfShapeListOfShape:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> TopTools_IndexedDataMapOfShapeListOfShape: ...
    def Last(self) -> TopTools_IndexedDataMapOfShapeListOfShape: ...
    def Append(self, theItem: TopTools_IndexedDataMapOfShapeListOfShape) -> TopTools_IndexedDataMapOfShapeListOfShape: ...
    def Prepend(self, theItem: TopTools_IndexedDataMapOfShapeListOfShape) -> TopTools_IndexedDataMapOfShapeListOfShape: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> TopTools_IndexedDataMapOfShapeListOfShape: ...
    def SetValue(self, theIndex: int, theValue: TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...

class TNaming_ListOfMapOfShape:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> TopTools_MapOfShape: ...
    def Last(self) -> TopTools_MapOfShape: ...
    def Append(self, theItem: TopTools_MapOfShape) -> TopTools_MapOfShape: ...
    def Prepend(self, theItem: TopTools_MapOfShape) -> TopTools_MapOfShape: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> TopTools_MapOfShape: ...
    def SetValue(self, theIndex: int, theValue: TopTools_MapOfShape) -> None: ...

class TNaming_ListOfNamedShape:
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

class TNaming_Evolution(IntEnum):
    TNaming_PRIMITIVE: int = ...
    TNaming_GENERATED: int = ...
    TNaming_MODIFY: int = ...
    TNaming_DELETE: int = ...
    TNaming_REPLACE: int = ...
    TNaming_SELECTED: int = ...

TNaming_PRIMITIVE = TNaming_Evolution.TNaming_PRIMITIVE
TNaming_GENERATED = TNaming_Evolution.TNaming_GENERATED
TNaming_MODIFY = TNaming_Evolution.TNaming_MODIFY
TNaming_DELETE = TNaming_Evolution.TNaming_DELETE
TNaming_REPLACE = TNaming_Evolution.TNaming_REPLACE
TNaming_SELECTED = TNaming_Evolution.TNaming_SELECTED

class TNaming_NameType(IntEnum):
    TNaming_UNKNOWN: int = ...
    TNaming_IDENTITY: int = ...
    TNaming_MODIFUNTIL: int = ...
    TNaming_GENERATION: int = ...
    TNaming_INTERSECTION: int = ...
    TNaming_UNION: int = ...
    TNaming_SUBSTRACTION: int = ...
    TNaming_CONSTSHAPE: int = ...
    TNaming_FILTERBYNEIGHBOURGS: int = ...
    TNaming_ORIENTATION: int = ...
    TNaming_WIREIN: int = ...
    TNaming_SHELLIN: int = ...

TNaming_UNKNOWN = TNaming_NameType.TNaming_UNKNOWN
TNaming_IDENTITY = TNaming_NameType.TNaming_IDENTITY
TNaming_MODIFUNTIL = TNaming_NameType.TNaming_MODIFUNTIL
TNaming_GENERATION = TNaming_NameType.TNaming_GENERATION
TNaming_INTERSECTION = TNaming_NameType.TNaming_INTERSECTION
TNaming_UNION = TNaming_NameType.TNaming_UNION
TNaming_SUBSTRACTION = TNaming_NameType.TNaming_SUBSTRACTION
TNaming_CONSTSHAPE = TNaming_NameType.TNaming_CONSTSHAPE
TNaming_FILTERBYNEIGHBOURGS = TNaming_NameType.TNaming_FILTERBYNEIGHBOURGS
TNaming_ORIENTATION = TNaming_NameType.TNaming_ORIENTATION
TNaming_WIREIN = TNaming_NameType.TNaming_WIREIN
TNaming_SHELLIN = TNaming_NameType.TNaming_SHELLIN

class tnaming:
    @staticmethod
    def ChangeShapes(label: TDF_Label, M: TopTools_DataMapOfShapeShape) -> None: ...
    @staticmethod
    def Displace(label: TDF_Label, aLocation: TopLoc_Location, WithOld: Optional[bool] = True) -> None: ...
    @staticmethod
    def FindUniqueContext(S: TopoDS_Shape, Context: TopoDS_Shape) -> TopoDS_Shape: ...
    @staticmethod
    def FindUniqueContextSet(S: TopoDS_Shape, Context: TopoDS_Shape, Arr: TopTools_HArray1OfShape) -> TopoDS_Shape: ...
    @staticmethod
    def IDList(anIDList: TDF_IDList) -> None: ...
    @staticmethod
    def MakeShape(MS: TopTools_MapOfShape) -> TopoDS_Shape: ...
    @staticmethod
    def OuterShell(theSolid: TopoDS_Solid, theShell: TopoDS_Shell) -> bool: ...
    @staticmethod
    def OuterWire(theFace: TopoDS_Face, theWire: TopoDS_Wire) -> bool: ...
    @overload
    @staticmethod
    def Print(EVOL: TNaming_Evolution) -> Tuple[Standard_OStream, str]: ...
    @overload
    @staticmethod
    def Print(NAME: TNaming_NameType) -> Tuple[Standard_OStream, str]: ...
    @overload
    @staticmethod
    def Print(ACCESS: TDF_Label) -> Tuple[Standard_OStream, str]: ...
    @overload
    @staticmethod
    def Replicate(NS: TNaming_NamedShape, T: gp_Trsf, L: TDF_Label) -> None: ...
    @overload
    @staticmethod
    def Replicate(SH: TopoDS_Shape, T: gp_Trsf, L: TDF_Label) -> None: ...
    @staticmethod
    def Substitute(labelsource: TDF_Label, labelcible: TDF_Label, mapOldNew: TopTools_DataMapOfShapeShape) -> None: ...
    @staticmethod
    def SubstituteSShape(accesslabel: TDF_Label, From: TopoDS_Shape, To: TopoDS_Shape) -> bool: ...
    @staticmethod
    def Transform(label: TDF_Label, aTransformation: gp_Trsf) -> None: ...
    @staticmethod
    def Update(label: TDF_Label, mapOldNew: TopTools_DataMapOfShapeShape) -> None: ...

class TNaming_Builder:
    def __init__(self, aLabel: TDF_Label) -> None: ...
    def Delete(self, oldShape: TopoDS_Shape) -> None: ...
    @overload
    def Generated(self, newShape: TopoDS_Shape) -> None: ...
    @overload
    def Generated(self, oldShape: TopoDS_Shape, newShape: TopoDS_Shape) -> None: ...
    def Modify(self, oldShape: TopoDS_Shape, newShape: TopoDS_Shape) -> None: ...
    def NamedShape(self) -> TNaming_NamedShape: ...
    def Select(self, aShape: TopoDS_Shape, inShape: TopoDS_Shape) -> None: ...

class TNaming_CopyShape:
    @staticmethod
    def CopyTool(aShape: TopoDS_Shape, aMap: TColStd_IndexedDataMapOfTransientTransient, aResult: TopoDS_Shape) -> None: ...
    @overload
    @staticmethod
    def Translate(aShape: TopoDS_Shape, aMap: TColStd_IndexedDataMapOfTransientTransient, aResult: TopoDS_Shape, TrTool: TNaming_TranslateTool) -> None: ...
    @overload
    @staticmethod
    def Translate(L: TopLoc_Location, aMap: TColStd_IndexedDataMapOfTransientTransient) -> TopLoc_Location: ...

class TNaming_DeltaOnModification(TDF_DeltaOnModification):
    def __init__(self, NS: TNaming_NamedShape) -> None: ...
    def Apply(self) -> None: ...

class TNaming_DeltaOnRemoval(TDF_DeltaOnRemoval):
    def __init__(self, NS: TNaming_NamedShape) -> None: ...
    def Apply(self) -> None: ...

class TNaming_Identifier:
    @overload
    def __init__(self, Lab: TDF_Label, S: TopoDS_Shape, Context: TopoDS_Shape, Geom: bool) -> None: ...
    @overload
    def __init__(self, Lab: TDF_Label, S: TopoDS_Shape, ContextNS: TNaming_NamedShape, Geom: bool) -> None: ...
    def AncestorIdentification(self, Localizer: TNaming_Localizer, Context: TopoDS_Shape) -> None: ...
    def ArgIsFeature(self) -> bool: ...
    def Feature(self) -> TNaming_NamedShape: ...
    def FeatureArg(self) -> TNaming_NamedShape: ...
    def GeneratedIdentification(self, Localizer: TNaming_Localizer, NS: TNaming_NamedShape) -> None: ...
    def Identification(self, Localizer: TNaming_Localizer, NS: TNaming_NamedShape) -> None: ...
    def InitArgs(self) -> None: ...
    def IsDone(self) -> bool: ...
    def IsFeature(self) -> bool: ...
    def MoreArgs(self) -> bool: ...
    def NamedShapeOfGeneration(self) -> TNaming_NamedShape: ...
    def NextArg(self) -> None: ...
    def PrimitiveIdentification(self, Localizer: TNaming_Localizer, NS: TNaming_NamedShape) -> None: ...
    def ShapeArg(self) -> TopoDS_Shape: ...
    def ShapeContext(self) -> TopoDS_Shape: ...
    def Type(self) -> TNaming_NameType: ...

class TNaming_Iterator:
    @overload
    def __init__(self, anAtt: TNaming_NamedShape) -> None: ...
    @overload
    def __init__(self, aLabel: TDF_Label) -> None: ...
    @overload
    def __init__(self, aLabel: TDF_Label, aTrans: int) -> None: ...
    def Evolution(self) -> TNaming_Evolution: ...
    def IsModification(self) -> bool: ...
    def More(self) -> bool: ...
    def NewShape(self) -> TopoDS_Shape: ...
    def Next(self) -> None: ...
    def OldShape(self) -> TopoDS_Shape: ...

class TNaming_IteratorOnShapesSet:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TNaming_ShapesSet) -> None: ...
    def Init(self, S: TNaming_ShapesSet) -> None: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def Value(self) -> TopoDS_Shape: ...

class TNaming_Localizer:
    def __init__(self) -> None: ...
    def Ancestors(self, S: TopoDS_Shape, Type: TopAbs_ShapeEnum) -> TopTools_IndexedDataMapOfShapeListOfShape: ...
    def Backward(self, NS: TNaming_NamedShape, S: TopoDS_Shape, Primitives: TNaming_MapOfNamedShape, ValidShapes: TopTools_MapOfShape) -> None: ...
    def FindFeaturesInAncestors(self, S: TopoDS_Shape, In: TopoDS_Shape, AncInFeatures: TopTools_MapOfShape) -> None: ...
    @staticmethod
    def FindGenerator(NS: TNaming_NamedShape, S: TopoDS_Shape, theListOfGenerators: TopTools_ListOfShape) -> None: ...
    def FindNeighbourg(self, Cont: TopoDS_Shape, S: TopoDS_Shape, Neighbourg: TopTools_MapOfShape) -> None: ...
    @staticmethod
    def FindShapeContext(NS: TNaming_NamedShape, theS: TopoDS_Shape, theSC: TopoDS_Shape) -> None: ...
    def GoBack(self, S: TopoDS_Shape, Lab: TDF_Label, Evol: TNaming_Evolution, OldS: TopTools_ListOfShape, OldLab: TNaming_ListOfNamedShape) -> None: ...
    def Init(self, US: TNaming_UsedShapes, CurTrans: int) -> None: ...
    @staticmethod
    def IsNew(S: TopoDS_Shape, NS: TNaming_NamedShape) -> bool: ...
    def SubShapes(self, S: TopoDS_Shape, Type: TopAbs_ShapeEnum) -> TopTools_MapOfShape: ...

class TNaming_Name:
    def __init__(self) -> None: ...
    def Append(self, arg: TNaming_NamedShape) -> None: ...
    def Arguments(self) -> TNaming_ListOfNamedShape: ...
    @overload
    def ContextLabel(self, theLab: TDF_Label) -> None: ...
    @overload
    def ContextLabel(self) -> TDF_Label: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    @overload
    def Index(self, I: int) -> None: ...
    @overload
    def Index(self) -> int: ...
    @overload
    def Orientation(self, theOrientation: TopAbs_Orientation) -> None: ...
    @overload
    def Orientation(self) -> TopAbs_Orientation: ...
    def Paste(self, into: TNaming_Name, RT: TDF_RelocationTable) -> None: ...
    @overload
    def Shape(self, theShape: TopoDS_Shape) -> None: ...
    @overload
    def Shape(self) -> TopoDS_Shape: ...
    @overload
    def ShapeType(self, aType: TopAbs_ShapeEnum) -> None: ...
    @overload
    def ShapeType(self) -> TopAbs_ShapeEnum: ...
    def Solve(self, aLab: TDF_Label, Valid: TDF_LabelMap) -> bool: ...
    @overload
    def StopNamedShape(self, arg: TNaming_NamedShape) -> None: ...
    @overload
    def StopNamedShape(self) -> TNaming_NamedShape: ...
    @overload
    def Type(self, aType: TNaming_NameType) -> None: ...
    @overload
    def Type(self) -> TNaming_NameType: ...

class TNaming_NamedShape(TDF_Attribute):
    def __init__(self) -> None: ...
    def AfterUndo(self, anAttDelta: TDF_AttributeDelta, forceIt: Optional[bool] = False) -> bool: ...
    def BackupCopy(self) -> TDF_Attribute: ...
    def BeforeRemoval(self) -> None: ...
    def BeforeUndo(self, anAttDelta: TDF_AttributeDelta, forceIt: Optional[bool] = False) -> bool: ...
    def Clear(self) -> None: ...
    @overload
    def DeltaOnModification(self, anOldAttribute: TDF_Attribute) -> TDF_DeltaOnModification: ...
    @overload
    def DeltaOnModification(self, aDelta: TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> TDF_DeltaOnRemoval: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def Evolution(self) -> TNaming_Evolution: ...
    def Get(self) -> TopoDS_Shape: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def IsEmpty(self) -> bool: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, intoAttribute: TDF_Attribute, aRelocTationable: TDF_RelocationTable) -> None: ...
    def References(self, aDataSet: TDF_DataSet) -> None: ...
    def Restore(self, anAttribute: TDF_Attribute) -> None: ...
    def SetVersion(self, version: int) -> None: ...
    def Version(self) -> int: ...

class TNaming_Naming(TDF_Attribute):
    def __init__(self) -> None: ...
    def ChangeName(self) -> TNaming_Name: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    def ExtendedDump(self, aFilter: TDF_IDFilter, aMap: TDF_AttributeIndexedMap) -> str: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def GetName(self) -> TNaming_Name: ...
    def ID(self) -> Standard_GUID: ...
    @staticmethod
    def Insert(under: TDF_Label) -> TNaming_Naming: ...
    def IsDefined(self) -> bool: ...
    @staticmethod
    def Name(where: TDF_Label, Selection: TopoDS_Shape, Context: TopoDS_Shape, Geometry: Optional[bool] = False, KeepOrientation: Optional[bool] = False, BNproblem: Optional[bool] = False) -> TNaming_NamedShape: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
    def References(self, aDataSet: TDF_DataSet) -> None: ...
    def Regenerate(self, scope: TDF_LabelMap) -> bool: ...
    def Restore(self, With: TDF_Attribute) -> None: ...
    def Solve(self, scope: TDF_LabelMap) -> bool: ...

class TNaming_NamingTool:
    @staticmethod
    def BuildDescendants(NS: TNaming_NamedShape, Labels: TDF_LabelMap) -> None: ...
    @staticmethod
    def CurrentShape(Valid: TDF_LabelMap, Forbiden: TDF_LabelMap, NS: TNaming_NamedShape, MS: TopTools_IndexedMapOfShape) -> None: ...
    @staticmethod
    def CurrentShapeFromShape(Valid: TDF_LabelMap, Forbiden: TDF_LabelMap, Acces: TDF_Label, S: TopoDS_Shape, MS: TopTools_IndexedMapOfShape) -> None: ...

class TNaming_NewShapeIterator:
    @overload
    def __init__(self, aShape: TopoDS_Shape, Transaction: int, access: TDF_Label) -> None: ...
    @overload
    def __init__(self, aShape: TopoDS_Shape, access: TDF_Label) -> None: ...
    @overload
    def __init__(self, anIterator: TNaming_NewShapeIterator) -> None: ...
    @overload
    def __init__(self, anIterator: TNaming_Iterator) -> None: ...
    def IsModification(self) -> bool: ...
    def Label(self) -> TDF_Label: ...
    def More(self) -> bool: ...
    def NamedShape(self) -> TNaming_NamedShape: ...
    def Next(self) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...

class TNaming_OldShapeIterator:
    @overload
    def __init__(self, aShape: TopoDS_Shape, Transaction: int, access: TDF_Label) -> None: ...
    @overload
    def __init__(self, aShape: TopoDS_Shape, access: TDF_Label) -> None: ...
    @overload
    def __init__(self, anIterator: TNaming_OldShapeIterator) -> None: ...
    @overload
    def __init__(self, anIterator: TNaming_Iterator) -> None: ...
    def IsModification(self) -> bool: ...
    def Label(self) -> TDF_Label: ...
    def More(self) -> bool: ...
    def NamedShape(self) -> TNaming_NamedShape: ...
    def Next(self) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...

class TNaming_RefShape:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shape) -> None: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    @overload
    def FirstUse(self, aPtr: TNaming_PtrNode) -> None: ...
    @overload
    def FirstUse(self) -> TNaming_PtrNode: ...
    def Label(self) -> TDF_Label: ...
    def NamedShape(self) -> TNaming_NamedShape: ...
    @overload
    def Shape(self, S: TopoDS_Shape) -> None: ...
    @overload
    def Shape(self) -> TopoDS_Shape: ...

class TNaming_SameShapeIterator:
    def __init__(self, aShape: TopoDS_Shape, access: TDF_Label) -> None: ...
    def Label(self) -> TDF_Label: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...

class TNaming_Scope:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, WithValid: bool) -> None: ...
    @overload
    def __init__(self, valid: TDF_LabelMap) -> None: ...
    def ChangeValid(self) -> TDF_LabelMap: ...
    def ClearValid(self) -> None: ...
    def CurrentShape(self, NS: TNaming_NamedShape) -> TopoDS_Shape: ...
    def GetValid(self) -> TDF_LabelMap: ...
    def IsValid(self, L: TDF_Label) -> bool: ...
    def Unvalid(self, L: TDF_Label) -> None: ...
    def UnvalidChildren(self, L: TDF_Label, withroot: Optional[bool] = True) -> None: ...
    def Valid(self, L: TDF_Label) -> None: ...
    def ValidChildren(self, L: TDF_Label, withroot: Optional[bool] = True) -> None: ...
    @overload
    def WithValid(self) -> bool: ...
    @overload
    def WithValid(self, mode: bool) -> None: ...

class TNaming_Selector:
    def __init__(self, aLabel: TDF_Label) -> None: ...
    def Arguments(self, args: TDF_AttributeMap) -> None: ...
    @staticmethod
    def IsIdentified(access: TDF_Label, selection: TopoDS_Shape, NS: TNaming_NamedShape, Geometry: Optional[bool] = False) -> bool: ...
    def NamedShape(self) -> TNaming_NamedShape: ...
    @overload
    def Select(self, Selection: TopoDS_Shape, Context: TopoDS_Shape, Geometry: Optional[bool] = False, KeepOrientatation: Optional[bool] = False) -> bool: ...
    @overload
    def Select(self, Selection: TopoDS_Shape, Geometry: Optional[bool] = False, KeepOrientatation: Optional[bool] = False) -> bool: ...
    def Solve(self, Valid: TDF_LabelMap) -> bool: ...

class TNaming_ShapesSet:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shape, Type: Optional[TopAbs_ShapeEnum] = TopAbs_SHAPE) -> None: ...
    @overload
    def Add(self, S: TopoDS_Shape) -> bool: ...
    @overload
    def Add(self, Shapes: TNaming_ShapesSet) -> None: ...
    def ChangeMap(self) -> TopTools_MapOfShape: ...
    def Clear(self) -> None: ...
    def Contains(self, S: TopoDS_Shape) -> bool: ...
    def Filter(self, Shapes: TNaming_ShapesSet) -> None: ...
    def IsEmpty(self) -> bool: ...
    def Map(self) -> TopTools_MapOfShape: ...
    def NbShapes(self) -> int: ...
    @overload
    def Remove(self, S: TopoDS_Shape) -> bool: ...
    @overload
    def Remove(self, Shapes: TNaming_ShapesSet) -> None: ...

class TNaming_Tool:
    @staticmethod
    def Collect(NS: TNaming_NamedShape, Labels: TNaming_MapOfNamedShape, OnlyModif: Optional[bool] = True) -> None: ...
    @overload
    @staticmethod
    def CurrentNamedShape(NS: TNaming_NamedShape, Updated: TDF_LabelMap) -> TNaming_NamedShape: ...
    @overload
    @staticmethod
    def CurrentNamedShape(NS: TNaming_NamedShape) -> TNaming_NamedShape: ...
    @overload
    @staticmethod
    def CurrentShape(NS: TNaming_NamedShape) -> TopoDS_Shape: ...
    @overload
    @staticmethod
    def CurrentShape(NS: TNaming_NamedShape, Updated: TDF_LabelMap) -> TopoDS_Shape: ...
    @staticmethod
    def FindShape(Valid: TDF_LabelMap, Forbiden: TDF_LabelMap, Arg: TNaming_NamedShape, S: TopoDS_Shape) -> None: ...
    @staticmethod
    def GeneratedShape(S: TopoDS_Shape, Generation: TNaming_NamedShape) -> TopoDS_Shape: ...
    @staticmethod
    def GetShape(NS: TNaming_NamedShape) -> TopoDS_Shape: ...
    @staticmethod
    def HasLabel(access: TDF_Label, aShape: TopoDS_Shape) -> bool: ...
    @staticmethod
    def InitialShape(aShape: TopoDS_Shape, anAcces: TDF_Label, Labels: TDF_LabelList) -> TopoDS_Shape: ...
    @staticmethod
    def Label(access: TDF_Label, aShape: TopoDS_Shape) -> Tuple[TDF_Label, int]: ...
    @staticmethod
    def NamedShape(aShape: TopoDS_Shape, anAcces: TDF_Label) -> TNaming_NamedShape: ...
    @staticmethod
    def OriginalShape(NS: TNaming_NamedShape) -> TopoDS_Shape: ...
    @staticmethod
    def ValidUntil(access: TDF_Label, S: TopoDS_Shape) -> int: ...

class TNaming_TranslateTool(Standard_Transient):
    def Add(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
    def MakeCompSolid(self, S: TopoDS_Shape) -> None: ...
    def MakeCompound(self, S: TopoDS_Shape) -> None: ...
    def MakeEdge(self, S: TopoDS_Shape) -> None: ...
    def MakeFace(self, S: TopoDS_Shape) -> None: ...
    def MakeShell(self, S: TopoDS_Shape) -> None: ...
    def MakeSolid(self, S: TopoDS_Shape) -> None: ...
    def MakeVertex(self, S: TopoDS_Shape) -> None: ...
    def MakeWire(self, S: TopoDS_Shape) -> None: ...
    def UpdateEdge(self, S1: TopoDS_Shape, S2: TopoDS_Shape, M: TColStd_IndexedDataMapOfTransientTransient) -> None: ...
    def UpdateFace(self, S1: TopoDS_Shape, S2: TopoDS_Shape, M: TColStd_IndexedDataMapOfTransientTransient) -> None: ...
    def UpdateShape(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
    def UpdateVertex(self, S1: TopoDS_Shape, S2: TopoDS_Shape, M: TColStd_IndexedDataMapOfTransientTransient) -> None: ...

class TNaming_Translator:
    def __init__(self) -> None: ...
    def Add(self, aShape: TopoDS_Shape) -> None: ...
    @overload
    def Copied(self, aShape: TopoDS_Shape) -> TopoDS_Shape: ...
    @overload
    def Copied(self) -> TopTools_DataMapOfShapeShape: ...
    def DumpMap(self, isWrite: Optional[bool] = False) -> None: ...
    def IsDone(self) -> bool: ...
    def Perform(self) -> None: ...

class TNaming_UsedShapes(TDF_Attribute):
    def AfterUndo(self, anAttDelta: TDF_AttributeDelta, forceIt: Optional[bool] = False) -> bool: ...
    def BackupCopy(self) -> TDF_Attribute: ...
    def BeforeRemoval(self) -> None: ...
    def DeltaOnAddition(self) -> TDF_DeltaOnAddition: ...
    def DeltaOnRemoval(self) -> TDF_DeltaOnRemoval: ...
    def Destroy(self) -> None: ...
    def Dump(self) -> Tuple[Standard_OStream, str]: ...
    def DumpJson(self, depth: Optional[int]=-1) -> str: ...
    @staticmethod
    def GetID() -> Standard_GUID: ...
    def ID(self) -> Standard_GUID: ...
    def Map(self) -> TNaming_DataMapOfShapePtrRefShape: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    def Paste(self, intoAttribute: TDF_Attribute, aRelocTationable: TDF_RelocationTable) -> None: ...
    def References(self, aDataSet: TDF_DataSet) -> None: ...
    def Restore(self, anAttribute: TDF_Attribute) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

