import typer

from apps import monitor, notify

app = typer.Typer()

app.add_typer(notify.app)
app.add_typer(monitor.app)


if __name__ == "__main__":
    app()
