from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    ENCODE_KEY: str
    ENCODE_ALGORITHM: str

    @property
    def DATABASE_URL(self):
        user = f"{self.DB_USER}:{self.DB_PASS}"
        database = f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+asyncpg://{user}@{database}"

    @property
    def ENCODE_KEY(self):
        return f"{self.ENCODE_KEY}"

    @property
    def ENCODE_ALGORITHM(self):
        return f"{self.ENCODE_ALGORITHM}"

    # Со 2 версии Pydantic класс Config был заменен на атрибут model_config
    # class Config:
    #     env_file = ".env"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

print(settings.DATABASE_URL)
