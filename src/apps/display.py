import sys
import typer

from core.config import read_display_modes_config
from core.types import AppName, DisplayMode, MonitorState
from services.monitors import set_monitor_off, set_monitor_on


app = typer.Typer(name=AppName.DISPLAY)


@app.command("mode")
def mode(display_mode: DisplayMode) -> None:
    config = read_display_modes_config()
    mode_config = config.get(display_mode)

    if mode_config is None:
        sys.exit(f"Display mode {display_mode} is not defined.")

    mode_config.sort(key=lambda x: x.get("state"), reverse=True)

    for monitor_config in mode_config:
        if monitor_config.get("state") == MonitorState.ON:
            set_monitor_on(
                monitor_config.get("name"),
                monitor_config.get("resolution"),
                monitor_config.get("position"),
                monitor_config.get("scale"),
            )
        elif monitor_config.get("state") == MonitorState.OFF:
            set_monitor_off(monitor_config.get("name"))
