from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoilStepTypeChillingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BOIL_STEP_TYPE_CHILLING_TYPE_UNSPECIFIED: _ClassVar[BoilStepTypeChillingType]
    BOIL_STEP_TYPE_CHILLING_TYPE_BATCH: _ClassVar[BoilStepTypeChillingType]
    BOIL_STEP_TYPE_CHILLING_TYPE_INLINE: _ClassVar[BoilStepTypeChillingType]
BOIL_STEP_TYPE_CHILLING_TYPE_UNSPECIFIED: BoilStepTypeChillingType
BOIL_STEP_TYPE_CHILLING_TYPE_BATCH: BoilStepTypeChillingType
BOIL_STEP_TYPE_CHILLING_TYPE_INLINE: BoilStepTypeChillingType

class BoilStepType(_message.Message):
    __slots__ = ("id", "end_gravity", "chilling_type", "description", "end_temperature", "ramp_time", "step_time", "start_gravity", "start_ph", "end_ph", "name", "start_temperature")
    ID_FIELD_NUMBER: _ClassVar[int]
    END_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    CHILLING_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    END_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    RAMP_TIME_FIELD_NUMBER: _ClassVar[int]
    STEP_TIME_FIELD_NUMBER: _ClassVar[int]
    START_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    START_PH_FIELD_NUMBER: _ClassVar[int]
    END_PH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    id: str
    end_gravity: _measureable_units_pb2.GravityType
    chilling_type: BoilStepTypeChillingType
    description: str
    end_temperature: _measureable_units_pb2.TemperatureType
    ramp_time: _measureable_units_pb2.TimeType
    step_time: _measureable_units_pb2.TimeType
    start_gravity: _measureable_units_pb2.GravityType
    start_ph: _measureable_units_pb2.AcidityType
    end_ph: _measureable_units_pb2.AcidityType
    name: str
    start_temperature: _measureable_units_pb2.TemperatureType
    def __init__(self, id: _Optional[str] = ..., end_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., chilling_type: _Optional[_Union[BoilStepTypeChillingType, str]] = ..., description: _Optional[str] = ..., end_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ..., ramp_time: _Optional[_Union[_measureable_units_pb2.TimeType, _Mapping]] = ..., step_time: _Optional[_Union[_measureable_units_pb2.TimeType, _Mapping]] = ..., start_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., start_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., end_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., name: _Optional[str] = ..., start_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ...) -> None: ...
