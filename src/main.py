import typer

from apps import monitor, notify, display

app = typer.Typer()

app.add_typer(notify.app)
app.add_typer(monitor.app)
app.add_typer(display.app)


def main():
    app()


if __name__ == "__main__":
    main()
