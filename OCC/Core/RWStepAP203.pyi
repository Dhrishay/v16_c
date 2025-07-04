from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepAP203 import *


class RWStepAP203_RWCcDesignApproval:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_CcDesignApproval) -> None: ...
    def Share(self, ent: StepAP203_CcDesignApproval, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_CcDesignApproval) -> None: ...

class RWStepAP203_RWCcDesignCertification:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_CcDesignCertification) -> None: ...
    def Share(self, ent: StepAP203_CcDesignCertification, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_CcDesignCertification) -> None: ...

class RWStepAP203_RWCcDesignContract:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_CcDesignContract) -> None: ...
    def Share(self, ent: StepAP203_CcDesignContract, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_CcDesignContract) -> None: ...

class RWStepAP203_RWCcDesignDateAndTimeAssignment:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_CcDesignDateAndTimeAssignment) -> None: ...
    def Share(self, ent: StepAP203_CcDesignDateAndTimeAssignment, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_CcDesignDateAndTimeAssignment) -> None: ...

class RWStepAP203_RWCcDesignPersonAndOrganizationAssignment:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_CcDesignPersonAndOrganizationAssignment) -> None: ...
    def Share(self, ent: StepAP203_CcDesignPersonAndOrganizationAssignment, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_CcDesignPersonAndOrganizationAssignment) -> None: ...

class RWStepAP203_RWCcDesignSecurityClassification:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_CcDesignSecurityClassification) -> None: ...
    def Share(self, ent: StepAP203_CcDesignSecurityClassification, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_CcDesignSecurityClassification) -> None: ...

class RWStepAP203_RWCcDesignSpecificationReference:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_CcDesignSpecificationReference) -> None: ...
    def Share(self, ent: StepAP203_CcDesignSpecificationReference, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_CcDesignSpecificationReference) -> None: ...

class RWStepAP203_RWChange:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_Change) -> None: ...
    def Share(self, ent: StepAP203_Change, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_Change) -> None: ...

class RWStepAP203_RWChangeRequest:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_ChangeRequest) -> None: ...
    def Share(self, ent: StepAP203_ChangeRequest, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_ChangeRequest) -> None: ...

class RWStepAP203_RWStartRequest:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_StartRequest) -> None: ...
    def Share(self, ent: StepAP203_StartRequest, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_StartRequest) -> None: ...

class RWStepAP203_RWStartWork:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP203_StartWork) -> None: ...
    def Share(self, ent: StepAP203_StartWork, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepAP203_StartWork) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

