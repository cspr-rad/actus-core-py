import dataclasses
import datetime
import json
import os
import pathlib
import typing
import uuid

import pytest

from pyactus.types.enums import ContractType
from pyactus.utils import convertor
from tests.fixtures.model import ContractTestData


# Path to test assets folder.
_ASSETS: pathlib.Path = pathlib.Path(os.path.dirname(__file__)).parent / "assets"


@pytest.fixture(scope="session")
def test_contracts() -> typing.List[typing.Tuple[ContractType, dict]]:
    """Returns set of test contract fixtures.

    """
    return list(_yield_contracts())


def _yield_contracts() -> typing.Iterator[typing.Tuple[ContractType, dict]]:
    """Yields set of test contract fixtures.

    """
    for contract_type in ContractType:
        for obj in _read_fixtures(contract_type):
            if "contractType" not in obj:
                obj["contractType"] = contract_type.name            
            yield contract_type, _map_fixture(contract_type, obj)


@pytest.fixture(scope="session")
def test_contracts1() -> typing.List[ContractTestData]:
    """Returns set of test contract fixtures.

    """
    def _yield_contracts() -> typing.Iterator[ContractTestData]:
        """Yields set of test contract fixtures.

        """
        for contract_type in ContractType:
            for obj in _read_fixtures(contract_type):
                if "contractType" not in obj:
                    obj["contractType"] = contract_type.name            
                yield _map_fixture1(contract_type, obj)

    return _yield_contracts()


def _read_fixtures(contract_type: ContractType) -> typing.List[dict]:
    """Reads an official ACTUS text fixture into memory.

    """
    fname: str = f"actus-tests-{contract_type.name.lower()}.json"
    fpath: pathlib.Path = _ASSETS / fname
    if not fpath.exists():
        return []

    with open(fpath, "r") as fstream:
        return json.loads(fstream.read()).values()


def _map_fixture(contract_type: ContractType, obj: dict) -> dict:
    """Maps a test contract fixture to it's over the wire ACTUS representation.

    """
    def _map_event(obj: dict):
        return obj | {
            "eventTimestamp": obj["eventDate"]
        }

    def _map_term_set():
        def _map_name(name: str):
            if name.endswith("ID"):
                return f"{name[:-2]}Id"
            elif name == "fixingDays":
                return "fixingPeriod"
            else:
                return name

        def _map_value(name: str, value: object):
            if name == "arrayFixedVariable" and isinstance(value, list):
                return [i[0] for i in value]
            elif name == "calendar" and value == "NOCALENDAR":
                return "NC"
            else:
                return value

        return {_map_name(k): _map_value(k, v) for k, v in obj["terms"].items()}

    def _map_to_date(val: str) -> datetime.datetime:
        val = val.strip()
        if val == "":
            try:
                val = obj["terms"]["maturityDate"]
            except KeyError:
                return None

        return convertor.to_iso_datetime(val)

    return {
        "contract_id": obj["terms"]["contractID"],
        "contract_type": contract_type.name,
        "event_sequence": [_map_event(i) for i in obj["results"]],
        "observed_data": obj["dataObserved"],
        "term_set": _map_term_set(),
        "to_date": _map_to_date(obj["to"])
    }


def _map_fixture1(contract_type: ContractType, obj: dict) -> ContractTestData:
    """Maps a test contract fixture to it's over the wire ACTUS representation.

    """
    def _map_event(obj: dict):
        return obj | {
            "eventTimestamp": obj["eventDate"]
        }
    
    def _map_observed_data(data: dict) -> typing.Optional[dict]:
        if data:
            return data

    def _map_observed_events(data: typing.List[dict]) -> typing.List[dict]:
        return data

    def _map_term_set():
        def _map_name(name: str):
            if name.endswith("ID"):
                return f"{name[:-2]}Id"
            elif name == "fixingDays":
                return "fixingPeriod"
            else:
                return name

        def _map_value(name: str, value: object):
            if name == "arrayFixedVariable" and isinstance(value, list):
                return [i[0] for i in value]
            elif name == "calendar" and value == "NOCALENDAR":
                return "NC"
            else:
                return value

        return {_map_name(k): _map_value(k, v) for k, v in obj["terms"].items()}

    def _map_to_date(val: str) -> datetime.datetime:
        val = val.strip()
        if val == "":
            try:
                val = obj["terms"]["maturityDate"]
            except KeyError:
                return None

        return convertor.to_iso_datetime(val)

    return ContractTestData(
        contract_id=obj["terms"]["contractID"],
        contract_type=contract_type,
        event_sequence=[_map_event(i) for i in obj["results"]],
        observed_data=_map_observed_data(obj["dataObserved"]),
        observed_events=_map_observed_events(obj["eventsObserved"]),
        term_set=_map_term_set(),
        to_date=_map_to_date(obj["to"])
    )
