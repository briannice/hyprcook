import typer

from core.types import AppName
from services.notifications import send_normal_notification

app = typer.Typer(name=AppName.NOTIFY)


@app.command("info")
def info(title: str, body: str):
    send_normal_notification(title, body)
