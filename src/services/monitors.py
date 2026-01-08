import os

from typing import Optional


def set_monitor_on(
    name: str,
    resolution: Optional[str] = None,
    position: Optional[str] = None,
    scale: Optional[float] = None,
) -> None:
    if resolution is None:
        resolution = "preferred"
    if position is None:
        position = "auto"
    if scale is None:
        scale = 1
    os.system(f"hyprctl keyword monitor {name},{resolution},{position},{scale}")


def set_monitor_off(name: str) -> None:
    os.system(f"hyprctl keyword monitor {name},disable")
