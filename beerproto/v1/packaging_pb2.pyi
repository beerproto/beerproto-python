from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from beerproto.v1 import packaging_vessel_pb2 as _packaging_vessel_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackagingProcedureType(_message.Message):
    __slots__ = ("id", "name", "packaged_volume", "description", "notes", "packaging_vessels")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGED_VOLUME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PACKAGING_VESSELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    packaged_volume: _measureable_units_pb2.VolumeType
    description: str
    notes: str
    packaging_vessels: _containers.RepeatedCompositeFieldContainer[_packaging_vessel_pb2.PackagingVesselType]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., packaged_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., description: _Optional[str] = ..., notes: _Optional[str] = ..., packaging_vessels: _Optional[_Iterable[_Union[_packaging_vessel_pb2.PackagingVesselType, _Mapping]]] = ...) -> None: ...
