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

class MiscellaneousBaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MISCELLANEOUS_BASE_TYPE_UNSPECIFIED: _ClassVar[MiscellaneousBaseType]
    MISCELLANEOUS_BASE_TYPE_SPICE: _ClassVar[MiscellaneousBaseType]
    MISCELLANEOUS_BASE_TYPE_FINING: _ClassVar[MiscellaneousBaseType]
    MISCELLANEOUS_BASE_TYPE_WATER_AGENT: _ClassVar[MiscellaneousBaseType]
    MISCELLANEOUS_BASE_TYPE_HERB: _ClassVar[MiscellaneousBaseType]
    MISCELLANEOUS_BASE_TYPE_FLAVOR: _ClassVar[MiscellaneousBaseType]
    MISCELLANEOUS_BASE_TYPE_WOOD: _ClassVar[MiscellaneousBaseType]
    MISCELLANEOUS_BASE_TYPE_OTHER: _ClassVar[MiscellaneousBaseType]
MISCELLANEOUS_BASE_TYPE_UNSPECIFIED: MiscellaneousBaseType
MISCELLANEOUS_BASE_TYPE_SPICE: MiscellaneousBaseType
MISCELLANEOUS_BASE_TYPE_FINING: MiscellaneousBaseType
MISCELLANEOUS_BASE_TYPE_WATER_AGENT: MiscellaneousBaseType
MISCELLANEOUS_BASE_TYPE_HERB: MiscellaneousBaseType
MISCELLANEOUS_BASE_TYPE_FLAVOR: MiscellaneousBaseType
MISCELLANEOUS_BASE_TYPE_WOOD: MiscellaneousBaseType
MISCELLANEOUS_BASE_TYPE_OTHER: MiscellaneousBaseType

class MiscellaneousBase(_message.Message):
    __slots__ = ("name", "producer", "product_id", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    producer: str
    product_id: str
    type: MiscellaneousBaseType
    def __init__(self, name: _Optional[str] = ..., producer: _Optional[str] = ..., product_id: _Optional[str] = ..., type: _Optional[_Union[MiscellaneousBaseType, str]] = ...) -> None: ...

class MiscellaneousType(_message.Message):
    __slots__ = ("base", "id", "use_for", "notes", "inventory")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    USE_FOR_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    base: MiscellaneousBase
    id: str
    use_for: str
    notes: str
    inventory: MiscellaneousInventoryType
    def __init__(self, base: _Optional[_Union[MiscellaneousBase, _Mapping]] = ..., id: _Optional[str] = ..., use_for: _Optional[str] = ..., notes: _Optional[str] = ..., inventory: _Optional[_Union[MiscellaneousInventoryType, _Mapping]] = ...) -> None: ...

class MiscellaneousAdditionType(_message.Message):
    __slots__ = ("base", "id", "timing", "mass", "unit", "volume")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    MASS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    base: MiscellaneousBase
    id: str
    timing: _timing_pb2.TimingType
    mass: _measureable_units_pb2.MassType
    unit: _measureable_units_pb2.UnitType
    volume: _measureable_units_pb2.VolumeType
    def __init__(self, base: _Optional[_Union[MiscellaneousBase, _Mapping]] = ..., id: _Optional[str] = ..., timing: _Optional[_Union[_timing_pb2.TimingType, _Mapping]] = ..., mass: _Optional[_Union[_measureable_units_pb2.MassType, _Mapping]] = ..., unit: _Optional[_Union[_measureable_units_pb2.UnitType, _Mapping]] = ..., volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ...) -> None: ...

class MiscellaneousInventoryType(_message.Message):
    __slots__ = ("mass", "unit", "volume", "best_before")
    MASS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    BEST_BEFORE_FIELD_NUMBER: _ClassVar[int]
    mass: _measureable_units_pb2.MassType
    unit: _measureable_units_pb2.UnitType
    volume: _measureable_units_pb2.VolumeType
    best_before: _timestamp_pb2.Timestamp
    def __init__(self, mass: _Optional[_Union[_measureable_units_pb2.MassType, _Mapping]] = ..., unit: _Optional[_Union[_measureable_units_pb2.UnitType, _Mapping]] = ..., volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., best_before: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
