from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from beerproto.v1 import timing_pb2 as _timing_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QualitativeRangeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUALITATIVE_RANGE_UNIT_UNSPECIFIED: _ClassVar[QualitativeRangeUnit]
    QUALITATIVE_RANGE_UNIT_VERY_LOW: _ClassVar[QualitativeRangeUnit]
    QUALITATIVE_RANGE_UNIT_LOW: _ClassVar[QualitativeRangeUnit]
    QUALITATIVE_RANGE_UNIT_MEDIUM_LOW: _ClassVar[QualitativeRangeUnit]
    QUALITATIVE_RANGE_UNIT_MEDIUM: _ClassVar[QualitativeRangeUnit]
    QUALITATIVE_RANGE_UNIT_MEDIUM_HIGH: _ClassVar[QualitativeRangeUnit]
    QUALITATIVE_RANGE_UNIT_HIGH: _ClassVar[QualitativeRangeUnit]
    QUALITATIVE_RANGE_UNIT_VERY_HIGH: _ClassVar[QualitativeRangeUnit]

class CultureBaseForm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CULTURE_BASE_FORM_UNSPECIFIED: _ClassVar[CultureBaseForm]
    CULTURE_BASE_FORM_LIQUID: _ClassVar[CultureBaseForm]
    CULTURE_BASE_FORM_DRY: _ClassVar[CultureBaseForm]
    CULTURE_BASE_FORM_SLANT: _ClassVar[CultureBaseForm]
    CULTURE_BASE_FORM_CULTURE: _ClassVar[CultureBaseForm]
    CULTURE_BASE_FORM_DREGS: _ClassVar[CultureBaseForm]

class CultureBaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CULTURE_BASE_TYPE_UNSPECIFIED: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_ALE: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_LAGER: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_KVEIK: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_BRETT: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_CHAMPAGNE: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_WINE: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_NON_SACCHAROMYCES: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_LACTO: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_PEDIO: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_MALOLACTIC: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_ACETIC: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_BACTERIA: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_MIXED_CULTURE: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_SPONTANEOUS: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_SCOBY: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_MOLD: _ClassVar[CultureBaseType]
    CULTURE_BASE_TYPE_OTHER: _ClassVar[CultureBaseType]
QUALITATIVE_RANGE_UNIT_UNSPECIFIED: QualitativeRangeUnit
QUALITATIVE_RANGE_UNIT_VERY_LOW: QualitativeRangeUnit
QUALITATIVE_RANGE_UNIT_LOW: QualitativeRangeUnit
QUALITATIVE_RANGE_UNIT_MEDIUM_LOW: QualitativeRangeUnit
QUALITATIVE_RANGE_UNIT_MEDIUM: QualitativeRangeUnit
QUALITATIVE_RANGE_UNIT_MEDIUM_HIGH: QualitativeRangeUnit
QUALITATIVE_RANGE_UNIT_HIGH: QualitativeRangeUnit
QUALITATIVE_RANGE_UNIT_VERY_HIGH: QualitativeRangeUnit
CULTURE_BASE_FORM_UNSPECIFIED: CultureBaseForm
CULTURE_BASE_FORM_LIQUID: CultureBaseForm
CULTURE_BASE_FORM_DRY: CultureBaseForm
CULTURE_BASE_FORM_SLANT: CultureBaseForm
CULTURE_BASE_FORM_CULTURE: CultureBaseForm
CULTURE_BASE_FORM_DREGS: CultureBaseForm
CULTURE_BASE_TYPE_UNSPECIFIED: CultureBaseType
CULTURE_BASE_TYPE_ALE: CultureBaseType
CULTURE_BASE_TYPE_LAGER: CultureBaseType
CULTURE_BASE_TYPE_KVEIK: CultureBaseType
CULTURE_BASE_TYPE_BRETT: CultureBaseType
CULTURE_BASE_TYPE_CHAMPAGNE: CultureBaseType
CULTURE_BASE_TYPE_WINE: CultureBaseType
CULTURE_BASE_TYPE_NON_SACCHAROMYCES: CultureBaseType
CULTURE_BASE_TYPE_LACTO: CultureBaseType
CULTURE_BASE_TYPE_PEDIO: CultureBaseType
CULTURE_BASE_TYPE_MALOLACTIC: CultureBaseType
CULTURE_BASE_TYPE_ACETIC: CultureBaseType
CULTURE_BASE_TYPE_BACTERIA: CultureBaseType
CULTURE_BASE_TYPE_MIXED_CULTURE: CultureBaseType
CULTURE_BASE_TYPE_SPONTANEOUS: CultureBaseType
CULTURE_BASE_TYPE_SCOBY: CultureBaseType
CULTURE_BASE_TYPE_MOLD: CultureBaseType
CULTURE_BASE_TYPE_OTHER: CultureBaseType

class CultureBase(_message.Message):
    __slots__ = ("name", "type", "form", "producer", "product_id", "glucoamylase")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    GLUCOAMYLASE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: CultureBaseType
    form: CultureBaseForm
    producer: str
    product_id: str
    glucoamylase: bool
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[CultureBaseType, str]] = ..., form: _Optional[_Union[CultureBaseForm, str]] = ..., producer: _Optional[str] = ..., product_id: _Optional[str] = ..., glucoamylase: _Optional[bool] = ...) -> None: ...

class CultureInformation(_message.Message):
    __slots__ = ("base", "id", "temperature_range", "notes", "best_for", "inventory", "alcohol_tolerance", "glucoamylase", "type", "flocculation", "attenuation_range", "max_reuse", "pof", "zymocide")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_RANGE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    BEST_FOR_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    ALCOHOL_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    GLUCOAMYLASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FLOCCULATION_FIELD_NUMBER: _ClassVar[int]
    ATTENUATION_RANGE_FIELD_NUMBER: _ClassVar[int]
    MAX_REUSE_FIELD_NUMBER: _ClassVar[int]
    POF_FIELD_NUMBER: _ClassVar[int]
    ZYMOCIDE_FIELD_NUMBER: _ClassVar[int]
    base: CultureBase
    id: str
    temperature_range: _measureable_units_pb2.TemperatureRangeType
    notes: str
    best_for: str
    inventory: CultureInventoryType
    alcohol_tolerance: _measureable_units_pb2.PercentType
    glucoamylase: bool
    type: CultureBaseType
    flocculation: QualitativeRangeUnit
    attenuation_range: _measureable_units_pb2.PercentRangeType
    max_reuse: int
    pof: bool
    zymocide: Zymocide
    def __init__(self, base: _Optional[_Union[CultureBase, _Mapping]] = ..., id: _Optional[str] = ..., temperature_range: _Optional[_Union[_measureable_units_pb2.TemperatureRangeType, _Mapping]] = ..., notes: _Optional[str] = ..., best_for: _Optional[str] = ..., inventory: _Optional[_Union[CultureInventoryType, _Mapping]] = ..., alcohol_tolerance: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., glucoamylase: _Optional[bool] = ..., type: _Optional[_Union[CultureBaseType, str]] = ..., flocculation: _Optional[_Union[QualitativeRangeUnit, str]] = ..., attenuation_range: _Optional[_Union[_measureable_units_pb2.PercentRangeType, _Mapping]] = ..., max_reuse: _Optional[int] = ..., pof: _Optional[bool] = ..., zymocide: _Optional[_Union[Zymocide, _Mapping]] = ...) -> None: ...

class CultureAdditionType(_message.Message):
    __slots__ = ("base", "id", "cell_count_billions", "times_cultured", "type", "attenuation", "timing", "mass", "unit", "volume")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CELL_COUNT_BILLIONS_FIELD_NUMBER: _ClassVar[int]
    TIMES_CULTURED_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTENUATION_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    MASS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    base: CultureBase
    id: str
    cell_count_billions: int
    times_cultured: int
    type: CultureBaseType
    attenuation: _measureable_units_pb2.PercentType
    timing: _timing_pb2.TimingType
    mass: _measureable_units_pb2.MassType
    unit: _measureable_units_pb2.UnitType
    volume: _measureable_units_pb2.VolumeType
    def __init__(self, base: _Optional[_Union[CultureBase, _Mapping]] = ..., id: _Optional[str] = ..., cell_count_billions: _Optional[int] = ..., times_cultured: _Optional[int] = ..., type: _Optional[_Union[CultureBaseType, str]] = ..., attenuation: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., timing: _Optional[_Union[_timing_pb2.TimingType, _Mapping]] = ..., mass: _Optional[_Union[_measureable_units_pb2.MassType, _Mapping]] = ..., unit: _Optional[_Union[_measureable_units_pb2.UnitType, _Mapping]] = ..., volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ...) -> None: ...

class CultureInventoryType(_message.Message):
    __slots__ = ("liquid", "dry", "slant", "culture", "manufacture_date", "generation")
    LIQUID_FIELD_NUMBER: _ClassVar[int]
    DRY_FIELD_NUMBER: _ClassVar[int]
    SLANT_FIELD_NUMBER: _ClassVar[int]
    CULTURE_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURE_DATE_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    liquid: _measureable_units_pb2.VolumeType
    dry: _measureable_units_pb2.MassType
    slant: _measureable_units_pb2.VolumeType
    culture: _measureable_units_pb2.VolumeType
    manufacture_date: str
    generation: int
    def __init__(self, liquid: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., dry: _Optional[_Union[_measureable_units_pb2.MassType, _Mapping]] = ..., slant: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., culture: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., manufacture_date: _Optional[str] = ..., generation: _Optional[int] = ...) -> None: ...

class Zymocide(_message.Message):
    __slots__ = ("no1", "no2", "no28", "klus", "neutral")
    NO1_FIELD_NUMBER: _ClassVar[int]
    NO2_FIELD_NUMBER: _ClassVar[int]
    NO28_FIELD_NUMBER: _ClassVar[int]
    KLUS_FIELD_NUMBER: _ClassVar[int]
    NEUTRAL_FIELD_NUMBER: _ClassVar[int]
    no1: bool
    no2: bool
    no28: bool
    klus: bool
    neutral: bool
    def __init__(self, no1: _Optional[bool] = ..., no2: _Optional[bool] = ..., no28: _Optional[bool] = ..., klus: _Optional[bool] = ..., neutral: _Optional[bool] = ...) -> None: ...
