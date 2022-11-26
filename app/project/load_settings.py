import json
from pathlib import Path
from typing import Any, Dict

from pydantic import AnyHttpUrl, BaseSettings

SETTINGS_PATH = Path(Path.cwd() / "project" / "settings.json")

if not SETTINGS_PATH.exists():
    raise FileNotFoundError("Settings file not found in path.")


def json_config_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    """
    A simple settings source that loads variables from a JSON file
    at the project's root.

    Here we happen to choose to use the `env_file_encoding` from Config
    when reading `config.json`
    """
    encoding = settings.__config__.env_file_encoding
    return json.loads(Path(SETTINGS_PATH).read_text(encoding))


class Settings(BaseSettings):
    PROJECT_NAME: str = "candidates_profiles"
    API_PREFIX: str = "/api"
    VERSION: str = "0.1.0"
    DEBUG: bool = False
    MONGODB_NAME: str
    MONGODB_URL: str
    SECRET_KEY: str
    JWT_SECRET: str
    MIN_CONNECTIONS_COUNT: int = 10
    MAX_CONNECTIONS_COUNT: int = 10

    class Config:
        env_file_encoding = "utf-8"

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                json_config_settings_source,
                env_settings,
                file_secret_settings,
            )
