import typer

from core.base import StatusEnum
from core.config import Config
from core.state import read_monitor_state, write_monitor_state
from services.monitors import set_monitor_off, set_monitor_on


app = typer.Typer(name="monitors")


@app.command(name="mode")
def mode(mode_id: str) -> None:
    config = Config()
    monitor_configs = config.get_monitor_mode_configs(mode_id)
    monitor_configs.sort(key=lambda x: x.get("state"), reverse=True)

    for monitor_config in monitor_configs:
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
    config = Config()
    monitor_configs = config.get_default_monitor_mode_configs()

    for monitor_config in monitor_configs:
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
