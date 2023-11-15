import dataclasses
import datetime

from pyactus.types.core import Cycle
from pyactus.types.core import Period
from pyactus.types.enums import ENUM_SET
from pyactus.utils import convertor
from pyactus.utils import logger


def decode_entity(typeof: type, encoded: dict):
    """Decodes a domain entity from it's dictionary representation.

    :param typeof: Type of domain entity to be decoded.
    :param encoded: Dictionary representation of a domain entity.
    :returns: A decoded domain entity.

    """
    entity: object = typeof()
    for fld in dataclasses.fields(typeof):
        setattr(entity, fld.name, _get_attr_value(entity, fld, encoded))

    return entity


def _get_attr_value(entity: object, fld: dataclasses.Field, encoded: dict):
    """Returns value of a field declared within a domain entity.

    """
    attr_name: str = convertor.to_pascal_case(fld.name)
    for encoded_name in encoded.keys():
        if encoded_name != attr_name:
            continue

        if fld.type in ENUM_SET:
            try:
                return convertor.to_enum(encoded[encoded_name], fld.type)
            except:
                logger.log_warning(f"Invalid enum member: {fld.type}.{encoded[encoded_name]}")
                break
            print(fld.name, fld.type, convertor.to_enum(encoded[encoded_name], fld.type))

        try:
            fld_mapper = _FIELD_MAPPERS[fld.type]
        except KeyError:
            logger.log_warning(f"Unsupported mapping target type: [{fld.type}].")
            break

        try:
            return fld_mapper(encoded[encoded_name], fld.type)
        except NotImplementedError:
            logger.log_warning(f"Unsupported mapping: '{type(entity).__name__}.{fld.name}'")
            break


# Map: Primitive type <-> Mapping function.
_FIELD_MAPPERS = {
    Cycle: lambda x, _: convertor.to_time_cycle(x),
    Period: lambda x, _: convertor.to_time_period(x),
    datetime.datetime: lambda x, _: convertor.to_datetime(x),
    datetime.timedelta: lambda x, _: convertor.to_timedelta(x),
    float: lambda x, _: convertor.to_float(x),
    str: lambda x, _: convertor.to_str(x),
} | {i: convertor.to_enum for i in ENUM_SET}
