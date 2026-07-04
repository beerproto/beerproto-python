from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MashStepUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MASH_STEP_UNIT_UNSPECIFIED: _ClassVar[MashStepUnit]
    MASH_STEP_UNIT_INFUSION: _ClassVar[MashStepUnit]
    MASH_STEP_UNIT_TEMPERATURE: _ClassVar[MashStepUnit]
    MASH_STEP_UNIT_DECOCTION: _ClassVar[MashStepUnit]
    MASH_STEP_UNIT_SOURING_MASH: _ClassVar[MashStepUnit]
    MASH_STEP_UNIT_SOURING_WORT: _ClassVar[MashStepUnit]
    MASH_STEP_UNIT_DRAIN_MASH_TUN: _ClassVar[MashStepUnit]
    MASH_STEP_UNIT_SPARGE: _ClassVar[MashStepUnit]
MASH_STEP_UNIT_UNSPECIFIED: MashStepUnit
MASH_STEP_UNIT_INFUSION: MashStepUnit
MASH_STEP_UNIT_TEMPERATURE: MashStepUnit
MASH_STEP_UNIT_DECOCTION: MashStepUnit
MASH_STEP_UNIT_SOURING_MASH: MashStepUnit
MASH_STEP_UNIT_SOURING_WORT: MashStepUnit
MASH_STEP_UNIT_DRAIN_MASH_TUN: MashStepUnit
MASH_STEP_UNIT_SPARGE: MashStepUnit

class MashStepType(_message.Message):
    __slots__ = ("id", "step_time", "ramp_time", "end_temperature", "description", "infuse_temperature", "start_ph", "end_ph", "name", "type", "amount", "step_temperature", "water_grain_ratio")
    ID_FIELD_NUMBER: _ClassVar[int]
    STEP_TIME_FIELD_NUMBER: _ClassVar[int]
    RAMP_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INFUSE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    START_PH_FIELD_NUMBER: _ClassVar[int]
    END_PH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    STEP_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    WATER_GRAIN_RATIO_FIELD_NUMBER: _ClassVar[int]
    id: str
    step_time: _measureable_units_pb2.TimeType
    ramp_time: _measureable_units_pb2.TimeType
    end_temperature: _measureable_units_pb2.TemperatureType
    description: str
    infuse_temperature: _measureable_units_pb2.TemperatureType
    start_ph: _measureable_units_pb2.AcidityType
    end_ph: _measureable_units_pb2.AcidityType
    name: str
    type: MashStepUnit
    amount: _measureable_units_pb2.VolumeType
    step_temperature: _measureable_units_pb2.TemperatureType
    water_grain_ratio: _measureable_units_pb2.SpecificVolumeType
    def __init__(self, id: _Optional[str] = ..., step_time: _Optional[_Union[_measureable_units_pb2.TimeType, _Mapping]] = ..., ramp_time: _Optional[_Union[_measureable_units_pb2.TimeType, _Mapping]] = ..., end_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ..., description: _Optional[str] = ..., infuse_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ..., start_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., end_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., name: _Optional[str] = ..., type: _Optional[_Union[MashStepUnit, str]] = ..., amount: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., step_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ..., water_grain_ratio: _Optional[_Union[_measureable_units_pb2.SpecificVolumeType, _Mapping]] = ...) -> None: ...
