import sys
import typer

from core.config import read_monitor_mode_settings
from core.types import MonitorModeConfigState, MonitorModeId
from services.monitors import set_monitor_defaults, set_monitor_off, set_monitor_on


app = typer.Typer(name="monitor")


@app.command(name="mode")
def mode(mode_id: MonitorModeId) -> None:
    mode_settings = read_monitor_mode_settings()
    mode_config = mode_settings.get(mode_id)

    if mode_config is None:
        sys.exit(f"Display mode {mode_id} is not defined.")

    mode_config.sort(key=lambda x: x.get("state"), reverse=True)

    for monitor_config in mode_config:
        if monitor_config.get("state") == MonitorModeConfigState.ON:
            set_monitor_on(
                monitor_config.get("name"),
                monitor_config.get("resolution"),
                monitor_config.get("position"),
                monitor_config.get("scale"),
            )
        elif monitor_config.get("state") == MonitorModeConfigState.OFF:
            set_monitor_off(monitor_config.get("name"))


@app.command(name="init")
def init() -> None:
    mode_settings = read_monitor_mode_settings()
    mode_config = mode_settings.get(MonitorModeId.LAPTOP)

    if mode_config is None:
        set_monitor_defaults()
        return

    for monitor_config in mode_config:
        if monitor_config.get("state") == MonitorModeConfigState.ON:
            set_monitor_on(
                monitor_config.get("name"),
                monitor_config.get("resolution"),
                monitor_config.get("position"),
                monitor_config.get("scale"),
            )
        elif monitor_config.get("state") == MonitorModeConfigState.OFF:
            set_monitor_off(monitor_config.get("name"))
