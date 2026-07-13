from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FermentationStepType(_message.Message):
    __slots__ = ("id", "name", "end_temperature", "step_time", "free_rise", "start_gravity", "end_gravity", "start_ph", "description", "start_temperature", "end_ph", "vessel", "vessel_pressure")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    END_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    STEP_TIME_FIELD_NUMBER: _ClassVar[int]
    FREE_RISE_FIELD_NUMBER: _ClassVar[int]
    START_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    END_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    START_PH_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    START_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    END_PH_FIELD_NUMBER: _ClassVar[int]
    VESSEL_FIELD_NUMBER: _ClassVar[int]
    VESSEL_PRESSURE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    end_temperature: _measureable_units_pb2.TemperatureType
    step_time: _measureable_units_pb2.TimeType
    free_rise: bool
    start_gravity: _measureable_units_pb2.GravityType
    end_gravity: _measureable_units_pb2.GravityType
    start_ph: _measureable_units_pb2.AcidityType
    description: str
    start_temperature: _measureable_units_pb2.TemperatureType
    end_ph: _measureable_units_pb2.AcidityType
    vessel: str
    vessel_pressure: _measureable_units_pb2.PressureType
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., end_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ..., step_time: _Optional[_Union[_measureable_units_pb2.TimeType, _Mapping]] = ..., free_rise: _Optional[bool] = ..., start_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., end_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., start_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., description: _Optional[str] = ..., start_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ..., end_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., vessel: _Optional[str] = ..., vessel_pressure: _Optional[_Union[_measureable_units_pb2.PressureType, _Mapping]] = ...) -> None: ...
