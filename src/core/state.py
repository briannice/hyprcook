import json
import os

from pathlib import Path
from typing import Optional, TypedDict


class HcDisplayState(TypedDict, total=False):
    gamma: int
    temp: int


class HcMonitorState(TypedDict, total=False):
    profile: str


class HcAppState(TypedDict, total=False):
    monitor: HcMonitorState
    display: HcDisplayState


class HcState:
    STATE_FILE_NAME = "hyprcook.json"

    def __init__(self) -> None:
        self._state_path = self._get_state_path()
        self._state: HcAppState
        self._load()

    def _get_state_path(self) -> Path:
        state_dir = os.getenv("XDG_RUNTIME_DIR")
        if state_dir is None:
            raise RuntimeError("Environment variable 'XDG_RUNTIME_DIR' is not set.")

        state_path = Path(state_dir)
        if not state_path.is_dir():
            raise RuntimeError("'XDG_RUNTIME_DIR' does not exist.")

        return state_path / self.STATE_FILE_NAME

    def _load(self) -> None:
        if not self._state_path.is_file():
            self._state = {}
            return
        with open(self._state_path) as state_file:
            state: HcAppState = json.load(state_file)
            self._state = state

    def save(self) -> None:
        tmp = self._state_path.with_suffix(".tmp")
        with open(tmp, "w") as f:
            json.dump(self._state, f, indent=4)
            f.write("\n")
        tmp.replace(self._state_path)

    def get_monitor_profile(self) -> Optional[str]:
        return self._state.get("monitor", {}).get("profile")

    def set_monitor_profile(self, profile_id: str) -> None:
        monitor_state = self._state.get("monitor")
        if monitor_state is None:
            self._state["monitor"] = {"profile": profile_id}
        else:
            monitor_state["profile"] = profile_id

    def get_display_gamma(self) -> Optional[int]:
        return self._state.get("display", {}).get("gamma")

    def set_display_gamma(self, n: int) -> None:
        display_state = self._state.get("display")
        if display_state is None:
            self._state["display"] = {"gamma": n}
        else:
            display_state["gamma"] = n

    def get_display_temp(self) -> Optional[int]:
        return self._state.get("display", {}).get("temp")

    def set_display_temp(self, n: int) -> None:
        display_state = self._state.get("display")
        if display_state is None:
            self._state["display"] = {"temp": n}
        else:
            display_state["temp"] = n
