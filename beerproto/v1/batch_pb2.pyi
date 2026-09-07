import datetime

from beerproto.v1 import equipment_pb2 as _equipment_pb2
from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from beerproto.v1 import water_pb2 as _water_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATCH_STATUS_TYPE_UNSPECIFIED: _ClassVar[BatchStatusType]
    BATCH_STATUS_TYPE_PLANNING: _ClassVar[BatchStatusType]
    BATCH_STATUS_TYPE_BREWING: _ClassVar[BatchStatusType]
    BATCH_STATUS_TYPE_FERMENTING: _ClassVar[BatchStatusType]
    BATCH_STATUS_TYPE_CONDITIONING: _ClassVar[BatchStatusType]
    BATCH_STATUS_TYPE_COMPLETED: _ClassVar[BatchStatusType]
    BATCH_STATUS_TYPE_ARCHIVED: _ClassVar[BatchStatusType]

class WaterAdjustmentStrategyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WATER_ADJUSTMENT_STRATEGY_TYPE_UNSPECIFIED: _ClassVar[WaterAdjustmentStrategyType]
    WATER_ADJUSTMENT_STRATEGY_TYPE_SALTS: _ClassVar[WaterAdjustmentStrategyType]
    WATER_ADJUSTMENT_STRATEGY_TYPE_DILUTION: _ClassVar[WaterAdjustmentStrategyType]
    WATER_ADJUSTMENT_STRATEGY_TYPE_ACID: _ClassVar[WaterAdjustmentStrategyType]

class MashAcidBasis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MASH_ACID_BASIS_UNSPECIFIED: _ClassVar[MashAcidBasis]
    MASH_ACID_BASIS_ESTIMATE: _ClassVar[MashAcidBasis]
    MASH_ACID_BASIS_MEASUREMENT: _ClassVar[MashAcidBasis]

class GrowthModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROWTH_MODEL_UNSPECIFIED: _ClassVar[GrowthModel]
    GROWTH_MODEL_BRAUKAISER: _ClassVar[GrowthModel]
    GROWTH_MODEL_C_WHITE_NO_AGITATION: _ClassVar[GrowthModel]
    GROWTH_MODEL_C_WHITE_SHAKING: _ClassVar[GrowthModel]
BATCH_STATUS_TYPE_UNSPECIFIED: BatchStatusType
BATCH_STATUS_TYPE_PLANNING: BatchStatusType
BATCH_STATUS_TYPE_BREWING: BatchStatusType
BATCH_STATUS_TYPE_FERMENTING: BatchStatusType
BATCH_STATUS_TYPE_CONDITIONING: BatchStatusType
BATCH_STATUS_TYPE_COMPLETED: BatchStatusType
BATCH_STATUS_TYPE_ARCHIVED: BatchStatusType
WATER_ADJUSTMENT_STRATEGY_TYPE_UNSPECIFIED: WaterAdjustmentStrategyType
WATER_ADJUSTMENT_STRATEGY_TYPE_SALTS: WaterAdjustmentStrategyType
WATER_ADJUSTMENT_STRATEGY_TYPE_DILUTION: WaterAdjustmentStrategyType
WATER_ADJUSTMENT_STRATEGY_TYPE_ACID: WaterAdjustmentStrategyType
MASH_ACID_BASIS_UNSPECIFIED: MashAcidBasis
MASH_ACID_BASIS_ESTIMATE: MashAcidBasis
MASH_ACID_BASIS_MEASUREMENT: MashAcidBasis
GROWTH_MODEL_UNSPECIFIED: GrowthModel
GROWTH_MODEL_BRAUKAISER: GrowthModel
GROWTH_MODEL_C_WHITE_NO_AGITATION: GrowthModel
GROWTH_MODEL_C_WHITE_SHAKING: GrowthModel

class Batch(_message.Message):
    __slots__ = ("id", "recipe_id", "name", "batch", "date", "status", "brew_step", "equipment", "starters", "water_adjustment_strategy", "mash_acid_additions", "fermentation_profile", "measurements", "estimates", "logs", "notes", "rating")
    ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BREW_STEP_FIELD_NUMBER: _ClassVar[int]
    EQUIPMENT_FIELD_NUMBER: _ClassVar[int]
    STARTERS_FIELD_NUMBER: _ClassVar[int]
    WATER_ADJUSTMENT_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MASH_ACID_ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    FERMENTATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATES_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    id: str
    recipe_id: str
    name: str
    batch: int
    date: _timestamp_pb2.Timestamp
    status: BatchStatusType
    brew_step: int
    equipment: _equipment_pb2.EquipmentType
    starters: _containers.RepeatedCompositeFieldContainer[Starter]
    water_adjustment_strategy: WaterAdjustmentStrategyType
    mash_acid_additions: _containers.RepeatedCompositeFieldContainer[MashAcidAddition]
    fermentation_profile: FermentationProfile
    measurements: Measurements
    estimates: Estimates
    logs: _containers.RepeatedCompositeFieldContainer[Log]
    notes: str
    rating: float
    def __init__(self, id: _Optional[str] = ..., recipe_id: _Optional[str] = ..., name: _Optional[str] = ..., batch: _Optional[int] = ..., date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[BatchStatusType, str]] = ..., brew_step: _Optional[int] = ..., equipment: _Optional[_Union[_equipment_pb2.EquipmentType, _Mapping]] = ..., starters: _Optional[_Iterable[_Union[Starter, _Mapping]]] = ..., water_adjustment_strategy: _Optional[_Union[WaterAdjustmentStrategyType, str]] = ..., mash_acid_additions: _Optional[_Iterable[_Union[MashAcidAddition, _Mapping]]] = ..., fermentation_profile: _Optional[_Union[FermentationProfile, _Mapping]] = ..., measurements: _Optional[_Union[Measurements, _Mapping]] = ..., estimates: _Optional[_Union[Estimates, _Mapping]] = ..., logs: _Optional[_Iterable[_Union[Log, _Mapping]]] = ..., notes: _Optional[str] = ..., rating: _Optional[float] = ...) -> None: ...

class MashAcidAddition(_message.Message):
    __slots__ = ("id", "acid", "amount", "target_ph", "from_ph", "basis", "volume", "confirmed")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PH_FIELD_NUMBER: _ClassVar[int]
    FROM_PH_FIELD_NUMBER: _ClassVar[int]
    BASIS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    id: str
    acid: _water_pb2.AcidType
    amount: float
    target_ph: _measureable_units_pb2.AcidityType
    from_ph: _measureable_units_pb2.AcidityType
    basis: MashAcidBasis
    volume: _measureable_units_pb2.VolumeType
    confirmed: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., acid: _Optional[_Union[_water_pb2.AcidType, str]] = ..., amount: _Optional[float] = ..., target_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., from_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., basis: _Optional[_Union[MashAcidBasis, str]] = ..., volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., confirmed: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Starter(_message.Message):
    __slots__ = ("id", "steps", "culture_id", "pitch_rate", "yeast_date", "pitch")
    ID_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    CULTURE_ID_FIELD_NUMBER: _ClassVar[int]
    PITCH_RATE_FIELD_NUMBER: _ClassVar[int]
    YEAST_DATE_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    id: str
    steps: _containers.RepeatedCompositeFieldContainer[StarterStep]
    culture_id: str
    pitch_rate: _measureable_units_pb2.PitchRateType
    yeast_date: _timestamp_pb2.Timestamp
    pitch: CulturePitchRate
    def __init__(self, id: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[StarterStep, _Mapping]]] = ..., culture_id: _Optional[str] = ..., pitch_rate: _Optional[_Union[_measureable_units_pb2.PitchRateType, _Mapping]] = ..., yeast_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., pitch: _Optional[_Union[CulturePitchRate, _Mapping]] = ...) -> None: ...

class StarterStep(_message.Message):
    __slots__ = ("id", "starter_size", "gravity", "model")
    ID_FIELD_NUMBER: _ClassVar[int]
    STARTER_SIZE_FIELD_NUMBER: _ClassVar[int]
    GRAVITY_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    starter_size: _measureable_units_pb2.VolumeType
    gravity: _measureable_units_pb2.GravityType
    model: GrowthModel
    def __init__(self, id: _Optional[str] = ..., starter_size: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., model: _Optional[_Union[GrowthModel, str]] = ...) -> None: ...

class StepRate(_message.Message):
    __slots__ = ("dme", "growth_rate", "ending_count", "pitch_rate")
    DME_FIELD_NUMBER: _ClassVar[int]
    GROWTH_RATE_FIELD_NUMBER: _ClassVar[int]
    ENDING_COUNT_FIELD_NUMBER: _ClassVar[int]
    PITCH_RATE_FIELD_NUMBER: _ClassVar[int]
    dme: _measureable_units_pb2.MassType
    growth_rate: float
    ending_count: _measureable_units_pb2.CellCountType
    pitch_rate: _measureable_units_pb2.PitchRateType
    def __init__(self, dme: _Optional[_Union[_measureable_units_pb2.MassType, _Mapping]] = ..., growth_rate: _Optional[float] = ..., ending_count: _Optional[_Union[_measureable_units_pb2.CellCountType, _Mapping]] = ..., pitch_rate: _Optional[_Union[_measureable_units_pb2.PitchRateType, _Mapping]] = ...) -> None: ...

class CulturePitchRate(_message.Message):
    __slots__ = ("target_pitch_rate_cells", "cells_available", "difference", "pitch_rate_as_is", "viability")
    TARGET_PITCH_RATE_CELLS_FIELD_NUMBER: _ClassVar[int]
    CELLS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DIFFERENCE_FIELD_NUMBER: _ClassVar[int]
    PITCH_RATE_AS_IS_FIELD_NUMBER: _ClassVar[int]
    VIABILITY_FIELD_NUMBER: _ClassVar[int]
    target_pitch_rate_cells: _measureable_units_pb2.CellCountType
    cells_available: _measureable_units_pb2.CellCountType
    difference: _measureable_units_pb2.CellCountType
    pitch_rate_as_is: _measureable_units_pb2.PitchRateType
    viability: _measureable_units_pb2.PercentType
    def __init__(self, target_pitch_rate_cells: _Optional[_Union[_measureable_units_pb2.CellCountType, _Mapping]] = ..., cells_available: _Optional[_Union[_measureable_units_pb2.CellCountType, _Mapping]] = ..., difference: _Optional[_Union[_measureable_units_pb2.CellCountType, _Mapping]] = ..., pitch_rate_as_is: _Optional[_Union[_measureable_units_pb2.PitchRateType, _Mapping]] = ..., viability: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ...) -> None: ...

class Log(_message.Message):
    __slots__ = ("id", "date", "notes", "status", "gravity", "temperature", "taste")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GRAVITY_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TASTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    date: _timestamp_pb2.Timestamp
    notes: str
    status: BatchStatusType
    gravity: _measureable_units_pb2.GravityType
    temperature: _measureable_units_pb2.TemperatureType
    taste: Taste
    def __init__(self, id: _Optional[str] = ..., date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., status: _Optional[_Union[BatchStatusType, str]] = ..., gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ..., taste: _Optional[_Union[Taste, _Mapping]] = ...) -> None: ...

class Taste(_message.Message):
    __slots__ = ("rating", "notes", "bitterness", "sweetness", "body", "aroma")
    RATING_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    BITTERNESS_FIELD_NUMBER: _ClassVar[int]
    SWEETNESS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    AROMA_FIELD_NUMBER: _ClassVar[int]
    rating: float
    notes: str
    bitterness: float
    sweetness: float
    body: float
    aroma: float
    def __init__(self, rating: _Optional[float] = ..., notes: _Optional[str] = ..., bitterness: _Optional[float] = ..., sweetness: _Optional[float] = ..., body: _Optional[float] = ..., aroma: _Optional[float] = ...) -> None: ...

class FermentationProfile(_message.Message):
    __slots__ = ("fermentation_start", "bottling_date")
    FERMENTATION_START_FIELD_NUMBER: _ClassVar[int]
    BOTTLING_DATE_FIELD_NUMBER: _ClassVar[int]
    fermentation_start: _timestamp_pb2.Timestamp
    bottling_date: _timestamp_pb2.Timestamp
    def __init__(self, fermentation_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., bottling_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Measurements(_message.Message):
    __slots__ = ("boil_volume", "pre_boil_volume", "post_boil_kettle_volume", "batch_volume", "fermenter_volume", "fermenter_topup", "bottling_volume", "packaging_volume", "boil_off_per_hour", "first_wort_gravity", "pre_boil_gravity", "post_boil_gravity", "original_gravity", "final_gravity", "conversion_efficiency", "lauter_efficiency", "mash_efficiency", "brewhouse_efficiency", "alcohol_by_volume", "attenuation", "color", "bitterness", "mash_ph", "beer_ph", "boil_time", "carbonation_temperature")
    BOIL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    PRE_BOIL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    POST_BOIL_KETTLE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    BATCH_VOLUME_FIELD_NUMBER: _ClassVar[int]
    FERMENTER_VOLUME_FIELD_NUMBER: _ClassVar[int]
    FERMENTER_TOPUP_FIELD_NUMBER: _ClassVar[int]
    BOTTLING_VOLUME_FIELD_NUMBER: _ClassVar[int]
    PACKAGING_VOLUME_FIELD_NUMBER: _ClassVar[int]
    BOIL_OFF_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    FIRST_WORT_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    PRE_BOIL_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    POST_BOIL_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    FINAL_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    LAUTER_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    MASH_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    BREWHOUSE_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    ALCOHOL_BY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    ATTENUATION_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    BITTERNESS_FIELD_NUMBER: _ClassVar[int]
    MASH_PH_FIELD_NUMBER: _ClassVar[int]
    BEER_PH_FIELD_NUMBER: _ClassVar[int]
    BOIL_TIME_FIELD_NUMBER: _ClassVar[int]
    CARBONATION_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    boil_volume: _measureable_units_pb2.VolumeType
    pre_boil_volume: _measureable_units_pb2.VolumeType
    post_boil_kettle_volume: _measureable_units_pb2.VolumeType
    batch_volume: _measureable_units_pb2.VolumeType
    fermenter_volume: _measureable_units_pb2.VolumeType
    fermenter_topup: _measureable_units_pb2.VolumeType
    bottling_volume: _measureable_units_pb2.VolumeType
    packaging_volume: _measureable_units_pb2.VolumeType
    boil_off_per_hour: _measureable_units_pb2.VolumeType
    first_wort_gravity: _measureable_units_pb2.GravityType
    pre_boil_gravity: _measureable_units_pb2.GravityType
    post_boil_gravity: _measureable_units_pb2.GravityType
    original_gravity: _measureable_units_pb2.GravityType
    final_gravity: _measureable_units_pb2.GravityType
    conversion_efficiency: _measureable_units_pb2.PercentType
    lauter_efficiency: _measureable_units_pb2.PercentType
    mash_efficiency: _measureable_units_pb2.PercentType
    brewhouse_efficiency: _measureable_units_pb2.PercentType
    alcohol_by_volume: _measureable_units_pb2.PercentType
    attenuation: _measureable_units_pb2.PercentType
    color: _measureable_units_pb2.ColorType
    bitterness: _measureable_units_pb2.BitternessType
    mash_ph: _measureable_units_pb2.AcidityType
    beer_ph: _measureable_units_pb2.AcidityType
    boil_time: _measureable_units_pb2.TimeType
    carbonation_temperature: _measureable_units_pb2.TemperatureType
    def __init__(self, boil_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., pre_boil_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., post_boil_kettle_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., batch_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., fermenter_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., fermenter_topup: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., bottling_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., packaging_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., boil_off_per_hour: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., first_wort_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., pre_boil_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., post_boil_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., original_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., final_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., conversion_efficiency: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., lauter_efficiency: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., mash_efficiency: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., brewhouse_efficiency: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., alcohol_by_volume: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., attenuation: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., color: _Optional[_Union[_measureable_units_pb2.ColorType, _Mapping]] = ..., bitterness: _Optional[_Union[_measureable_units_pb2.BitternessType, _Mapping]] = ..., mash_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., beer_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., boil_time: _Optional[_Union[_measureable_units_pb2.TimeType, _Mapping]] = ..., carbonation_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ...) -> None: ...

class Estimates(_message.Message):
    __slots__ = ("pre_boil_volume", "pre_boil_gravity", "bitterness", "mash_ph", "mash_ph_model")
    PRE_BOIL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    PRE_BOIL_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    BITTERNESS_FIELD_NUMBER: _ClassVar[int]
    MASH_PH_FIELD_NUMBER: _ClassVar[int]
    MASH_PH_MODEL_FIELD_NUMBER: _ClassVar[int]
    pre_boil_volume: _measureable_units_pb2.VolumeType
    pre_boil_gravity: _measureable_units_pb2.GravityType
    bitterness: _measureable_units_pb2.BitternessType
    mash_ph: _measureable_units_pb2.AcidityType
    mash_ph_model: _water_pb2.MashPhModel
    def __init__(self, pre_boil_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., pre_boil_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., bitterness: _Optional[_Union[_measureable_units_pb2.BitternessType, _Mapping]] = ..., mash_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., mash_ph_model: _Optional[_Union[_water_pb2.MashPhModel, str]] = ...) -> None: ...
