import json
import os
import sys

from pathlib import Path

from core.types import AppSettings, MonitorModeSettings, MonitorSettings


CONFIG_DIR = "config"
CONFIG_FILE_NAMES = ["default.jsonc", "default.json"]


def get_config_path() -> Path:
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


def read_app_settings() -> AppSettings:
    config_path = get_config_path()

    with open(config_path) as config_file:
        settings: AppSettings = json.load(config_file)
        return settings


def read_monitor_settings() -> MonitorSettings:
    app_settings = read_app_settings()
    return app_settings.get("monitor")


def read_monitor_mode_settings() -> MonitorModeSettings:
    monitor_settings = read_monitor_settings()
    return monitor_settings.get("mode")
