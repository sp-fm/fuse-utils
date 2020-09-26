#!/usr/bin/env python
"""Tests for `fuse_utils` package."""
import pytest
from dynaconf.vendor.box.exceptions import BoxKeyError

from fuse_utils.dynaconf.cli import Main


def test_command_line_interface(caplog):
    """Test the CLI"""

    Main.package_name()
    assert "Package Name: " in caplog.text

    with pytest.raises(BoxKeyError):
        Main.database(key="test")
