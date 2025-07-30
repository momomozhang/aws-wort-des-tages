"""Test the aws_wort_des_tages package functionality."""

import aws_wort_des_tages


def test_package_version():
    """Test that package has a version attribute."""
    assert hasattr(aws_wort_des_tages, "__version__")
    assert aws_wort_des_tages.__version__ is not None
