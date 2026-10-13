"""Setup verification and smoke tests."""

import data_pipeline
from data_pipeline.config import Settings
from data_pipeline.main import main


def test_package_import():
    """Verify that data_pipeline is importable and has package metadata."""
    assert hasattr(data_pipeline, "__version__")
    assert data_pipeline.__version__ == "0.1.0"


def test_main_execution(capsys):
    """Verify that main entrypoint runs and produces output."""
    main()
    captured = capsys.readouterr()
    assert "Hello from first-data-en-project!" in captured.out


def test_settings_load():
    """Verify that Settings loads values correctly from environment."""
    cfg = Settings()
    assert cfg.environment == "test"
    assert cfg.weather_city == "Bangkok"
    assert cfg.weather_api_key == "test_mock_api_key"
    assert cfg.s3_bucket == "test-mock-bucket"
