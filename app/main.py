from app.composition.container import get_container
from app.infrastructure.configuration.logging import configure_logging

def main() -> None:
    configure_logging()
    container = get_container()

    print(
        f"AI Procurement Agent started "
        f"(environment={container.settings.environment})"
    )

if __name__ == "__main__":
    main()