import json
import os
import sys

from pathlib import Path
from typing import Dict, List, Optional, TypedDict

from core.base import StatusEnum


class MonitorModeConfig(TypedDict):
    name: str
    state: StatusEnum
    resolution: Optional[str]
    position: Optional[str]
    scale: Optional[float]


class MonitorConfig(TypedDict):
    modes: Dict[str, List[MonitorModeConfig]]
    default: Optional[str]


class AppConfig(TypedDict):
    monitors: MonitorConfig


class Config:

    CONFIG_DIR = "config"
    CONFIG_FILE_NAMES = ["default.jsonc", "default.json"]

    def __init__(self) -> None:
        self.config: AppConfig
        self.load()

    def get_config_path(self) -> Path:
        home_dir = os.getenv("HYPRCOOK_HOME")
        if home_dir is None:
            sys.exit("Environment variable 'HYPRCOOK_HOME' is not set.")

        dir_path = Path(home_dir)
        if not dir_path.is_dir():
            sys.exit(f"Hyprcook home directory '{dir_path}' does not exist.")

        dir_path = dir_path / self.CONFIG_DIR
        if not dir_path.is_dir():
            sys.exit(f"Hyprcook config directory '{dir_path}' does not exist.")

        for file_name in self.CONFIG_FILE_NAMES:
            file_path = dir_path / file_name
            if file_path.is_file():
                return file_path

        sys.exit("Configuration file does not exist.")

    def load(self) -> None:
        config_path = self.get_config_path()
        with open(config_path) as config_file:
            config: AppConfig = json.load(config_file)
            self.config = config

    def get_monitor_mode_configs(self, mode_id: str) -> List[MonitorModeConfig]:
        monitor_mode_configs = self.config.get("monitors").get("modes").get(mode_id)
        if monitor_mode_configs is None:
            sys.exit(f"Monitor mode config with id '{mode_id}' does not exist.")

        return monitor_mode_configs

    def get_default_monitor_mode_configs(self) -> List[MonitorModeConfig]:
        default = self.config.get("monitors").get("default")
        if default is None:
            sys.exit(f"Default monitor mode config not found in config.")

        monitor_mode_configs = self.config.get("monitors").get("modes").get(default)
        if monitor_mode_configs is None:
            sys.exit(f"Monitor mode config does not exist for default id {default}.")

        return monitor_mode_configs
