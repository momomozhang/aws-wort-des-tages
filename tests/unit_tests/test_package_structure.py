"""Test package structure and basic functionality."""

import aws_wort_des_tages


def test_package_can_be_imported():
    """Test that the package can be imported without errors."""
    # Package should have the expected structure
    assert hasattr(aws_wort_des_tages, "__version__")
