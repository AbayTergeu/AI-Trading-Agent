from app.infrastructure.configuration.settings import get_settings


def test_settings_load_from_environment():
    settings = get_settings()

    assert settings.anthropic_api_key.get_secret_value()
    assert settings.environment == "development"