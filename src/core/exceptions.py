import typer


class HcError(typer.Exit):

    def __init__(self, msg: str, code: int = 1) -> None:
        typer.echo(msg, err=True)
        super().__init__(code)
