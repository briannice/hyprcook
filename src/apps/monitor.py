import sys
import typer

from core.config import StatusEnum, read_monitor_config
from core.state import read_monitor_state, write_monitor_state
from services.monitors import set_monitor_defaults, set_monitor_off, set_monitor_on


app = typer.Typer(name="monitors")


@app.command(name="mode")
def mode(mode_id: str) -> None:
    monitor_config = read_monitor_config()
    monitor_modes = monitor_config.get("modes").get(mode_id)

    if monitor_modes is None:
        sys.exit(f"Display mode {mode_id} is not defined.")

    monitor_modes.sort(key=lambda x: x.get("state"), reverse=True)

    for monitor_config in monitor_modes:
        if monitor_config.get("state") == StatusEnum.ON:
            set_monitor_on(
                monitor_config.get("name"),
                monitor_config.get("resolution"),
                monitor_config.get("position"),
                monitor_config.get("scale"),
            )
        elif monitor_config.get("state") == StatusEnum.OFF:
            set_monitor_off(monitor_config.get("name"))

    monitor_state = read_monitor_state()
    monitor_state["mode"] = mode_id
    write_monitor_state(monitor_state)


@app.command(name="init")
def init() -> None:
    monitor_config = read_monitor_config()
    monitor_mode = monitor_config.get("modes").get("laptop")

    if monitor_mode is None:
        set_monitor_defaults()
        return

    for monitor_config in monitor_mode:
        if monitor_config.get("state") == StatusEnum.ON:
            set_monitor_on(
                monitor_config.get("name"),
                monitor_config.get("resolution"),
                monitor_config.get("position"),
                monitor_config.get("scale"),
            )
        elif monitor_config.get("state") == StatusEnum.OFF:
            set_monitor_off(monitor_config.get("name"))

    monitor_state = read_monitor_state()
    monitor_state["mode"] = "laptop"
    write_monitor_state(monitor_state)
