from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USE_TYPE_UNSPECIFIED: _ClassVar[UseType]
    USE_TYPE_ADD_TO_MASH: _ClassVar[UseType]
    USE_TYPE_ADD_TO_BOIL: _ClassVar[UseType]
    USE_TYPE_ADD_TO_FERMENTATION: _ClassVar[UseType]
    USE_TYPE_ADD_TO_PACKAGE: _ClassVar[UseType]
USE_TYPE_UNSPECIFIED: UseType
USE_TYPE_ADD_TO_MASH: UseType
USE_TYPE_ADD_TO_BOIL: UseType
USE_TYPE_ADD_TO_FERMENTATION: UseType
USE_TYPE_ADD_TO_PACKAGE: UseType

class TimingType(_message.Message):
    __slots__ = ("time", "duration", "continuous", "specific_gravity", "ph", "step", "use")
    TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    PH_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    USE_FIELD_NUMBER: _ClassVar[int]
    time: _measureable_units_pb2.TimeType
    duration: _measureable_units_pb2.TimeType
    continuous: bool
    specific_gravity: _measureable_units_pb2.GravityType
    ph: _measureable_units_pb2.AcidityType
    step: int
    use: UseType
    def __init__(self, time: _Optional[_Union[_measureable_units_pb2.TimeType, _Mapping]] = ..., duration: _Optional[_Union[_measureable_units_pb2.TimeType, _Mapping]] = ..., continuous: _Optional[bool] = ..., specific_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., step: _Optional[int] = ..., use: _Optional[_Union[UseType, str]] = ...) -> None: ...
