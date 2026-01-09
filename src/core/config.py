import json
import os
import sys

from enum import StrEnum
from pathlib import Path
from typing import Dict, List, Optional, TypedDict


class StatusEnum(StrEnum):
    ON = "on"
    OFF = "off"


class MonitorConfigModeConfig(TypedDict):
    name: str
    state: StatusEnum
    resolution: Optional[str]
    position: Optional[str]
    scale: Optional[float]


class MonitorConfig(TypedDict):
    modes: Dict[str, List[MonitorConfigModeConfig]]
    default: str


class AppConfig(TypedDict):
    monitors: MonitorConfig


def get_config_path() -> Path:
    CONFIG_DIR = "config"
    CONFIG_FILE_NAMES = ["default.jsonc", "default.json"]

    runtime_dir = os.getenv("HYPRCOOK_HOME")

    if runtime_dir is None:
        sys.exit("Environment variable 'HYPRCOOK_HOME' is not set.")

    dir_path = Path(runtime_dir)

    if not dir_path.is_dir():
        sys.exit(f"Hyprcook home directory '{dir_path}' does not exist.")

    dir_path = dir_path / CONFIG_DIR

    if not dir_path.is_dir():
        sys.exit(f"Hyprcook config directory '{dir_path}' does not exist.")

    for file_name in CONFIG_FILE_NAMES:
        file_path = dir_path / file_name
        if file_path.is_file():
            return file_path

    sys.exit("Configuration file does not exist.")


def read_app_config() -> AppConfig:
    config_path = get_config_path()

    with open(config_path) as config_file:
        config: AppConfig = json.load(config_file)
        return config


def read_monitor_config() -> MonitorConfig:
    app_config = read_app_config()
    return app_config.get("monitors")
