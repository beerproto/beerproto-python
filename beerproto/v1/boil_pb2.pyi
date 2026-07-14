from beerproto.v1 import boil_step_pb2 as _boil_step_pb2
from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoilProcedureType(_message.Message):
    __slots__ = ("id", "pre_boil_size", "boil_time", "boil_steps", "name", "description", "notes", "whirlpool_temperature")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRE_BOIL_SIZE_FIELD_NUMBER: _ClassVar[int]
    BOIL_TIME_FIELD_NUMBER: _ClassVar[int]
    BOIL_STEPS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    WHIRLPOOL_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    id: str
    pre_boil_size: _measureable_units_pb2.VolumeType
    boil_time: _measureable_units_pb2.TimeType
    boil_steps: _containers.RepeatedCompositeFieldContainer[_boil_step_pb2.BoilStepType]
    name: str
    description: str
    notes: str
    whirlpool_temperature: _measureable_units_pb2.TemperatureType
    def __init__(self, id: _Optional[str] = ..., pre_boil_size: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., boil_time: _Optional[_Union[_measureable_units_pb2.TimeType, _Mapping]] = ..., boil_steps: _Optional[_Iterable[_Union[_boil_step_pb2.BoilStepType, _Mapping]]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., notes: _Optional[str] = ..., whirlpool_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ...) -> None: ...
