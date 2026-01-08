from enum import StrEnum
from typing import Dict, List, Optional, TypedDict


# --------------------------------------------------------------------------------------
# Monitors
# --------------------------------------------------------------------------------------

MonitorName = str
MonitorResolution = str
MonitorPosition = str
MonitorScale = float


class MonitorState(StrEnum):
    ON = "on"
    OFF = "off"


class MonitorConfig(TypedDict):
    name: MonitorName
    state: MonitorState
    resolution: Optional[MonitorResolution]
    position: Optional[MonitorPosition]
    scale: Optional[MonitorScale]


# --------------------------------------------------------------------------------------
# Display
# --------------------------------------------------------------------------------------


class DisplayMode(StrEnum):
    LAPTOP = "laptop"
    SINGLE_MONITOR = "smon"


DisplayModeConfig = Dict[DisplayMode, List[MonitorConfig]]


class DisplayConfig(TypedDict):
    modes: DisplayModeConfig


# --------------------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------------------


class AppName(StrEnum):
    NOTIFY = "notify"
    DISPLAY = "display"


class AppConfig(TypedDict):
    display: DisplayConfig
