"""Test main module functionality."""

from ai_document_platform import main


def test_main_function_exists() -> None:
    """Test that main function exists and is callable."""
    assert callable(main)


def test_version_import() -> None:
    """Test that version can be imported."""
    from ai_document_platform import __version__

    assert __version__ == "0.1.0"
