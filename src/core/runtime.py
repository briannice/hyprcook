#!/usr/bin/env python3

import os
import sys

from pathlib import Path
from typing import Dict


CONFIG_NAME = "hyprkoek.conf"


def get_config_path() -> Path:
    runtime_dir = os.getenv("XDG_RUNTIME_DIR")

    if runtime_dir is None:
        sys.exit("Environment variable 'XDG_RUNTIME_DIR' is not set.")

    path = Path(runtime_dir)

    if not path.is_dir():
        sys.exit("User runtime directory 'XDG_RUNTIME_DIR' does not exist.")

    return path / CONFIG_NAME


def read_config() -> Dict[str, str]:
    config: Dict[str, str] = {}
    config_path = get_config_path()

    if not config_path.is_file():
        return config

    with config_path.open() as file:
        for line in file:
            line = line.strip()

            if not line or "=" not in line:
                continue

            key, value = line.split("=", 1)
            config[key] = value

    return config


def write_config(config: Dict[str, str]) -> None:
    config_path = get_config_path()

    with config_path.open("w") as file:
        for key, value in config.items():
            file.write(f"{key}={value}\n")
