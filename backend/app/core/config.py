from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    DATABASE_URL: str

    GROQ_API_KEY: str
    GROQ_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()


# Unlike a normal Python class, BaseSettings automatically reads values from .env.

# If .env contains:  APP_NAME=AI Backend

# then: settings.APP_NAME

# returns: AI Backend

# without us manually opening the file.

