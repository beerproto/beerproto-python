from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from beerproto.v1 import packaging_graphic_pb2 as _packaging_graphic_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackagingVesselUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PACKAGING_VESSEL_UNIT_UNSPECIFIED: _ClassVar[PackagingVesselUnit]
    PACKAGING_VESSEL_UNIT_KEG: _ClassVar[PackagingVesselUnit]
    PACKAGING_VESSEL_UNIT_BOTTLE: _ClassVar[PackagingVesselUnit]
    PACKAGING_VESSEL_UNIT_CASK: _ClassVar[PackagingVesselUnit]
    PACKAGING_VESSEL_UNIT_TANK: _ClassVar[PackagingVesselUnit]
    PACKAGING_VESSEL_UNIT_FIRKIN: _ClassVar[PackagingVesselUnit]
    PACKAGING_VESSEL_UNIT_OTHER: _ClassVar[PackagingVesselUnit]
    PACKAGING_VESSEL_UNIT_CAN: _ClassVar[PackagingVesselUnit]

class CarbonationStep(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CARBONATION_STEP_UNSPECIFIED: _ClassVar[CarbonationStep]
    CARBONATION_STEP_FORCE_CARBONATION: _ClassVar[CarbonationStep]
    CARBONATION_STEP_PRIMING: _ClassVar[CarbonationStep]
    CARBONATION_STEP_SPUNDING: _ClassVar[CarbonationStep]
    CARBONATION_STEP_NATURAL_CONDITIONING: _ClassVar[CarbonationStep]
PACKAGING_VESSEL_UNIT_UNSPECIFIED: PackagingVesselUnit
PACKAGING_VESSEL_UNIT_KEG: PackagingVesselUnit
PACKAGING_VESSEL_UNIT_BOTTLE: PackagingVesselUnit
PACKAGING_VESSEL_UNIT_CASK: PackagingVesselUnit
PACKAGING_VESSEL_UNIT_TANK: PackagingVesselUnit
PACKAGING_VESSEL_UNIT_FIRKIN: PackagingVesselUnit
PACKAGING_VESSEL_UNIT_OTHER: PackagingVesselUnit
PACKAGING_VESSEL_UNIT_CAN: PackagingVesselUnit
CARBONATION_STEP_UNSPECIFIED: CarbonationStep
CARBONATION_STEP_FORCE_CARBONATION: CarbonationStep
CARBONATION_STEP_PRIMING: CarbonationStep
CARBONATION_STEP_SPUNDING: CarbonationStep
CARBONATION_STEP_NATURAL_CONDITIONING: CarbonationStep

class PackagingVesselBase(_message.Message):
    __slots__ = ("name", "type", "vessel_volume", "vessel_quantity", "description", "graphics")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VESSEL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    VESSEL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GRAPHICS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: PackagingVesselUnit
    vessel_volume: _measureable_units_pb2.VolumeType
    vessel_quantity: int
    description: str
    graphics: _containers.RepeatedCompositeFieldContainer[_packaging_graphic_pb2.PackagingGraphicType]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[PackagingVesselUnit, str]] = ..., vessel_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., vessel_quantity: _Optional[int] = ..., description: _Optional[str] = ..., graphics: _Optional[_Iterable[_Union[_packaging_graphic_pb2.PackagingGraphicType, _Mapping]]] = ...) -> None: ...

class PackagingVesselType(_message.Message):
    __slots__ = ("base", "id", "package_date", "step_time", "start_gravity", "end_gravity", "start_ph", "end_ph", "start_temperature", "end_temperature", "target_carbonation", "notes", "carbonation_step")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_DATE_FIELD_NUMBER: _ClassVar[int]
    STEP_TIME_FIELD_NUMBER: _ClassVar[int]
    START_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    END_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    START_PH_FIELD_NUMBER: _ClassVar[int]
    END_PH_FIELD_NUMBER: _ClassVar[int]
    START_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    END_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TARGET_CARBONATION_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CARBONATION_STEP_FIELD_NUMBER: _ClassVar[int]
    base: PackagingVesselBase
    id: str
    package_date: str
    step_time: _measureable_units_pb2.TimeType
    start_gravity: _measureable_units_pb2.GravityType
    end_gravity: _measureable_units_pb2.GravityType
    start_ph: _measureable_units_pb2.AcidityType
    end_ph: _measureable_units_pb2.AcidityType
    start_temperature: _measureable_units_pb2.TemperatureType
    end_temperature: _measureable_units_pb2.TemperatureType
    target_carbonation: _measureable_units_pb2.CarbonationType
    notes: str
    carbonation_step: CarbonationStep
    def __init__(self, base: _Optional[_Union[PackagingVesselBase, _Mapping]] = ..., id: _Optional[str] = ..., package_date: _Optional[str] = ..., step_time: _Optional[_Union[_measureable_units_pb2.TimeType, _Mapping]] = ..., start_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., end_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., start_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., end_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., start_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ..., end_temperature: _Optional[_Union[_measureable_units_pb2.TemperatureType, _Mapping]] = ..., target_carbonation: _Optional[_Union[_measureable_units_pb2.CarbonationType, _Mapping]] = ..., notes: _Optional[str] = ..., carbonation_step: _Optional[_Union[CarbonationStep, str]] = ...) -> None: ...
