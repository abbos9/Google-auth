from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OUATH_GOOGLE_CLIENT_SECRET: str
    OUATH_GOOGLE_CLIENT_ID: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
