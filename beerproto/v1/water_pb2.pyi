from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from beerproto.v1 import timing_pb2 as _timing_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WaterBase(_message.Message):
    __slots__ = ("calcium", "nitrite", "chloride", "name", "potassium", "carbonate", "iron", "flouride", "sulfate", "magnesium", "producer", "bicarbonate", "nitrate", "sodium")
    CALCIUM_FIELD_NUMBER: _ClassVar[int]
    NITRITE_FIELD_NUMBER: _ClassVar[int]
    CHLORIDE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POTASSIUM_FIELD_NUMBER: _ClassVar[int]
    CARBONATE_FIELD_NUMBER: _ClassVar[int]
    IRON_FIELD_NUMBER: _ClassVar[int]
    FLOURIDE_FIELD_NUMBER: _ClassVar[int]
    SULFATE_FIELD_NUMBER: _ClassVar[int]
    MAGNESIUM_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_FIELD_NUMBER: _ClassVar[int]
    BICARBONATE_FIELD_NUMBER: _ClassVar[int]
    NITRATE_FIELD_NUMBER: _ClassVar[int]
    SODIUM_FIELD_NUMBER: _ClassVar[int]
    calcium: _measureable_units_pb2.ConcentrationType
    nitrite: _measureable_units_pb2.ConcentrationType
    chloride: _measureable_units_pb2.ConcentrationType
    name: str
    potassium: _measureable_units_pb2.ConcentrationType
    carbonate: _measureable_units_pb2.ConcentrationType
    iron: _measureable_units_pb2.ConcentrationType
    flouride: _measureable_units_pb2.ConcentrationType
    sulfate: _measureable_units_pb2.ConcentrationType
    magnesium: _measureable_units_pb2.ConcentrationType
    producer: str
    bicarbonate: _measureable_units_pb2.ConcentrationType
    nitrate: _measureable_units_pb2.ConcentrationType
    sodium: _measureable_units_pb2.ConcentrationType
    def __init__(self, calcium: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., nitrite: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., chloride: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., name: _Optional[str] = ..., potassium: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., carbonate: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., iron: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., flouride: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., sulfate: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., magnesium: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., producer: _Optional[str] = ..., bicarbonate: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., nitrate: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ..., sodium: _Optional[_Union[_measureable_units_pb2.ConcentrationType, _Mapping]] = ...) -> None: ...

class WaterType(_message.Message):
    __slots__ = ("base", "id", "notes", "ph")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PH_FIELD_NUMBER: _ClassVar[int]
    base: WaterBase
    id: str
    notes: str
    ph: _measureable_units_pb2.AcidityType
    def __init__(self, base: _Optional[_Union[WaterBase, _Mapping]] = ..., id: _Optional[str] = ..., notes: _Optional[str] = ..., ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ...) -> None: ...

class WaterAdditionType(_message.Message):
    __slots__ = ("base", "id", "amount", "timing")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    base: WaterBase
    id: str
    amount: _measureable_units_pb2.VolumeType
    timing: _timing_pb2.TimingType
    def __init__(self, base: _Optional[_Union[WaterBase, _Mapping]] = ..., id: _Optional[str] = ..., amount: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., timing: _Optional[_Union[_timing_pb2.TimingType, _Mapping]] = ...) -> None: ...
