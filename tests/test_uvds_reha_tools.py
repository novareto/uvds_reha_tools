#!/usr/bin/env python

"""Tests for `uvds_reha_tools` package."""

import pytest
from pathlib import Path

from uvds_reha_tools.uvds_reha_tools import convert_ds
from icecream import ic


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    f = str(Path(__file__).parent / "openapi.json")
    with open(f, 'r') as json_file:
        res = convert_ds(json_file)
    assert isinstance(res, dict)
    assert res['$id'] == "LD_000_0A1109"
    assert res['description'] == "Abgabemitteilung an Ärzte"
    assert isinstance(res['properties'], list)
    ic(res)
