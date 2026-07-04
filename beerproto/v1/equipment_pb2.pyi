from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipmentBaseForm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EQUIPMENT_BASE_FORM_UNSPECIFIED: _ClassVar[EquipmentBaseForm]
    EQUIPMENT_BASE_FORM_HLT: _ClassVar[EquipmentBaseForm]
    EQUIPMENT_BASE_FORM_MASH_TUN: _ClassVar[EquipmentBaseForm]
    EQUIPMENT_BASE_FORM_LAUTER_TUN: _ClassVar[EquipmentBaseForm]
    EQUIPMENT_BASE_FORM_BREW_KETTLE: _ClassVar[EquipmentBaseForm]
    EQUIPMENT_BASE_FORM_FERMENTER: _ClassVar[EquipmentBaseForm]
    EQUIPMENT_BASE_FORM_AGING_VESSEL: _ClassVar[EquipmentBaseForm]
    EQUIPMENT_BASE_FORM_PACKAGING_VESSEL: _ClassVar[EquipmentBaseForm]
    EQUIPMENT_BASE_FORM_WHIRLPOOL_VESSEL: _ClassVar[EquipmentBaseForm]
EQUIPMENT_BASE_FORM_UNSPECIFIED: EquipmentBaseForm
EQUIPMENT_BASE_FORM_HLT: EquipmentBaseForm
EQUIPMENT_BASE_FORM_MASH_TUN: EquipmentBaseForm
EQUIPMENT_BASE_FORM_LAUTER_TUN: EquipmentBaseForm
EQUIPMENT_BASE_FORM_BREW_KETTLE: EquipmentBaseForm
EQUIPMENT_BASE_FORM_FERMENTER: EquipmentBaseForm
EQUIPMENT_BASE_FORM_AGING_VESSEL: EquipmentBaseForm
EQUIPMENT_BASE_FORM_PACKAGING_VESSEL: EquipmentBaseForm
EQUIPMENT_BASE_FORM_WHIRLPOOL_VESSEL: EquipmentBaseForm

class EquipmentBase(_message.Message):
    __slots__ = ("name", "type", "form", "maximum_volume")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_VOLUME_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    form: EquipmentBaseForm
    maximum_volume: _measureable_units_pb2.VolumeType
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., form: _Optional[_Union[EquipmentBaseForm, str]] = ..., maximum_volume: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ...) -> None: ...

class EquipmentItemType(_message.Message):
    __slots__ = ("base", "id", "notes", "boil_rate_per_hour", "drain_rate_per_minute", "specific_heat", "grain_absorption_rate", "weight", "loss", "efficiency", "transfer_loss")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    BOIL_RATE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    DRAIN_RATE_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_HEAT_FIELD_NUMBER: _ClassVar[int]
    GRAIN_ABSORPTION_RATE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    LOSS_FIELD_NUMBER: _ClassVar[int]
    EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_LOSS_FIELD_NUMBER: _ClassVar[int]
    base: EquipmentBase
    id: str
    notes: str
    boil_rate_per_hour: _measureable_units_pb2.VolumeType
    drain_rate_per_minute: _measureable_units_pb2.VolumeType
    specific_heat: _measureable_units_pb2.SpecificHeatType
    grain_absorption_rate: _measureable_units_pb2.SpecificVolumeType
    weight: _measureable_units_pb2.MassType
    loss: _measureable_units_pb2.VolumeType
    efficiency: _measureable_units_pb2.PercentType
    transfer_loss: _measureable_units_pb2.VolumeType
    def __init__(self, base: _Optional[_Union[EquipmentBase, _Mapping]] = ..., id: _Optional[str] = ..., notes: _Optional[str] = ..., boil_rate_per_hour: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., drain_rate_per_minute: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., specific_heat: _Optional[_Union[_measureable_units_pb2.SpecificHeatType, _Mapping]] = ..., grain_absorption_rate: _Optional[_Union[_measureable_units_pb2.SpecificVolumeType, _Mapping]] = ..., weight: _Optional[_Union[_measureable_units_pb2.MassType, _Mapping]] = ..., loss: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., efficiency: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., transfer_loss: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ...) -> None: ...

class EquipmentType(_message.Message):
    __slots__ = ("id", "name", "equipment_items", "brewhouse_efficiency")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EQUIPMENT_ITEMS_FIELD_NUMBER: _ClassVar[int]
    BREWHOUSE_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    equipment_items: _containers.RepeatedCompositeFieldContainer[EquipmentItemType]
    brewhouse_efficiency: _measureable_units_pb2.PercentType
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., equipment_items: _Optional[_Iterable[_Union[EquipmentItemType, _Mapping]]] = ..., brewhouse_efficiency: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ...) -> None: ...
