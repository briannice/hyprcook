import typer

from core.config import HcConfig
from core.exceptions import HcError
from core.state import HcState
from services.display import HcDisplayService

app = typer.Typer(name="display")


@app.command("gamma")
def set_gamma(gamma: str) -> None:
    pass


@app.command("init")
def init() -> None:
    config = HcConfig()
    state = HcState()
    display_service = HcDisplayService()

    default_gamma = config.get_display_default_gamma()
    if default_gamma is None:
        raise HcError("Default gamma is not configured.")
    if not display_service.validate_gamma(default_gamma):
        raise HcError(f"Invalid default gamma value configured: {default_gamma}")

    default_temp = config.get_display_default_temp()
    if default_temp is None:
        raise HcError("Default temparature is not configured.")
    if not display_service.validate_temp(default_temp):
        raise HcError(f"Invalid default temperature value configured: {default_temp}")

    display_service.set_gamma(default_gamma)
    display_service.set_temp(default_temp)

    state.set_display_gamma(default_gamma)
    state.set_display_temp(default_temp)
    state.save()


@app.command("mode")
def mode(id: str) -> None:
    config = HcConfig()
    state = HcState()
    display_service = HcDisplayService()

    gamma = config.get_display_gamma_by_id(id)
    if gamma is None:
        raise HcError(f"Gamma is not configured for id {id}.")
    if not display_service.validate_gamma(gamma):
        raise HcError(f"Invalid gamma value configured for id {id}: {gamma}")

    temp = config.get_display_temp_by_id(id)
    print(temp)
    if temp is None:
        raise HcError(f"Temparature is not configured for id {id}.")
    if not display_service.validate_temp(temp):
        raise HcError(f"Invalid temperature value configured for id {id}: {temp}")

    display_service.set_gamma(gamma)
    display_service.set_temp(temp)

    state.set_display_gamma(gamma)
    state.set_display_temp(temp)
    state.save()
