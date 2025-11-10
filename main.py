import typer
from rich import print
from rich.console import Console
from rich.table import Table
import utils.operators as operators  # <- clearer alias

app = typer.Typer()
console = Console()


@app.command()
def version():
    print("xyrculator version [bold red]pre:[green]0.1")
# multiplication sub command


@app.command()
def multiply(a: int, b: int):
    table = Table("operation", "answer")
    table.add_row(f"{str(a)} × {str(b)}", str(operators.multiply(a, b)))
    console.print(table)
# division sub command


@app.command()
def divide(a: int, b: int):
    table = Table("operation", "answer")
    table.add_row(f"{str(a)}÷{str(b)}", str(operators.divide(a, b)))
    console.print(table)


if __name__ == "__main__":
    app()
