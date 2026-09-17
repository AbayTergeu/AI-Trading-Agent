from functools import lru_cache

from app.infrastructure.configuration.settings import Settings, get_settings


class Container:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings


@lru_cache
def get_container() -> Container:
    settings = get_settings()

    return Container(settings)