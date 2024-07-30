from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    textlocal_api_key: str
    textlocal_sender: str
    gmail_username: str
    gmail_password: str

    class Config:
        env_file = ".env"

settings = Settings()
