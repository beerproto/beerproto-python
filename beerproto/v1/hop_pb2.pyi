from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from beerproto.v1 import timing_pb2 as _timing_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VarietyInformationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VARIETY_INFORMATION_TYPE_UNSPECIFIED: _ClassVar[VarietyInformationType]
    VARIETY_INFORMATION_TYPE_AROMA: _ClassVar[VarietyInformationType]
    VARIETY_INFORMATION_TYPE_BITTERING: _ClassVar[VarietyInformationType]
    VARIETY_INFORMATION_TYPE_FLAVOR: _ClassVar[VarietyInformationType]
    VARIETY_INFORMATION_TYPE_AROMA_BITTERING: _ClassVar[VarietyInformationType]
    VARIETY_INFORMATION_TYPE_BITTERING_FLAVOR: _ClassVar[VarietyInformationType]
    VARIETY_INFORMATION_TYPE_AROMA_FLAVOR: _ClassVar[VarietyInformationType]
    VARIETY_INFORMATION_TYPE_AROMA_BITTERING_FLAVOR: _ClassVar[VarietyInformationType]

class HopVarietyBaseForm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HOP_VARIETY_BASE_FORM_UNSPECIFIED: _ClassVar[HopVarietyBaseForm]
    HOP_VARIETY_BASE_FORM_EXTRACT: _ClassVar[HopVarietyBaseForm]
    HOP_VARIETY_BASE_FORM_LEAF: _ClassVar[HopVarietyBaseForm]
    HOP_VARIETY_BASE_FORM_LEAFWET: _ClassVar[HopVarietyBaseForm]
    HOP_VARIETY_BASE_FORM_PELLET: _ClassVar[HopVarietyBaseForm]
    HOP_VARIETY_BASE_FORM_POWDER: _ClassVar[HopVarietyBaseForm]
    HOP_VARIETY_BASE_FORM_PLUG: _ClassVar[HopVarietyBaseForm]

class IBUMethodUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IBU_METHOD_UNIT_UNSPECIFIED: _ClassVar[IBUMethodUnit]
    IBU_METHOD_UNIT_RAGER: _ClassVar[IBUMethodUnit]
    IBU_METHOD_UNIT_TINSETH: _ClassVar[IBUMethodUnit]
    IBU_METHOD_UNIT_GARETZ: _ClassVar[IBUMethodUnit]
    IBU_METHOD_UNIT_OTHER: _ClassVar[IBUMethodUnit]
VARIETY_INFORMATION_TYPE_UNSPECIFIED: VarietyInformationType
VARIETY_INFORMATION_TYPE_AROMA: VarietyInformationType
VARIETY_INFORMATION_TYPE_BITTERING: VarietyInformationType
VARIETY_INFORMATION_TYPE_FLAVOR: VarietyInformationType
VARIETY_INFORMATION_TYPE_AROMA_BITTERING: VarietyInformationType
VARIETY_INFORMATION_TYPE_BITTERING_FLAVOR: VarietyInformationType
VARIETY_INFORMATION_TYPE_AROMA_FLAVOR: VarietyInformationType
VARIETY_INFORMATION_TYPE_AROMA_BITTERING_FLAVOR: VarietyInformationType
HOP_VARIETY_BASE_FORM_UNSPECIFIED: HopVarietyBaseForm
HOP_VARIETY_BASE_FORM_EXTRACT: HopVarietyBaseForm
HOP_VARIETY_BASE_FORM_LEAF: HopVarietyBaseForm
HOP_VARIETY_BASE_FORM_LEAFWET: HopVarietyBaseForm
HOP_VARIETY_BASE_FORM_PELLET: HopVarietyBaseForm
HOP_VARIETY_BASE_FORM_POWDER: HopVarietyBaseForm
HOP_VARIETY_BASE_FORM_PLUG: HopVarietyBaseForm
IBU_METHOD_UNIT_UNSPECIFIED: IBUMethodUnit
IBU_METHOD_UNIT_RAGER: IBUMethodUnit
IBU_METHOD_UNIT_TINSETH: IBUMethodUnit
IBU_METHOD_UNIT_GARETZ: IBUMethodUnit
IBU_METHOD_UNIT_OTHER: IBUMethodUnit

class HopVarietyBase(_message.Message):
    __slots__ = ("name", "producer", "product_id", "origin", "year", "form", "alpha_acid", "beta_acid", "percent_lost")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELD_NUMBER: _ClassVar[int]
    ALPHA_ACID_FIELD_NUMBER: _ClassVar[int]
    BETA_ACID_FIELD_NUMBER: _ClassVar[int]
    PERCENT_LOST_FIELD_NUMBER: _ClassVar[int]
    name: str
    producer: str
    product_id: str
    origin: str
    year: str
    form: HopVarietyBaseForm
    alpha_acid: _measureable_units_pb2.PercentType
    beta_acid: _measureable_units_pb2.PercentType
    percent_lost: _measureable_units_pb2.PercentType
    def __init__(self, name: _Optional[str] = ..., producer: _Optional[str] = ..., product_id: _Optional[str] = ..., origin: _Optional[str] = ..., year: _Optional[str] = ..., form: _Optional[_Union[HopVarietyBaseForm, str]] = ..., alpha_acid: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., beta_acid: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., percent_lost: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ...) -> None: ...

class VarietyInformation(_message.Message):
    __slots__ = ("base", "id", "inventory", "type", "oil_content", "percent_lost", "substitutes", "notes")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OIL_CONTENT_FIELD_NUMBER: _ClassVar[int]
    PERCENT_LOST_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTES_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    base: HopVarietyBase
    id: str
    inventory: HopInventoryType
    type: VarietyInformationType
    oil_content: OilContentType
    percent_lost: _measureable_units_pb2.PercentType
    substitutes: str
    notes: str
    def __init__(self, base: _Optional[_Union[HopVarietyBase, _Mapping]] = ..., id: _Optional[str] = ..., inventory: _Optional[_Union[HopInventoryType, _Mapping]] = ..., type: _Optional[_Union[VarietyInformationType, str]] = ..., oil_content: _Optional[_Union[OilContentType, _Mapping]] = ..., percent_lost: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., substitutes: _Optional[str] = ..., notes: _Optional[str] = ...) -> None: ...

class HopAdditionType(_message.Message):
    __slots__ = ("base", "id", "timing", "mass", "volume")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    MASS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    base: HopVarietyBase
    id: str
    timing: _timing_pb2.TimingType
    mass: _measureable_units_pb2.MassType
    volume: _measureable_units_pb2.VolumeType
    def __init__(self, base: _Optional[_Union[HopVarietyBase, _Mapping]] = ..., id: _Optional[str] = ..., timing: _Optional[_Union[_timing_pb2.TimingType, _Mapping]] = ..., mass: _Optional[_Union[_measureable_units_pb2.MassType, _Mapping]] = ..., volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ...) -> None: ...

class IBUEstimateType(_message.Message):
    __slots__ = ("method",)
    METHOD_FIELD_NUMBER: _ClassVar[int]
    method: IBUMethodUnit
    def __init__(self, method: _Optional[_Union[IBUMethodUnit, str]] = ...) -> None: ...

class OilContentType(_message.Message):
    __slots__ = ("polyphenols", "total_oil_ml_per_100g", "farnesene", "limonene", "nerol", "geraniol", "b_pinene", "linalool", "caryophyllene", "cohumulone", "xanthohumol", "humulene", "myrcene", "pinene")
    POLYPHENOLS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OIL_ML_PER_100G_FIELD_NUMBER: _ClassVar[int]
    FARNESENE_FIELD_NUMBER: _ClassVar[int]
    LIMONENE_FIELD_NUMBER: _ClassVar[int]
    NEROL_FIELD_NUMBER: _ClassVar[int]
    GERANIOL_FIELD_NUMBER: _ClassVar[int]
    B_PINENE_FIELD_NUMBER: _ClassVar[int]
    LINALOOL_FIELD_NUMBER: _ClassVar[int]
    CARYOPHYLLENE_FIELD_NUMBER: _ClassVar[int]
    COHUMULONE_FIELD_NUMBER: _ClassVar[int]
    XANTHOHUMOL_FIELD_NUMBER: _ClassVar[int]
    HUMULENE_FIELD_NUMBER: _ClassVar[int]
    MYRCENE_FIELD_NUMBER: _ClassVar[int]
    PINENE_FIELD_NUMBER: _ClassVar[int]
    polyphenols: _measureable_units_pb2.PercentType
    total_oil_ml_per_100g: float
    farnesene: _measureable_units_pb2.PercentType
    limonene: _measureable_units_pb2.PercentType
    nerol: _measureable_units_pb2.PercentType
    geraniol: _measureable_units_pb2.PercentType
    b_pinene: _measureable_units_pb2.PercentType
    linalool: _measureable_units_pb2.PercentType
    caryophyllene: _measureable_units_pb2.PercentType
    cohumulone: _measureable_units_pb2.PercentType
    xanthohumol: _measureable_units_pb2.PercentType
    humulene: _measureable_units_pb2.PercentType
    myrcene: _measureable_units_pb2.PercentType
    pinene: _measureable_units_pb2.PercentType
    def __init__(self, polyphenols: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., total_oil_ml_per_100g: _Optional[float] = ..., farnesene: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., limonene: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., nerol: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., geraniol: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., b_pinene: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., linalool: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., caryophyllene: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., cohumulone: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., xanthohumol: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., humulene: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., myrcene: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., pinene: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ...) -> None: ...

class HopInventoryType(_message.Message):
    __slots__ = ("mass", "volume")
    MASS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    mass: _measureable_units_pb2.MassType
    volume: _measureable_units_pb2.VolumeType
    def __init__(self, mass: _Optional[_Union[_measureable_units_pb2.MassType, _Mapping]] = ..., volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ...) -> None: ...
