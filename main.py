import typer
import typing
from typing import Optional
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

#division sub command
@app.command()
def divide(a: int, b:int):
    table = Table("operation", "answer")
    table.add_row(f"{str(a)}÷{str(b)}", str(operators.divide(a,b)))
    console.print(table)

#
@app.command()
def to_numbers(value: str):
    """
    Tried to use operators.to_numbers if available; otherwise attempt a best-effort parse.
    Prints a table of parsed numeric values like the others.
    """
    nums = None
    if hasattr(operators, "to_numbers"):
        try:
            nums = operators.to_numbers(value)
        except Exception as e:
            nums = None
    if nums is None:
        # best-effort parsing: split on commas or whitespace
        parts = [p for p in (v.strip() for v in value.replace(",", " ").split()) if p]
        parsed = []
        for p in parts:
            try:
                if "." in p:
                    parsed.append(float(p))
                else:
                    parsed.append(int(p))
            except Exception:
                # this is if it couldn't parse, it should keep raw
                parsed.append(p)
        nums = parsed

    table = Table("input", "parsed")
    table.add_row(value, str(nums))
    console.print(table)

@app.command()
def add(a: float, b: float):
    """Add two numbers using operators.add if it there, otherwise fallback to local add."""
    if hasattr(operators, "add"):
        result = operators.add(a, b)
    else:
        result = a + b
    table = Table("operation", "answer")
    table.add_row(f"{a} + {b}", str(result))
    console.print(table)

@app.command()
def subtract(a: float, b: float):
    """Subtract two numbers using operators.subtract if its there, otherwise fallback."""
    if hasattr(operators, "subtract"):
        result = operators.subtract(a, b)
    else:
        result = a - b
    table = Table("operation", "answer")
    table.add_row(f"{a} - {b}", str(result))
    console.print(table)

@app.command()
def call(op_name: str, args: str = typer.Argument("", help="space/comma separated args")):
    """
    Call any function from utils.operators by name.
    Example: call add "1 2"  or call multiply "3,4"
    """
    if not hasattr(operators, op_name):
        print(f"[red]operators has no function named[/red] [bold]{op_name}[/bold]")
        raise typer.Exit(code=1)

    # parse args
    parts = [p for p in (v for v in args.replace(",", " ").split()) if p]
    parsed = []
    for p in parts:
        try:
            parsed.append(int(p) if p.isdigit() else float(p))
        except Exception:
            parsed.append(p)

    func = getattr(operators, op_name)
    try:
        result = func(*parsed)
    except TypeError:
        # try passing the whole string if signature differs
        result = func(args)

    table = Table("operation", "answer")
    table.add_row(f"{op_name}({', '.join(map(str, parsed))})", str(result))
    console.print(table)

# simple fallback in-process memory store (used if utils.operators doesn't provide one)
_MEMORY: dict = {}

def _parse_value_for_store(value: str):
    """Try to convert to int/float using operators.to_numbers if available, else fallback."""
    if hasattr(operators, "to_numbers"):
        try:
            nums = operators.to_numbers(value)
            # if operators.to_numbers returns a single value or list, prefer the first scalar
            if isinstance(nums, (list, tuple)) and len(nums) == 1:
                return nums[0]
            return nums
        except Exception:
            pass
    # fallback single-value parse
    try:
        if "." in value:
            return float(value)
        return int(value)
    except Exception:
        return value

def _memory_set(key: str, value):
    """Set a key in whichever memory backend is available or fallback to local _MEMORY."""
    # check for common placements in utils.operators
    if hasattr(operators, "memory") and isinstance(getattr(operators, "memory"), dict):
        getattr(operators, "memory")[key] = value
        return True
    if hasattr(operators, "memory_set"):
        getattr(operators, "memory_set")(key, value)
        return True
    if hasattr(operators, "store"):
        getattr(operators, "store")(key, value)
        return True
    # fallback
    _MEMORY[key] = value
    return True

def _memory_get(key: str):
    """Get a key from backend or fallback; returns (found_flag, value)"""
    if hasattr(operators, "memory") and isinstance(getattr(operators, "memory"), dict):
        mem = getattr(operators, "memory")
        return (key in mem, mem.get(key))
    if hasattr(operators, "memory_get"):
        try:
            val = getattr(operators, "memory_get")(key)
            return (True, val)
        except Exception:
            return (False, None)
    if hasattr(operators, "recall"):
        try:
            val = getattr(operators, "recall")(key)
            return (True, val)
        except Exception:
            return (False, None)
    # fallback
    return (key in _MEMORY, _MEMORY.get(key))

def _memory_clear(key: Optional[str] = None):
    """Clear one key or all keys in backend or fallback."""
    if hasattr(operators, "memory") and isinstance(getattr(operators, "memory"), dict):
        mem = getattr(operators, "memory")
        if key is None:
            mem.clear()
        else:
            mem.pop(key, None)
        return True
    if hasattr(operators, "memory_clear"):
        getattr(operators, "memory_clear")(key) if key is not None else getattr(operators, "memory_clear")()
        return True
    if hasattr(operators, "clear_memory"):
        getattr(operators, "clear_memory")(key) if key is not None else getattr(operators, "clear_memory")()
        return True
    # fallback
    if key is None:
        _MEMORY.clear()
    else:
        _MEMORY.pop(key, None)
    return True

def _memory_items():
    """Return mapping of memory items from backend or fallback."""
    if hasattr(operators, "memory") and isinstance(getattr(operators, "memory"), dict):
        return dict(getattr(operators, "memory"))
    if hasattr(operators, "memory_items"):
        try:
            return dict(getattr(operators, "memory_items")())
        except Exception:
            pass
    if hasattr(operators, "list_memory"):
        try:
            return dict(getattr(operators, "list_memory")())
        except Exception:
            pass
    return dict(_MEMORY)

@app.command()
def mem_set(key: str, value: str):
    """
    Store a value under a key into the memory backend (or local fallback).
    Value will be parsed as int/float when reasonable.
    """
    parsed = _parse_value_for_store(value)
    _memory_set(key, parsed)
    table = Table("action", "key", "value")
    table.add_row("set", key, str(parsed))
    console.print(table)

@app.command()
def mem_get(key: str):
    """Retrieve a value from memory (prints not-found as well)."""
    found, val = _memory_get(key)
    table = Table("action", "key", "value")
    table.add_row("get", key, str(val) if found else "[red]<not found>[/red]")
    console.print(table)

#Trial
@app.command()
def mem_clear(key: Optional[str] = typer.Argument(None, help="key to clear; omit to clear all")):
    """Clear a key from memory or clear all if no key provided."""
    _memory_clear(key)
    table = Table("action", "key")
    table.add_row("clear", str(key) if key is not None else "<all>")
    console.print(table)

@app.command()
def mem_list():
    """List all memory keys and values."""
    items = _memory_items()
    table = Table("key", "value")
    if not items:
        table.add_row("<empty>", "")
    else:
        for k, v in items.items():
            table.add_row(str(k), str(v))
    console.print(table)

@app.command()
def ops_list():
    """List callable functions available in utils.operators."""
    names = [n for n in dir(operators) if not n.startswith("_")]
    callables = [n for n in names if callable(getattr(operators, n))]
    table = Table("callable ops")
    if not callables:
        table.add_row("<none>")
    else:
        for n in sorted(callables):
            table.add_row(n)
    console.print(table)


if __name__ == "__main__":
    app()
