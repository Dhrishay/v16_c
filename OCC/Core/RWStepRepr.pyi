from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from from odoo.addons.OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepRepr import *


class RWStepRepr_RWAllAroundShapeAspect:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_AllAroundShapeAspect) -> None: ...
    def Share(self, ent: StepRepr_AllAroundShapeAspect, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_AllAroundShapeAspect) -> None: ...

class RWStepRepr_RWApex:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_Apex) -> None: ...
    def Share(self, ent: StepRepr_Apex, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_Apex) -> None: ...

class RWStepRepr_RWAssemblyComponentUsage:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_AssemblyComponentUsage) -> None: ...
    def Share(self, ent: StepRepr_AssemblyComponentUsage, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_AssemblyComponentUsage) -> None: ...

class RWStepRepr_RWAssemblyComponentUsageSubstitute:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_AssemblyComponentUsageSubstitute) -> None: ...
    def Share(self, ent: StepRepr_AssemblyComponentUsageSubstitute, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_AssemblyComponentUsageSubstitute) -> None: ...

class RWStepRepr_RWBetweenShapeAspect:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_BetweenShapeAspect) -> None: ...
    def Share(self, ent: StepRepr_BetweenShapeAspect, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_BetweenShapeAspect) -> None: ...

class RWStepRepr_RWCentreOfSymmetry:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_CentreOfSymmetry) -> None: ...
    def Share(self, ent: StepRepr_CentreOfSymmetry, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_CentreOfSymmetry) -> None: ...

class RWStepRepr_RWCharacterizedRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_CharacterizedRepresentation) -> None: ...
    def Share(self, ent: StepRepr_CharacterizedRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_CharacterizedRepresentation) -> None: ...

class RWStepRepr_RWCompGroupShAspAndCompShAspAndDatumFeatAndShAsp:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp) -> None: ...
    def Share(self, ent: StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp) -> None: ...

class RWStepRepr_RWCompShAspAndDatumFeatAndShAsp:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_CompShAspAndDatumFeatAndShAsp) -> None: ...
    def Share(self, ent: StepRepr_CompShAspAndDatumFeatAndShAsp, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_CompShAspAndDatumFeatAndShAsp) -> None: ...

class RWStepRepr_RWCompositeGroupShapeAspect:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_CompositeGroupShapeAspect) -> None: ...
    def Share(self, ent: StepRepr_CompositeGroupShapeAspect, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_CompositeGroupShapeAspect) -> None: ...

class RWStepRepr_RWCompositeShapeAspect:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_CompositeShapeAspect) -> None: ...
    def Share(self, ent: StepRepr_CompositeShapeAspect, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_CompositeShapeAspect) -> None: ...

class RWStepRepr_RWCompoundRepresentationItem:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_CompoundRepresentationItem) -> None: ...
    def Share(self, ent: StepRepr_CompoundRepresentationItem, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_CompoundRepresentationItem) -> None: ...

class RWStepRepr_RWConfigurationDesign:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ConfigurationDesign) -> None: ...
    def Share(self, ent: StepRepr_ConfigurationDesign, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ConfigurationDesign) -> None: ...

class RWStepRepr_RWConfigurationEffectivity:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ConfigurationEffectivity) -> None: ...
    def Share(self, ent: StepRepr_ConfigurationEffectivity, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ConfigurationEffectivity) -> None: ...

class RWStepRepr_RWConfigurationItem:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ConfigurationItem) -> None: ...
    def Share(self, ent: StepRepr_ConfigurationItem, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ConfigurationItem) -> None: ...

class RWStepRepr_RWConstructiveGeometryRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ConstructiveGeometryRepresentation) -> None: ...
    def Share(self, ent: StepRepr_ConstructiveGeometryRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ConstructiveGeometryRepresentation) -> None: ...

class RWStepRepr_RWConstructiveGeometryRepresentationRelationship:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ConstructiveGeometryRepresentationRelationship) -> None: ...
    def Share(self, ent: StepRepr_ConstructiveGeometryRepresentationRelationship, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ConstructiveGeometryRepresentationRelationship) -> None: ...

class RWStepRepr_RWContinuosShapeAspect:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ContinuosShapeAspect) -> None: ...
    def Share(self, ent: StepRepr_ContinuosShapeAspect, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ContinuosShapeAspect) -> None: ...

class RWStepRepr_RWDataEnvironment:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_DataEnvironment) -> None: ...
    def Share(self, ent: StepRepr_DataEnvironment, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_DataEnvironment) -> None: ...

class RWStepRepr_RWDefinitionalRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_DefinitionalRepresentation) -> None: ...
    def Share(self, ent: StepRepr_DefinitionalRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_DefinitionalRepresentation) -> None: ...

class RWStepRepr_RWDerivedShapeAspect:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_DerivedShapeAspect) -> None: ...
    def Share(self, ent: StepRepr_DerivedShapeAspect, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_DerivedShapeAspect) -> None: ...

class RWStepRepr_RWDescriptiveRepresentationItem:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_DescriptiveRepresentationItem) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_DescriptiveRepresentationItem) -> None: ...

class RWStepRepr_RWExtension:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_Extension) -> None: ...
    def Share(self, ent: StepRepr_Extension, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_Extension) -> None: ...

class RWStepRepr_RWFeatureForDatumTargetRelationship:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_FeatureForDatumTargetRelationship) -> None: ...
    def Share(self, ent: StepRepr_FeatureForDatumTargetRelationship, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_FeatureForDatumTargetRelationship) -> None: ...

class RWStepRepr_RWFunctionallyDefinedTransformation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_FunctionallyDefinedTransformation) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_FunctionallyDefinedTransformation) -> None: ...

class RWStepRepr_RWGeometricAlignment:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_GeometricAlignment) -> None: ...
    def Share(self, ent: StepRepr_GeometricAlignment, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_GeometricAlignment) -> None: ...

class RWStepRepr_RWGlobalUncertaintyAssignedContext:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_GlobalUncertaintyAssignedContext) -> None: ...
    def Share(self, ent: StepRepr_GlobalUncertaintyAssignedContext, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_GlobalUncertaintyAssignedContext) -> None: ...

class RWStepRepr_RWGlobalUnitAssignedContext:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_GlobalUnitAssignedContext) -> None: ...
    def Share(self, ent: StepRepr_GlobalUnitAssignedContext, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_GlobalUnitAssignedContext) -> None: ...

class RWStepRepr_RWIntegerRepresentationItem:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_IntegerRepresentationItem) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_IntegerRepresentationItem) -> None: ...

class RWStepRepr_RWItemDefinedTransformation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ItemDefinedTransformation) -> None: ...
    def Share(self, ent: StepRepr_ItemDefinedTransformation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ItemDefinedTransformation) -> None: ...

class RWStepRepr_RWMakeFromUsageOption:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_MakeFromUsageOption) -> None: ...
    def Share(self, ent: StepRepr_MakeFromUsageOption, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_MakeFromUsageOption) -> None: ...

class RWStepRepr_RWMappedItem:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_MappedItem) -> None: ...
    def Share(self, ent: StepRepr_MappedItem, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_MappedItem) -> None: ...

class RWStepRepr_RWMaterialDesignation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_MaterialDesignation) -> None: ...
    def Share(self, ent: StepRepr_MaterialDesignation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_MaterialDesignation) -> None: ...

class RWStepRepr_RWMaterialProperty:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_MaterialProperty) -> None: ...
    def Share(self, ent: StepRepr_MaterialProperty, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_MaterialProperty) -> None: ...

class RWStepRepr_RWMaterialPropertyRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_MaterialPropertyRepresentation) -> None: ...
    def Share(self, ent: StepRepr_MaterialPropertyRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_MaterialPropertyRepresentation) -> None: ...

class RWStepRepr_RWMeasureRepresentationItem:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_MeasureRepresentationItem) -> None: ...
    def Share(self, ent: StepRepr_MeasureRepresentationItem, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_MeasureRepresentationItem) -> None: ...

class RWStepRepr_RWParallelOffset:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ParallelOffset) -> None: ...
    def Share(self, ent: StepRepr_ParallelOffset, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ParallelOffset) -> None: ...

class RWStepRepr_RWParametricRepresentationContext:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ParametricRepresentationContext) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ParametricRepresentationContext) -> None: ...

class RWStepRepr_RWPerpendicularTo:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_PerpendicularTo) -> None: ...
    def Share(self, ent: StepRepr_PerpendicularTo, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_PerpendicularTo) -> None: ...

class RWStepRepr_RWProductConcept:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ProductConcept) -> None: ...
    def Share(self, ent: StepRepr_ProductConcept, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ProductConcept) -> None: ...

class RWStepRepr_RWProductDefinitionShape:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ProductDefinitionShape) -> None: ...
    def Share(self, ent: StepRepr_ProductDefinitionShape, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ProductDefinitionShape) -> None: ...

class RWStepRepr_RWPropertyDefinition:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_PropertyDefinition) -> None: ...
    def Share(self, ent: StepRepr_PropertyDefinition, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_PropertyDefinition) -> None: ...

class RWStepRepr_RWPropertyDefinitionRelationship:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_PropertyDefinitionRelationship) -> None: ...
    def Share(self, ent: StepRepr_PropertyDefinitionRelationship, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_PropertyDefinitionRelationship) -> None: ...

class RWStepRepr_RWPropertyDefinitionRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_PropertyDefinitionRepresentation) -> None: ...
    def Share(self, ent: StepRepr_PropertyDefinitionRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_PropertyDefinitionRepresentation) -> None: ...

class RWStepRepr_RWQuantifiedAssemblyComponentUsage:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_QuantifiedAssemblyComponentUsage) -> None: ...
    def Share(self, ent: StepRepr_QuantifiedAssemblyComponentUsage, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_QuantifiedAssemblyComponentUsage) -> None: ...

class RWStepRepr_RWReprItemAndLengthMeasureWithUnit:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ReprItemAndLengthMeasureWithUnit) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ReprItemAndLengthMeasureWithUnit) -> None: ...

class RWStepRepr_RWReprItemAndLengthMeasureWithUnitAndQRI:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ReprItemAndLengthMeasureWithUnitAndQRI) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ReprItemAndLengthMeasureWithUnitAndQRI) -> None: ...

class RWStepRepr_RWReprItemAndPlaneAngleMeasureWithUnit:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ReprItemAndPlaneAngleMeasureWithUnit) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ReprItemAndPlaneAngleMeasureWithUnit) -> None: ...

class RWStepRepr_RWReprItemAndPlaneAngleMeasureWithUnitAndQRI:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ReprItemAndPlaneAngleMeasureWithUnitAndQRI) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ReprItemAndPlaneAngleMeasureWithUnitAndQRI) -> None: ...

class RWStepRepr_RWRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_Representation) -> None: ...
    def Share(self, ent: StepRepr_Representation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_Representation) -> None: ...

class RWStepRepr_RWRepresentationContext:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_RepresentationContext) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_RepresentationContext) -> None: ...

class RWStepRepr_RWRepresentationContextReference:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theAch: Interface_Check, theEnt: StepRepr_RepresentationContextReference) -> None: ...
    def Share(self, theEnt: StepRepr_RepresentationContextReference, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, theEnt: StepRepr_RepresentationContextReference) -> None: ...

class RWStepRepr_RWRepresentationItem:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_RepresentationItem) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_RepresentationItem) -> None: ...

class RWStepRepr_RWRepresentationMap:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_RepresentationMap) -> None: ...
    def Share(self, ent: StepRepr_RepresentationMap, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_RepresentationMap) -> None: ...

class RWStepRepr_RWRepresentationReference:
    def __init__(self) -> None: ...
    def ReadStep(self, theData: StepData_StepReaderData, theNum: int, theAch: Interface_Check, theEnt: StepRepr_RepresentationReference) -> None: ...
    def Share(self, theEnt: StepRepr_RepresentationReference, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, theEnt: StepRepr_RepresentationReference) -> None: ...

class RWStepRepr_RWRepresentationRelationship:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_RepresentationRelationship) -> None: ...
    def Share(self, ent: StepRepr_RepresentationRelationship, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_RepresentationRelationship) -> None: ...

class RWStepRepr_RWRepresentationRelationshipWithTransformation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_RepresentationRelationshipWithTransformation) -> None: ...
    def Share(self, ent: StepRepr_RepresentationRelationshipWithTransformation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_RepresentationRelationshipWithTransformation) -> None: ...

class RWStepRepr_RWShapeAspect:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ShapeAspect) -> None: ...
    def Share(self, ent: StepRepr_ShapeAspect, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ShapeAspect) -> None: ...

class RWStepRepr_RWShapeAspectDerivingRelationship:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ShapeAspectDerivingRelationship) -> None: ...
    def Share(self, ent: StepRepr_ShapeAspectDerivingRelationship, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ShapeAspectDerivingRelationship) -> None: ...

class RWStepRepr_RWShapeAspectRelationship:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ShapeAspectRelationship) -> None: ...
    def Share(self, ent: StepRepr_ShapeAspectRelationship, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ShapeAspectRelationship) -> None: ...

class RWStepRepr_RWShapeAspectTransition:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ShapeAspectTransition) -> None: ...
    def Share(self, ent: StepRepr_ShapeAspectTransition, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ShapeAspectTransition) -> None: ...

class RWStepRepr_RWShapeRepresentationRelationshipWithTransformation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ShapeRepresentationRelationshipWithTransformation) -> None: ...
    def Share(self, ent: StepRepr_ShapeRepresentationRelationshipWithTransformation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ShapeRepresentationRelationshipWithTransformation) -> None: ...

class RWStepRepr_RWSpecifiedHigherUsageOccurrence:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_SpecifiedHigherUsageOccurrence) -> None: ...
    def Share(self, ent: StepRepr_SpecifiedHigherUsageOccurrence, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_SpecifiedHigherUsageOccurrence) -> None: ...

class RWStepRepr_RWStructuralResponseProperty:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_StructuralResponseProperty) -> None: ...
    def Share(self, ent: StepRepr_StructuralResponseProperty, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_StructuralResponseProperty) -> None: ...

class RWStepRepr_RWStructuralResponsePropertyDefinitionRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_StructuralResponsePropertyDefinitionRepresentation) -> None: ...
    def Share(self, ent: StepRepr_StructuralResponsePropertyDefinitionRepresentation, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_StructuralResponsePropertyDefinitionRepresentation) -> None: ...

class RWStepRepr_RWTangent:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_Tangent) -> None: ...
    def Share(self, ent: StepRepr_Tangent, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_Tangent) -> None: ...

class RWStepRepr_RWValueRepresentationItem:
    def __init__(self) -> None: ...
    def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepRepr_ValueRepresentationItem) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepRepr_ValueRepresentationItem) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

