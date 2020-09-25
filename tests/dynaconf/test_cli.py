#!/usr/bin/env python
"""Tests for `fuse_utils` package."""
from click.testing import CliRunner

from fuse_utils.dynaconf import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()

    result = runner.invoke(cli.main, ["package-name"])
    assert result.exit_code == 0
    assert "Package Name: " in result.output

    result = runner.invoke(cli.main, ["database", "test"])
    assert result.exit_code == 1

    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit." in help_result.output
