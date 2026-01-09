import typer

from services.notifications import send_normal_notification

app = typer.Typer(name="notify")


@app.command(name="info")
def info(title: str, body: str):
    send_normal_notification(title, body)
