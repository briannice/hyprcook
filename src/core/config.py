import json
import os

from pathlib import Path
from typing import Dict, Optional, Required, TypedDict

from core.enums import StatusEnum
from core.exceptions import HcError


class HcMonitorProfileConfig(TypedDict):
    name: Required[str]
    state: Required[StatusEnum]
    resolution: str
    position: str
    scale: float


HcMonitorProfile = list[HcMonitorProfileConfig]


class HcMonitorConfig(TypedDict, total=False):
    profiles: Dict[str, HcMonitorProfile]
    default: str


class HcDisplayGammaConfig(TypedDict, total=False):
    default: int
    night: int


class HcDisplayTempConfig(TypedDict, total=False):
    default: int
    night: int


class HcDisplayConfig(TypedDict, total=False):
    gamma: HcDisplayGammaConfig
    temperature: HcDisplayTempConfig


class HcAppConfig(TypedDict, total=False):
    monitors: HcMonitorConfig
    display: HcDisplayConfig


class HcConfig:
    CONFIG_DIR = "config"
    CONFIG_FILE_NAMES = ["default.jsonc", "default.json"]

    def __init__(self) -> None:
        self._config_path = self._get_config_path()
        self._config: HcAppConfig
        self._load()

    def _get_config_path(self) -> Path:
        home_dir = os.getenv("HYPRCOOK_HOME")
        if home_dir is None:
            raise HcError("Environment variable 'HYPRCOOK_HOME' is not set.")

        dir_path = Path(home_dir)
        if not dir_path.is_dir():
            raise HcError(f"Hyprcook home directory '{dir_path}' does not exist.")

        dir_path = dir_path / self.CONFIG_DIR
        if not dir_path.is_dir():
            raise HcError(f"Hyprcook config directory '{dir_path}' does not exist.")

        for file_name in self.CONFIG_FILE_NAMES:
            file_path = dir_path / file_name
            if file_path.is_file():
                return file_path

        raise HcError("Configuration file does not exist.")

    def _load(self) -> None:
        config_path = self._get_config_path()
        with open(config_path) as config_file:
            config: HcAppConfig = json.load(config_file)
            self._config = config

    def get_monitor_profile_by_id(self, profile_id: str) -> Optional[HcMonitorProfile]:
        return self._config.get("monitors", {}).get("profiles", {}).get(profile_id)

    def get_monitor_default_profile_id(self) -> Optional[str]:
        return self._config.get("monitors", {}).get("default")

    def get_display_default_gamma(self) -> Optional[int]:
        return self._config.get("display", {}).get("gamma", {}).get("default")

    def get_display_night_gamma(self) -> Optional[int]:
        return self._config.get("display", {}).get("gamma", {}).get("night")

    def get_display_gamma_by_id(self, id: str) -> Optional[int]:
        return self._config.get("display", {}).get("gamma", {}).get(id)

    def get_display_default_temp(self) -> Optional[int]:
        return self._config.get("display", {}).get("temperature", {}).get("default")

    def get_display_night_temp(self) -> Optional[int]:
        return self._config.get("display", {}).get("temperature", {}).get("night")

    def get_display_temp_by_id(self, id: str) -> Optional[int]:
        return self._config.get("display", {}).get("temperature", {}).get(id)
