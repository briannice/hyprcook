import json
import os
import sys

from pathlib import Path
from typing import TypedDict


class MonitorState(TypedDict, total=False):
    mode: str


class AppState(TypedDict, total=False):
    monitor: MonitorState


def get_state_file_path() -> Path:
    STATE_FILE_NAME = "hyprcook.json"

    state_dir = os.getenv("XDG_RUNTIME_DIR")

    if state_dir is None:
        sys.exit("Environment variable 'XDG_RUNTIME_DIR' is not set.")

    state_path = Path(state_dir)

    if not state_path.is_dir():
        sys.exit("User runtime directory 'XDG_RUNTIME_DIR' does not exist.")

    return state_path / STATE_FILE_NAME


def read_app_state() -> AppState:
    config_path = get_state_file_path()

    if not config_path.is_file():
        return {}

    with config_path.open() as file:
        config: AppState = json.load(file)
        return config


def read_monitor_state() -> MonitorState:
    app_state = read_app_state()
    monitor_state = app_state.get("monitor")

    if monitor_state is None:
        return {}

    return monitor_state


def write_app_state(state: AppState) -> None:
    config_path = get_state_file_path()

    with config_path.open("w") as file:
        json.dump(state, file, indent=2)


def write_monitor_state(monitor_state: MonitorState) -> None:
    app_state = read_app_state()
    app_state["monitor"] = monitor_state
    write_app_state(app_state)
