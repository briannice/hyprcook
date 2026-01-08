import typer

from apps import notify, display

app = typer.Typer()

app.add_typer(notify.app)
app.add_typer(display.app)


if __name__ == "__main__":
    app()
