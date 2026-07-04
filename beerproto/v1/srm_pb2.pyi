from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SRM(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SRM_UNSPECIFIED: _ClassVar[SRM]
    SRM_1: _ClassVar[SRM]
    SRM_2: _ClassVar[SRM]
    SRM_3: _ClassVar[SRM]
    SRM_4: _ClassVar[SRM]
    SRM_5: _ClassVar[SRM]
    SRM_6: _ClassVar[SRM]
    SRM_7: _ClassVar[SRM]
    SRM_8: _ClassVar[SRM]
    SRM_9: _ClassVar[SRM]
    SRM_10: _ClassVar[SRM]
    SRM_11: _ClassVar[SRM]
    SRM_12: _ClassVar[SRM]
    SRM_13: _ClassVar[SRM]
    SRM_14: _ClassVar[SRM]
    SRM_15: _ClassVar[SRM]
    SRM_16: _ClassVar[SRM]
    SRM_17: _ClassVar[SRM]
    SRM_18: _ClassVar[SRM]
    SRM_19: _ClassVar[SRM]
    SRM_20: _ClassVar[SRM]
    SRM_21: _ClassVar[SRM]
    SRM_22: _ClassVar[SRM]
    SRM_23: _ClassVar[SRM]
    SRM_24: _ClassVar[SRM]
    SRM_25: _ClassVar[SRM]
    SRM_26: _ClassVar[SRM]
    SRM_27: _ClassVar[SRM]
    SRM_28: _ClassVar[SRM]
    SRM_29: _ClassVar[SRM]
    SRM_30: _ClassVar[SRM]
SRM_UNSPECIFIED: SRM
SRM_1: SRM
SRM_2: SRM
SRM_3: SRM
SRM_4: SRM
SRM_5: SRM
SRM_6: SRM
SRM_7: SRM
SRM_8: SRM
SRM_9: SRM
SRM_10: SRM
SRM_11: SRM
SRM_12: SRM
SRM_13: SRM
SRM_14: SRM
SRM_15: SRM
SRM_16: SRM
SRM_17: SRM
SRM_18: SRM
SRM_19: SRM
SRM_20: SRM
SRM_21: SRM
SRM_22: SRM
SRM_23: SRM
SRM_24: SRM
SRM_25: SRM
SRM_26: SRM
SRM_27: SRM
SRM_28: SRM
SRM_29: SRM
SRM_30: SRM
COLOR_FIELD_NUMBER: _ClassVar[int]
color: _descriptor.FieldDescriptor

class Color(_message.Message):
    __slots__ = ("a", "r", "g", "b")
    A_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    G_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    r: int
    g: int
    b: int
    def __init__(self, a: _Optional[int] = ..., r: _Optional[int] = ..., g: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...
