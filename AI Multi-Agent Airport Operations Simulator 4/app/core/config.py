from pydantic_settings import BaseSettings, SettingsConfigDict

class A(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    app_name: str = "AI Multi-Agent Airport Operations Simulator"
    app_env: str = "dev"
    database_url: str = "sqlite:///./airport_operations.db"
    redis_url: str = "redis://localhost:6379/0"
    celery_broker_url: str = "redis://localhost:6379/1"
    celery_result_backend: str = "redis://localhost:6379/2"
    openai_api_key: str = ""
    sentry_dsn: str = ""
    otel_exporter_otlp_endpoint: str = ""

a = A()
