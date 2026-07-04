from beerproto.v1 import fermentation_step_pb2 as _fermentation_step_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FermentationProcedureType(_message.Message):
    __slots__ = ("id", "description", "notes", "fermentation_steps", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    FERMENTATION_STEPS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    notes: str
    fermentation_steps: _containers.RepeatedCompositeFieldContainer[_fermentation_step_pb2.FermentationStepType]
    name: str
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., notes: _Optional[str] = ..., fermentation_steps: _Optional[_Iterable[_Union[_fermentation_step_pb2.FermentationStepType, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...
