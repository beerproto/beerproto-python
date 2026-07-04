from beerproto.v1 import mash_step_pb2 as _mash_step_pb2
from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MashProcedureType(_message.Message):
    __slots__ = ("id", "grain_temperature", "notes", "mash_steps", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    GRAIN_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    MASH_STEPS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    grain_temperature: _measureable_units_pb2.TemperatureType
    notes: str
    mash_steps: _containers.RepeatedCompositeFieldContainer[_mash_step_pb2.MashStepType]
    name: str
    def __init__(self, id: _Optional[str] = ..., grain_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ..., notes: _Optional[str] = ..., mash_steps: _Optional[_Iterable[_Union[_mash_step_pb2.MashStepType, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...
