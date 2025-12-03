from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    llm_model: str
    llm_endpoint: str
    app_env: str | None = None
    app_debug: bool | None = None
    agent_name: str | None = None
    llm_timeout: int | None = None

    class Config:
        env_file = ".env"

settings = Settings()
