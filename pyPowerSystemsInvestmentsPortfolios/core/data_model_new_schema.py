# generated by datamodel-codegen:
#   filename:  SiennaInvestSchema.json
#   timestamp: 2024-06-25T15:23:12+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class Items(BaseModel):
    field_ref: str = Field(..., alias='$ref')


class SupplyTechnologies(BaseModel):
    type: str
    items: Items


class StorageTechnologies(BaseModel):
    type: str
    items: Items


class DemandsideTechnologies(BaseModel):
    type: str
    items: Items


class TransportTechnologies(BaseModel):
    type: str
    items: Items


class DemandRequirements(BaseModel):
    type: str
    items: Items


class Properties(BaseModel):
    supply_technologies: SupplyTechnologies
    storage_technologies: StorageTechnologies
    demandside_technologies: DemandsideTechnologies
    transport_technologies: TransportTechnologies
    DemandRequirements: DemandRequirements


class Name(BaseModel):
    type: str
    description: str


class GenID(BaseModel):
    type: str
    description: str


class Available(BaseModel):
    type: str
    description: str


class PowerSystemsType(BaseModel):
    type: str
    description: str


class BalancingTopology(BaseModel):
    type: str
    description: str


class BasePower(BaseModel):
    type: str
    description: str


class PrimeMoverType(BaseModel):
    type: str
    enum: List[str]
    default: str
    description: str


class Fuel(BaseModel):
    type: str
    enum: List[str]
    default: str
    description: str


class CapitalCost(BaseModel):
    type: str
    description: str
    default: str


class OperationsCost(BaseModel):
    type: str
    description: str
    default: str


class VariableCost(BaseModel):
    type: str
    description: str
    default: str


class InitialCapacity(BaseModel):
    type: str
    description: str
    default: str


class MaximumCapacity(BaseModel):
    type: str
    description: str
    default: str


class MinimumRequiredCapacity(BaseModel):
    type: str
    description: str
    default: str


class CapacityFactor(BaseModel):
    type: str
    description: str
    default: str


class Ext(BaseModel):
    type: str
    default: str
    description: str


class Internal(BaseModel):
    type: str
    default: str
    description: str


class Properties1(BaseModel):
    name: Name
    gen_ID: GenID
    available: Available
    power_systems_type: PowerSystemsType
    balancing_topology: BalancingTopology
    base_power: BasePower
    prime_mover_type: PrimeMoverType
    fuel: Fuel
    capital_cost: CapitalCost
    operations_cost: OperationsCost
    variable_cost: VariableCost
    initial_capacity: InitialCapacity
    maximum_capacity: MaximumCapacity
    minimum_required_capacity: MinimumRequiredCapacity
    capacity_factor: CapacityFactor
    ext: Ext
    internal: Internal


class SupplyTechnology(BaseModel):
    type: str
    required: List[str]
    properties: Properties1
    supertype: str
    parametric: str


class PrimeMoverType1(BaseModel):
    type: str
    enum: List[str]
    description: str


class StorageTech(BaseModel):
    type: str
    enum: List[str]
    description: str


class Properties2(BaseModel):
    name: Name
    available: Available
    power_systems_type: PowerSystemsType
    prime_mover_type: PrimeMoverType1
    storage_tech: StorageTech
    ext: Ext
    internal: Internal


class StorageTechnology(BaseModel):
    type: str
    required: List[str]
    properties: Properties2
    supertype: str
    parametric: str


class Properties3(BaseModel):
    name: Name
    available: Available
    power_systems_type: PowerSystemsType
    ext: Ext
    internal: Internal


class DemandSideTechnology(BaseModel):
    type: str
    required: List[str]
    properties: Properties3
    supertype: str
    parametric: str


class Properties4(BaseModel):
    name: Name
    available: Available
    power_systems_type: PowerSystemsType
    ext: Ext
    internal: Internal


class TransportTechnology(BaseModel):
    type: str
    required: List[str]
    properties: Properties4
    supertype: str
    parametric: str


class Available4(BaseModel):
    type: str
    description: str
    default: str


class PeakLoad(BaseModel):
    type: str
    description: str
    default: str


class Region(BaseModel):
    type: str
    description: str


class LoadGrowth(BaseModel):
    type: str
    description: str
    default: str


class Properties5(BaseModel):
    name: Name
    available: Available4
    power_systems_type: PowerSystemsType
    peak_load: PeakLoad
    region: Region
    load_growth: LoadGrowth
    ext: Ext
    internal: Internal


class DemandRequirement(BaseModel):
    type: str
    required: List[str]
    properties: Properties5
    supertype: str
    parametric: str


class FieldDefs(BaseModel):
    SupplyTechnology: SupplyTechnology
    StorageTechnology: StorageTechnology
    DemandSideTechnology: DemandSideTechnology
    TransportTechnology: TransportTechnology
    DemandRequirement: DemandRequirement


class Model(BaseModel):
    field_id: str = Field(..., alias='$id')
    field_schema: str = Field(..., alias='$schema')
    description: str
    title: str
    type: str
    properties: Properties
    field_defs: FieldDefs = Field(..., alias='$defs')
