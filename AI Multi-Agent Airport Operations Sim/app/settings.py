import os
from dataclasses import dataclass, asdict
from typing import Any


def get_text(name: str, default: str) -> str:
    val = os.getenv(name)
    if val is None:
        return default
    return val.strip()


def get_int(name: str, default: int) -> int:
    val = os.getenv(name)
    if val is None:
        return default
    try:
        return int(val)
    except ValueError:
        return default


def get_float(name: str, default: float) -> float:
    val = os.getenv(name)
    if val is None:
        return default
    try:
        return float(val)
    except ValueError:
        return default


def get_bool(name: str, default: bool) -> bool:
    val = os.getenv(name)
    if val is None:
        return default
    val = val.strip().lower()
    if val in {"1", "true", "yes", "on"}:
        return True
    if val in {"0", "false", "no", "off"}:
        return False
    return default


@dataclass
class Settings:
    app_name: str = "AI Multi-Agent Airport Operations Simulator"
    app_version: str = "1.0.0"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_debug: bool = False
    api_prefix: str = "/api"
    database_url: str = "sqlite:///./airport_simulator.db"
    redis_url: str = "redis://localhost:6379/0"
    celery_broker_url: str = "redis://localhost:6379/1"
    celery_result_url: str = "redis://localhost:6379/2"
    openai_api_key: str = ""
    openai_model: str = "gpt-4.1-mini"
    use_database: bool = True
    use_redis: bool = True
    use_celery: bool = True
    use_ai: bool = False
    max_simulations: int = 200
    max_events_per_sim: int = 20000
    max_ticks: int = 5000
    tick_seconds: int = 60
    default_seed: int = 42
    default_algorithm: str = "weighted"
    default_flights: int = 30
    default_runways: int = 3
    default_gates: int = 12
    default_weather: str = "clear"
    low_fuel: float = 25.0
    critical_fuel: float = 12.0
    diversion_fuel: float = 6.0
    landing_fuel_cost: float = 2.0
    holding_fuel_cost: float = 0.7
    taxi_fuel_cost: float = 0.2
    landing_time: int = 3
    runway_gap: int = 2
    gate_hold_time: int = 18
    weather_change_rate: float = 0.08
    emergency_rate: float = 0.03
    failure_rate: float = 0.01
    storm_close_rate: float = 0.45
    fog_slow_rate: float = 0.35
    wind_slow_rate: float = 0.25
    rain_slow_rate: float = 0.15
    snow_slow_rate: float = 0.40
    passenger_weight: float = 0.02
    wait_weight: float = 1.1
    fuel_weight: float = 2.3
    emergency_weight: float = 100.0
    size_weight: float = 1.5
    airline_fairness_weight: float = 1.0
    request_timeout: int = 20
    websocket_ping: int = 20
    cache_seconds: int = 3600
    log_level: str = "INFO"
    allowed_origins: str = "*"
    worker_count: int = 2
    sql_echo: bool = False
    save_events: bool = True
    save_snapshots: bool = True
    snapshot_gap: int = 10
    ai_temperature: float = 0.2
    ai_max_tokens: int = 500
    solver_time_limit: int = 3
    benchmark_runs: int = 5
    benchmark_parallel: bool = False
    random_airlines: str = "UA,AA,DL,WN,B6,AS,NK,F9,AC,BA,LH,AF,EK,QR,AI"
    airport_code: str = "SIM"
    timezone: str = "UTC"
    startup_seed: bool = False

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)

    def airlines(self) -> list[str]:
        return [x.strip() for x in self.random_airlines.split(",") if x.strip()]

    def origins(self) -> list[str]:
        return [
            "JFK",
            "EWR",
            "LGA",
            "ORD",
            "ATL",
            "DFW",
            "LAX",
            "SFO",
            "SEA",
            "MIA",
            "BOS",
            "DEN",
            "PHX",
            "IAH",
            "CLT",
            "MSP",
            "DTW",
            "LAS",
            "MCO",
            "IAD",
            "BWI",
            "PHL",
            "SAN",
            "TPA",
            "AUS",
            "PDX",
            "SLC",
            "RDU",
            "CLE",
            "PIT",
            "IND",
            "CMH",
            "MCI",
            "STL",
            "BNA",
            "MSY",
            "SJU",
            "YYZ",
            "YVR",
            "LHR",
            "CDG",
            "FRA",
            "AMS",
            "DXB",
            "DOH",
            "BOM",
            "DEL",
            "HYD",
            "SIN",
            "HND",
        ]


def load_settings() -> Settings:
    return Settings(
        app_name=get_text("APP_NAME", "AI Multi-Agent Airport Operations Simulator"),
        app_version=get_text("APP_VERSION", "1.0.0"),
        app_host=get_text("APP_HOST", "0.0.0.0"),
        app_port=get_int("APP_PORT", 8000),
        app_debug=get_bool("APP_DEBUG", False),
        api_prefix=get_text("API_PREFIX", "/api"),
        database_url=get_text("DATABASE_URL", "sqlite:///./airport_simulator.db"),
        redis_url=get_text("REDIS_URL", "redis://localhost:6379/0"),
        celery_broker_url=get_text("CELERY_BROKER_URL", "redis://localhost:6379/1"),
        celery_result_url=get_text("CELERY_RESULT_URL", "redis://localhost:6379/2"),
        openai_api_key=get_text("OPENAI_API_KEY", ""),
        openai_model=get_text("OPENAI_MODEL", "gpt-4.1-mini"),
        use_database=get_bool("USE_DATABASE", True),
        use_redis=get_bool("USE_REDIS", True),
        use_celery=get_bool("USE_CELERY", True),
        use_ai=get_bool("USE_AI", False),
        max_simulations=get_int("MAX_SIMULATIONS", 200),
        max_events_per_sim=get_int("MAX_EVENTS_PER_SIM", 20000),
        max_ticks=get_int("MAX_TICKS", 5000),
        tick_seconds=get_int("TICK_SECONDS", 60),
        default_seed=get_int("DEFAULT_SEED", 42),
        default_algorithm=get_text("DEFAULT_ALGORITHM", "weighted"),
        default_flights=get_int("DEFAULT_FLIGHTS", 30),
        default_runways=get_int("DEFAULT_RUNWAYS", 3),
        default_gates=get_int("DEFAULT_GATES", 12),
        default_weather=get_text("DEFAULT_WEATHER", "clear"),
        low_fuel=get_float("LOW_FUEL", 25.0),
        critical_fuel=get_float("CRITICAL_FUEL", 12.0),
        diversion_fuel=get_float("DIVERSION_FUEL", 6.0),
        landing_fuel_cost=get_float("LANDING_FUEL_COST", 2.0),
        holding_fuel_cost=get_float("HOLDING_FUEL_COST", 0.7),
        taxi_fuel_cost=get_float("TAXI_FUEL_COST", 0.2),
        landing_time=get_int("LANDING_TIME", 3),
        runway_gap=get_int("RUNWAY_GAP", 2),
        gate_hold_time=get_int("GATE_HOLD_TIME", 18),
        weather_change_rate=get_float("WEATHER_CHANGE_RATE", 0.08),
        emergency_rate=get_float("EMERGENCY_RATE", 0.03),
        failure_rate=get_float("FAILURE_RATE", 0.01),
        storm_close_rate=get_float("STORM_CLOSE_RATE", 0.45),
        fog_slow_rate=get_float("FOG_SLOW_RATE", 0.35),
        wind_slow_rate=get_float("WIND_SLOW_RATE", 0.25),
        rain_slow_rate=get_float("RAIN_SLOW_RATE", 0.15),
        snow_slow_rate=get_float("SNOW_SLOW_RATE", 0.40),
        passenger_weight=get_float("PASSENGER_WEIGHT", 0.02),
        wait_weight=get_float("WAIT_WEIGHT", 1.1),
        fuel_weight=get_float("FUEL_WEIGHT", 2.3),
        emergency_weight=get_float("EMERGENCY_WEIGHT", 100.0),
        size_weight=get_float("SIZE_WEIGHT", 1.5),
        airline_fairness_weight=get_float("AIRLINE_FAIRNESS_WEIGHT", 1.0),
        request_timeout=get_int("REQUEST_TIMEOUT", 20),
        websocket_ping=get_int("WEBSOCKET_PING", 20),
        cache_seconds=get_int("CACHE_SECONDS", 3600),
        log_level=get_text("LOG_LEVEL", "INFO"),
        allowed_origins=get_text("ALLOWED_ORIGINS", "*"),
        worker_count=get_int("WORKER_COUNT", 2),
        sql_echo=get_bool("SQL_ECHO", False),
        save_events=get_bool("SAVE_EVENTS", True),
        save_snapshots=get_bool("SAVE_SNAPSHOTS", True),
        snapshot_gap=get_int("SNAPSHOT_GAP", 10),
        ai_temperature=get_float("AI_TEMPERATURE", 0.2),
        ai_max_tokens=get_int("AI_MAX_TOKENS", 500),
        solver_time_limit=get_int("SOLVER_TIME_LIMIT", 3),
        benchmark_runs=get_int("BENCHMARK_RUNS", 5),
        benchmark_parallel=get_bool("BENCHMARK_PARALLEL", False),
        random_airlines=get_text("RANDOM_AIRLINES", "UA,AA,DL,WN,B6,AS,NK,F9,AC,BA,LH,AF,EK,QR,AI"),
        airport_code=get_text("AIRPORT_CODE", "SIM"),
        timezone=get_text("TIMEZONE", "UTC"),
        startup_seed=get_bool("STARTUP_SEED", False),
    )


settings = load_settings()


def reload_settings() -> Settings:
    global settings
    settings = load_settings()
    return settings


def get_setting(name: str, default: Any = None) -> Any:
    return getattr(settings, name, default)


def set_setting(name: str, val: Any) -> Any:
    if not hasattr(settings, name):
        raise KeyError(name)
    old = getattr(settings, name)
    setattr(settings, name, val)
    return old


def public_settings() -> dict[str, Any]:
    data = settings.as_dict()
    data["openai_api_key"] = "set" if settings.openai_api_key else ""
    data["database_url"] = data["database_url"].split("@")[0] if "@" in data["database_url"] else data["database_url"]
    return data
