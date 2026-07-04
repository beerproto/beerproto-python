from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackagingGraphicType(_message.Message):
    __slots__ = ("position", "type", "base64_data", "urls", "dpi", "width", "height", "units")
    class PositionUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POSITION_UNIT_UNSPECIFIED: _ClassVar[PackagingGraphicType.PositionUnit]
        POSITION_UNIT_BODY_FRONT: _ClassVar[PackagingGraphicType.PositionUnit]
        POSITION_UNIT_BODY_BACK: _ClassVar[PackagingGraphicType.PositionUnit]
        POSITION_UNIT_BODY_WRAP_AROUND: _ClassVar[PackagingGraphicType.PositionUnit]
        POSITION_UNIT_NECK_FRONT: _ClassVar[PackagingGraphicType.PositionUnit]
        POSITION_UNIT_NECK_BACK: _ClassVar[PackagingGraphicType.PositionUnit]
        POSITION_UNIT_NECK_WRAP_AROUND: _ClassVar[PackagingGraphicType.PositionUnit]
        POSITION_UNIT_CAP: _ClassVar[PackagingGraphicType.PositionUnit]
        POSITION_UNIT_CARRIER: _ClassVar[PackagingGraphicType.PositionUnit]
    POSITION_UNIT_UNSPECIFIED: PackagingGraphicType.PositionUnit
    POSITION_UNIT_BODY_FRONT: PackagingGraphicType.PositionUnit
    POSITION_UNIT_BODY_BACK: PackagingGraphicType.PositionUnit
    POSITION_UNIT_BODY_WRAP_AROUND: PackagingGraphicType.PositionUnit
    POSITION_UNIT_NECK_FRONT: PackagingGraphicType.PositionUnit
    POSITION_UNIT_NECK_BACK: PackagingGraphicType.PositionUnit
    POSITION_UNIT_NECK_WRAP_AROUND: PackagingGraphicType.PositionUnit
    POSITION_UNIT_CAP: PackagingGraphicType.PositionUnit
    POSITION_UNIT_CARRIER: PackagingGraphicType.PositionUnit
    class GraphicType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GRAPHIC_TYPE_UNSPECIFIED: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_SVG: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_SVGZ: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_AI: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_CDR: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_CDX: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_ODG: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_EPS: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_PDF: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_PNG: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_JPG: _ClassVar[PackagingGraphicType.GraphicType]
        GRAPHIC_TYPE_GIF: _ClassVar[PackagingGraphicType.GraphicType]
    GRAPHIC_TYPE_UNSPECIFIED: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_SVG: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_SVGZ: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_AI: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_CDR: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_CDX: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_ODG: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_EPS: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_PDF: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_PNG: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_JPG: PackagingGraphicType.GraphicType
    GRAPHIC_TYPE_GIF: PackagingGraphicType.GraphicType
    class UnitsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNITS_TYPE_UNSPECIFIED: _ClassVar[PackagingGraphicType.UnitsType]
        UNITS_TYPE_MM: _ClassVar[PackagingGraphicType.UnitsType]
        UNITS_TYPE_IN: _ClassVar[PackagingGraphicType.UnitsType]
    UNITS_TYPE_UNSPECIFIED: PackagingGraphicType.UnitsType
    UNITS_TYPE_MM: PackagingGraphicType.UnitsType
    UNITS_TYPE_IN: PackagingGraphicType.UnitsType
    POSITION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BASE64_DATA_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    DPI_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    position: PackagingGraphicType.PositionUnit
    type: PackagingGraphicType.GraphicType
    base64_data: str
    urls: _containers.RepeatedScalarFieldContainer[str]
    dpi: int
    width: int
    height: int
    units: PackagingGraphicType.UnitsType
    def __init__(self, position: _Optional[_Union[PackagingGraphicType.PositionUnit, str]] = ..., type: _Optional[_Union[PackagingGraphicType.GraphicType, str]] = ..., base64_data: _Optional[str] = ..., urls: _Optional[_Iterable[str]] = ..., dpi: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., units: _Optional[_Union[PackagingGraphicType.UnitsType, str]] = ...) -> None: ...
