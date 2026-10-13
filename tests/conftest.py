"""Pytest fixtures and test environment setup."""

import pytest


@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    """
    Isolate test runs by mocking environment variables.
    Prevents tests from relying on or modifying real .env files.
    """
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("WEATHER_CITY", "Bangkok")
    monkeypatch.setenv("OPENWEATHER_API_KEY", "test_mock_api_key")
    monkeypatch.setenv("S3_BUCKET_NAME", "test-mock-bucket")
