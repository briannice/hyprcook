from enum import StrEnum
from typing import Dict, List, Optional, TypedDict


# --------------------------------------------------------------------------------------
# Monitors
# --------------------------------------------------------------------------------------

MonitorName = str
MonitorResolution = str
MonitorPosition = str
MonitorScale = float


class MonitorModeConfigState(StrEnum):
    ON = "on"
    OFF = "off"


class MonitorModeConfig(TypedDict):
    name: MonitorName
    state: MonitorModeConfigState
    resolution: Optional[MonitorResolution]
    position: Optional[MonitorPosition]
    scale: Optional[MonitorScale]


class MonitorModeId(StrEnum):
    LAPTOP = "laptop"
    SINGLE_MONITOR = "smon"


MonitorModeSettings = Dict[MonitorModeId, List[MonitorModeConfig]]


class MonitorSettings(TypedDict):
    mode: MonitorModeSettings


# --------------------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------------------


class AppSettings(TypedDict):
    monitor: MonitorSettings
