import typer

from core.enums import StatusEnum
from core.config import HcConfig
from core.exceptions import HcError
from core.state import HcState
from services.monitors import HcMonitorService


app = typer.Typer(name="monitors")


@app.command(name="profile")
def profile(profile_id: str) -> None:
    config = HcConfig()
    state = HcState()
    monitor_service = HcMonitorService()

    monitor_configs = config.get_monitor_profile_by_id(profile_id)
    if monitor_configs is None:
        raise HcError(f"Profile with id '{profile_id}' does not exist")

    monitor_configs.sort(key=lambda x: x.get("state"), reverse=True)

    for monitor_config in monitor_configs:
        if monitor_config.get("state") == StatusEnum.ON:
            monitor_service.turn_monitor_on(
                monitor_config.get("name"),
                monitor_config.get("resolution"),
                monitor_config.get("position"),
                monitor_config.get("scale"),
            )
        elif monitor_config.get("state") == StatusEnum.OFF:
            monitor_service.turn_monitor_off(monitor_config.get("name"))

    state.set_monitor_profile(profile_id)
    state.save()


@app.command(name="init")
def init() -> None:
    config = HcConfig()
    state = HcState()
    monitor_service = HcMonitorService()

    default_profile_id = config.get_monitor_default_profile_id()
    if default_profile_id is None:
        raise HcError("No default monitor profile defined.")

    monitor_configs = config.get_monitor_profile_by_id(default_profile_id)
    if monitor_configs is None:
        raise HcError(
            f"Profile with id '{default_profile_id}' (default) does not exist."
        )

    for monitor_config in monitor_configs:
        if monitor_config.get("state") == StatusEnum.ON:
            monitor_service.turn_monitor_on(
                monitor_config.get("name"),
                monitor_config.get("resolution"),
                monitor_config.get("position"),
                monitor_config.get("scale"),
            )
        elif monitor_config.get("state") == StatusEnum.OFF:
            monitor_service.turn_monitor_off(monitor_config.get("name"))

    state.set_monitor_profile(default_profile_id)
    state.save()
