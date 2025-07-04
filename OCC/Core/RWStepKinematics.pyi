from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepKinematics import *


class RWStepKinematics_RWActuatedKinPairAndOrderKinPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_ActuatedKinPairAndOrderKinPair) -> None: ...
    def Share(self, theEnt: StepKinematics_ActuatedKinPairAndOrderKinPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_ActuatedKinPairAndOrderKinPair) -> None: ...

class RWStepKinematics_RWActuatedKinematicPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_ActuatedKinematicPair) -> None: ...
    def Share(self, theEnt: StepKinematics_ActuatedKinematicPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_ActuatedKinematicPair) -> None: ...

class RWStepKinematics_RWContextDependentKinematicLinkRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_ContextDependentKinematicLinkRepresentation) -> None: ...
    def Share(self, theEnt: StepKinematics_ContextDependentKinematicLinkRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_ContextDependentKinematicLinkRepresentation) -> None: ...

class RWStepKinematics_RWCylindricalPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_CylindricalPair) -> None: ...
    def Share(self, theEnt: StepKinematics_CylindricalPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_CylindricalPair) -> None: ...

class RWStepKinematics_RWCylindricalPairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_CylindricalPairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_CylindricalPairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_CylindricalPairValue) -> None: ...

class RWStepKinematics_RWCylindricalPairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_CylindricalPairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_CylindricalPairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_CylindricalPairWithRange) -> None: ...

class RWStepKinematics_RWFullyConstrainedPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_FullyConstrainedPair) -> None: ...
    def Share(self, theEnt: StepKinematics_FullyConstrainedPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_FullyConstrainedPair) -> None: ...

class RWStepKinematics_RWGearPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_GearPair) -> None: ...
    def Share(self, theEnt: StepKinematics_GearPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_GearPair) -> None: ...

class RWStepKinematics_RWGearPairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_GearPairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_GearPairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_GearPairValue) -> None: ...

class RWStepKinematics_RWGearPairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_GearPairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_GearPairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_GearPairWithRange) -> None: ...

class RWStepKinematics_RWHomokineticPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_HomokineticPair) -> None: ...
    def Share(self, theEnt: StepKinematics_HomokineticPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_HomokineticPair) -> None: ...

class RWStepKinematics_RWKinematicJoint:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_KinematicJoint) -> None: ...
    def Share(self, theEnt: StepKinematics_KinematicJoint, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_KinematicJoint) -> None: ...

class RWStepKinematics_RWKinematicLink:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_KinematicLink) -> None: ...
    def Share(self, theEnt: StepKinematics_KinematicLink, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_KinematicLink) -> None: ...

class RWStepKinematics_RWKinematicLinkRepresentationAssociation:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_KinematicLinkRepresentationAssociation) -> None: ...
    def Share(self, theEnt: StepKinematics_KinematicLinkRepresentationAssociation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_KinematicLinkRepresentationAssociation) -> None: ...

class RWStepKinematics_RWKinematicPropertyMechanismRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_KinematicPropertyMechanismRepresentation) -> None: ...
    def Share(self, theEnt: StepKinematics_KinematicPropertyMechanismRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_KinematicPropertyMechanismRepresentation) -> None: ...

class RWStepKinematics_RWKinematicTopologyDirectedStructure:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_KinematicTopologyDirectedStructure) -> None: ...
    def Share(self, theEnt: StepKinematics_KinematicTopologyDirectedStructure, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_KinematicTopologyDirectedStructure) -> None: ...

class RWStepKinematics_RWKinematicTopologyNetworkStructure:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_KinematicTopologyNetworkStructure) -> None: ...
    def Share(self, theEnt: StepKinematics_KinematicTopologyNetworkStructure, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_KinematicTopologyNetworkStructure) -> None: ...

class RWStepKinematics_RWKinematicTopologyStructure:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_KinematicTopologyStructure) -> None: ...
    def Share(self, theEnt: StepKinematics_KinematicTopologyStructure, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_KinematicTopologyStructure) -> None: ...

class RWStepKinematics_RWLinearFlexibleAndPinionPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_LinearFlexibleAndPinionPair) -> None: ...
    def Share(self, theEnt: StepKinematics_LinearFlexibleAndPinionPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_LinearFlexibleAndPinionPair) -> None: ...

class RWStepKinematics_RWLinearFlexibleAndPlanarCurvePair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_LinearFlexibleAndPlanarCurvePair) -> None: ...
    def Share(self, theEnt: StepKinematics_LinearFlexibleAndPlanarCurvePair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_LinearFlexibleAndPlanarCurvePair) -> None: ...

class RWStepKinematics_RWLinearFlexibleLinkRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_LinearFlexibleLinkRepresentation) -> None: ...
    def Share(self, theEnt: StepKinematics_LinearFlexibleLinkRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_LinearFlexibleLinkRepresentation) -> None: ...

class RWStepKinematics_RWLowOrderKinematicPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_LowOrderKinematicPair) -> None: ...
    def Share(self, theEnt: StepKinematics_LowOrderKinematicPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_LowOrderKinematicPair) -> None: ...

class RWStepKinematics_RWLowOrderKinematicPairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_LowOrderKinematicPairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_LowOrderKinematicPairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_LowOrderKinematicPairValue) -> None: ...

class RWStepKinematics_RWLowOrderKinematicPairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_LowOrderKinematicPairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_LowOrderKinematicPairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_LowOrderKinematicPairWithRange) -> None: ...

class RWStepKinematics_RWMechanismRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_MechanismRepresentation) -> None: ...
    def Share(self, theEnt: StepKinematics_MechanismRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_MechanismRepresentation) -> None: ...

class RWStepKinematics_RWMechanismStateRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_MechanismStateRepresentation) -> None: ...
    def Share(self, theEnt: StepKinematics_MechanismStateRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_MechanismStateRepresentation) -> None: ...

class RWStepKinematics_RWOrientedJoint:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_OrientedJoint) -> None: ...
    def Share(self, theEnt: StepKinematics_OrientedJoint, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_OrientedJoint) -> None: ...

class RWStepKinematics_RWPairRepresentationRelationship:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PairRepresentationRelationship) -> None: ...
    def Share(self, theEnt: StepKinematics_PairRepresentationRelationship, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PairRepresentationRelationship) -> None: ...

class RWStepKinematics_RWPlanarCurvePair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PlanarCurvePair) -> None: ...
    def Share(self, theEnt: StepKinematics_PlanarCurvePair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PlanarCurvePair) -> None: ...

class RWStepKinematics_RWPlanarCurvePairRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PlanarCurvePairRange) -> None: ...
    def Share(self, theEnt: StepKinematics_PlanarCurvePairRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PlanarCurvePairRange) -> None: ...

class RWStepKinematics_RWPlanarPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PlanarPair) -> None: ...
    def Share(self, theEnt: StepKinematics_PlanarPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PlanarPair) -> None: ...

class RWStepKinematics_RWPlanarPairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PlanarPairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_PlanarPairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PlanarPairValue) -> None: ...

class RWStepKinematics_RWPlanarPairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PlanarPairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_PlanarPairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PlanarPairWithRange) -> None: ...

class RWStepKinematics_RWPointOnPlanarCurvePair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PointOnPlanarCurvePair) -> None: ...
    def Share(self, theEnt: StepKinematics_PointOnPlanarCurvePair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PointOnPlanarCurvePair) -> None: ...

class RWStepKinematics_RWPointOnPlanarCurvePairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PointOnPlanarCurvePairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_PointOnPlanarCurvePairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PointOnPlanarCurvePairValue) -> None: ...

class RWStepKinematics_RWPointOnPlanarCurvePairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PointOnPlanarCurvePairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_PointOnPlanarCurvePairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PointOnPlanarCurvePairWithRange) -> None: ...

class RWStepKinematics_RWPointOnSurfacePair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PointOnSurfacePair) -> None: ...
    def Share(self, theEnt: StepKinematics_PointOnSurfacePair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PointOnSurfacePair) -> None: ...

class RWStepKinematics_RWPointOnSurfacePairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PointOnSurfacePairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_PointOnSurfacePairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PointOnSurfacePairValue) -> None: ...

class RWStepKinematics_RWPointOnSurfacePairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PointOnSurfacePairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_PointOnSurfacePairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PointOnSurfacePairWithRange) -> None: ...

class RWStepKinematics_RWPrismaticPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PrismaticPair) -> None: ...
    def Share(self, theEnt: StepKinematics_PrismaticPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PrismaticPair) -> None: ...

class RWStepKinematics_RWPrismaticPairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PrismaticPairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_PrismaticPairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PrismaticPairValue) -> None: ...

class RWStepKinematics_RWPrismaticPairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_PrismaticPairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_PrismaticPairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_PrismaticPairWithRange) -> None: ...

class RWStepKinematics_RWProductDefinitionKinematics:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_ProductDefinitionKinematics) -> None: ...
    def Share(self, theEnt: StepKinematics_ProductDefinitionKinematics, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_ProductDefinitionKinematics) -> None: ...

class RWStepKinematics_RWProductDefinitionRelationshipKinematics:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_ProductDefinitionRelationshipKinematics) -> None: ...
    def Share(self, theEnt: StepKinematics_ProductDefinitionRelationshipKinematics, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_ProductDefinitionRelationshipKinematics) -> None: ...

class RWStepKinematics_RWRackAndPinionPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RackAndPinionPair) -> None: ...
    def Share(self, theEnt: StepKinematics_RackAndPinionPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RackAndPinionPair) -> None: ...

class RWStepKinematics_RWRackAndPinionPairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RackAndPinionPairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_RackAndPinionPairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RackAndPinionPairValue) -> None: ...

class RWStepKinematics_RWRackAndPinionPairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RackAndPinionPairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_RackAndPinionPairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RackAndPinionPairWithRange) -> None: ...

class RWStepKinematics_RWRevolutePair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RevolutePair) -> None: ...
    def Share(self, theEnt: StepKinematics_RevolutePair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RevolutePair) -> None: ...

class RWStepKinematics_RWRevolutePairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RevolutePairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_RevolutePairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RevolutePairValue) -> None: ...

class RWStepKinematics_RWRevolutePairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RevolutePairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_RevolutePairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RevolutePairWithRange) -> None: ...

class RWStepKinematics_RWRigidLinkRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RigidLinkRepresentation) -> None: ...
    def Share(self, theEnt: StepKinematics_RigidLinkRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RigidLinkRepresentation) -> None: ...

class RWStepKinematics_RWRollingCurvePair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RollingCurvePair) -> None: ...
    def Share(self, theEnt: StepKinematics_RollingCurvePair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RollingCurvePair) -> None: ...

class RWStepKinematics_RWRollingCurvePairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RollingCurvePairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_RollingCurvePairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RollingCurvePairValue) -> None: ...

class RWStepKinematics_RWRollingSurfacePair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RollingSurfacePair) -> None: ...
    def Share(self, theEnt: StepKinematics_RollingSurfacePair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RollingSurfacePair) -> None: ...

class RWStepKinematics_RWRollingSurfacePairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RollingSurfacePairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_RollingSurfacePairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RollingSurfacePairValue) -> None: ...

class RWStepKinematics_RWRotationAboutDirection:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_RotationAboutDirection) -> None: ...
    def Share(self, theEnt: StepKinematics_RotationAboutDirection, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_RotationAboutDirection) -> None: ...

class RWStepKinematics_RWScrewPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_ScrewPair) -> None: ...
    def Share(self, theEnt: StepKinematics_ScrewPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_ScrewPair) -> None: ...

class RWStepKinematics_RWScrewPairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_ScrewPairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_ScrewPairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_ScrewPairValue) -> None: ...

class RWStepKinematics_RWScrewPairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_ScrewPairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_ScrewPairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_ScrewPairWithRange) -> None: ...

class RWStepKinematics_RWSlidingCurvePair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_SlidingCurvePair) -> None: ...
    def Share(self, theEnt: StepKinematics_SlidingCurvePair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_SlidingCurvePair) -> None: ...

class RWStepKinematics_RWSlidingCurvePairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_SlidingCurvePairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_SlidingCurvePairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_SlidingCurvePairValue) -> None: ...

class RWStepKinematics_RWSlidingSurfacePair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_SlidingSurfacePair) -> None: ...
    def Share(self, theEnt: StepKinematics_SlidingSurfacePair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_SlidingSurfacePair) -> None: ...

class RWStepKinematics_RWSlidingSurfacePairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_SlidingSurfacePairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_SlidingSurfacePairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_SlidingSurfacePairValue) -> None: ...

class RWStepKinematics_RWSphericalPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_SphericalPair) -> None: ...
    def Share(self, theEnt: StepKinematics_SphericalPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_SphericalPair) -> None: ...

class RWStepKinematics_RWSphericalPairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_SphericalPairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_SphericalPairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_SphericalPairValue) -> None: ...

class RWStepKinematics_RWSphericalPairWithPin:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_SphericalPairWithPin) -> None: ...
    def Share(self, theEnt: StepKinematics_SphericalPairWithPin, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_SphericalPairWithPin) -> None: ...

class RWStepKinematics_RWSphericalPairWithPinAndRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_SphericalPairWithPinAndRange) -> None: ...
    def Share(self, theEnt: StepKinematics_SphericalPairWithPinAndRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_SphericalPairWithPinAndRange) -> None: ...

class RWStepKinematics_RWSphericalPairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_SphericalPairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_SphericalPairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_SphericalPairWithRange) -> None: ...

class RWStepKinematics_RWSurfacePairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_SurfacePairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_SurfacePairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_SurfacePairWithRange) -> None: ...

class RWStepKinematics_RWUnconstrainedPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_UnconstrainedPair) -> None: ...
    def Share(self, theEnt: StepKinematics_UnconstrainedPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_UnconstrainedPair) -> None: ...

class RWStepKinematics_RWUnconstrainedPairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_UnconstrainedPairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_UnconstrainedPairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_UnconstrainedPairValue) -> None: ...

class RWStepKinematics_RWUniversalPair:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_UniversalPair) -> None: ...
    def Share(self, theEnt: StepKinematics_UniversalPair, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_UniversalPair) -> None: ...

class RWStepKinematics_RWUniversalPairValue:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_UniversalPairValue) -> None: ...
    def Share(self, theEnt: StepKinematics_UniversalPairValue, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_UniversalPairValue) -> None: ...

class RWStepKinematics_RWUniversalPairWithRange:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theArch: Interface_Check, theEnt: StepKinematics_UniversalPairWithRange) -> None: ...
    def Share(self, theEnt: StepKinematics_UniversalPairWithRange, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, theSW: StepData_StepWriter, theEnt: StepKinematics_UniversalPairWithRange) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

