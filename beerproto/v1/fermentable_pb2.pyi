import datetime

from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from beerproto.v1 import timing_pb2 as _timing_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrainCrush(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRAIN_CRUSH_UNSPECIFIED: _ClassVar[GrainCrush]
    GRAIN_CRUSH_UNCRUSHED: _ClassVar[GrainCrush]
    GRAIN_CRUSH_COARSE: _ClassVar[GrainCrush]
    GRAIN_CRUSH_MEDIUM: _ClassVar[GrainCrush]
    GRAIN_CRUSH_FINE: _ClassVar[GrainCrush]

class FermentableBaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FERMENTABLE_BASE_TYPE_UNSPECIFIED: _ClassVar[FermentableBaseType]
    FERMENTABLE_BASE_TYPE_DRY_EXTRACT: _ClassVar[FermentableBaseType]
    FERMENTABLE_BASE_TYPE_EXTRACT: _ClassVar[FermentableBaseType]
    FERMENTABLE_BASE_TYPE_GRAIN: _ClassVar[FermentableBaseType]
    FERMENTABLE_BASE_TYPE_SUGAR: _ClassVar[FermentableBaseType]
    FERMENTABLE_BASE_TYPE_FRUIT: _ClassVar[FermentableBaseType]
    FERMENTABLE_BASE_TYPE_JUICE: _ClassVar[FermentableBaseType]
    FERMENTABLE_BASE_TYPE_HONEY: _ClassVar[FermentableBaseType]
    FERMENTABLE_BASE_TYPE_OTHER: _ClassVar[FermentableBaseType]

class GrainGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRAIN_GROUP_UNSPECIFIED: _ClassVar[GrainGroup]
    GRAIN_GROUP_BASE: _ClassVar[GrainGroup]
    GRAIN_GROUP_CARAMEL: _ClassVar[GrainGroup]
    GRAIN_GROUP_FLAKED: _ClassVar[GrainGroup]
    GRAIN_GROUP_ROASTED: _ClassVar[GrainGroup]
    GRAIN_GROUP_SPECIALTY: _ClassVar[GrainGroup]
    GRAIN_GROUP_SMOKED: _ClassVar[GrainGroup]
    GRAIN_GROUP_ADJUNCT: _ClassVar[GrainGroup]
GRAIN_CRUSH_UNSPECIFIED: GrainCrush
GRAIN_CRUSH_UNCRUSHED: GrainCrush
GRAIN_CRUSH_COARSE: GrainCrush
GRAIN_CRUSH_MEDIUM: GrainCrush
GRAIN_CRUSH_FINE: GrainCrush
FERMENTABLE_BASE_TYPE_UNSPECIFIED: FermentableBaseType
FERMENTABLE_BASE_TYPE_DRY_EXTRACT: FermentableBaseType
FERMENTABLE_BASE_TYPE_EXTRACT: FermentableBaseType
FERMENTABLE_BASE_TYPE_GRAIN: FermentableBaseType
FERMENTABLE_BASE_TYPE_SUGAR: FermentableBaseType
FERMENTABLE_BASE_TYPE_FRUIT: FermentableBaseType
FERMENTABLE_BASE_TYPE_JUICE: FermentableBaseType
FERMENTABLE_BASE_TYPE_HONEY: FermentableBaseType
FERMENTABLE_BASE_TYPE_OTHER: FermentableBaseType
GRAIN_GROUP_UNSPECIFIED: GrainGroup
GRAIN_GROUP_BASE: GrainGroup
GRAIN_GROUP_CARAMEL: GrainGroup
GRAIN_GROUP_FLAKED: GrainGroup
GRAIN_GROUP_ROASTED: GrainGroup
GRAIN_GROUP_SPECIALTY: GrainGroup
GRAIN_GROUP_SMOKED: GrainGroup
GRAIN_GROUP_ADJUNCT: GrainGroup

class FermentableBase(_message.Message):
    __slots__ = ("type", "origin", "grain_group", "color", "name", "producer", "product_id", "diastatic_power")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    GRAIN_GROUP_FIELD_NUMBER: _ClassVar[int]
    YIELD_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    DIASTATIC_POWER_FIELD_NUMBER: _ClassVar[int]
    type: FermentableBaseType
    origin: str
    grain_group: GrainGroup
    color: _measureable_units_pb2.ColorType
    name: str
    producer: str
    product_id: str
    diastatic_power: _measureable_units_pb2.DiastaticPowerType
    def __init__(self, type: _Optional[_Union[FermentableBaseType, str]] = ..., origin: _Optional[str] = ..., grain_group: _Optional[_Union[GrainGroup, str]] = ..., color: _Optional[_Union[_measureable_units_pb2.ColorType, _Mapping]] = ..., name: _Optional[str] = ..., producer: _Optional[str] = ..., product_id: _Optional[str] = ..., diastatic_power: _Optional[_Union[_measureable_units_pb2.DiastaticPowerType, _Mapping]] = ..., **kwargs) -> None: ...

class FermentableType(_message.Message):
    __slots__ = ("base", "id", "max_in_batch", "recommend_mash", "protein", "alpha_amylase", "diastatic_power", "moisture", "inventory", "kolbach_index", "glassy", "plump", "half", "mealy", "thru", "friability", "di_ph", "viscosity", "dms_p", "fan", "fermentability", "beta_glucan", "notes")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MAX_IN_BATCH_FIELD_NUMBER: _ClassVar[int]
    RECOMMEND_MASH_FIELD_NUMBER: _ClassVar[int]
    PROTEIN_FIELD_NUMBER: _ClassVar[int]
    ALPHA_AMYLASE_FIELD_NUMBER: _ClassVar[int]
    DIASTATIC_POWER_FIELD_NUMBER: _ClassVar[int]
    MOISTURE_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    KOLBACH_INDEX_FIELD_NUMBER: _ClassVar[int]
    GLASSY_FIELD_NUMBER: _ClassVar[int]
    PLUMP_FIELD_NUMBER: _ClassVar[int]
    HALF_FIELD_NUMBER: _ClassVar[int]
    MEALY_FIELD_NUMBER: _ClassVar[int]
    THRU_FIELD_NUMBER: _ClassVar[int]
    FRIABILITY_FIELD_NUMBER: _ClassVar[int]
    DI_PH_FIELD_NUMBER: _ClassVar[int]
    VISCOSITY_FIELD_NUMBER: _ClassVar[int]
    DMS_P_FIELD_NUMBER: _ClassVar[int]
    FAN_FIELD_NUMBER: _ClassVar[int]
    FERMENTABILITY_FIELD_NUMBER: _ClassVar[int]
    BETA_GLUCAN_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    base: FermentableBase
    id: str
    max_in_batch: _measureable_units_pb2.PercentType
    recommend_mash: bool
    protein: _measureable_units_pb2.PercentType
    alpha_amylase: _measureable_units_pb2.EnzymeActivityType
    diastatic_power: _measureable_units_pb2.DiastaticPowerType
    moisture: _measureable_units_pb2.PercentType
    inventory: FermentableInventoryType
    kolbach_index: _measureable_units_pb2.PercentType
    glassy: _measureable_units_pb2.PercentType
    plump: _measureable_units_pb2.PercentType
    half: _measureable_units_pb2.PercentType
    mealy: _measureable_units_pb2.PercentType
    thru: _measureable_units_pb2.PercentType
    friability: _measureable_units_pb2.PercentType
    di_ph: _measureable_units_pb2.AcidityType
    viscosity: _measureable_units_pb2.ViscosityType
    dms_p: _measureable_units_pb2.ConcentrationType
    fan: _measureable_units_pb2.ConcentrationType
    fermentability: _measureable_units_pb2.PercentType
    beta_glucan: _measureable_units_pb2.ConcentrationType
    notes: str
    def __init__(self, base: _Optional[_Union[FermentableBase, _Mapping]] = ..., id: _Optional[str] = ..., max_in_batch: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., recommend_mash: _Optional[bool] = ..., protein: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., alpha_amylase: _Optional[_Union[_measureable_units_pb2.EnzymeActivityType, _Mapping]] = ..., diastatic_power: _Optional[_Union[_measureable_units_pb2.DiastaticPowerType, _Mapping]] = ..., moisture: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., inventory: _Optional[_Union[FermentableInventoryType, _Mapping]] = ..., kolbach_index: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., glassy: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., plump: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., half: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., mealy: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., thru: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., friability: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., di_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., viscosity: _Optional[_Union[_measureable_units_pb2.ViscosityType, _Mapping]] = ..., dms_p: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., fan: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., fermentability: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., beta_glucan: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., notes: _Optional[str] = ...) -> None: ...

class FermentableAdditionType(_message.Message):
    __slots__ = ("base", "id", "timing", "mass", "volume")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    MASS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    base: FermentableBase
    id: str
    timing: _timing_pb2.TimingType
    mass: _measureable_units_pb2.MassType
    volume: _measureable_units_pb2.VolumeType
    def __init__(self, base: _Optional[_Union[FermentableBase, _Mapping]] = ..., id: _Optional[str] = ..., timing: _Optional[_Union[_timing_pb2.TimingType, _Mapping]] = ..., mass: _Optional[_Union[_measureable_units_pb2.MassType, _Mapping]] = ..., volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ...) -> None: ...

class YieldType(_message.Message):
    __slots__ = ("fine_grind", "coarse_grind", "fine_coarse_difference", "potential")
    FINE_GRIND_FIELD_NUMBER: _ClassVar[int]
    COARSE_GRIND_FIELD_NUMBER: _ClassVar[int]
    FINE_COARSE_DIFFERENCE_FIELD_NUMBER: _ClassVar[int]
    POTENTIAL_FIELD_NUMBER: _ClassVar[int]
    fine_grind: _measureable_units_pb2.PercentType
    coarse_grind: _measureable_units_pb2.PercentType
    fine_coarse_difference: _measureable_units_pb2.PercentType
    potential: _measureable_units_pb2.GravityType
    def __init__(self, fine_grind: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., coarse_grind: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., fine_coarse_difference: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., potential: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ...) -> None: ...

class FermentableInventoryType(_message.Message):
    __slots__ = ("mass", "volume", "best_before", "lot_potential", "crush", "moisture")
    MASS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    BEST_BEFORE_FIELD_NUMBER: _ClassVar[int]
    LOT_POTENTIAL_FIELD_NUMBER: _ClassVar[int]
    CRUSH_FIELD_NUMBER: _ClassVar[int]
    MOISTURE_FIELD_NUMBER: _ClassVar[int]
    mass: _measureable_units_pb2.MassType
    volume: _measureable_units_pb2.VolumeType
    best_before: _timestamp_pb2.Timestamp
    lot_potential: _measureable_units_pb2.GravityType
    crush: GrainCrush
    moisture: _measureable_units_pb2.PercentType
    def __init__(self, mass: _Optional[_Union[_measureable_units_pb2.MassType, _Mapping]] = ..., volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., best_before: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., lot_potential: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., crush: _Optional[_Union[GrainCrush, str]] = ..., moisture: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ...) -> None: ...
