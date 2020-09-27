#!/usr/bin/env python
"""Tests for `fuse_utils` package."""
import pytest
from dynaconf.vendor.box.exceptions import BoxKeyError

from fuse_utils.dynaconf.cli import Main


class TestMain:
    @staticmethod
    def test_project_name(caplog):
        project_name = Main.project_name()
        assert "Project Name: " in caplog.text
        assert project_name == "fuse-utils"

    @staticmethod
    def test_database(caplog):
        with pytest.raises(BoxKeyError):
            Main.database(key="test")

        # dynaconf sets your default env to 'development'
        database = Main.database()
        assert "Database: " in caplog.text
        assert database == {
            "host": "localhost",
            "user": "dev_user",
            "password": "dev_password",
        }

        database = Main("default").database("user")
        assert "User: " in caplog.text
        assert database == {"user": "default"}

        # Once your env is set it won't change
        database = Main.database("user")
        assert "User: " in caplog.text
        assert database == {"user": "default"}
