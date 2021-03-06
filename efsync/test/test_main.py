import pytest
from efsync.main import efsync, load_args_from_yaml


def test_load_args_from_yaml():
    res = load_args_from_yaml()

    assert isinstance(res, dict)


def test_main():
    res = efsync('./efsync.yaml')
    assert res == True
