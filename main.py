#the entry files
import typer
from rich import print

app = typer.Typer()

@app.command()
def version(version: str):
    print(f"xyrculator version [bold red]pre:[green]0.1")


if __name__ == "__main__":
    app()
