import logging

from app.infrastructure.configuration.logging import configure_logging


def test_logging_configuration(caplog):
    configure_logging()

    logger = logging.getLogger("test")

    with caplog.at_level(logging.INFO):
        logger.info("test message")

    assert "test message" in caplog.text