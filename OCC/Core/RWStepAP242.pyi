from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepAP242 import *


class RWStepAP242_RWDraughtingModelItemAssociation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP242_DraughtingModelItemAssociation) -> None: ...
    def Share(self, ent: StepAP242_DraughtingModelItemAssociation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP242_DraughtingModelItemAssociation) -> None: ...

class RWStepAP242_RWGeometricItemSpecificUsage:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP242_GeometricItemSpecificUsage) -> None: ...
    def Share(self, ent: StepAP242_GeometricItemSpecificUsage, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP242_GeometricItemSpecificUsage) -> None: ...

class RWStepAP242_RWIdAttribute:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP242_IdAttribute) -> None: ...
    def Share(self, ent: StepAP242_IdAttribute, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP242_IdAttribute) -> None: ...

class RWStepAP242_RWItemIdentifiedRepresentationUsage:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP242_ItemIdentifiedRepresentationUsage) -> None: ...
    def Share(self, ent: StepAP242_ItemIdentifiedRepresentationUsage, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP242_ItemIdentifiedRepresentationUsage) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

